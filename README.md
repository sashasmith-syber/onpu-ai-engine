# 🎵 ONPU AI Engine

> Persona-Driven AI Prompt Engine optimized for **KIMI K2**

Expertise in text-music, [🔷 SOUNDBLUEPRINT™©] [音符]-music, code-music generation, and sound design prompt engineering.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![KIMI K2 Optimized](https://img.shields.io/badge/KIMI%20K2-Optimized-ff6b6b)](https://github.com/MoonshotAI/Kimi-K2)

## 🌟 Overview

ONPU AI Engine is a persona-driven AI prompt engineering framework designed specifically for music and sound generation tasks. It leverages **MoonshotAI's KIMI K2** model capabilities - a state-of-the-art mixture-of-experts (MoE) language model with 1 trillion parameters and 32 billion active parameters.

### Key Features

- 🎭 **Persona-Driven AI**: Specialized personas for composers, sound designers, producers, and code musicians
- 🔷 **SOUNDBLUEPRINT™ Notation**: Structured music description format optimized for AI comprehension
- 🛠️ **Tool-Calling Support**: Native integration with KIMI K2's agentic tool-calling capabilities
- 🎼 **Music Generation Prompts**: Optimized prompting for text-to-music AI systems
- 💻 **Code-Music Integration**: Algorithmic composition and creative coding support

## 📦 Installation

```bash
# Basic installation
pip install onpu-ai-engine

# With API support (OpenAI-compatible client)
pip install onpu-ai-engine[api]

# For development
pip install onpu-ai-engine[dev]
```

Or install from source:

```bash
git clone https://github.com/sashasmith-syber/onpu-ai-engine.git
cd onpu-ai-engine
pip install -e .
```

## 🚀 Quick Start

### Basic Usage

```python
from onpu_ai_engine import OnpuEngine, SoundBlueprint, DynamicLevel, Section

# Initialize the engine
engine = OnpuEngine()

# Set a specialized persona
engine.set_persona("composer")

# Create a music generation prompt
prompt = engine.generate_music_prompt(
    description="A peaceful morning melody with gentle piano",
    style="ambient",
    duration="2:00",
    instruments=["piano", "strings"]
)

print(prompt)
```

### Using SOUNDBLUEPRINT™ Notation

```python
from onpu_ai_engine import SoundBlueprint, Section, DynamicLevel

# Create a detailed music blueprint
blueprint = SoundBlueprint(
    title="Sunrise Serenade",
    genre="ambient",
    mood="peaceful",
    tempo=72,
    key="C major"
)

# Add sections
blueprint.add_section(Section(
    name="Intro",
    start_time="0:00",
    end_time="0:30",
    instruments=["piano", "soft strings"],
    dynamics=DynamicLevel.PIANO,
    melody_description="Gentle ascending arpeggios"
))

blueprint.add_section(Section(
    name="Main Theme",
    start_time="0:30",
    end_time="1:30",
    instruments=["piano", "strings", "soft pads"],
    dynamics=DynamicLevel.MEZZO_PIANO,
    melody_description="Flowing melodic phrases with warmth"
))

# Generate the prompt
print(blueprint.to_prompt())
```

Output:
```
[🔷 SOUNDBLUEPRINT™]
Title: Sunrise Serenade
Genre: ambient
Mood: peaceful
Tempo: 72 BPM
Time Signature: 4/4
Key: C major

[音符 SECTIONS]
Section: Intro (0:00-0:30)
  Instruments: piano, soft strings
  Dynamics: p
  Texture: moderate
  Melody: Gentle ascending arpeggios

Section: Main Theme (0:30-1:30)
  Instruments: piano, strings, soft pads
  Dynamics: mp
  Texture: moderate
  Melody: Flowing melodic phrases with warmth
```

### Using Personas

```python
from onpu_ai_engine import OnpuEngine

engine = OnpuEngine()

# Available built-in personas:
# - "composer" - Music composition and arrangement
# - "sound_designer" - Sound design and synthesis
# - "producer" - Music production and beat-making
# - "code_musician" - Algorithmic and generative music
# - "soundblueprint" - SOUNDBLUEPRINT™ notation specialist

engine.set_persona("sound_designer")

# Create a custom persona
engine.create_persona(
    name="film_scorer",
    description="Film and media composer",
    system_prompt="You are an expert film composer...",
    expertise=["film scoring", "orchestration", "sound design"]
)
```

### Integration with KIMI K2

```python
from onpu_ai_engine import OnpuEngine, EngineConfig

# Configure for KIMI K2
config = EngineConfig(
    model="moonshotai/Kimi-K2-Instruct",
    temperature=0.6,  # KIMI K2 recommended
    api_base="https://api.moonshot.cn/v1",
    api_key="your-api-key"
)

engine = OnpuEngine(config=config)
engine.set_persona("composer")

# Add a user message
engine.add_user_message("Create a dramatic orchestral piece for a movie trailer")

# Get the request payload (ready for API call)
payload = engine.get_request_payload()
```

### Tool Calling Support

```python
from onpu_ai_engine import OnpuEngine

engine = OnpuEngine()

# Register a custom tool
def generate_midi(notes: list, tempo: int) -> dict:
    return {"status": "success", "file": "output.mid"}

engine.add_tool(
    name="generate_midi",
    description="Generate a MIDI file from note data",
    parameters={
        "type": "object",
        "required": ["notes", "tempo"],
        "properties": {
            "notes": {"type": "array", "description": "List of notes"},
            "tempo": {"type": "integer", "description": "Tempo in BPM"}
        }
    },
    handler=generate_midi
)

# Get tools schema for KIMI K2
tools = engine.get_tools_schema()
```

## 🎭 Built-in Personas

| Persona | Description | Expertise |
|---------|-------------|-----------|
| `composer` | Music composer and arranger | Composition, arrangement, music theory, orchestration |
| `sound_designer` | Sound design specialist | Synthesis, audio engineering, spatial audio |
| `producer` | Music producer | Beat-making, mixing, commercial music |
| `code_musician` | Creative coder | Algorithmic composition, audio programming |
| `soundblueprint` | Notation specialist | SOUNDBLUEPRINT™ format, AI prompting |

## 🔷 SOUNDBLUEPRINT™ Format

The SOUNDBLUEPRINT™ notation system is a structured format for describing music to AI models:

```
[🔷 SOUNDBLUEPRINT™]
Title: <title>
Genre: <genre>
Mood: <mood>
Tempo: <bpm> BPM
Key: <key>

[音符 SECTIONS]
Section: <name> (<start>-<end>)
  Instruments: <list>
  Dynamics: <pp/p/mp/mf/f/ff>
  Texture: <sparse/moderate/dense>
  Melody: <description>
  Harmony: <progression>

Visual Notation Symbols:
• ○ ◐ ● - Note density (sparse/moderate/dense)
• ↑ ↓ — - Melodic contour
• ⟨ ⟩ - Dynamic swells
• ≈ - Sustained tones
• ♪ ♫ - Rhythmic patterns
```

## 🔧 Configuration

```python
from onpu_ai_engine import EngineConfig

config = EngineConfig(
    # KIMI K2 settings
    model="moonshotai/Kimi-K2-Instruct",
    temperature=0.6,
    max_tokens=4096,
    
    # API configuration
    api_base="https://api.moonshot.cn/v1",
    api_key="your-key",
    
    # Engine settings
    enable_tool_calling=True,
    enable_streaming=True,
    context_length=128000
)
```

## 🤝 Why KIMI K2?

ONPU AI Engine is optimized for [KIMI K2](https://github.com/MoonshotAI/Kimi-K2) because of its:

- **Agentic Intelligence**: Strong tool-calling and autonomous task execution
- **Large Context**: 128K token context window for complex compositions
- **Mixture of Experts**: 384 expert sub-models for specialized tasks
- **Open Source**: Available for research and commercial use

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- [MoonshotAI](https://www.moonshot.ai/) for the KIMI K2 model
- The music AI and creative coding community

---

<p align="center">
  Made with 🎵 by ONPU AI
</p>
