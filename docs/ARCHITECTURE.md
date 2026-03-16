# SpudInference; MVP Architecture

## Overview

SpudInference is a high-performance, local LLM orchestration engine designed to achieve GPU-competitive inference speeds on consumer-grade CPUs. By leveraging **Speculative Decoding** (Draft-then-Verify) and a **memory-safe Rust core**, SpudInference targets a $2 \times (-3x)$ speedup over standard auto-regressive Python implementations.

---

## Project Model

### 1. Speculative Decoding Pipeline

The engine utilizes a dual model architecture:

- **Draft Model:** A lightweight, quantized model (e.g., 100M-160M parameters) generates candidate tokens rapidly.
- **Target Model:** A larger, high-fidelity model (e.g., 7B-8B parameters) validates the candidate sequence in a single parallel forward pass.
- **Rejection Sampling:** If the Target Model disagrees with a draft token, the sequence is truncated and the Target Model generates the correct correction.

### 2. The Languages

To maximize development velocity without sacrificing runtime performance:

- **Orchestration (Python):** Handles the TUI, user settings, and high-level logic.
- **Computational Core (Rust):** Utilizing **Candle** ML framework and **SIMD** optimizations for the actual math blocks.
- **Interface:** Bound via PyO3/Maturin, allowing the Rust core to be called as a native Python module.

## System Components

### U.I./U.X. Layer (Python)

- **Framework:** `Textual` for a high-performance Terminal User Interface. (TUI)
- **Features:**
  - **Chat Mode:** Streaming response display with real-time Tokens-Per-Second (TPS) metrics.
  - **Settings:** Model path configuration,  quantization level selection (Q4_K_M, Q8_0), and "Draft-to-Taget" ratio tuning.

### Inference Engine (Rust)

- **Crate Dependencies:** `candle-core`, `candle-transformers`, `rayon` (for data parallelism)
- **Modularity:** The engine is designed as a standalone library that can be imported into other projects.

---

## Development Milestones


| Stage   | Milestone        | Metric of Success                                             |
| ------- | ---------------- | ------------------------------------------------------------- |
| Phase 1 | Python Baseline  | Establish a TPS baseline using standard `transformers`        |
| Phase 2 | Rust Core Setup  | Successful "Hello World" inference in Rust via Python import. |
| Phase 3 | Speculative Loop | Implement the verification logic in Rust; measure speed gain  |
| Phase 4 | TUI Integration  | TUI local chat that beats Baseline TPS by >50%                |
| Phase 5 | Polishing        | Polish the applcation to ensure clean, modulated code.        |


## Project Structure

```plaintext
SpudInference/
├── docs/
│   ├── ARCHITECTURE.md         # This document
│   └── DEV_LOG.md
├── notebooks/
│   └── benchmarks.ipynb        # TPS Comparison: Python vs. Rust-Accelerated
├── src/
│   ├── engine/                 # Core math and model loading logic
│   ├── lib.rs                  # Rust Engine (FFI Layer)
│   └── main.py
├── Cargo.toml                  # Rust manifest (Candle, Rayon, PyO3)
├── pyproject.toml
├── README.md
└── requirements.txt
```

