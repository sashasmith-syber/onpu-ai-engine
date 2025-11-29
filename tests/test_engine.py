"""
ONPU AI Engine - Test Suite for Engine Module
"""

import pytest
from onpu_ai_engine.engine import PromptEngine, Persona, GenerationResult, DEFAULT_PERSONAS


class TestPersona:
    """Tests for the Persona model."""
    
    def test_persona_creation(self):
        """Test creating a persona with default values."""
        persona = Persona(name="test")
        assert persona.name == "test"
        assert persona.style == "neutral"
        assert persona.temperature == 0.7
    
    def test_persona_custom_values(self):
        """Test creating a persona with custom values."""
        persona = Persona(
            name="custom",
            description="Custom persona",
            style="jazz",
            temperature=0.9,
            system_prompt="You are a jazz musician.",
        )
        assert persona.name == "custom"
        assert persona.style == "jazz"
        assert persona.temperature == 0.9
    
    def test_default_personas_exist(self):
        """Test that default personas are defined."""
        assert "default" in DEFAULT_PERSONAS
        assert "ambient" in DEFAULT_PERSONAS
        assert "electronic" in DEFAULT_PERSONAS
        assert "orchestral" in DEFAULT_PERSONAS
        assert "soundblueprint" in DEFAULT_PERSONAS


class TestPromptEngine:
    """Tests for the PromptEngine class."""
    
    def test_engine_initialization(self):
        """Test engine initialization with default persona."""
        engine = PromptEngine()
        assert engine.current_persona.name == "default"
    
    def test_engine_with_specific_persona(self):
        """Test engine initialization with specific persona."""
        engine = PromptEngine(persona="ambient")
        assert engine.current_persona.name == "ambient"
    
    def test_engine_invalid_persona(self):
        """Test engine initialization with invalid persona."""
        with pytest.raises(ValueError):
            PromptEngine(persona="nonexistent")
    
    def test_set_persona(self):
        """Test changing the persona."""
        engine = PromptEngine()
        engine.set_persona("electronic")
        assert engine.current_persona.name == "electronic"
    
    def test_generate_returns_result(self):
        """Test that generate returns a GenerationResult."""
        engine = PromptEngine()
        result = engine.generate("Create ambient music")
        
        assert isinstance(result, GenerationResult)
        assert result.prompt == "Create ambient music"
        assert result.persona == "default"
        assert len(result.output) > 0
    
    def test_generate_with_different_personas(self):
        """Test generation with different personas."""
        engine = PromptEngine(persona="soundblueprint")
        result = engine.generate("Create experimental soundscape")
        
        assert result.persona == "soundblueprint"
        assert "SOUNDBLUEPRINT" in result.output
    
    def test_list_personas(self):
        """Test listing available personas."""
        engine = PromptEngine()
        personas = engine.list_personas()
        
        assert isinstance(personas, dict)
        assert "default" in personas
        assert len(personas) >= 5
    
    def test_custom_persona_registration(self):
        """Test registering custom personas."""
        custom = {
            "jazz": Persona(
                name="jazz",
                description="Jazz music specialist",
                style="jazz",
            )
        }
        engine = PromptEngine(custom_personas=custom)
        
        assert "jazz" in engine.personas
        engine.set_persona("jazz")
        assert engine.current_persona.name == "jazz"
