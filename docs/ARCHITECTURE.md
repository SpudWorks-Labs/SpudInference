# SpudInference; MVP Architecture

## Overview

SpudInference is a specialized, local-first LLM ecosystem designed to operate on low-end hardware. It bypasses the need for high-end VRAM by utilizing CPU-based training and inference. The project centers on a "Router-Draft" paradigm, where a smaller, faster model handles trivialities while a larger, "thoughtful" model is reserved for complex reasoning.

---

## Project Model
* **Hybrid Dual-Server Inference:** Utilizes a dual-port system (8080/8081) to separate the Turbo and Thought model instances.
* **Asynchronous PEFT/LoRA Pipeline: Enables model customization on consumer-grade CPUs by training low-rank adapters without altering the base model weights.
* **Intelligence Routing:** A classification layer that evaluates user intent to optimize token-per-second (TPS) delivery based on query complexity.


## System Components
* **Orchestration Layer (`main.py`): The central command-line interface providing a gateway to training, conversion, and chat utilities.
* **Inference Engine (`brain.py`):** The logic center that managesHTTP requests to the local completion endpoints and executes the "Simple vs. Complex" routing.
* **Dataset Tooling:** A suite comprising of `create_training.py` and `dataset_handling.py` for manual data entry and JSONL-to-Chat ML conversion.
* **Training Core (`train.py`): A Hugging Face-integrated pipeline configured for LoRA fine-tuning on Linux-based CPU environments.
* **Post-Processor (`clean_tensors.py`): A utility to sanitize tensor keys, ensuring compatibility between training outputs and inference model structures.


## Project Phases
* **Phase 1; Data Acquisition:** Synthesizing uncensored datasets and manually refining interaction pairs for model alignment.
* **Phase 2; Optimization:** Executing CPU-bound fine-tuning and cleaning resulting adapters for deployment.
* **Phase 3; Deployment:** Running dual-model servers for real-time, routed inference via The SpudBrain interface.

---

## Project Structure
```plaintext
SpudInference/
├── docs/
│   ├── ARCHITECTURE.md
│   └── DEV_LOG.md
├── models/                     # The LLM Models required for this project.
│   ├── Qwen3.5-0.8B-Q8_0.gguf   # Sym-Link
│   └── Qwen3.5-9B-Q4_K_M.gguf   # Sym-Link
├── src/
│   ├── engine/                 # Core math and model loading logic
│   │   └── brain.py
│   ├── tools/                  # The tools for the models.
│   │   ├── clean_tensors.py
│   │   ├── create_training.py
│   │   ├── dataset_handling.py
│   │   └── train.py
│   └── main.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```