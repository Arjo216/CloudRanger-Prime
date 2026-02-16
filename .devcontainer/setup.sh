#!/bin/bash
set -e

echo "🚀 CloudRanger Prime: Initializing Environment..."

# 1. Install Kind (Kubernetes in Docker)
if ! command -v kind &> /dev/null; then
    echo "📦 Installing Kind (The Cluster)..."
    curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
    chmod +x ./kind
    sudo mv ./kind /usr/local/bin/kind
fi

# 2. Install Ollama (The AI Brain)
if ! command -v ollama &> /dev/null; then
    echo "🧠 Installing Ollama (The Intelligence)..."
    curl -fsSL https://ollama.com/install.sh | sh
fi

echo "✅ Environment Ready! Run 'ollama serve' to wake up the AI."
