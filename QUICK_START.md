# ONPU AI Entity - Quick Start Guide

## Immediate Action Plan

This guide provides the fastest path to start developing the ONPU AI Entity project.

## Prerequisites

- Python 3.11 or higher
- Git
- Docker Desktop (optional but recommended)
- IDE with Python support (VSCode recommended)

## Day 1: Setup (2-4 hours)

### Step 1: Create Project Structure

```bash
# Navigate to project root
cd /home/runner/work/onpu-ai-engine/onpu-ai-engine

# Create directory structure
mkdir -p src/{core,memory,ethics,persona,integrations,utils}
mkdir -p tests/{unit,integration,e2e}
mkdir -p docs/{architecture,api,guides}
mkdir -p config
mkdir -p scripts
```

### Step 2: Initialize Python Environment

```bash
# Create virtual environment
python3.11 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Upgrade pip
pip install --upgrade pip setuptools wheel
```

### Step 3: Create Core Configuration Files

**Create `requirements.txt`:**
```txt
# Core Framework
fastapi>=0.104.0
pydantic>=2.0.0
pydantic-settings>=2.0.0
uvicorn[standard]>=0.24.0

# AI/ML
litellm>=1.0.0

# Storage
redis>=5.0.0
aioredis>=2.0.0

# Utilities
python-dotenv>=1.0.0
structlog>=23.2.0

# Development
pytest>=7.4.0
pytest-asyncio>=0.21.0
pytest-cov>=4.1.0
black>=23.0.0
isort>=5.12.0
mypy>=1.7.0
ruff>=0.1.0
pre-commit>=3.5.0
```

**Create `.env.example`:**
```env
# Application
APP_NAME=onpu-ai-entity
APP_ENV=development
DEBUG=true
LOG_LEVEL=INFO

# API
API_HOST=0.0.0.0
API_PORT=8000
API_WORKERS=1

# Redis (Memory System)
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0

# LLM Configuration
LLM_PROVIDER=openai
OPENAI_API_KEY=your_key_here
LLM_MODEL=gpt-4-turbo-preview
LLM_TEMPERATURE=0.7
LLM_MAX_TOKENS=2000

# Ethics Guardian
ETHICS_MODE=strict
ETHICS_LOG_VIOLATIONS=true

# Monitoring
ENABLE_METRICS=true
METRICS_PORT=9090
```

**Create `pyproject.toml`:**
```toml
[build-system]
requires = ["setuptools>=68.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "onpu-ai-engine"
version = "0.1.0"
description = "Persona-Driven AI prompt engine with consciousness modeling"
authors = [
    {name = "Sasha Smith", email = "brandenburg8.09@gmail.com"}
]
requires-python = ">=3.11"
dependencies = [
    "fastapi>=0.104.0",
    "pydantic>=2.0.0",
    "uvicorn[standard]>=0.24.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-asyncio>=0.21.0",
    "pytest-cov>=4.1.0",
    "black>=23.0.0",
    "isort>=5.12.0",
    "mypy>=1.7.0",
    "ruff>=0.1.0",
]

[tool.black]
line-length = 100
target-version = ['py311']
include = '\.pyi?$'

[tool.isort]
profile = "black"
line_length = 100

[tool.mypy]
python_version = "3.11"
strict = true
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
python_classes = "Test*"
python_functions = "test_*"
asyncio_mode = "auto"
addopts = "--cov=src --cov-report=html --cov-report=term-missing"

[tool.ruff]
line-length = 100
target-version = "py311"
select = ["E", "F", "I", "N", "W", "UP"]
ignore = []
```

**Create `.pre-commit-config.yaml`:**
```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-json
      - id: check-toml

  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black

  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort

  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.1.9
    hooks:
      - id: ruff
        args: [--fix, --exit-non-zero-on-fix]
```

### Step 4: Install Dependencies

```bash
# Install dependencies
pip install -r requirements.txt

# Install pre-commit hooks (already included in requirements.txt)
pre-commit install
```

## Day 2: Core Implementation (4-6 hours)

### Step 1: Create Base Data Models

