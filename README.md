# onpu-ai-engine

Persona_Driven AI prompt engine. Expertise in text-music, [🔷 SOUNDBLUEPRINT™©] [音符]-music, code-music generation. Sound design prompt engineering.

## 🎵 Overview

ONPU AI Engine is a sophisticated persona-driven AI prompt engine designed for music generation and sound design. It supports multiple personas tailored for different musical styles and use cases.

## ✨ Features

- **Persona-Driven Generation**: Switch between specialized personas for different musical styles
- **[🔷 SOUNDBLUEPRINT™©]**: Advanced sound design prompt engineering
- **[音符] Music Generation**: Text-to-music and code-to-music capabilities
- **REST API**: FastAPI-powered REST API for easy integration
- **Docker Support**: Ready for containerized deployment
- **Extensible**: Easy to add custom personas

## 🚀 Quick Start

### Using Docker

```bash
docker-compose up -d
```

### Using Python

```bash
pip install -r requirements.txt
python -m uvicorn onpu_ai_engine.api:app --host 127.0.0.1 --port 8000
```

## 📖 Documentation

- [Local Deployment Guide](docs/LOCAL_DEPLOYMENT.md)

## 🎭 Available Personas

| Persona | Description |
|---------|-------------|
| `default` | Standard music generation |
| `ambient` | Atmospheric soundscapes |
| `electronic` | Electronic/synthesizer music |
| `orchestral` | Classical orchestral |
| `soundblueprint` | [🔷 SOUNDBLUEPRINT™©] Advanced sound design |

## 🔧 API Usage

```bash
# Health check
curl http://localhost:8000/health

# Generate music prompt
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Create ambient soundscape", "persona": "ambient"}'
```

## 📁 Project Structure

```
onpu-ai-engine/
├── src/onpu_ai_engine/    # Core engine code
│   ├── api.py             # FastAPI application
│   ├── engine.py          # Prompt engine
│   ├── config.py          # Configuration
│   └── main.py            # CLI entry point
├── config/                # Configuration files
├── docs/                  # Documentation
├── tests/                 # Test suite
├── Dockerfile             # Docker image
└── docker-compose.yml     # Docker Compose config
```

## 📜 License

MIT License - see [LICENSE](LICENSE) for details.

## 👤 Author

Sasha Smith

