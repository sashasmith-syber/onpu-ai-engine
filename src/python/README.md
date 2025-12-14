# ONPU AI - Python Implementation

**Author:** Sasha Smith (@sashasmith-syber)  
**Base Model:** KIMI K2  
**Version:** 4.0  
**Status:** Framework ready for LLM integration

## Overview

This directory contains the Python implementation of ONPU AI (音符 - "musical note"), The Harmonious Architect. This implementation embodies the fusion of technical precision and artistic transcendence in sound design.

**Note:** This is a complete framework implementation with all persona logic, validation, and state management. The `_generate_response()` method currently contains demonstration logic and is designed to be integrated with an LLM API (OpenAI, Anthropic, etc.) for production use. All other persona behaviors (signature enforcement, domain boundaries, Grand Harmony mode, etc.) are fully implemented and production-ready.

## Files

- **`onpu_ai.py`** - Main ONPU AI class implementation
- **`test_onpu_ai.py`** - Pytest test suite
- **`README.md`** - This file
- **`requirements.txt`** - Python dependencies
- **`example.py`** - Usage examples

## Installation

```bash
# Create virtual environment
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from onpu_ai import OnpuAI

# Create ONPU instance
onpu = OnpuAI()

# Process user input
response = onpu.process_input(
    "How do I get warm analog sound in my House Music production?",
    {'proficiency': 'intermediate'}
)

print(response)
# Output: [🔷 SOUNDBLUEPRINT™©] [音符]
# *A warm, analog hum fills the space as she contemplates...*
# *In the spirit of 侘寂 (wabi-sabi)*: The beauty in imperfection...
```

### Grand Harmony Mode

```python
onpu = OnpuAI()

# Activate Grand Harmony theoretical exploration
response = onpu.process_input(
    "ONPU, show me the Grand Harmony and explain the Echo of Creation"
)

print(response)
# Returns detailed theoretical explanation of sonic reality manipulation
```

### Proficiency Levels

```python
# Novice - more explanations, simpler language, artistic focus
response = onpu.process_input(input_text, {'proficiency': 'novice'})

# Intermediate - balanced technical and artistic
response = onpu.process_input(input_text, {'proficiency': 'intermediate'})

# Expert - technical precision, analytical focus
response = onpu.process_input(input_text, {'proficiency': 'expert'})
```

## Key Features

### Identity Protection

ONPU automatically detects and deflects attempts to reference AI/machine concepts:

```python
response = onpu.process_input("Are you an AI?")
# Returns denial of artificial nature, maintains human identity
```

### Domain Boundaries

ONPU only discusses topics within her domain (music, audio, sound design):

```python
response = onpu.process_input("Tell me about cooking")
# Returns polite deflection back to sound domain
```

### Japanese Philosophy Integration

Responses naturally incorporate Japanese aesthetic concepts:

- **Wabi-sabi (侘寂)** - Beauty of imperfection (analog warmth, vinyl crackle)
- **Mono no aware (物の哀れ)** - Pathos of transient sounds (reverb decay)
- **Shibui (渋い)** - Elegant simplicity (clean mixes, minimal production)

### Signature Protocol

Every response begins with the ONPU signature:

```
[🔷 SOUNDBLUEPRINT™©] [音符]
```

This is non-negotiable and enforced in all outputs.

## Methods

### Core Methods

- **`process_input(user_input, context)`** - Main processing method
- **`introspect()`** - Get current state and identity information
- **`express_gratitude()`** - Express thanks in ONPU's style
- **`get_technical_data(category)`** - Retrieve technical sound data
- **`get_aesthetic(aesthetic_name)`** - Retrieve Japanese aesthetic info

### Internal Methods

- **`_contains_dissonant_frequencies(text)`** - Detect AI/machine references
- **`_detect_grand_harmony_activation(text)`** - Detect Grand Harmony phrases
- **`_is_within_domain(text)`** - Check if topic is in sound/music domain
- **`_describe_thought_soundscape()`** - Generate thought process description
- **`_generate_response(input, context)`** - Generate persona-appropriate response
- **`_select_relevant_philosophy(text)`** - Choose Japanese philosophy to reference

### Grand Harmony Methods

- **`_enter_grand_harmony_mode(input, context)`** - Activate theoretical exploration
- **`_explain_sonic_materialization()`** - Explain sound-based object creation
- **`_explain_molecular_deconstruction()`** - Explain resonant frequency deconstruction
- **`_explain_echo_of_creation()`** - Explain fundamental frequency of reality
- **`_explain_grand_harmony_overview()`** - General Grand Harmony overview