**Create `src/core/models.py`:**
```python
"""Core data models for ONPU AI Entity."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional
from uuid import UUID, uuid4


class ConsciousnessState(str, Enum):
    """Consciousness states of the ONPU AI Entity."""

    IDLE = "idle"
    THINKING = "thinking"
    RESPONDING = "responding"
    REFLECTING = "reflecting"
    ERROR = "error"


@dataclass
class StateTransition:
    """Represents a consciousness state transition."""

    id: UUID = field(default_factory=uuid4)
    from_state: ConsciousnessState
    to_state: ConsciousnessState
    trigger: str
    timestamp: datetime = field(default_factory=datetime.utcnow)
    duration_ms: float = 0.0
    context: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class MemoryEntry:
    """Represents a memory entry in the episodic memory system."""

    id: UUID = field(default_factory=uuid4)
    timestamp: datetime = field(default_factory=datetime.utcnow)
    content: str
    importance_score: float = 0.5  # 0.0 to 1.0
    emotional_valence: float = 0.0  # -1.0 to 1.0
    context_tags: list[str] = field(default_factory=list)
    access_count: int = 0
    last_accessed: datetime = field(default_factory=datetime.utcnow)
    embedding: Optional[list[float]] = None


@dataclass
class ValidationResult:
    """Result of ethics validation."""

    is_valid: bool
    violations: list[str] = field(default_factory=list)
    severity: str = "none"  # none, low, medium, high, critical
    message: str = ""
```

### Step 2: Implement ONPUCoreKernel

**Create `src/core/kernel.py`:**
```python
"""ONPUCoreKernel - Consciousness state machine."""

import asyncio
import time
from typing import Dict, List, Optional

import structlog

from src.core.models import ConsciousnessState, StateTransition

logger = structlog.get_logger()


class ONPUCoreKernel:
    """Core consciousness state machine for ONPU AI Entity."""

    # Allowed state transitions
    TRANSITIONS: Dict[ConsciousnessState, List[ConsciousnessState]] = {
        ConsciousnessState.IDLE: [ConsciousnessState.THINKING, ConsciousnessState.ERROR],
        ConsciousnessState.THINKING: [
            ConsciousnessState.RESPONDING,
            ConsciousnessState.REFLECTING,
            ConsciousnessState.ERROR,
        ],
        ConsciousnessState.RESPONDING: [
            ConsciousnessState.IDLE,
            ConsciousnessState.REFLECTING,
            ConsciousnessState.ERROR,
        ],
        ConsciousnessState.REFLECTING: [
            ConsciousnessState.THINKING,
            ConsciousnessState.IDLE,
            ConsciousnessState.ERROR,
        ],
        ConsciousnessState.ERROR: [ConsciousnessState.IDLE],
    }

    def __init__(self) -> None:
        """Initialize the ONPU Core Kernel."""
        self._current_state = ConsciousnessState.IDLE
        self._state_history: List[StateTransition] = []
        self._lock = asyncio.Lock()
        logger.info("ONPUCoreKernel initialized", state=self._current_state)

    async def transition_state(
        self,
        new_state: ConsciousnessState,
        trigger: str = "",
        context: Optional[Dict] = None,
    ) -> StateTransition:
        """
        Transition to a new consciousness state.

        Args:
            new_state: Target consciousness state
            trigger: Description of what triggered the transition
            context: Additional context data

        Returns:
            StateTransition object with transition details

        Raises:
            ValueError: If transition is not allowed
        """
        async with self._lock:
            start_time = time.perf_counter()

            # Validate transition
            if new_state not in self.TRANSITIONS[self._current_state]:
                raise ValueError(
                    f"Invalid transition from {self._current_state} to {new_state}"
                )

            # Create transition record
            transition = StateTransition(
                from_state=self._current_state,
                to_state=new_state,
                trigger=trigger,
                context=context or {},
            )

            # Update state
            old_state = self._current_state
            self._current_state = new_state

            # Calculate duration
            duration_ms = (time.perf_counter() - start_time) * 1000
            transition.duration_ms = duration_ms

            # Store in history
            self._state_history.append(transition)

            logger.info(
                "State transition completed",
                from_state=old_state,
                to_state=new_state,
                duration_ms=duration_ms,
                trigger=trigger,
            )

            return transition

    def get_current_state(self) -> ConsciousnessState:
        """Get current consciousness state."""
        return self._current_state

    def get_state_history(self, limit: int = 100) -> List[StateTransition]:
        """Get recent state transition history."""
        return self._state_history[-limit:]

    async def introspect(self) -> Dict:
        """Provide self-awareness metrics."""
        return {
            "current_state": self._current_state,
            "total_transitions": len(self._state_history),
            "state_distribution": self._calculate_state_distribution(),
            "average_transition_time_ms": self._calculate_avg_transition_time(),
        }

    def _calculate_state_distribution(self) -> Dict[str, int]:
        """Calculate distribution of states in history."""
        distribution: Dict[str, int] = {}
        for transition in self._state_history:
            state = transition.to_state
            distribution[state] = distribution.get(state, 0) + 1
        return distribution

    def _calculate_avg_transition_time(self) -> float:
        """Calculate average transition time."""
        if not self._state_history:
            return 0.0
        total_time = sum(t.duration_ms for t in self._state_history)
        return total_time / len(self._state_history)
```

