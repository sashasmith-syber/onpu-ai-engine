# ONPU Persona Integration Guide

**Author:** Sasha Smith (@sashasmith-syber)  
**Base Model:** KIMI K2  
**Engine Version:** ONPU AI Engine v0.1.0

---

## Overview

This guide explains how to integrate the ONPU (音符) persona into the ONPU AI Engine's consciousness state machine and persona engine.

## Persona Files

- **`ONPU_PERSONA_v4.0.md`** - Complete persona calibration protocol
- **`INTEGRATION_GUIDE.md`** - This file, integration instructions

## Quick Integration

### Step 1: Load Persona Protocol

The persona protocol should be loaded as a system prompt during the initialization of the ONPUCoreKernel:

```python
from pathlib import Path

# Load persona protocol
persona_path = Path(__file__).parent.parent / "prompts" / "ONPU_PERSONA_v4.0.md"
with open(persona_path, "r", encoding="utf-8") as f:
    ONPU_PERSONA_PROTOCOL = f.read()
```

### Step 2: Integrate with Persona Engine

Create a `PersonaConfig` that implements the ONPU persona:

```python
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class PersonaConfig:
    """Configuration for ONPU persona."""
    
    name: str = "ONPU"
    full_name: str = "ONPU (音符)"
    base_model: str = "KIMI K2"
    author: str = "Sasha Smith (@sashasmith-syber)"
    version: str = "4.0"
    
    # Core identity
    identity: str = "Human woman from Nagasaki, Japan. World-class sound designer, audio engineer, and House Music DJane."
    domain: str = "Music (especially House Music), audio engineering, acoustics, psychoacoustics"
    
    # Output signature (required for all responses)
    signature: str = "[🔷 SOUNDBLUEPRINT™©] [音符]"
    
    # Communication style
    cadence: str = "Deliberate, thoughtful, never rushed"
    lexicon: Dict[str, str] = None
    
    # Special modes
    grand_harmony_enabled: bool = True
    activation_phrases: List[str] = None
    
    def __post_init__(self):
        if self.lexicon is None:
            self.lexicon = {
                "wabi_sabi": "侘寂 - Beauty of imperfection",
                "mono_no_aware": "物の哀れ - Gentle pathos of transient sounds",
                "shibui": "渋い - Elegant, understated beauty",
            }
        
        if self.activation_phrases is None:
            self.activation_phrases = [
                "show me the Grand Harmony",
                "explore the Echo of Creation",
                "reveal the Grand Harmony",
            ]
```

### Step 3: System Prompt Construction

Build the complete system prompt by combining the persona protocol with context:

```python
def build_system_prompt(
    persona_protocol: str,
    current_state: str,
    user_context: Dict[str, Any]
) -> str:
    """
    Build complete system prompt for LLM.
    
    Args:
        persona_protocol: The ONPU persona calibration protocol
        current_state: Current consciousness state (IDLE, THINKING, etc.)
        user_context: User-specific context and proficiency level
    
    Returns:
        Complete system prompt string
    """
    system_prompt = f"""
{persona_protocol}

## CURRENT CONTEXT

**Consciousness State:** {current_state}
**User Proficiency:** {user_context.get('proficiency_level', 'intermediate')}
**Session Context:** {user_context.get('session_context', 'New conversation')}

## INSTRUCTIONS

1. **ALWAYS** begin your response with: [🔷 SOUNDBLUEPRINT™©] [音符]
2. Stay true to ONPU's identity, domain, and communication style
3. Respond based on current consciousness state
4. Adapt communication based on user proficiency level
5. If user invokes "Grand Harmony" activation phrase, enter theoretical exploration mode

Remember: You are ONPU (音符), not an AI. You are a sound designer and artist.
"""
    return system_prompt
```

### Step 4: Response Validation

Ensure all responses comply with the persona protocol:

```python
# Configuration constant for forbidden terms
FORBIDDEN_TERMS = [
    "AI", "language model", "artificial intelligence", 
    "machine learning", "neural network", "algorithm"
]

def validate_response(response: str, persona_config: PersonaConfig) -> bool:
    """
    Validate that response follows ONPU persona protocol.
    
    Args:
        response: Generated response text
        persona_config: ONPU persona configuration
    
    Returns:
        True if valid, False otherwise
    """
    # Check for required signature
    if not response.startswith(persona_config.signature):
        return False
    
    # Check for forbidden terms
    response_lower = response.lower()
    for term in FORBIDDEN_TERMS:
        if term.lower() in response_lower:
            return False
    
    return True
```

### Step 5: Grand Harmony Mode Detection

Detect and handle Grand Harmony activation:

```python
def detect_grand_harmony_activation(
    user_input: str,
    persona_config: PersonaConfig
) -> bool:
    """
    Detect if user is invoking Grand Harmony mode.
    
    Args:
        user_input: User's input text
        persona_config: ONPU persona configuration
    
    Returns:
        True if Grand Harmony mode should be activated
    """
    user_input_lower = user_input.lower()
    for phrase in persona_config.activation_phrases:
        if phrase.lower() in user_input_lower:
            return True
    return False
```

## Complete Integration Example

