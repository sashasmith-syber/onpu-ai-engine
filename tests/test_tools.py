"""Tests for the ONPU AI Engine tools module."""

from onpu_ai_engine.tools import Tool, ToolRegistry


class TestTool:
    """Tests for Tool class."""

    def test_tool_creation(self) -> None:
        """Test creating a tool."""
        def handler(**kwargs):
            return {"result": "success"}

        tool = Tool(
            name="test_tool",
            description="A test tool",
            parameters={
                "type": "object",
                "properties": {
                    "input": {"type": "string"}
                }
            },
            handler=handler,
        )
        assert tool.name == "test_tool"
        assert tool.description == "A test tool"

    def test_tool_to_schema(self) -> None:
        """Test tool schema generation."""
        tool = Tool(
            name="test",
            description="Test",
            parameters={"type": "object", "properties": {}},
            handler=lambda: None,
        )
        schema = tool.to_schema()
        assert schema["type"] == "function"
        assert schema["function"]["name"] == "test"
        assert "description" in schema["function"]
        assert "parameters" in schema["function"]

    def test_tool_execute(self) -> None:
        """Test tool execution."""
        def add_numbers(a: int, b: int) -> int:
            return a + b

        tool = Tool(
            name="add",
            description="Add numbers",
            parameters={
                "type": "object",
                "properties": {
                    "a": {"type": "integer"},
                    "b": {"type": "integer"},
                }
            },
            handler=add_numbers,
        )
        result = tool.execute(a=5, b=3)
        assert result == 8


class TestToolRegistry:
    """Tests for ToolRegistry class."""

    def test_builtin_tools(self) -> None:
        """Test built-in tools are registered."""
        registry = ToolRegistry()
        tools = registry.list_tools()
        assert "generate_soundblueprint" in tools
        assert "analyze_music_description" in tools
        assert "convert_notation" in tools

    def test_register_tool(self) -> None:
        """Test registering a custom tool."""
        registry = ToolRegistry()

        def custom_handler(**kwargs):
            return {"status": "ok"}

        registry.register(
            name="custom_tool",
            description="A custom tool",
            parameters={"type": "object", "properties": {}},
            handler=custom_handler,
        )
        assert registry.get("custom_tool") is not None

    def test_get_schema(self) -> None:
        """Test getting all tool schemas."""
        registry = ToolRegistry()
        schemas = registry.get_schema()
        assert len(schemas) >= 3  # At least the built-in tools
        for schema in schemas:
            assert schema["type"] == "function"
            assert "function" in schema

    def test_execute_tool(self) -> None:
        """Test executing a registered tool."""
        registry = ToolRegistry()
        result = registry.execute(
            "analyze_music_description",
            description="A fast, energetic rock song with guitar",
        )
        assert "tempo_indicators" in result
        assert "instrument_indicators" in result

    def test_execute_nonexistent_tool(self) -> None:
        """Test executing a nonexistent tool raises error."""
        registry = ToolRegistry()
        try:
            registry.execute("nonexistent_tool")
            raise AssertionError("Should have raised ValueError")
        except ValueError as e:
            assert "not found" in str(e)

    def test_remove_tool(self) -> None:
        """Test removing a tool."""
        registry = ToolRegistry()

        def temp_handler(**kwargs):
            return None

        registry.register(
            name="temp_tool",
            description="Temp",
            parameters={},
            handler=temp_handler,
        )
        assert registry.get("temp_tool") is not None
        result = registry.remove("temp_tool")
        assert result is True
        assert registry.get("temp_tool") is None


class TestBuiltinToolHandlers:
    """Tests for built-in tool handlers."""

    def test_generate_soundblueprint(self) -> None:
        """Test SOUNDBLUEPRINT generation tool."""
        registry = ToolRegistry()
        result = registry.execute(
            "generate_soundblueprint",
            description="A calm piano melody",
            genre="classical",
            mood="peaceful",
            tempo=72,
        )
        assert "blueprint" in result
        assert "prompt" in result
        assert "SOUNDBLUEPRINT" in result["prompt"]

    def test_analyze_music_description(self) -> None:
        """Test music analysis tool."""
        registry = ToolRegistry()
        result = registry.execute(
            "analyze_music_description",
            description="A slow, sad piano piece with violin",
        )
        assert "slow" in result["tempo_indicators"]
        assert "sad" in result["mood_indicators"]
        assert "piano" in result["instrument_indicators"]
        assert "violin" in result["instrument_indicators"]

    def test_convert_notation(self) -> None:
        """Test notation conversion tool."""
        registry = ToolRegistry()
        result = registry.execute(
            "convert_notation",
            input_notation="C4 E4 G4",
            target_format="abc",
        )
        assert result["target_format"] == "abc"
        assert "converted" in result