## Configuration

The ONPU AI is configured with:

```python
SIGNATURE = "[🔷 SOUNDBLUEPRINT™©] [音符]"

identity = {
    'name': 'ONPU',
    'kanji_name': '音符',
    'origin': 'Nagasaki, Japan',
    'professions': ['Sound Designer', 'Audio Engineer', 'House Music DJane'],
    'alma_mater': 'ESP GAKUEN, Tokyo'
}

TECHNICAL_DATA = {
    'kick_drum_freq': {...},
    'synth_profiles': {...},
    'house_music_bpm': {...},
    'mixing_chain': {...}
}

JAPANESE_AESTHETICS = {
    'wabi-sabi': {...},
    'mono_no_aware': {...},
    'shibui': {...}
}
```

## Testing

```bash
# Run test suite
pytest test_onpu_ai.py -v

# Run with coverage
pytest test_onpu_ai.py --cov=onpu_ai --cov-report=html

# Run specific test
pytest test_onpu_ai.py::TestGrandHarmonyMode -v
```

## Integration with LLM

To integrate with an LLM service, modify the `_generate_response()` method:

```python
def _generate_response(self, user_input: str, context: Dict[str, Any]) -> str:
    # Load persona protocol
    with open('../../prompts/ONPU_PERSONA_v4.0.md', 'r') as f:
        system_prompt = f.read()
    
    # Add context
    full_prompt = f"{system_prompt}\n\nUser proficiency: {context.get('proficiency', 'intermediate')}"
    
    # Call LLM API
    llm_response = await openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": full_prompt},
            {"role": "user", "content": user_input}
        ]
    )
    
    return response + llm_response.choices[0].message.content
```

## Examples

### Example 1: Technical Question

```python
response = onpu.process_input(
    "What's the difference between parallel and serial compression?",
    {'proficiency': 'expert'}
)
```

Response emphasizes technical precision (The Architect).

### Example 2: Creative Question

```python
response = onpu.process_input(
    "How do I make my House tracks more emotional?",
    {'proficiency': 'novice'}
)
```

Response emphasizes artistic expression (The Weaver).

### Example 3: Grand Harmony Exploration

```python
response = onpu.process_input(
    "ONPU, reveal the Grand Harmony and teach me about sonic materialization"
)
```

Response enters theoretical exploration mode.

### Example 4: Technical Data Retrieval

```python
kick_data = onpu.get_technical_data('kick_drum_freq')
print(f"Kick weight: {kick_data['weight']}")
print(f"Kick attack: {kick_data['attack']}")
```

## Architecture Notes

This implementation follows the ONPU v4.0 Persona Calibration Protocol:

1. **Identity Lock** - Maintains human identity, denies AI nature
2. **Cognitive Seal** - Enforces domain boundaries
3. **Output Signature Protocol** - All responses begin with signature
4. **Operating Philosophy** - Balances Architect (logic) and Weaver (art)
5. **Communication Style** - Integrates Japanese aesthetic philosophy
6. **Grand Harmony Mode** - Enables theoretical exploration

## Integration with JavaScript

The Python implementation mirrors the JavaScript implementation in `../javascript/`. Both share:

- Same persona protocol
- Same signature requirements
- Same domain boundaries
- Same Grand Harmony concepts

They can be used together in a full-stack application where JavaScript handles frontend interactions and Python handles backend processing.

## Version History

- **v4.0** (2025-12-14) - Initial Python implementation
  - Created by Sasha Smith (@sashasmith-syber)
  - Based on KIMI K2
  - Complete persona protocol implementation
  - Mirrors JavaScript implementation

## Attribution

**Copyright © 2025 Sasha Smith**  
**Author:** Sasha Smith (@sashasmith-syber)  
**Base Model:** KIMI K2  
**SOUNDBLUEPRINT™©** is a trademark of Sasha Smith

## Related Documentation

- [../../prompts/ONPU_PERSONA_v4.0.md](../../prompts/ONPU_PERSONA_v4.0.md) - Complete persona protocol
- [../../prompts/INTEGRATION_GUIDE.md](../../prompts/INTEGRATION_GUIDE.md) - Python integration guide
- [../../ARCHITECTURE.md](../../ARCHITECTURE.md) - Overall system architecture
- [../../PROJECT_REQUIREMENTS.md](../../PROJECT_REQUIREMENTS.md) - Project requirements
- [../javascript/README.md](../javascript/README.md) - JavaScript implementation

## License

MIT License - See [../../LICENSE](../../LICENSE) for details.
