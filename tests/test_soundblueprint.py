"""Tests for the ONPU AI Engine SOUNDBLUEPRINT module."""

from onpu_ai_engine.soundblueprint import (
    DynamicLevel,
    MusicNotation,
    Section,
    SoundBlueprint,
)
from onpu_ai_engine.soundblueprint.notation import create_simple_blueprint


class TestDynamicLevel:
    """Tests for DynamicLevel enum."""

    def test_dynamic_values(self) -> None:
        """Test dynamic level string values."""
        assert str(DynamicLevel.PIANISSIMO) == "pp"
        assert str(DynamicLevel.PIANO) == "p"
        assert str(DynamicLevel.MEZZO_PIANO) == "mp"
        assert str(DynamicLevel.MEZZO_FORTE) == "mf"
        assert str(DynamicLevel.FORTE) == "f"
        assert str(DynamicLevel.FORTISSIMO) == "ff"


class TestSection:
    """Tests for Section class."""

    def test_section_creation(self) -> None:
        """Test creating a section."""
        section = Section(
            name="Intro",
            start_time="0:00",
            end_time="0:30",
            instruments=["piano"],
            dynamics=DynamicLevel.PIANO,
        )
        assert section.name == "Intro"
        assert section.start_time == "0:00"
        assert section.end_time == "0:30"

    def test_section_to_notation(self) -> None:
        """Test converting section to notation string."""
        section = Section(
            name="Verse",
            start_time="0:30",
            end_time="1:00",
            instruments=["guitar", "bass"],
            dynamics=DynamicLevel.MEZZO_FORTE,
            melody_description="Ascending melody",
        )
        notation = section.to_notation()
        assert "Verse" in notation
        assert "guitar" in notation
        assert "mf" in notation
        assert "Ascending melody" in notation

    def test_section_to_dict(self) -> None:
        """Test section serialization."""
        section = Section(
            name="Test",
            start_time="0:00",
            end_time="0:15",
        )
        data = section.to_dict()
        assert data["name"] == "Test"
        assert data["timing"] == "0:00-0:15"


class TestMusicNotation:
    """Tests for MusicNotation class."""

    def test_add_notes(self) -> None:
        """Test adding notes to notation."""
        notation = MusicNotation()
        notation.add_note("C4")
        notation.add_note("E4")
        notation.add_note("G4")
        assert len(notation.notes) == 3

    def test_add_articulation(self) -> None:
        """Test adding articulations."""
        notation = MusicNotation()
        notation.add_articulation("staccato")
        notation.add_articulation("legato")
        assert len(notation.articulations) == 2

    def test_to_string(self) -> None:
        """Test notation to string."""
        notation = MusicNotation()
        notation.add_note("C4")
        notation.add_articulation("legato")
        string = notation.to_string()
        assert "音符" in string
        assert "C4" in string
        assert "legato" in string

    def test_density_pattern(self) -> None:
        """Test creating density pattern."""
        notation = MusicNotation()
        pattern = notation.create_density_pattern(
            ["sparse", "moderate", "dense"]
        )
        assert "○" in pattern
        assert "◐" in pattern
        assert "●" in pattern

    def test_contour_pattern(self) -> None:
        """Test creating contour pattern."""
        notation = MusicNotation()
        pattern = notation.create_contour_pattern(["up", "down", "stable"])
        assert "↑" in pattern
        assert "↓" in pattern


class TestSoundBlueprint:
    """Tests for SoundBlueprint class."""

    def test_blueprint_creation(self) -> None:
        """Test creating a blueprint."""
        blueprint = SoundBlueprint(
            title="Test Piece",
            genre="ambient",
            mood="calm",
            tempo=80,
        )
        assert blueprint.title == "Test Piece"
        assert blueprint.genre == "ambient"
        assert blueprint.tempo == 80

    def test_add_section(self) -> None:
        """Test adding sections to blueprint."""
        blueprint = SoundBlueprint()
        blueprint.add_section(Section(
            name="Intro",
            start_time="0:00",
            end_time="0:30",
        ))
        blueprint.add_section(Section(
            name="Main",
            start_time="0:30",
            end_time="1:30",
        ))
        assert len(blueprint.sections) == 2

    def test_add_reference(self) -> None:
        """Test adding references."""
        blueprint = SoundBlueprint()
        blueprint.add_reference("Brian Eno - Music for Airports")
        assert len(blueprint.references) == 1

    def test_add_tag(self) -> None:
        """Test adding tags."""
        blueprint = SoundBlueprint()
        blueprint.add_tag("relaxing")
        blueprint.add_tag("meditation")
        assert len(blueprint.tags) == 2

    def test_to_prompt(self) -> None:
        """Test generating prompt."""
        blueprint = SoundBlueprint(
            title="Morning",
            genre="ambient",
            mood="peaceful",
            tempo=72,
        )
        blueprint.add_section(Section(
            name="Intro",
            start_time="0:00",
            end_time="0:30",
            instruments=["piano"],
            dynamics=DynamicLevel.PIANO,
        ))
        prompt = blueprint.to_prompt()
        assert "SOUNDBLUEPRINT" in prompt
        assert "Morning" in prompt
        assert "ambient" in prompt
        assert "peaceful" in prompt
        assert "72 BPM" in prompt
        assert "Intro" in prompt
        assert "piano" in prompt

    def test_to_dict(self) -> None:
        """Test blueprint serialization."""
        blueprint = SoundBlueprint(
            title="Test",
            genre="rock",
            tempo=120,
        )
        data = blueprint.to_dict()
        assert data["title"] == "Test"
        assert data["genre"] == "rock"
        assert data["tempo"] == 120

    def test_from_dict(self) -> None:
        """Test blueprint deserialization."""
        data = {
            "title": "Restored",
            "genre": "jazz",
            "mood": "smooth",
            "tempo": 90,
            "sections": [
                {
                    "name": "Intro",
                    "timing": "0:00-0:20",
                    "dynamics": "p",
                }
            ]
        }
        blueprint = SoundBlueprint.from_dict(data)
        assert blueprint.title == "Restored"
        assert blueprint.genre == "jazz"
        assert len(blueprint.sections) == 1


class TestCreateSimpleBlueprint:
    """Tests for create_simple_blueprint function."""

    def test_simple_blueprint(self) -> None:
        """Test creating a simple blueprint."""
        blueprint = create_simple_blueprint(
            description="A calm piano melody",
            genre="classical",
            mood="peaceful",
            tempo=72,
        )
        assert blueprint.genre == "classical"
        assert blueprint.mood == "peaceful"
        assert blueprint.tempo == 72
        assert len(blueprint.sections) == 3  # intro, main, outro

    def test_section_structure(self) -> None:
        """Test that simple blueprint has proper sections."""
        blueprint = create_simple_blueprint("Test")
        section_names = [s.name for s in blueprint.sections]
        assert "Intro" in section_names
        assert "Main" in section_names
        assert "Outro" in section_names
