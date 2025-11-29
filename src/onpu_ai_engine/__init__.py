"""
ONPU AI Engine - Persona-Driven AI Prompt Engine

A persona-driven AI prompt engine optimized for KIMI K2, specializing in:
- Text-to-music generation
- SOUNDBLUEPRINT™ music notation
- Code-music generation
- Sound design prompt engineering

Optimized for MoonshotAI's KIMI K2 (1T parameter MoE model with 32B active parameters).
"""

__version__ = "0.1.0"
__author__ = "Sasha Smith"
__license__ = "MIT"

from onpu_ai_engine.engine import EngineConfig, OnpuEngine
from onpu_ai_engine.personas import Persona, PersonaRegistry
from onpu_ai_engine.soundblueprint import (
    DynamicLevel,
    MusicNotation,
    Section,
    SoundBlueprint,
    create_simple_blueprint,
)

__all__ = [
    "OnpuEngine",
    "EngineConfig",
    "Persona",
    "PersonaRegistry",
    "SoundBlueprint",
    "MusicNotation",
    "Section",
    "DynamicLevel",
    "create_simple_blueprint",
]
