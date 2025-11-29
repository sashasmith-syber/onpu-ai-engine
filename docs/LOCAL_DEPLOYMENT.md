# ONPU AI Engine - Local Deployment Guide

This guide covers how to deploy the ONPU AI Engine locally for development and testing.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Quick Start](#quick-start)
3. [Configuration](#configuration)
4. [Running with Docker](#running-with-docker)
5. [Running with Python](#running-with-python)
6. [API Usage](#api-usage)
7. [Troubleshooting](#troubleshooting)

## Prerequisites

- Python 3.10 or higher
- Docker and Docker Compose (optional, for containerized deployment)
- Git

## Quick Start

### Option 1: Docker (Recommended)

```bash
# Clone the repository
git clone https://github.com/sashasmith-syber/onpu-ai-engine.git
cd onpu-ai-engine

# Start the engine
docker-compose up -d

# Check status
docker-compose ps
```

### Option 2: Python Virtual Environment

```bash
# Clone the repository
git clone https://github.com/sashasmith-syber/onpu-ai-engine.git
cd onpu-ai-engine

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set PYTHONPATH and run the engine
export PYTHONPATH="./src:$PYTHONPATH"
python -m uvicorn onpu_ai_engine.api:app --host 127.0.0.1 --port 8000
```

## Configuration

### Environment Variables

Copy `.env.example` to `.env` and configure:

```bash
cp .env.example .env
```

Key variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `ONPU_HOST` | Server host | `127.0.0.1` |
| `ONPU_PORT` | Server port | `8000` |
| `ONPU_DEBUG` | Enable debug mode | `false` |
| `OPENAI_API_KEY` | OpenAI API key | (required for AI features) |

### YAML Configuration

Edit `config/settings.yaml` for detailed configuration:

```yaml
server:
  host: "127.0.0.1"
  port: 8000

engine:
  default_persona: "default"

sound_design:
  soundblueprint:
    enabled: true
```

## Running with Docker

### Production Mode

```bash
# Build and start
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

### Development Mode (with hot-reload)

```bash
# Start with dev profile
docker-compose --profile dev up onpu-engine-dev

# Access at http://localhost:8001
```

## Running with Python

### Install as Package

```bash
pip install -e .
```

### CLI Commands

```bash
# Show version
onpu --version

# Start server
onpu serve --host 127.0.0.1 --port 8000

# Generate prompt
onpu generate --prompt "Create ambient soundscape" --persona ambient
```

## API Usage

### Health Check

```bash
curl http://localhost:8000/health
```

### List Personas

```bash
curl http://localhost:8000/personas
```

### Generate Music Prompt

```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Create relaxing ambient music", "persona": "ambient"}'
```

### API Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Available Personas

| Persona | Description |
|---------|-------------|
| `default` | Standard music generation |
| `ambient` | Atmospheric soundscapes |
| `electronic` | Electronic/synthesizer music |
| `orchestral` | Classical orchestral compositions |
| `soundblueprint` | [🔷 SOUNDBLUEPRINT™©] Advanced sound design |

## Troubleshooting

### Port Already in Use

```bash
# Check what's using the port
lsof -i :8000

# Use a different port
onpu serve --port 8001
```

### Docker Permission Issues

```bash
# Add user to docker group
sudo usermod -aG docker $USER
```

### Module Not Found

```bash
# Ensure PYTHONPATH includes src
export PYTHONPATH="./src:$PYTHONPATH"
```

## Development

### Run Tests

```bash
pytest tests/
```

### Code Formatting

```bash
black src/ tests/
flake8 src/ tests/
```

## [🔷 SOUNDBLUEPRINT™©] [音符] Features

The engine includes advanced sound design capabilities:

- **Persona-driven prompts**: Tailored generation based on musical style
- **Multi-modal support**: Text-to-music, code-to-music generation
- **Extensible architecture**: Easy to add custom personas

---

For more information, see the [main README](../README.md).
