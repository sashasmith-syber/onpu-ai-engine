"""Tests for the ONPU AI Engine core module."""

import json

from onpu_ai_engine import OnpuEngine
from onpu_ai_engine.engine import Conversation, EngineConfig, Message


class TestEngineConfig:
    """Tests for EngineConfig."""

    def test_default_config(self) -> None:
        """Test default configuration values."""
        config = EngineConfig()
        assert config.temperature == 0.6
        assert config.max_tokens == 4096
        assert config.model == "moonshotai/Kimi-K2-Instruct"
        assert config.enable_tool_calling is True

    def test_custom_config(self) -> None:
        """Test custom configuration."""
        config = EngineConfig(
            temperature=0.8,
            max_tokens=2048,
            model="custom-model",
        )
        assert config.temperature == 0.8
        assert config.max_tokens == 2048
        assert config.model == "custom-model"

    def test_config_to_dict(self) -> None:
        """Test config serialization."""
        config = EngineConfig()
        config_dict = config.to_dict()
        assert "temperature" in config_dict
        assert "model" in config_dict


class TestMessage:
    """Tests for Message class."""

    def test_basic_message(self) -> None:
        """Test basic message creation."""
        msg = Message(role="user", content="Hello")
        assert msg.role == "user"
        assert msg.content == "Hello"

    def test_message_to_dict(self) -> None:
        """Test message serialization."""
        msg = Message(role="assistant", content="Hi there!")
        msg_dict = msg.to_dict()
        assert msg_dict["role"] == "assistant"
        assert msg_dict["content"] == "Hi there!"


class TestConversation:
    """Tests for Conversation class."""

    def test_add_message(self) -> None:
        """Test adding messages to conversation."""
        conv = Conversation()
        conv.add_message("user", "Hello")
        conv.add_message("assistant", "Hi!")
        assert len(conv.messages) == 2

    def test_get_system_prompt_default(self) -> None:
        """Test default system prompt."""
        conv = Conversation()
        prompt = conv.get_system_prompt()
        assert "ONPU" in prompt

    def test_to_messages(self) -> None:
        """Test converting conversation to messages list."""
        conv = Conversation()
        conv.add_message("user", "Test message")
        messages = conv.to_messages()
        assert len(messages) == 2  # system + user
        assert messages[0]["role"] == "system"
        assert messages[1]["role"] == "user"


class TestOnpuEngine:
    """Tests for OnpuEngine class."""

    def test_engine_initialization(self) -> None:
        """Test engine initialization."""
        engine = OnpuEngine()
        assert engine.config is not None
        assert engine.persona_registry is not None
        assert engine.tool_registry is not None

    def test_set_persona(self) -> None:
        """Test setting a persona."""
        engine = OnpuEngine()
        engine.set_persona("composer")
        assert engine.conversation.persona is not None
        assert engine.conversation.persona.name == "composer"

    def test_create_persona(self) -> None:
        """Test creating a custom persona."""
        engine = OnpuEngine()
        persona = engine.create_persona(
            name="test_persona",
            description="Test persona",
            system_prompt="You are a test persona.",
            expertise=["testing"],
        )
        assert persona.name == "test_persona"
        assert engine.persona_registry.get("test_persona") is not None

    def test_add_user_message(self) -> None:
        """Test adding a user message."""
        engine = OnpuEngine()
        engine.add_user_message("Hello")
        assert len(engine.conversation.messages) == 1
        assert engine.conversation.messages[0].content == "Hello"

    def test_new_conversation(self) -> None:
        """Test starting a new conversation."""
        engine = OnpuEngine()
        engine.add_user_message("Hello")
        engine.new_conversation()
        assert len(engine.conversation.messages) == 0

    def test_get_request_payload(self) -> None:
        """Test getting request payload."""
        engine = OnpuEngine()
        engine.set_persona("composer")
        engine.add_user_message("Create a melody")
        payload = engine.get_request_payload()
        assert "model" in payload
        assert "messages" in payload
        assert "temperature" in payload

    def test_generate_music_prompt(self) -> None:
        """Test generating a music prompt."""
        engine = OnpuEngine()
        prompt = engine.generate_music_prompt(
            description="A calm piano piece",
            style="classical",
            duration="2:00",
            instruments=["piano"],
        )
        assert "calm piano piece" in prompt
        assert "classical" in prompt
        assert "piano" in prompt

    def test_format_soundblueprint_prompt(self) -> None:
        """Test SOUNDBLUEPRINT prompt formatting."""
        engine = OnpuEngine()
        sections = [
            {"timing": "0:00-0:30", "notation": "Intro theme"},
            {"timing": "0:30-1:00", "notation": "Main melody"},
        ]
        prompt = engine.format_soundblueprint_prompt(
            sections=sections, genre="ambient", mood="calm", tempo=72
        )
        assert "SOUNDBLUEPRINT" in prompt
        assert "ambient" in prompt
        assert "72 BPM" in prompt

    def test_to_json(self) -> None:
        """Test JSON serialization."""
        engine = OnpuEngine()
        engine.set_persona("composer")
        engine.add_user_message("Test")
        json_str = engine.to_json()
        data = json.loads(json_str)
        assert "config" in data
        assert "persona" in data
        assert "messages" in data
