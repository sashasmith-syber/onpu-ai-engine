"""
ONPU AI Engine - SOUNDBLUEPRINT™ Notation System

A structured notation system for describing music to AI models,
optimized for KIMI K2's comprehension and generation capabilities.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class DynamicLevel(Enum):
    """Musical dynamic levels."""

    PIANISSIMO = "pp"
    PIANO = "p"
    MEZZO_PIANO = "mp"
    MEZZO_FORTE = "mf"
    FORTE = "f"
    FORTISSIMO = "ff"

    def __str__(self) -> str:
        return self.value


class TextureType(Enum):
    """Musical texture density."""

    SPARSE = "sparse"
    MODERATE = "moderate"
    DENSE = "dense"

    def __str__(self) -> str:
        return self.value


@dataclass
class Section:
    """
    A section of music in SOUNDBLUEPRINT™ notation.

    Represents a time-bounded segment of a musical piece
    with specific characteristics.
    """

    name: str
    start_time: str
    end_time: str
    instruments: list[str] = field(default_factory=list)
    dynamics: DynamicLevel = DynamicLevel.MEZZO_FORTE
    texture: TextureType = TextureType.MODERATE
    melody_description: str = ""
    harmony: str = ""
    rhythm: str = ""
    notes: str = ""

    def to_notation(self) -> str:
        """Convert section to SOUNDBLUEPRINT™ notation string."""
        lines = [f"Section: {self.name} ({self.start_time}-{self.end_time})"]

        if self.instruments:
            lines.append(f"  Instruments: {', '.join(self.instruments)}")

        lines.append(f"  Dynamics: {self.dynamics}")
        lines.append(f"  Texture: {self.texture}")

        if self.melody_description:
            lines.append(f"  Melody: {self.melody_description}")

        if self.harmony:
            lines.append(f"  Harmony: {self.harmony}")

        if self.rhythm:
            lines.append(f"  Rhythm: {self.rhythm}")

        if self.notes:
            lines.append(f"  Notes: {self.notes}")

        return "\n".join(lines)

    def to_dict(self) -> dict[str, Any]:
        """Convert section to dictionary."""
        return {
            "name": self.name,
            "timing": f"{self.start_time}-{self.end_time}",
            "instruments": self.instruments,
            "dynamics": str(self.dynamics),
            "texture": str(self.texture),
            "melody": self.melody_description,
            "harmony": self.harmony,
            "rhythm": self.rhythm,
            "notes": self.notes,
        }


@dataclass
class MusicNotation:
    """
    音符 (Onpu) Music Notation container.

    Represents the detailed musical notation for a piece,
    including note-level information.
    """

    notes: list[str] = field(default_factory=list)
    articulations: list[str] = field(default_factory=list)
    expressions: list[str] = field(default_factory=list)

    # Visual notation symbols
    DENSITY_SPARSE = "○"
    DENSITY_MODERATE = "◐"
    DENSITY_DENSE = "●"
    CONTOUR_UP = "↑"
    CONTOUR_DOWN = "↓"
    SWELL_START = "⟨"
    SWELL_END = "⟩"
    SUSTAIN = "≈"
    RHYTHM_SINGLE = "♪"
    RHYTHM_DOUBLE = "♫"

    def add_note(self, note: str) -> None:
        """Add a note to the notation."""
        self.notes.append(note)

    def add_articulation(self, articulation: str) -> None:
        """Add an articulation marking."""
        self.articulations.append(articulation)

    def add_expression(self, expression: str) -> None:
        """Add an expression marking."""
        self.expressions.append(expression)

    def to_string(self) -> str:
        """Convert to notation string."""
        parts = ["[音符 NOTATION]"]

        if self.notes:
            parts.append(f"Notes: {' '.join(self.notes)}")

        if self.articulations:
            parts.append(f"Articulations: {', '.join(self.articulations)}")

        if self.expressions:
            parts.append(f"Expressions: {', '.join(self.expressions)}")

        return "\n".join(parts)

    def create_density_pattern(
        self, levels: list[str], duration_seconds: float = 60
    ) -> str:
        """
        Create a visual density pattern.

        Args:
            levels: List of density levels ("sparse", "moderate", "dense")
            duration_seconds: Total duration in seconds

        Returns:
            Visual pattern string
        """
        symbol_map = {
            "sparse": self.DENSITY_SPARSE,
            "moderate": self.DENSITY_MODERATE,
            "dense": self.DENSITY_DENSE,
        }
        pattern = [symbol_map.get(level, self.DENSITY_MODERATE) for level in levels]
        return " ".join(pattern)

    def create_contour_pattern(self, directions: list[str]) -> str:
        """
        Create a melodic contour pattern.

        Args:
            directions: List of directions ("up", "down", "stable")

        Returns:
            Visual contour string
        """
        symbol_map = {"up": self.CONTOUR_UP, "down": self.CONTOUR_DOWN, "stable": "—"}
        pattern = [symbol_map.get(d, "—") for d in directions]
        return "".join(pattern)


@dataclass
class SoundBlueprint:
    """
    🔷 SOUNDBLUEPRINT™ - Complete music description format.

    A comprehensive format for describing music to AI models,
    optimized for KIMI K2's understanding and generation.

    Example:
        >>> blueprint = SoundBlueprint(
        ...     title="Calm Morning",
        ...     genre="ambient",
        ...     mood="peaceful",
        ...     tempo=72
        ... )
        >>> blueprint.add_section(Section(
        ...     name="Intro",
        ...     start_time="0:00",
        ...     end_time="0:30",
        ...     instruments=["piano", "strings"],
        ...     dynamics=DynamicLevel.PIANO
        ... ))
        >>> print(blueprint.to_prompt())
    """

    title: str = ""
    genre: str = ""
    mood: str = ""
    tempo: int = 120
    time_signature: str = "4/4"
    key: str = "C major"
    duration: str = ""
    sections: list[Section] = field(default_factory=list)
    notation: MusicNotation = field(default_factory=MusicNotation)
    references: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)

    def add_section(self, section: Section) -> None:
        """Add a section to the blueprint."""
        self.sections.append(section)

    def add_reference(self, reference: str) -> None:
        """Add a reference track or style."""
        self.references.append(reference)

    def add_tag(self, tag: str) -> None:
        """Add a descriptive tag."""
        self.tags.append(tag)

    def to_prompt(self) -> str:
        """
        Convert the blueprint to a KIMI K2-optimized prompt.

        Returns:
            Formatted SOUNDBLUEPRINT™ prompt string
        """
        lines = ["[🔷 SOUNDBLUEPRINT™]"]

        # Header section
        if self.title:
            lines.append(f"Title: {self.title}")
        if self.genre:
            lines.append(f"Genre: {self.genre}")
        if self.mood:
            lines.append(f"Mood: {self.mood}")
        lines.append(f"Tempo: {self.tempo} BPM")
        lines.append(f"Time Signature: {self.time_signature}")
        lines.append(f"Key: {self.key}")
        if self.duration:
            lines.append(f"Duration: {self.duration}")

        # Tags
        if self.tags:
            lines.append(f"Tags: {', '.join(self.tags)}")

        # References
        if self.references:
            lines.append(f"References: {', '.join(self.references)}")

        # Sections
        if self.sections:
            lines.append("\n[音符 SECTIONS]")
            for section in self.sections:
                lines.append(section.to_notation())

        # Notation details
        if self.notation.notes or self.notation.articulations:
            lines.append(f"\n{self.notation.to_string()}")

        return "\n".join(lines)

    def to_dict(self) -> dict[str, Any]:
        """Convert blueprint to dictionary."""
        return {
            "title": self.title,
            "genre": self.genre,
            "mood": self.mood,
            "tempo": self.tempo,
            "time_signature": self.time_signature,
            "key": self.key,
            "duration": self.duration,
            "sections": [s.to_dict() for s in self.sections],
            "references": self.references,
            "tags": self.tags,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "SoundBlueprint":
        """Create a SoundBlueprint from dictionary."""
        blueprint = cls(
            title=data.get("title", ""),
            genre=data.get("genre", ""),
            mood=data.get("mood", ""),
            tempo=data.get("tempo", 120),
            time_signature=data.get("time_signature", "4/4"),
            key=data.get("key", "C major"),
            duration=data.get("duration", ""),
            references=data.get("references", []),
            tags=data.get("tags", []),
        )

        # Add sections
        for section_data in data.get("sections", []):
            timing = section_data.get("timing", "0:00-0:30")
            times = timing.split("-")
            start_time = times[0] if len(times) > 0 else "0:00"
            end_time = times[1] if len(times) > 1 else "0:30"

            section = Section(
                name=section_data.get("name", "Section"),
                start_time=start_time,
                end_time=end_time,
                instruments=section_data.get("instruments", []),
                dynamics=DynamicLevel(section_data.get("dynamics", "mf")),
                melody_description=section_data.get("melody", ""),
                harmony=section_data.get("harmony", ""),
                rhythm=section_data.get("rhythm", ""),
                notes=section_data.get("notes", ""),
            )
            blueprint.add_section(section)

        return blueprint


def create_simple_blueprint(
    description: str,
    genre: str = "",
    mood: str = "",
    tempo: int = 120,
    duration: str = "2:00",
) -> SoundBlueprint:
    """
    Create a simple SOUNDBLUEPRINT™ from a text description.

    Args:
        description: Natural language description of the music
        genre: Musical genre
        mood: Desired mood
        tempo: BPM
        duration: Target duration

    Returns:
        A SoundBlueprint with a single section
    """
    blueprint = SoundBlueprint(
        title=description[:50] if len(description) > 50 else description,
        genre=genre,
        mood=mood,
        tempo=tempo,
        duration=duration,
    )

    # Create a simple intro-main-outro structure
    sections = [
        Section(
            name="Intro",
            start_time="0:00",
            end_time="0:20",
            dynamics=DynamicLevel.PIANO,
            texture=TextureType.SPARSE,
            melody_description="Opening theme introduction",
        ),
        Section(
            name="Main",
            start_time="0:20",
            end_time="1:40",
            dynamics=DynamicLevel.MEZZO_FORTE,
            texture=TextureType.MODERATE,
            melody_description=description,
        ),
        Section(
            name="Outro",
            start_time="1:40",
            end_time="2:00",
            dynamics=DynamicLevel.PIANO,
            texture=TextureType.SPARSE,
            melody_description="Gentle fade and resolution",
        ),
    ]

    for section in sections:
        blueprint.add_section(section)

    return blueprint
