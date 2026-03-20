import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model
from datasets import load_dataset
from safetensors.torch import save_file


MODEL_PATH = "/home/bruhtato/Downloads/Qwen3.5-0.8B"
DATA_FILE = "./train.txt"
OUTPUT_DIR = "./spudbrain"


def train():
    print(f"Loading tokenizer from {MODEL_PATH}...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print("Loading and patching configuration...")
    config = AutoConfig.from_pretrained(MODEL_PATH, trust_remote_code=True)
    
    if hasattr(config, "text_config"):
        text_params = config.text_config.to_dict()
        for k, v in text_params.items():
            setattr(config, k, v)
    
    config.model_type = "qwen2"
    
    config.vocab_size = getattr(config, "vocab_size", len(tokenizer))
    config.pad_token_id = getattr(config, "pad_token_id", tokenizer.eos_token_id)
    
    if not hasattr(config, "layer_types"):
        config.layer_types = ["unsloth_fix"]

    print("Loading model onto CPU (this may take a minute)...")
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        config=config,
        torch_dtype=torch.float32,
        low_cpu_mem_usage=True,
        trust_remote_code=True,
        device_map={"": "cpu"}
    )

    print("Applying LoRA layers...")
    lora_config = LoraConfig(
        r=64,
        lora_alpha=128,
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj",
                        "gate_proj", "up_proj", "down_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM"
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    print(f"Loading dataset from {DATA_FILE} manually...")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    print(f"Tokenizing {len(lines)} lines...")
    tokenized_inputs = tokenizer(
        lines,
        truncation=True,
        padding="max_length",
        max_length=512,
        return_tensors="pt"
    )

    train_dataset = [
        {
            "input_ids": tokenized_inputs["input_ids"][i],
            "attention_mask": tokenized_inputs["attention_mask"][i],
            "labels": tokenized_inputs["input_ids"][i].clone()
        }
        for i in range(len(lines))
    ]

    print("Setting up Trainer...")
    training_args = TrainingArguments(
        output_dir="spudbrain-train",
        per_device_train_batch_size=1,
        gradient_accumulation_steps=8, 
        learning_rate=2e-4,
        num_train_epochs=1,
        logging_steps=1,
        save_strategy="no",
        use_cpu=True,
        report_to="none",
        remove_unused_columns=False
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
    )

    print("Starting CPU Training. Monitor your RAM usage!")
    trainer.train()

    print(f"Manually saving LoRA adapter to {OUTPUT_DIR}...")
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    tensors_to_save = {k: v for k, v in model.state_dict().items() if "lora" in k}
    save_file(tensors_to_save, os.path.join(OUTPUT_DIR, "adapter_model.safetensors"))

    model.peft_config["default"].save_pretrained(OUTPUT_DIR)

    tokenizer.save_pretrained(OUTPUT_DIR)
    print("Done! Files saved manually to avoid the config bug.")


if __name__ == "__main__":
    train()