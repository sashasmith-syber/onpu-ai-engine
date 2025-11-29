#!/usr/bin/env python3
"""
ONPU AI Engine - Main Entry Point

Persona-Driven AI prompt engine for text-music, [🔷 SOUNDBLUEPRINT™©] [音符]-music,
code-music generation. Sound design prompt engineering.
"""

import argparse
import sys
from typing import Optional


def create_parser() -> argparse.ArgumentParser:
    """Create command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="onpu",
        description="ONPU AI Engine - Persona-Driven AI Prompt Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  onpu --version          Show version information
  onpu serve              Start the local API server
  onpu generate --prompt "Create ambient soundscape"
        """,
    )
    
    parser.add_argument(
        "--version",
        action="store_true",
        help="Show version information",
    )
    
    parser.add_argument(
        "--config",
        type=str,
        default="config/settings.yaml",
        help="Path to configuration file",
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Serve command
    serve_parser = subparsers.add_parser("serve", help="Start the local API server")
    serve_parser.add_argument(
        "--host",
        type=str,
        default="127.0.0.1",
        help="Host to bind the server",
    )
    serve_parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to bind the server",
    )
    
    # Generate command
    generate_parser = subparsers.add_parser("generate", help="Generate music prompt")
    generate_parser.add_argument(
        "--prompt",
        type=str,
        required=True,
        help="Input prompt for music generation",
    )
    generate_parser.add_argument(
        "--persona",
        type=str,
        default="default",
        help="Persona to use for generation",
    )
    
    return parser


def main(argv: Optional[list] = None) -> int:
    """Main entry point for ONPU AI Engine."""
    from onpu_ai_engine import __version__
    
    parser = create_parser()
    args = parser.parse_args(argv)
    
    if args.version:
        print(f"ONPU AI Engine v{__version__}")
        return 0
    
    if args.command == "serve":
        print(f"Starting ONPU AI Engine server on {args.host}:{args.port}")
        # Import here to avoid circular imports
        from onpu_ai_engine.api import create_app
        import uvicorn
        
        app = create_app()
        uvicorn.run(app, host=args.host, port=args.port)
        return 0
    
    if args.command == "generate":
        print(f"Generating with prompt: {args.prompt}")
        print(f"Using persona: {args.persona}")
        # Import and run engine
        from onpu_ai_engine.engine import PromptEngine
        
        engine = PromptEngine(persona=args.persona)
        result = engine.generate(args.prompt)
        print(f"Result: {result}")
        return 0
    
    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
