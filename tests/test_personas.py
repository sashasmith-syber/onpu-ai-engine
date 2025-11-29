"""Tests for the ONPU AI Engine personas module."""

from onpu_ai_engine.personas import Persona, PersonaRegistry


class TestPersona:
    """Tests for Persona class."""

    def test_persona_creation(self) -> None:
        """Test creating a persona."""
        persona = Persona(
            name="test",
            description="Test persona",
            system_prompt="You are a test assistant.",
        )
        assert persona.name == "test"
        assert persona.description == "Test persona"

    def test_get_system_prompt(self) -> None:
        """Test getting system prompt."""
        persona = Persona(
            name="test",
            description="Test",
            system_prompt="Base prompt",
            expertise=["testing", "validation"],
            style="Professional",
        )
        prompt = persona.get_system_prompt()
        assert "Base prompt" in prompt
        assert "testing" in prompt
        assert "Professional" in prompt

    def test_persona_to_dict(self) -> None:
        """Test persona serialization."""
        persona = Persona(
            name="test",
            description="Test",
            system_prompt="Prompt",
        )
        data = persona.to_dict()
        assert data["name"] == "test"
        assert data["description"] == "Test"

    def test_persona_from_dict(self) -> None:
        """Test persona deserialization."""
        data = {
            "name": "restored",
            "description": "Restored persona",
            "system_prompt": "Restored prompt",
            "expertise": ["restoration"],
        }
        persona = Persona.from_dict(data)
        assert persona.name == "restored"
        assert "restoration" in persona.expertise


class TestPersonaRegistry:
    """Tests for PersonaRegistry class."""

    def test_builtin_personas(self) -> None:
        """Test built-in personas are registered."""
        registry = PersonaRegistry()
        personas = registry.list_personas()
        assert "composer" in personas
        assert "sound_designer" in personas
        assert "producer" in personas
        assert "code_musician" in personas
        assert "soundblueprint" in personas

    def test_get_persona(self) -> None:
        """Test getting a persona."""
        registry = PersonaRegistry()
        composer = registry.get("composer")
        assert composer is not None
        assert composer.name == "composer"

    def test_register_custom_persona(self) -> None:
        """Test registering a custom persona."""
        registry = PersonaRegistry()
        persona = Persona(
            name="custom",
            description="Custom persona",
            system_prompt="Custom prompt",
        )
        registry.register(persona)
        assert registry.get("custom") is not None

    def test_remove_persona(self) -> None:
        """Test removing a persona."""
        registry = PersonaRegistry()
        persona = Persona(
            name="to_remove",
            description="Temporary",
            system_prompt="Temp",
        )
        registry.register(persona)
        assert registry.get("to_remove") is not None
        result = registry.remove("to_remove")
        assert result is True
        assert registry.get("to_remove") is None

    def test_get_all_personas(self) -> None:
        """Test getting all personas."""
        registry = PersonaRegistry()
        all_personas = registry.get_all()
        assert len(all_personas) >= 5  # At least the built-in ones
