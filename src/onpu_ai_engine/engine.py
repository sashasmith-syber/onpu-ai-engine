"""
ONPU AI Engine - Core Engine Module

Persona-driven prompt engine for music generation.
Supports text-music, [🔷 SOUNDBLUEPRINT™©] [音符]-music, and code-music generation.
"""

from typing import Any, Dict, Optional
from pydantic import BaseModel, Field


class GenerationResult(BaseModel):
    """Result of a prompt generation."""
    
    prompt: str = Field(..., description="Original input prompt")
    persona: str = Field(..., description="Persona used for generation")
    output: str = Field(..., description="Generated output")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")


class Persona(BaseModel):
    """Persona configuration for prompt generation."""
    
    name: str = Field(..., description="Persona name")
    description: str = Field(default="", description="Persona description")
    style: str = Field(default="neutral", description="Musical style preference")
    temperature: float = Field(default=0.7, ge=0.0, le=2.0, description="Generation temperature")
    system_prompt: str = Field(default="", description="System prompt for the persona")


# Default personas for the engine
DEFAULT_PERSONAS: Dict[str, Persona] = {
    "default": Persona(
        name="default",
        description="Standard music generation persona",
        style="versatile",
        temperature=0.7,
        system_prompt="You are a professional music producer and sound designer.",
    ),
    "ambient": Persona(
        name="ambient",
        description="Ambient and atmospheric soundscape specialist",
        style="ambient",
        temperature=0.8,
        system_prompt="You are an ambient music specialist, focusing on atmospheric textures and evolving soundscapes.",
    ),
    "electronic": Persona(
        name="electronic",
        description="Electronic and synthesizer music expert",
        style="electronic",
        temperature=0.6,
        system_prompt="You are an electronic music producer specializing in synthesizers and digital sound design.",
    ),
    "orchestral": Persona(
        name="orchestral",
        description="Classical and orchestral composition specialist",
        style="orchestral",
        temperature=0.5,
        system_prompt="You are a classical composer with expertise in orchestral arrangements and instrumentation.",
    ),
    "soundblueprint": Persona(
        name="soundblueprint",
        description="[🔷 SOUNDBLUEPRINT™©] Advanced sound design persona",
        style="experimental",
        temperature=0.9,
        system_prompt="You are the SOUNDBLUEPRINT™ AI, an advanced sound design system specializing in innovative audio textures and sonic architecture.",
    ),
}


class PromptEngine:
    """
    Persona-driven AI prompt engine for music generation.
    
    Supports multiple personas for different musical styles and use cases.
    """
    
    def __init__(
        self,
        persona: str = "default",
        custom_personas: Optional[Dict[str, Persona]] = None,
    ):
        """
        Initialize the prompt engine.
        
        Args:
            persona: Name of the persona to use
            custom_personas: Optional dictionary of custom personas
        """
        self.personas = {**DEFAULT_PERSONAS}
        if custom_personas:
            self.personas.update(custom_personas)
        
        self.current_persona = self._get_persona(persona)
    
    def _get_persona(self, name: str) -> Persona:
        """Get a persona by name."""
        if name not in self.personas:
            available = ", ".join(self.personas.keys())
            raise ValueError(f"Unknown persona '{name}'. Available: {available}")
        return self.personas[name]
    
    def set_persona(self, name: str) -> None:
        """Change the current persona."""
        self.current_persona = self._get_persona(name)
    
    def generate(self, prompt: str, **kwargs: Any) -> GenerationResult:
        """
        Generate a music prompt using the current persona.
        
        Args:
            prompt: Input prompt for music generation
            **kwargs: Additional generation parameters
            
        Returns:
            GenerationResult with the generated output
        """
        # Build the enhanced prompt using persona
        enhanced_prompt = self._enhance_prompt(prompt)
        
        # For local deployment, return the enhanced prompt
        # In production, this would call an AI API
        output = self._process_prompt(enhanced_prompt, **kwargs)
        
        return GenerationResult(
            prompt=prompt,
            persona=self.current_persona.name,
            output=output,
            metadata={
                "style": self.current_persona.style,
                "temperature": self.current_persona.temperature,
                "enhanced_prompt": enhanced_prompt,
            },
        )
    
    def _enhance_prompt(self, prompt: str) -> str:
        """Enhance the prompt using the current persona."""
        return f"""[Persona: {self.current_persona.name}]
[Style: {self.current_persona.style}]
{self.current_persona.system_prompt}

User Request: {prompt}

Generate a detailed music production prompt based on the above request."""
    
    def _process_prompt(self, enhanced_prompt: str, **kwargs: Any) -> str:
        """
        Process the enhanced prompt.
        
        In local deployment mode, returns a structured response.
        In production, this would call an AI API.
        """
        # Local processing mode - return structured template
        return f"""[🔷 SOUNDBLUEPRINT™©] Music Generation Output

Persona: {self.current_persona.name}
Style: {self.current_persona.style}

Generated Prompt:
{enhanced_prompt}

[音符] Sound Design Elements:
- Texture: Based on {self.current_persona.style} style
- Mood: Determined by prompt analysis
- Instrumentation: Persona-appropriate selection

Ready for integration with external AI music generation APIs."""
    
    def list_personas(self) -> Dict[str, str]:
        """List all available personas."""
        return {name: p.description for name, p in self.personas.items()}
