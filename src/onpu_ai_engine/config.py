"""
ONPU AI Engine - Configuration Management

Handles loading and validation of configuration settings.
"""

import os
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings


class ServerConfig(BaseModel):
    """Server configuration settings."""
    
    host: str = Field(default="127.0.0.1", description="Server host")
    port: int = Field(default=8000, description="Server port")
    debug: bool = Field(default=False, description="Enable debug mode")
    reload: bool = Field(default=False, description="Enable auto-reload")


class APIConfig(BaseModel):
    """API configuration settings."""
    
    title: str = Field(default="ONPU AI Engine", description="API title")
    version: str = Field(default="0.1.0", description="API version")
    docs_enabled: bool = Field(default=True, description="Enable API docs")
    cors_origins: List[str] = Field(
        default=["http://localhost:3000"],
        description="CORS allowed origins",
    )


class EngineConfig(BaseModel):
    """Engine configuration settings."""
    
    default_persona: str = Field(default="default", description="Default persona")
    max_prompt_length: int = Field(default=4096, description="Max prompt length")
    timeout_seconds: int = Field(default=30, description="Request timeout")


class AIProviderConfig(BaseModel):
    """AI provider configuration settings."""
    
    provider: str = Field(default="openai", description="AI provider name")
    model: str = Field(default="gpt-4", description="Model name")
    api_key_env: str = Field(default="OPENAI_API_KEY", description="API key env var")
    temperature: float = Field(default=0.7, description="Generation temperature")
    max_tokens: int = Field(default=2048, description="Max tokens")


class SoundBlueprintConfig(BaseModel):
    """[🔷 SOUNDBLUEPRINT™©] configuration settings."""
    
    enabled: bool = Field(default=True, description="Enable SOUNDBLUEPRINT")
    texture_depth: int = Field(default=3, description="Texture depth level")
    harmonic_complexity: str = Field(default="medium", description="Harmonic complexity")


class MusicGenerationConfig(BaseModel):
    """[音符] Music generation configuration settings."""
    
    default_bpm: int = Field(default=120, description="Default BPM")
    default_key: str = Field(default="C", description="Default key")
    default_scale: str = Field(default="major", description="Default scale")


class SoundDesignConfig(BaseModel):
    """Sound design configuration settings."""
    
    soundblueprint: SoundBlueprintConfig = Field(
        default_factory=SoundBlueprintConfig,
        description="SOUNDBLUEPRINT settings",
    )
    music_generation: MusicGenerationConfig = Field(
        default_factory=MusicGenerationConfig,
        description="Music generation settings",
    )


class LoggingConfig(BaseModel):
    """Logging configuration settings."""
    
    level: str = Field(default="INFO", description="Log level")
    format: str = Field(
        default="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        description="Log format",
    )
    file: Optional[str] = Field(default=None, description="Log file path")


class LocalConfig(BaseModel):
    """Local deployment configuration settings."""
    
    data_dir: str = Field(default="./data", description="Data directory")
    cache_enabled: bool = Field(default=True, description="Enable caching")
    cache_ttl_seconds: int = Field(default=3600, description="Cache TTL")


class Settings(BaseSettings):
    """Main application settings."""
    
    server: ServerConfig = Field(default_factory=ServerConfig)
    api: APIConfig = Field(default_factory=APIConfig)
    engine: EngineConfig = Field(default_factory=EngineConfig)
    ai_provider: AIProviderConfig = Field(default_factory=AIProviderConfig)
    sound_design: SoundDesignConfig = Field(default_factory=SoundDesignConfig)
    logging: LoggingConfig = Field(default_factory=LoggingConfig)
    local: LocalConfig = Field(default_factory=LocalConfig)
    
    class Config:
        env_prefix = "ONPU_"
        env_nested_delimiter = "__"


def load_settings(config_path: Optional[str] = None) -> Settings:
    """
    Load settings from a YAML configuration file.
    
    Args:
        config_path: Path to the configuration file
        
    Returns:
        Settings object with loaded configuration
    """
    config_data: Dict[str, Any] = {}
    
    if config_path:
        path = Path(config_path)
        if path.exists():
            with open(path, "r") as f:
                config_data = yaml.safe_load(f) or {}
    
    return Settings(**config_data)


def get_settings() -> Settings:
    """
    Get settings from environment or default config.
    
    Returns:
        Settings object
    """
    config_path = os.environ.get("ONPU_CONFIG_PATH", "config/settings.yaml")
    return load_settings(config_path)


# Global settings instance (lazy loaded)
_settings: Optional[Settings] = None


def settings() -> Settings:
    """Get the global settings instance."""
    global _settings
    if _settings is None:
        _settings = get_settings()
    return _settings
