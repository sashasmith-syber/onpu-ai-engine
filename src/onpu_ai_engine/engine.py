"""
ONPU AI Engine - Core Engine Module

The main engine class for persona-driven AI interactions,
optimized for KIMI K2's agentic intelligence capabilities.
"""

import json
from dataclasses import dataclass, field
from typing import Any

from onpu_ai_engine.personas import Persona, PersonaRegistry
from onpu_ai_engine.tools import ToolRegistry


@dataclass
class EngineConfig:
    """Configuration for the ONPU AI Engine."""

    # KIMI K2 recommended settings
    temperature: float = 0.6
    max_tokens: int = 4096
    model: str = "moonshotai/Kimi-K2-Instruct"

    # API configuration
    api_base: str = "https://api.moonshot.cn/v1"
    api_key: str = ""

    # Engine settings
    enable_tool_calling: bool = True
    enable_streaming: bool = True
    context_length: int = 128000

    def to_dict(self) -> dict[str, Any]:
        """Convert config to dictionary."""
        return {
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "model": self.model,
            "api_base": self.api_base,
            "enable_tool_calling": self.enable_tool_calling,
            "enable_streaming": self.enable_streaming,
            "context_length": self.context_length,
        }


@dataclass
class Message:
    """A message in the conversation."""

    role: str
    content: str | list[dict[str, Any]]
    name: str | None = None
    tool_call_id: str | None = None
    tool_calls: list[dict[str, Any]] | None = None

    def to_dict(self) -> dict[str, Any]:
        """Convert message to API-compatible dictionary."""
        msg = {"role": self.role, "content": self.content}
        if self.name:
            msg["name"] = self.name
        if self.tool_call_id:
            msg["tool_call_id"] = self.tool_call_id
        if self.tool_calls:
            msg["tool_calls"] = self.tool_calls
        return msg


@dataclass
class Conversation:
    """A conversation with the AI engine."""

    messages: list[Message] = field(default_factory=list)
    persona: Persona | None = None

    def add_message(self, role: str, content: str, **kwargs: Any) -> None:
        """Add a message to the conversation."""
        self.messages.append(Message(role=role, content=content, **kwargs))

    def get_system_prompt(self) -> str:
        """Get the system prompt including persona."""
        if self.persona:
            return self.persona.get_system_prompt()
        return (
            "You are ONPU, an AI assistant specialized in music generation "
            "and sound design, created by ONPU AI."
        )

    def to_messages(self) -> list[dict[str, Any]]:
        """Convert conversation to API-compatible messages list."""
        messages = [{"role": "system", "content": self.get_system_prompt()}]
        messages.extend([msg.to_dict() for msg in self.messages])
        return messages


