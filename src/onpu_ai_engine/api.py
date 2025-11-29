"""
ONPU AI Engine - FastAPI Application

REST API for the persona-driven prompt engine.
"""

from typing import Any, Dict, List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from onpu_ai_engine import __version__
from onpu_ai_engine.engine import PromptEngine, GenerationResult


class GenerateRequest(BaseModel):
    """Request model for prompt generation."""
    
    prompt: str = Field(..., description="Input prompt for music generation")
    persona: str = Field(default="default", description="Persona to use")


class GenerateResponse(BaseModel):
    """Response model for prompt generation."""
    
    success: bool = Field(..., description="Whether the generation was successful")
    result: Optional[GenerationResult] = Field(None, description="Generation result")
    error: Optional[str] = Field(None, description="Error message if failed")


class PersonaInfo(BaseModel):
    """Persona information model."""
    
    name: str
    description: str


class HealthResponse(BaseModel):
    """Health check response model."""
    
    status: str = Field(..., description="Service status")
    version: str = Field(..., description="API version")


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    
    app = FastAPI(
        title="ONPU AI Engine",
        description="Persona-Driven AI Prompt Engine for Music Generation",
        version=__version__,
        docs_url="/docs",
        redoc_url="/redoc",
    )
    
    # Initialize the engine
    engine = PromptEngine()
    
    @app.get("/", response_model=HealthResponse)
    async def root() -> Dict[str, str]:
        """Health check endpoint."""
        return {"status": "healthy", "version": __version__}
    
    @app.get("/health", response_model=HealthResponse)
    async def health() -> Dict[str, str]:
        """Health check endpoint."""
        return {"status": "healthy", "version": __version__}
    
    @app.get("/personas", response_model=List[PersonaInfo])
    async def list_personas() -> List[Dict[str, str]]:
        """List all available personas."""
        personas = engine.list_personas()
        return [{"name": name, "description": desc} for name, desc in personas.items()]
    
    @app.post("/generate", response_model=GenerateResponse)
    async def generate(request: GenerateRequest) -> Dict[str, Any]:
        """Generate a music prompt using the specified persona."""
        try:
            # Set the persona
            engine.set_persona(request.persona)
            
            # Generate the result
            result = engine.generate(request.prompt)
            
            return {
                "success": True,
                "result": result,
                "error": None,
            }
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            return {
                "success": False,
                "result": None,
                "error": str(e),
            }
    
    return app


# Create app instance for uvicorn
app = create_app()