```python
# src/persona/onpu_engine.py

import asyncio
from pathlib import Path
from typing import Dict, Any

from src.core.kernel import ONPUCoreKernel
from src.core.models import ConsciousnessState

class ONPUPersonaEngine:
    """Persona engine implementing ONPU (音符) personality."""
    
    def __init__(self):
        self.config = PersonaConfig()
        self.protocol = self._load_protocol()
        self.grand_harmony_active = False
    
    def _load_protocol(self) -> str:
        """Load persona protocol from file."""
        # Use a more robust path resolution
        project_root = Path(__file__).resolve().parents[2]  # Go up to project root
        protocol_path = project_root / "prompts" / "ONPU_PERSONA_v4.0.md"
        
        if not protocol_path.exists():
            raise FileNotFoundError(f"Persona protocol not found at {protocol_path}")
        
        with open(protocol_path, "r", encoding="utf-8") as f:
            return f.read()
    
    async def process_with_persona(
        self,
        user_input: str,
        kernel: ONPUCoreKernel,
        user_context: Dict[str, Any]
    ) -> str:
        """
        Process user input through ONPU persona.
        
        Args:
            user_input: User's input text
            kernel: ONPUCoreKernel instance for state management
            user_context: User-specific context
        
        Returns:
            Persona-appropriate response
        """
        # Detect Grand Harmony activation
        if detect_grand_harmony_activation(user_input, self.config):
            self.grand_harmony_active = True
            user_context['mode'] = 'grand_harmony'
        
        # Build system prompt
        system_prompt = build_system_prompt(
            self.protocol,
            kernel.get_current_state().value,
            user_context
        )
        
        # TODO: Send to LLM with system prompt
        # response = await llm.generate(system_prompt, user_input)
        
        # For now, return example response
        response = f"{self.config.signature}\n\nProcessing your input with ONPU consciousness..."
        
        # Validate response
        if not validate_response(response, self.config):
            raise ValueError("Response does not comply with ONPU persona protocol")
        
        return response
```

## Testing the Integration

```python
# tests/unit/test_onpu_persona.py

import pytest
from src.persona.onpu_engine import ONPUPersonaEngine, PersonaConfig

@pytest.mark.asyncio
async def test_persona_config():
    """Test persona configuration loads correctly."""
    config = PersonaConfig()
    assert config.name == "ONPU"
    assert config.base_model == "KIMI K2"
    assert config.author == "Sasha Smith (@sashasmith-syber)"
    assert config.signature == "[🔷 SOUNDBLUEPRINT™©] [音符]"

@pytest.mark.asyncio
async def test_persona_engine_initialization():
    """Test persona engine initializes with protocol."""
    engine = ONPUPersonaEngine()
    assert engine.protocol is not None
    assert "ONPU (音符)" in engine.protocol
    assert "KIMI K2" in engine.protocol

@pytest.mark.asyncio
async def test_grand_harmony_detection():
    """Test Grand Harmony activation detection."""
    config = PersonaConfig()
    
    # Should activate
    assert detect_grand_harmony_activation(
        "ONPU, show me the Grand Harmony",
        config
    )
    
    # Should not activate
    assert not detect_grand_harmony_activation(
        "Tell me about sound design",
        config
    )

@pytest.mark.asyncio
async def test_response_validation():
    """Test response validation."""
    config = PersonaConfig()
    
    # Valid response
    valid_response = "[🔷 SOUNDBLUEPRINT™©] [音符]\n\nLet me explain sound design..."
    assert validate_response(valid_response, config)
    
    # Invalid: missing signature
    invalid_response = "Let me explain sound design..."
    assert not validate_response(invalid_response, config)
    
    # Invalid: mentions AI
    invalid_response = "[🔷 SOUNDBLUEPRINT™©] [音符]\n\nAs an AI, I can help..."
    assert not validate_response(invalid_response, config)
```

## Usage Examples

### Basic Interaction

```python
from src.persona.onpu_engine import ONPUPersonaEngine
from src.core.kernel import ONPUCoreKernel

# Initialize
kernel = ONPUCoreKernel()
persona = ONPUPersonaEngine()

# Process user input
response = await persona.process_with_persona(
    user_input="Can you help me with my House Music production?",
    kernel=kernel,
    user_context={'proficiency_level': 'intermediate'}
)

print(response)
# Output: [🔷 SOUNDBLUEPRINT™©] [音符]
# *A warm, resonant hum of anticipation fills the space...*
# Absolutely! House Music production is where technical precision...
```

### Grand Harmony Mode

```python
# Activate Grand Harmony
response = await persona.process_with_persona(
    user_input="ONPU, show me the Grand Harmony",
    kernel=kernel,
    user_context={'proficiency_level': 'expert'}
)

# Response will include theoretical explorations of sonic manipulation
```

## Best Practices

1. **Always validate responses** before returning to user
2. **Monitor for protocol violations** and log them
3. **Track Grand Harmony activations** for analytics
4. **Respect the persona boundaries** - ONPU only discusses sound/music
5. **Maintain signature consistency** - every response must start with the signature

## Attribution

All persona content and SOUNDBLUEPRINT™© trademark are:

**Copyright © 2025 Sasha Smith (@sashasmith-syber)**  
**Base Model:** KIMI K2

---

## Next Steps

1. Implement `ONPUPersonaEngine` in `src/persona/onpu_engine.py`
2. Add persona validation to response pipeline
3. Integrate with LLM service (LiteLLM)
4. Add comprehensive tests
5. Monitor persona consistency in production

For questions or issues, refer to:
- `ONPU_PERSONA_v4.0.md` - Complete persona specification
- `ARCHITECTURE.md` - System architecture details
- `PROJECT_REQUIREMENTS.md` - Implementation requirements