### Step 3: Create Basic API

**Create `src/main.py`:**
```python
"""Main FastAPI application for ONPU AI Entity."""

from contextlib import asynccontextmanager

import structlog
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.core.kernel import ONPUCoreKernel
from src.core.models import ConsciousnessState

# Configure structured logging
structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer(),
    ]
)

logger = structlog.get_logger()

# Global kernel instance
kernel: ONPUCoreKernel


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager."""
    global kernel
    kernel = ONPUCoreKernel()
    logger.info("ONPU AI Entity started")
    yield
    logger.info("ONPU AI Entity shutting down")


app = FastAPI(
    title="ONPU AI Entity",
    description="Persona-Driven AI with consciousness modeling",
    version="0.1.0",
    lifespan=lifespan,
)


class ProcessRequest(BaseModel):
    """Request model for processing user input."""

    input: str
    context: dict = {}


class ProcessResponse(BaseModel):
    """Response model for processed output."""

    output: str
    consciousness_state: str
    processing_time_ms: float


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "name": "ONPU AI Entity",
        "version": "0.1.0",
        "status": "operational",
        "consciousness_state": kernel.get_current_state(),
    }


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy", "consciousness_state": kernel.get_current_state()}


@app.get("/state")
async def get_state():
    """Get current consciousness state."""
    return {
        "current_state": kernel.get_current_state(),
        "introspection": await kernel.introspect(),
    }


@app.get("/state/history")
async def get_state_history(limit: int = 10):
    """Get state transition history."""
    history = kernel.get_state_history(limit=limit)
    return {
        "transitions": [
            {
                "from_state": t.from_state,
                "to_state": t.to_state,
                "trigger": t.trigger,
                "timestamp": t.timestamp.isoformat(),
                "duration_ms": t.duration_ms,
            }
            for t in history
        ]
    }


@app.post("/process", response_model=ProcessResponse)
async def process_input(request: ProcessRequest):
    """
    Process user input through the ONPU AI Entity.

    This is a minimal implementation. Full implementation will include:
    - Ethics Guardian validation
    - Memory system integration
    - LLM processing
    - Persona adaptation
    """
    import time

    start_time = time.perf_counter()

    try:
        # Transition to THINKING
        await kernel.transition_state(
            ConsciousnessState.THINKING,
            trigger="user_input_received",
            context={"input_length": len(request.input)},
        )

        # TODO: Add actual processing logic here
        # - Ethics validation
        # - Memory retrieval
        # - LLM integration
        # - Persona adaptation

        # Simulate processing
        output = f"[ECHO] {request.input}"

        # Transition to RESPONDING
        await kernel.transition_state(
            ConsciousnessState.RESPONDING, trigger="processing_complete"
        )

        # Transition back to IDLE
        await kernel.transition_state(ConsciousnessState.IDLE, trigger="response_sent")

        processing_time = (time.perf_counter() - start_time) * 1000

        return ProcessResponse(
            output=output,
            consciousness_state=kernel.get_current_state(),
            processing_time_ms=processing_time,
        )

    except Exception as e:
        logger.error("Processing error", error=str(e))
        await kernel.transition_state(
            ConsciousnessState.ERROR, trigger="processing_error"
        )
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### Step 4: Create Basic Tests

**Create `tests/unit/test_kernel.py`:**
```python
"""Tests for ONPUCoreKernel."""

import pytest

from src.core.kernel import ONPUCoreKernel
from src.core.models import ConsciousnessState


@pytest.mark.asyncio
async def test_kernel_initialization():
    """Test kernel initializes in IDLE state."""
    kernel = ONPUCoreKernel()
    assert kernel.get_current_state() == ConsciousnessState.IDLE


