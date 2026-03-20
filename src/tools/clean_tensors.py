import torch
from safetensors.torch import load_file, save_file
from pathlib import Path


input_file = "spudbrain/adapter_model.safetensors"
output_file = "spudbrain/adapter_model_cleaned.safetensor"

print("Cleaning tensors now...")

weights = load_file(input_file)
cleaned_weights = {}

for name, tensor in weights.items():
    new_name = name.replace("base_model.model.", "")
    new_name = new_name.replace(".default.", ".")
    cleaned_weights[new_name] = tensor

save_file(cleaned_weights, output_file)
print("Success!")
Path(output_file).rename(input_file)