class OnpuEngine:
    """
    ONPU AI Engine - Persona-Driven AI for Music and Sound Generation.

    This engine is optimized for KIMI K2's agentic intelligence capabilities,
    providing specialized support for:
    - Text-to-music prompts
    - SOUNDBLUEPRINT™ notation system
    - Code-music generation
    - Sound design engineering

    Example:
        >>> engine = OnpuEngine()
        >>> engine.set_persona("composer")
        >>> response = engine.generate("Create a calm piano melody")
    """

    def __init__(self, config: EngineConfig | None = None) -> None:
        """Initialize the ONPU AI Engine."""
        self.config = config or EngineConfig()
        self.persona_registry = PersonaRegistry()
        self.tool_registry = ToolRegistry()
        self.conversation = Conversation()
        self._client: Any = None

    def set_api_key(self, api_key: str) -> None:
        """Set the API key for KIMI K2."""
        self.config.api_key = api_key

    def set_persona(self, persona_name: str) -> None:
        """Set the active persona for the engine."""
        persona = self.persona_registry.get(persona_name)
        if persona:
            self.conversation.persona = persona

    def create_persona(
        self,
        name: str,
        description: str,
        system_prompt: str,
        expertise: list[str] | None = None,
    ) -> Persona:
        """Create and register a new persona."""
        persona = Persona(
            name=name,
            description=description,
            system_prompt=system_prompt,
            expertise=expertise or [],
        )
        self.persona_registry.register(persona)
        return persona

    def add_tool(
        self,
        name: str,
        description: str,
        parameters: dict[str, Any],
        handler: Any,
    ) -> None:
        """Register a tool for the engine to use."""
        self.tool_registry.register(
            name=name,
            description=description,
            parameters=parameters,
            handler=handler,
        )

    def get_tools_schema(self) -> list[dict[str, Any]]:
        """Get the OpenAI-compatible tools schema."""
        return self.tool_registry.get_schema()

    def new_conversation(self, persona_name: str | None = None) -> Conversation:
        """Start a new conversation, optionally with a persona."""
        self.conversation = Conversation()
        if persona_name:
            self.set_persona(persona_name)
        return self.conversation

    def add_user_message(self, content: str) -> None:
        """Add a user message to the conversation."""
        self.conversation.add_message("user", content)

    def add_assistant_message(self, content: str) -> None:
        """Add an assistant message to the conversation."""
        self.conversation.add_message("assistant", content)

    def get_request_payload(self) -> dict[str, Any]:
        """
        Get the request payload for the KIMI K2 API.

        Returns a dictionary ready to be sent to the chat completions endpoint.
        """
        payload: dict[str, Any] = {
            "model": self.config.model,
            "messages": self.conversation.to_messages(),
            "temperature": self.config.temperature,
            "max_tokens": self.config.max_tokens,
        }

        if self.config.enable_tool_calling:
            tools = self.get_tools_schema()
            if tools:
                payload["tools"] = tools
                payload["tool_choice"] = "auto"

        return payload

    def format_soundblueprint_prompt(
        self,
        sections: list[dict[str, Any]],
        genre: str | None = None,
        mood: str | None = None,
        tempo: int | None = None,
    ) -> str:
        """
        Format a SOUNDBLUEPRINT™ prompt for music generation.

        Args:
            sections: List of section definitions with timing and notation
            genre: Musical genre (e.g., "classical", "electronic")
            mood: Desired mood (e.g., "calm", "energetic")
            tempo: BPM (beats per minute)

        Returns:
            Formatted SOUNDBLUEPRINT™ prompt string
        """
        prompt_parts = ["[🔷 SOUNDBLUEPRINT™ NOTATION]"]

        if genre:
            prompt_parts.append(f"Genre: {genre}")
        if mood:
            prompt_parts.append(f"Mood: {mood}")
        if tempo:
            prompt_parts.append(f"Tempo: {tempo} BPM")

        prompt_parts.append("\n[音符] Musical Sections:")

        for i, section in enumerate(sections, 1):
            timing = section.get("timing", "")
            notation = section.get("notation", "")
            dynamics = section.get("dynamics", "")
            instruments = section.get("instruments", [])

            section_text = f"\nSection {i}"
            if timing:
                section_text += f" ({timing})"
            section_text += ":"
            if notation:
                section_text += f"\n  Notation: {notation}"
            if dynamics:
                section_text += f"\n  Dynamics: {dynamics}"
            if instruments:
                section_text += f"\n  Instruments: {', '.join(instruments)}"

            prompt_parts.append(section_text)

        return "\n".join(prompt_parts)

    def generate_music_prompt(
        self,
        description: str,
        style: str | None = None,
        duration: str | None = None,
        instruments: list[str] | None = None,
    ) -> str:
        """
        Generate an optimized music generation prompt.

        Args:
            description: Natural language description of desired music
            style: Musical style or genre
            duration: Desired duration
            instruments: List of instruments to include

        Returns:
            Optimized prompt for music generation AI
        """
        prompt_parts = [f"[🎵 Music Generation Request]\n{description}"]

        if style:
            prompt_parts.append(f"\nStyle: {style}")
        if duration:
            prompt_parts.append(f"Duration: {duration}")
        if instruments:
            prompt_parts.append(f"Instruments: {', '.join(instruments)}")

        return "\n".join(prompt_parts)

    def to_json(self) -> str:
        """Export the current state as JSON."""
        state = {
            "config": self.config.to_dict(),
            "persona": self.conversation.persona.to_dict()
            if self.conversation.persona
            else None,
            "messages": [msg.to_dict() for msg in self.conversation.messages],
            "tools": self.get_tools_schema(),
        }
        return json.dumps(state, indent=2)
