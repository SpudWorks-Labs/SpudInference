import json


def dataset_to_prompts(dataset_path):
    prompts = []

    with open(dataset_path, 'r', encoding='utf-8') as dataset:
        for line in dataset:
            try:
                prompt = json.loads(line)
                system_prompt = user_prompt = assistant_prompt = None

                for message in prompt.get("messages"):
                    if message['role'] == 'system':
                        system_prompt = message['content']
                    elif message['role'] == 'user':
                        user_prompt = message['content']
                    elif message['role'] == 'assistant':
                        assistant_prompt = message['content']

                    prompts.append(f"<|im_start|>system\n{system_prompt}<|im_end|>\n<|im_start|>user\n{user_prompt}<|im_end|>\n<|im_start|>assistant\n{assistant_prompt}<|im_end|>\n\n")

            except Exception as e:
                print(f"Error decoding the JSON fron line: {line.strip()}. Error: {e}")

    return prompts


prompts = dataset_to_prompts('uncensored_dataset.jsonl')
count = 0

for prompt in prompts:
    with open('traino.txt', 'a', encoding='utf-8') as train_file:
        train_file.write(prompt)

    count += 1

print(f"Conversion completed!\n\nSaved {count} prompts!")
