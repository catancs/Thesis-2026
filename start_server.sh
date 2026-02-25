#!/bin/bash
# Make executable: chmod +x start_server.sh

if [ -z "$1" ]; then
  echo "Usage: ./start_server.sh models/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf"
  exit 1
fi

# Activate the venv
source venv/bin/activate

MODEL_PATH="$1"

echo "Starting llama_cpp.server with model: $MODEL_PATH"

# Launch the server
python3 -m llama_cpp.server \
  --model "$MODEL_PATH" \
  --host 127.0.0.1 \
  --port 8000 \
  --n_gpu_layers -1 \
  --n_ctx 4096
