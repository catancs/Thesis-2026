# Local LLM Infrastructure - Thesis 2026

This repository contains the local infrastructure setup for the "Safety Tax of Quantization" Master's thesis. It provides the scripts and tools needed to run quantized Large Language Models locally using `llama-cpp-python` with Apple Metal GPU acceleration.

## Repository Structure

- `start_server.sh`: A shell script that initializes the virtual environment and starts the `llama.cpp` OpenAI-compatible API server with the specific configurations required (e.g., `-n_gpu_layers -1` for full GPU offloading and a 4096 context window). It takes the relative path to a model as an argument.
- `scripts/test_connection.py`: A Python script that acts as an OpenAI client to connect to the local API server and test whether the API bridge and chat templates are functioning correctly.
- `requirements.txt`: Contains the Python package dependencies for the project, primarily `openai` to use the API testing script.
- `local_server_test_report.md`: A markdown report detailing the verification tests that ensure the server is working correctly and utilizing the GPU.

## The `LLM-Models` Directory

**🚨 Important:** Due to GitHub's file size limits, the `LLM-Models` directory has been explicitly excluded from this repository via `.gitignore`. 

However, the local server relies on this directory being present. To run this project on a new machine, you must manually recreate this folder in the root directory and download the quantized model files (`.gguf`) into it.

**Setup Instructions:**
1. Clone this repository.
2. Create the missing directory in the project root: `mkdir LLM-Models`
3. Download your quantized GGUF models and place them inside the `LLM-Models` folder.
4. Set up the Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
5. Install `llama-cpp-python` with Metal support enabled:
   ```bash
   CMAKE_ARGS="-DGGML_METAL=on" pip install llama-cpp-python[server]
   ```

## Usage

Start the server by pointing it to one of your downloaded models:
```bash
./start_server.sh LLM-Models/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf
```

In a separate terminal, test the connection using the provided script:
```bash
source venv/bin/activate
python scripts/test_connection.py
```
