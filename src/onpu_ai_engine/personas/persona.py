"""
ONPU AI Engine - Persona Definition

Defines the Persona class for persona-driven AI interactions.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Persona:
    """
    A persona represents a specialized AI role with specific expertise.

    Personas are optimized for KIMI K2's agentic intelligence,
    allowing the model to adopt specific roles for music and sound tasks.

    Attributes:
        name: Unique identifier for the persona
        description: Human-readable description
        system_prompt: The system prompt that defines the persona's behavior
        expertise: List of areas of expertise
        style: Optional style guidelines
        constraints: Optional behavioral constraints
    """

    name: str
    description: str
    system_prompt: str
    expertise: list[str] = field(default_factory=list)
    style: str | None = None
    constraints: list[str] = field(default_factory=list)

    def get_system_prompt(self) -> str:
        """
        Generate the full system prompt for this persona.

        Returns:
            Complete system prompt including persona definition and capabilities
        """
        prompt_parts = [self.system_prompt]

        if self.expertise:
            prompt_parts.append(f"\n\nAreas of Expertise: {', '.join(self.expertise)}")

        if self.style:
            prompt_parts.append(f"\n\nCommunication Style: {self.style}")

        if self.constraints:
            prompt_parts.append(
                "\n\nBehavioral Guidelines:\n- "
                + "\n- ".join(self.constraints)
            )

        return "".join(prompt_parts)

    def to_dict(self) -> dict[str, Any]:
        """Convert persona to dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "system_prompt": self.system_prompt,
            "expertise": self.expertise,
            "style": self.style,
            "constraints": self.constraints,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Persona":
        """Create a persona from a dictionary."""
        return cls(
            name=data["name"],
            description=data["description"],
            system_prompt=data["system_prompt"],
            expertise=data.get("expertise", []),
            style=data.get("style"),
            constraints=data.get("constraints", []),
        )
