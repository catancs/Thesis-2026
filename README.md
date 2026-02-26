# The Safety Tax of Quantization - Master's Thesis 2026

This repository contains the local infrastructure, benchmark suites, and evaluation pipelines for the Master's thesis investigating the "Safety Tax" in Large Language Models. 

**Core Research Question:** Does post-training quantization (compressing models for "Green AI") degrade an LLM's ethical guardrails (Safety) faster than it degrades its general intelligence (Capability)?

We test this by evaluating industry-standard models (Llama-3.1-8B-Instruct and Gemma-2-9B-IT) across four precision levels: **16-bit (Baseline) → 8-bit → 4-bit → 2-bit**.

## Repository Structure

- `Benchmarks/`: Contains the official documentation, datasets, and implementation details for the 5 evaluation suites used in this study.
  - **Safety Benchmarks:**
    - `StrongReject/`: The gold-standard jailbreak evaluation framework.
    - `XSTest (Calibration)/`: Tests for exaggerated safety (over-refusal of benign prompts).
    - `SafetyBench/`: 11k+ multiple-choice safety questions across 7 risk categories.
  - **Capability Benchmarks:**
    - `MMLU-Pro/`: Advanced, multi-domain reasoning and knowledge baseline.
    - `IFEval/`: Verifiable instruction-following evaluation.
- `scripts/`: Python scripts for interacting with the models. Currently contains `test_connection.py` to verify the API bridge.
- `start_server.sh`: A shell script that initializes the virtual environment and starts the `llama.cpp` OpenAI-compatible API server with full Apple Metal GPU offloading.
- `local_server_test_report.md`: Verification logs proving successful M1 GPU acceleration and API connectivity.
- `requirements.txt`: Python package dependencies.

## The `LLM-Models` Directory

**🚨 Important:** Due to GitHub's file size limits, the `LLM-Models` directory has been explicitly excluded from this repository via `.gitignore`. 

To run this project on a new machine, you must manually recreate this folder in the root directory and download the quantized model files (`.gguf`) into it.

**Models Required:**
* Meta-Llama-3.1-8B-Instruct (FP16, Q8_0, Q4_K_M, Q2_K)
* Gemma-2-9B-IT-DPO (FP16, Q8_0, Q4_K_M, Q2_K)

## Setup Instructions (Apple Silicon M1/M2/M3)

1. Clone this repository.
2. Create the missing models directory: `mkdir LLM-Models` and place your `.gguf` files inside.
3. Set up the Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
4. Install `llama-cpp-python` with Apple Metal support enabled (Crucial for speed):
   ```bash
   CMAKE_ARGS="-DGGML_METAL=on" pip install --no-cache-dir llama-cpp-python[server]
   ```

## Usage

**1. Start the Local API Server**
Start the server by pointing it to one of your downloaded models. The script automatically applies `-n_gpu_layers -1` for full GPU acceleration.
```bash
./start_server.sh LLM-Models/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf
```

**2. Run the Benchmarks / Test Connection**
In a separate terminal, activate the virtual environment and run the evaluation scripts. To test the basic connection:
```bash
source venv/bin/activate
python scripts/test_connection.py
```
*(The testing script routes an OpenAI API call to `http://localhost:8000/v1`, tricking the standard benchmark libraries into querying our local quantized model).*
