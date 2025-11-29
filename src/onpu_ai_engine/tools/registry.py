"""
ONPU AI Engine - Tool Registry

Manages tools for KIMI K2's agentic tool-calling capabilities.
"""

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any


@dataclass
class Tool:
    """
    A tool that can be called by KIMI K2.

    Tools enable the AI to interact with external systems,
    such as music generation APIs, DAWs, or notation software.
    """

    name: str
    description: str
    parameters: dict[str, Any]
    handler: Callable[..., Any]

    def to_schema(self) -> dict[str, Any]:
        """Convert tool to OpenAI-compatible schema."""
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.parameters,
            },
        }

    def execute(self, **kwargs: Any) -> Any:
        """Execute the tool with the given arguments."""
        return self.handler(**kwargs)


class ToolRegistry:
    """
    Registry for managing tools in the ONPU AI Engine.

    Tools are registered with their schemas and handlers,
    allowing KIMI K2 to call them during conversations.
    """

    def __init__(self) -> None:
        """Initialize the tool registry."""
        self._tools: dict[str, Tool] = {}
        self._register_builtin_tools()

    def _register_builtin_tools(self) -> None:
        """Register built-in music and sound tools."""
        # Generate SOUNDBLUEPRINT tool
        self.register(
            name="generate_soundblueprint",
            description="Generate a SOUNDBLUEPRINT™ music notation from a text description",
            parameters={
                "type": "object",
                "required": ["description"],
                "properties": {
                    "description": {
                        "type": "string",
                        "description": "Natural language description of the desired music",
                    },
                    "genre": {
                        "type": "string",
                        "description": "Musical genre (e.g., classical, electronic, jazz)",
                    },
                    "mood": {
                        "type": "string",
                        "description": "Desired mood (e.g., calm, energetic, melancholic)",
                    },
                    "tempo": {
                        "type": "integer",
                        "description": "Tempo in BPM (beats per minute)",
                    },
                    "duration": {
                        "type": "string",
                        "description": "Desired duration (e.g., '2:30' for 2 minutes 30 seconds)",
                    },
                },
            },
            handler=self._generate_soundblueprint_handler,
        )

        # Analyze music tool
        self.register(
            name="analyze_music_description",
            description="Analyze a music description and extract key parameters",
            parameters={
                "type": "object",
                "required": ["description"],
                "properties": {
                    "description": {
                        "type": "string",
                        "description": "Music description to analyze",
                    },
                },
            },
            handler=self._analyze_music_handler,
        )

        # Convert notation tool
        self.register(
            name="convert_notation",
            description="Convert between different notation formats",
            parameters={
                "type": "object",
                "required": ["input_notation", "target_format"],
                "properties": {
                    "input_notation": {
                        "type": "string",
                        "description": "The input notation string",
                    },
                    "target_format": {
                        "type": "string",
                        "enum": ["soundblueprint", "abc", "lilypond", "musicxml"],
                        "description": "Target notation format",
                    },
                },
            },
            handler=self._convert_notation_handler,
        )

    def _generate_soundblueprint_handler(
        self,
        description: str,
        genre: str = "",
        mood: str = "",
        tempo: int = 120,
        duration: str = "2:00",
    ) -> dict[str, Any]:
        """Handler for generating SOUNDBLUEPRINT notation."""
        from onpu_ai_engine.soundblueprint import create_simple_blueprint

        blueprint = create_simple_blueprint(
            description=description,
            genre=genre,
            mood=mood,
            tempo=tempo,
            duration=duration,
        )
        return {
            "blueprint": blueprint.to_dict(),
            "prompt": blueprint.to_prompt(),
        }

    def _analyze_music_handler(self, description: str) -> dict[str, Any]:
        """Handler for analyzing music descriptions."""
        # Simple keyword-based analysis
        analysis: dict[str, list[str]] = {
            "tempo_indicators": [],
            "mood_indicators": [],
            "genre_indicators": [],
            "instrument_indicators": [],
        }

        # Tempo keywords
        tempo_keywords = {
            "fast": ["fast", "quick", "upbeat", "energetic", "lively"],
            "slow": ["slow", "calm", "peaceful", "gentle", "relaxed"],
            "moderate": ["moderate", "medium", "steady"],
        }

        # Mood keywords
        mood_keywords = {
            "happy": ["happy", "joyful", "cheerful", "bright", "uplifting"],
            "sad": ["sad", "melancholic", "sorrowful", "lonely", "emotional"],
            "calm": ["calm", "peaceful", "serene", "tranquil", "relaxing"],
            "energetic": ["energetic", "powerful", "intense", "driving", "dynamic"],
        }

        desc_lower = description.lower()

        for category, keywords in tempo_keywords.items():
            for keyword in keywords:
                if keyword in desc_lower:
                    analysis["tempo_indicators"].append(category)
                    break

        for category, keywords in mood_keywords.items():
            for keyword in keywords:
                if keyword in desc_lower:
                    analysis["mood_indicators"].append(category)
                    break

        # Common instruments
        instruments = [
            "piano",
            "guitar",
            "drums",
            "bass",
            "violin",
            "strings",
            "synth",
            "synthesizer",
            "vocal",
            "voice",
            "trumpet",
            "saxophone",
            "flute",
        ]
        for instrument in instruments:
            if instrument in desc_lower:
                analysis["instrument_indicators"].append(instrument)

        return analysis

    def _convert_notation_handler(
        self, input_notation: str, target_format: str
    ) -> dict[str, Any]:
        """Handler for converting notation formats."""
        # Placeholder implementation
        return {
            "original": input_notation,
            "target_format": target_format,
            "converted": f"[Converted to {target_format}]\n{input_notation}",
            "status": "conversion_placeholder",
        }

    def register(
        self,
        name: str,
        description: str,
        parameters: dict[str, Any],
        handler: Callable[..., Any],
    ) -> None:
        """Register a tool in the registry."""
        tool = Tool(
            name=name,
            description=description,
            parameters=parameters,
            handler=handler,
        )
        self._tools[name] = tool

    def get(self, name: str) -> Tool | None:
        """Get a tool by name."""
        return self._tools.get(name)

    def get_schema(self) -> list[dict[str, Any]]:
        """Get all tool schemas for the API."""
        return [tool.to_schema() for tool in self._tools.values()]

    def execute(self, name: str, **kwargs: Any) -> Any:
        """Execute a tool by name."""
        tool = self._tools.get(name)
        if tool:
            return tool.execute(**kwargs)
        raise ValueError(f"Tool '{name}' not found")

    def list_tools(self) -> list[str]:
        """List all registered tool names."""
        return list(self._tools.keys())

    def remove(self, name: str) -> bool:
        """Remove a tool from the registry."""
        if name in self._tools:
            del self._tools[name]
            return True
        return False