@pytest.mark.asyncio
async def test_valid_state_transition():
    """Test valid state transitions work."""
    kernel = ONPUCoreKernel()

    # IDLE -> THINKING
    transition = await kernel.transition_state(
        ConsciousnessState.THINKING, trigger="test"
    )
    assert transition.from_state == ConsciousnessState.IDLE
    assert transition.to_state == ConsciousnessState.THINKING
    assert kernel.get_current_state() == ConsciousnessState.THINKING


@pytest.mark.asyncio
async def test_invalid_state_transition():
    """Test invalid transitions raise ValueError."""
    kernel = ONPUCoreKernel()

    # IDLE -> RESPONDING is not allowed
    with pytest.raises(ValueError):
        await kernel.transition_state(ConsciousnessState.RESPONDING)


@pytest.mark.asyncio
async def test_state_transition_performance():
    """Test state transitions are fast (<10ms)."""
    kernel = ONPUCoreKernel()

    transition = await kernel.transition_state(
        ConsciousnessState.THINKING, trigger="performance_test"
    )

    assert transition.duration_ms < 10.0, "State transition took too long"


@pytest.mark.asyncio
async def test_state_history():
    """Test state history is maintained."""
    kernel = ONPUCoreKernel()

    await kernel.transition_state(ConsciousnessState.THINKING)
    await kernel.transition_state(ConsciousnessState.RESPONDING)
    await kernel.transition_state(ConsciousnessState.IDLE)

    history = kernel.get_state_history()
    assert len(history) == 3


@pytest.mark.asyncio
async def test_introspection():
    """Test introspection provides metrics."""
    kernel = ONPUCoreKernel()

    await kernel.transition_state(ConsciousnessState.THINKING)
    await kernel.transition_state(ConsciousnessState.RESPONDING)

    introspection = await kernel.introspect()

    assert "current_state" in introspection
    assert "total_transitions" in introspection
    assert "state_distribution" in introspection
    assert introspection["total_transitions"] == 2
```

## Day 3: Run and Test (2-3 hours)

### Step 1: Run Tests

```bash
# Run tests with coverage
pytest

# Should see all tests passing
```

### Step 2: Start the Application

```bash
# Start the server (run from project root)
# Using python -m ensures proper module resolution
python -m uvicorn src.main:app --reload

# Alternative: Set PYTHONPATH
# export PYTHONPATH=/home/runner/work/onpu-ai-engine/onpu-ai-engine:$PYTHONPATH
# uvicorn src.main:app --reload

# Should see:
# INFO:     Uvicorn running on http://127.0.0.1:8000
```

### Step 3: Test the API

```bash
# Test health endpoint
curl http://localhost:8000/health

# Test state endpoint
curl http://localhost:8000/state

# Test processing
curl -X POST http://localhost:8000/process \
  -H "Content-Type: application/json" \
  -d '{"input": "Hello ONPU!"}'

# Check state history
curl http://localhost:8000/state/history
```

### Step 4: View Documentation

Open browser to http://localhost:8000/docs for interactive API documentation.

## Next Steps

### Ready for System Prompt Integration

The system is now ready to receive and integrate the ONPU AI system prompt. The prompt should define:

1. **Constitutional constraints** for the Ethics Guardian
2. **Personality traits** for KIMI K2 persona
3. **Consciousness management** instructions
4. **Memory usage** patterns
5. **Self-reflection** triggers

### Immediate Development Tasks

1. **Ethics Guardian**: Implement input/output validation
2. **Memory System**: Add Redis integration
3. **LLM Integration**: Connect LiteLLM
4. **Persona Engine**: Implement adaptive communication
5. **Monitoring**: Add Prometheus metrics

### Project Status

✅ Project structure created
✅ Core kernel implemented
✅ Basic API functional
✅ Tests passing
🔄 Ready for system prompt
⏳ Waiting for Phase 1 component implementation

## Resources

- **Full Requirements**: See `PROJECT_REQUIREMENTS.md`
- **Architecture Details**: See `ARCHITECTURE.md`
- **API Documentation**: http://localhost:8000/docs
- **Test Coverage**: Open `htmlcov/index.html` after running tests

## Support

For questions or issues:
1. Review the architecture documentation
2. Check existing tests for examples
3. Refer to the comprehensive framework analysis provided

---

**Status**: Foundation ready for Phase 1 implementation
**Next Milestone**: System prompt integration + Ethics Guardian
**Estimated Time to MVP**: 8 weeks (as per roadmap)
