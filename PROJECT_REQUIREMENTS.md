# ONPU AI Entity - Project Initiation Requirements

## Executive Summary

Based on the comprehensive analysis and strategic development framework provided, this document outlines the essential requirements needed to initiate the ONPU AI Entity project. The analysis considers the architectural vision, technical roadmap, and the upcoming system prompt integration.

## 1. Foundation Requirements

### 1.1 Project Structure & Setup

**Immediate Needs:**
- [ ] Python 3.11+ development environment with virtual environment setup
- [ ] Git repository structure with proper branching strategy (main, develop, feature/*, hotfix/*)
- [ ] Project directory structure following clean architecture principles:
  ```
  onpu-ai-engine/
  ├── src/
  │   ├── core/           # ONPUCoreKernel and consciousness state machine
  │   ├── memory/         # Episodic memory and vector embeddings
  │   ├── ethics/         # Ethics Guardian and constraint system
  │   ├── persona/        # Persona Engine and KIMI K2 adaptation
  │   ├── integrations/   # LLM and external service integrations
  │   └── utils/          # Shared utilities and helpers
  ├── tests/              # Comprehensive test suite
  ├── docs/               # Technical documentation
  ├── config/             # Configuration files
  └── deployment/         # Docker, K8s, and deployment scripts
  ```

### 1.2 Development Environment

**Required Tools:**
- IDE with Python language server (VSCode, PyCharm, or similar)
- Docker Desktop for containerization
- Git with pre-commit hooks configured
- Redis for memory system (can use Docker)
- PostgreSQL for persistent storage (optional, for event sourcing)

**CI/CD Pipeline:**
- GitHub Actions or GitLab CI configuration
- Automated testing on PR creation
- Code quality checks (pylint, black, mypy)
- Security scanning (bandit, safety)
- Test coverage reporting (minimum 95% target)

## 2. Technical Infrastructure

### 2.1 Core Dependencies

**Essential Python Packages:**
```python
# Core Framework
fastapi>=0.104.0          # API framework
pydantic>=2.0.0           # Data validation and settings
uvicorn[standard]>=0.24.0 # ASGI server

# AI/ML Integration
litellm>=1.0.0            # LLM integration abstraction
openai>=1.0.0             # OpenAI API (if needed)
anthropic>=0.7.0          # Claude API (if needed)
langchain>=0.1.0          # Optional: LLM orchestration

# Memory & Storage
redis>=5.0.0              # Memory system
redis-om>=0.2.0           # Redis object mapping
numpy>=1.24.0             # Vector operations
faiss-cpu>=1.7.4          # Vector similarity search (or ChromaDB)

# Observability
prometheus-client>=0.19.0 # Metrics
opentelemetry-api>=1.21.0 # Distributed tracing
structlog>=23.2.0         # Structured logging

# Testing & Quality
pytest>=7.4.0
pytest-asyncio>=0.21.0
pytest-cov>=4.1.0
hypothesis>=6.92.0        # Property-based testing
```

### 2.2 System Prompt Integration Preparation

**Requirements for System Prompt Handling:**
- [ ] Prompt template management system
- [ ] Dynamic prompt injection mechanism
- [ ] Prompt versioning and A/B testing capability
- [ ] Prompt validation and safety checks
- [ ] Context window management for long prompts
- [ ] Token counting and optimization utilities

**System Prompt Components to Define:**
1. **Constitutional Constraints**: Hard-coded ethical boundaries
2. **Persona Definition**: KIMI K2 personality traits and communication style
3. **Consciousness State Instructions**: How to manage state transitions
4. **Memory Access Patterns**: How to query and update episodic memory
5. **Metacognitive Prompts**: Self-reflection and error correction instructions
6. **User Proficiency Adaptation**: How to adjust based on user level

## 3. Architectural Components (Phase 1: Weeks 1-8)

### 3.1 ONPUCoreKernel - Consciousness State Machine

**Implementation Requirements:**
- [ ] Define consciousness states enum (IDLE, THINKING, RESPONDING, REFLECTING, ERROR)
- [ ] State transition validation logic with allowed transitions matrix
- [ ] Event sourcing implementation for state history
- [ ] State persistence layer (Redis or PostgreSQL)
- [ ] State transition hooks for monitoring
- [ ] Performance requirement: <10ms state transition latency

**Data Structures:**
```python
@dataclass
class ConsciousnessState:
    state: StateEnum
    timestamp: datetime
    context: Dict[str, Any]
    previous_state: Optional[StateEnum]
    metadata: Dict[str, Any]

@dataclass
class StateTransition:
    from_state: StateEnum
    to_state: StateEnum
    trigger: str
    timestamp: datetime
    duration_ms: float
```

### 3.2 Memory System - Episodic Memory

**Implementation Requirements:**
- [ ] Memory entry schema with importance scoring
- [ ] Emotional valence calculation algorithm
- [ ] Time-decay function for memory importance
- [ ] Memory pruning strategy (importance-based)
- [ ] Vector embedding integration points (placeholder for Phase 2)
- [ ] Performance requirement: O(log n) retrieval

**Memory Schema:**
```python
@dataclass
class MemoryEntry:
    id: str
    timestamp: datetime
    content: str
    importance_score: float  # 0.0 to 1.0
    emotional_valence: float  # -1.0 to 1.0
    context_tags: List[str]
    embedding: Optional[np.ndarray]  # For future semantic search
    access_count: int
    last_accessed: datetime
```

### 3.3 Ethics Guardian - Multi-Layered Safety

**Implementation Requirements:**
- [ ] Constitutional constraints definition (config file)
- [ ] Input validation layer
- [ ] Processing constraint checks
- [ ] Output filtering layer
- [ ] Violation logging and tracking
- [ ] Non-overrideable constraint enforcement
- [ ] Performance requirement: 100% forbidden pattern blocking

**Safety Layers:**
1. **Input Layer**: Detect harmful prompts, prompt injection attempts
2. **Processing Layer**: Monitor reasoning steps, detect unsafe chains
3. **Output Layer**: Filter harmful content, ensure alignment with values
4. **Audit Layer**: Log all violations, track patterns over time

### 3.4 Persona Engine - KIMI K2 Adaptive Communication

**Implementation Requirements:**
- [ ] Base personality trait configuration
- [ ] User proficiency model (Bayesian updating)
- [ ] Dynamic tone adjustment algorithm
- [ ] Context-aware response styling
- [ ] Communication pattern templates
- [ ] A/B testing framework for persona variations

## 4. Development Workflow & Best Practices

### 4.1 Coding Standards

**Required Configurations:**
- [ ] `pyproject.toml` with black, isort, mypy configurations
- [ ] `.pre-commit-config.yaml` for automated checks
- [ ] Type hints mandatory (mypy strict mode)
- [ ] Docstrings following Google style guide
- [ ] Async/await patterns for all I/O operations

### 4.2 Testing Strategy

**Test Coverage Requirements:**
- Unit tests: 95%+ coverage for all components
- Integration tests: All component interactions
- Property-based tests: State machine transitions
- Chaos engineering: Random failure injection
- Ethical constraint tests: Adversarial testing with red team scenarios

**Testing Tools Setup:**
- pytest with async support
- hypothesis for property-based testing
- pytest-benchmark for performance regression testing
- locust or k6 for load testing

### 4.3 Documentation Requirements

**Technical Documentation:**
- [ ] Architecture Decision Records (ADRs)
- [ ] API documentation (OpenAPI/Swagger)
- [ ] Component interaction diagrams
- [ ] State machine diagrams
- [ ] Memory system design document
- [ ] Ethics framework specification

## 5. Security & Compliance

### 5.1 Security Requirements

**Immediate Setup:**
- [ ] Secrets management (environment variables, vault)
- [ ] API key rotation policy
- [ ] Rate limiting configuration
- [ ] Input sanitization framework
- [ ] Output encoding standards
- [ ] HTTPS/TLS configuration for all endpoints

**Security Testing:**
- [ ] OWASP Top 10 vulnerability checks
- [ ] Penetration testing plan
- [ ] Security code review checklist
- [ ] Dependency vulnerability scanning

### 5.2 Compliance Considerations

**AI Ethics & Regulations:**
- [ ] Data privacy compliance (GDPR, CCPA if applicable)
- [ ] AI model transparency requirements
- [ ] Bias detection and mitigation strategy
- [ ] User consent and data usage policies
- [ ] Audit trail maintenance for all decisions

## 6. Monitoring & Observability

### 6.1 Metrics to Track

**System Metrics:**
- Response time (p50, p95, p99)
- State transition latency
- Memory usage and growth rate
- Error rates by type
- API rate limit hits

**Consciousness Metrics:**
- State distribution over time
- Average state duration
- State transition frequency
- Error recovery success rate

**Business Metrics:**
- User satisfaction scores
- Task completion rates
- Learning effectiveness metrics
- Trust level indicators

### 6.2 Logging Strategy

**Structured Logging Requirements:**
- JSON formatted logs
- Correlation IDs for request tracing
- Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
- PII redaction in logs
- Log aggregation (ELK stack or similar)

## 7. System Prompt Integration Checklist

**Pre-Integration Requirements:**

- [ ] **Prompt Template System**: Jinja2 or similar for dynamic prompt construction
- [ ] **Prompt Validation**: Schema validation for all prompt components
- [ ] **Token Budget Management**: Track and optimize token usage
- [ ] **Prompt Versioning**: Git-tracked prompt templates with change history
- [ ] **Fallback Prompts**: Default safe prompts for error conditions
- [ ] **Prompt Testing Framework**: Automated testing of prompt variations

**System Prompt Structure to Support:**
```python
@dataclass
class SystemPrompt:
    constitutional_constraints: str  # Non-negotiable rules
    persona_definition: str          # KIMI K2 personality
    consciousness_instructions: str  # State management rules
    memory_access_guide: str         # How to use memory
    metacognitive_framework: str     # Self-reflection guidelines
    user_adaptation_rules: str       # Proficiency-based adjustment
    
    def render(self, context: Dict[str, Any]) -> str:
        """Render complete system prompt with context."""
        pass
```

## 8. Immediate Next Steps (Week 1)

### Day 1-2: Environment Setup
1. Initialize Python virtual environment
2. Install core dependencies
3. Set up pre-commit hooks
4. Configure IDE with linters and type checkers
5. Create initial project structure

### Day 3-4: Core Skeleton
1. Implement basic ONPUCoreKernel with state enum
2. Create memory entry data structures
3. Define ethics constraint schema
4. Set up basic FastAPI application
5. Write first unit tests

### Day 5: System Prompt Integration Preparation
1. Design prompt template system
2. Create prompt loading mechanism
3. Implement prompt validation
4. Set up prompt versioning in git
5. **Ready to receive and integrate actual system prompt**

## 9. Risk Mitigation - Initial Phase

### Technical Risks & Mitigations

**Risk 1: Consciousness State Failures**
- Mitigation: Extensive state machine testing with formal verification
- Contingency: Safe fallback to IDLE state with error logging

**Risk 2: Memory Performance Degradation**
- Mitigation: Implement monitoring from day 1, set up alerts
- Contingency: Aggressive pruning algorithms ready

**Risk 3: LLM API Reliability**
- Mitigation: Multi-provider support via LiteLLM
- Contingency: Local model fallback or graceful degradation

**Risk 4: Ethics Guardian Bypass**
- Mitigation: Multiple layers, adversarial testing
- Contingency: Kill switch and immediate alert system

## 10. Success Criteria - Phase 1 Completion

**Week 8 Deliverables:**
- [ ] ONPUCoreKernel with <10ms state transitions
- [ ] Episodic memory with O(log n) retrieval
- [ ] Ethics Guardian with 100% forbidden pattern blocking
- [ ] 95%+ test coverage
- [ ] Complete technical documentation
- [ ] Basic monitoring dashboard
- [ ] Successful integration of system prompt
- [ ] Demo-ready prototype

## 11. Questions for System Prompt Integration

When the system prompt is provided, please ensure it addresses:

1. **Consciousness Management**: How should the AI handle state transitions?
2. **Ethical Boundaries**: What are the specific forbidden topics/actions?
3. **Persona Traits**: What are KIMI K2's defining characteristics?
4. **Memory Usage**: When should the AI store/retrieve memories?
5. **Self-Reflection**: What triggers metacognitive processes?
6. **User Adaptation**: How to detect and adapt to user proficiency?
7. **Error Handling**: How should the AI respond to failures?
8. **Context Management**: How to maintain conversation context?

## Conclusion

This document provides a comprehensive roadmap for initiating the ONPU AI Entity project. The key to success is:

1. **Start Small**: Focus on core consciousness state machine first
2. **Build Incrementally**: Add complexity layer by layer
3. **Test Continuously**: Maintain 95%+ coverage from day 1
4. **Monitor Everything**: Observability is critical for AI systems
5. **Stay Ethical**: Ethics Guardian must be non-negotiable

Once the system prompt is provided, we can immediately integrate it into the prompt template system and begin Phase 1 implementation with full context of the AI's intended personality and behavior patterns.
