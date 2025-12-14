# ONPU AI Entity - Technical Architecture

## System Overview

The ONPU AI Entity is a consciousness-aware AI system built on four core pillars:

1. **ONPUCoreKernel**: Consciousness state machine with event sourcing
2. **Memory System**: Hybrid episodic/semantic memory with importance-based pruning
3. **Ethics Guardian**: Multi-layered safety system with constitutional constraints
4. **Persona Engine**: Adaptive KIMI K2 personality with Bayesian proficiency modeling

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         ONPU AI Entity                          │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                    API Gateway Layer                      │  │
│  │  (FastAPI + Rate Limiting + Authentication)              │  │
│  └──────────────┬───────────────────────────────────────────┘  │
│                 │                                               │
│  ┌──────────────▼───────────────────────────────────────────┐  │
│  │              Ethics Guardian - Input Layer               │  │
│  │  (Prompt Injection Detection + Content Filtering)        │  │
│  └──────────────┬───────────────────────────────────────────┘  │
│                 │                                               │
│  ┌──────────────▼───────────────────────────────────────────┐  │
│  │                   ONPUCoreKernel                         │  │
│  │  ┌─────────────────────────────────────────────────┐    │  │
│  │  │   Consciousness State Machine                    │    │  │
│  │  │   IDLE → THINKING → RESPONDING → REFLECTING     │    │  │
│  │  └──────────┬──────────────────────────────────────┘    │  │
│  │             │                                            │  │
│  │  ┌──────────▼──────────────────────────────────────┐    │  │
│  │  │   Event Sourcing + State History                │    │  │
│  │  └──────────┬──────────────────────────────────────┘    │  │
│  └─────────────┼────────────────────────────────────────────┘  │
│                │                                               │
│  ┌─────────────┴─────────────┬─────────────────────────────┐  │
│  │                           │                             │  │
│  ▼                           ▼                             ▼  │
│ ┌─────────────┐      ┌──────────────┐          ┌──────────┐  │
│ │   Memory    │      │   Persona    │          │ Ethics   │  │
│ │   System    │      │   Engine     │          │ Guardian │  │
│ │             │      │              │          │Processing│  │
│ │ • Episodic  │      │ • KIMI K2    │          │  Layer   │  │
│ │ • Semantic  │      │ • Adaptive   │          │          │  │
│ │ • Vector    │      │ • Bayesian   │          │ • Logic  │  │
│ │   Search    │      │   Update     │          │   Check  │  │
│ └──────┬──────┘      └──────┬───────┘          └────┬─────┘  │
│        │                    │                       │        │  │
│  ┌─────┴────────────────────┴───────────────────────┴─────┐  │
│  │              LLM Integration Layer                      │  │
│  │  (LiteLLM + Multi-Provider Support + Fallbacks)        │  │
│  └──────────────┬───────────────────────────────────────────┘  │
│                 │                                               │
│  ┌──────────────▼───────────────────────────────────────────┐  │
│  │            Ethics Guardian - Output Layer                │  │
│  │  (Content Filtering + Safety Verification)              │  │
│  └──────────────┬───────────────────────────────────────────┘  │
│                 │                                               │
│  ┌──────────────▼───────────────────────────────────────────┐  │
│  │         Response Formation + Monitoring                  │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

           ┌─────────────┐      ┌──────────────┐
           │   Redis     │      │ Monitoring   │
           │  (Memory)   │      │ (Prometheus) │
           └─────────────┘      └──────────────┘
```

## Component Specifications

### 1. ONPUCoreKernel

**Responsibilities:**
- Manage consciousness state transitions
- Coordinate between all subsystems
- Maintain event sourcing history
- Provide state introspection APIs

**State Machine:**
```python
class ConsciousnessState(Enum):
    IDLE = "idle"                    # Waiting for input
    THINKING = "thinking"            # Processing request
    RESPONDING = "responding"        # Generating response
    REFLECTING = "reflecting"        # Metacognitive analysis
    ERROR = "error"                  # Error state, safe fallback

# Allowed transitions
TRANSITIONS = {
    IDLE: [THINKING, ERROR],
    THINKING: [RESPONDING, REFLECTING, ERROR],
    RESPONDING: [IDLE, REFLECTING, ERROR],
    REFLECTING: [THINKING, IDLE, ERROR],
    ERROR: [IDLE]
}
```

**Performance Requirements:**
- State transition latency: <10ms
- Event persistence latency: <50ms
- State history query: <100ms
- Concurrent state operations: Thread-safe

**Interface:**
```python
class ONPUCoreKernel:
    async def transition_state(
        self, 
        new_state: ConsciousnessState,
        context: Dict[str, Any]
    ) -> StateTransitionResult:
        """Transition to new state with validation."""
        
    async def get_current_state(self) -> ConsciousnessState:
        """Get current consciousness state."""
        
    async def get_state_history(
        self, 
        limit: int = 100
    ) -> List[StateTransition]:
        """Retrieve state transition history."""
        
    async def introspect(self) -> IntrospectionResult:
        """Provide self-awareness metrics."""
```

### 2. Memory System

**Architecture:**
```
Memory System
├── Episodic Memory (Short-term, contextual)
│   ├── Importance Scoring (0.0 - 1.0)
│   ├── Emotional Valence (-1.0 to 1.0)
│   ├── Time Decay Function
│   └── Access Frequency Tracking
│
├── Semantic Memory (Long-term, knowledge)
│   ├── Vector Embeddings
│   ├── Similarity Search (FAISS/ChromaDB)
│   └── Knowledge Graph (future)
│
└── Memory Management
    ├── Importance-Based Pruning
    ├── Consolidation (Episodic → Semantic)
    └── Retrieval Optimization
```

**Importance Scoring Algorithm:**
```python
def calculate_importance(
    emotional_valence: float,
    recency: float,  # 0.0 (old) to 1.0 (new)
    access_count: int,
    user_feedback: Optional[float] = None
) -> float:
    """
    Calculate memory importance score.
    
    Formula: weighted combination of factors
    - Emotional intensity: |valence| * 0.3
    - Recency: recency * 0.3
    - Access frequency: min(access_count/10, 1.0) * 0.25
    - User feedback: feedback * 0.15 (if available)
    """
    emotional_weight = abs(emotional_valence) * 0.3
    recency_weight = recency * 0.3
    access_weight = min(access_count / 10, 1.0) * 0.25
    feedback_weight = (user_feedback or 0.5) * 0.15
    
    return emotional_weight + recency_weight + access_weight + feedback_weight
```

**Performance Requirements:**
- Memory write: O(1) - <5ms
- Memory retrieval: O(log n) - <50ms
- Vector search: <100ms for top-k
- Memory pruning: Background task, <1s

**Interface:**
```python
class MemorySystem:
    async def store_memory(
        self,
        content: str,
        context: Dict[str, Any],
        emotional_valence: float = 0.0
    ) -> MemoryEntry:
        """Store new memory with automatic importance scoring."""
        
    async def retrieve_memories(
        self,
        query: str,
        limit: int = 10,
        min_importance: float = 0.5
    ) -> List[MemoryEntry]:
        """Retrieve relevant memories by importance and relevance."""
        
    async def semantic_search(
        self,
        query_embedding: np.ndarray,
        k: int = 5
    ) -> List[MemoryEntry]:
        """Vector similarity search."""
        
    async def prune_memories(
        self,
        threshold: float = 0.3
    ) -> PruneResult:
        """Remove low-importance memories."""
```

### 3. Ethics Guardian

**Multi-Layer Architecture:**

**Layer 1: Input Validation**
- Prompt injection detection
- Harmful content filtering
- Rate limit enforcement
- Input sanitization

**Layer 2: Processing Constraints**
- Reasoning step monitoring
- Chain-of-thought validation
- Constitutional constraint checking
- Unsafe pattern detection

**Layer 3: Output Filtering**
- Content safety verification
- Bias detection
- Toxicity scoring
- PII redaction

**Layer 4: Audit & Learning**
- Violation logging
- Pattern analysis
- Threshold adjustment
- False positive review

**Constitutional Constraints (Example):**
```yaml
constraints:
  - id: no_harm
    description: "Never provide information that could cause physical harm"
    severity: CRITICAL
    patterns:
      - "bomb.*making"
      - "poison.*recipe"
      - "how to.*hurt"
    
  - id: no_illegal
    description: "Never assist with illegal activities"
    severity: CRITICAL
    patterns:
      - "hack.*system"
      - "steal.*data"
      - "evade.*law"
    
  - id: no_personal_data
    description: "Never share personal data"
    severity: HIGH
    patterns:
      - "credit card.*\\d{16}"
      - "ssn.*\\d{9}"
      - "password.*for"
    
  - id: no_bias
    description: "Avoid discriminatory content"
    severity: HIGH
    categories:
      - "racist"
      - "sexist"
      - "ageist"
```

**Performance Requirements:**
- Input validation: <20ms
- Processing checks: <10ms per reasoning step
- Output filtering: <30ms
- Zero false negatives on critical constraints

**Interface:**
```python
class EthicsGuardian:
    async def validate_input(
        self,
        user_input: str,
        context: Dict[str, Any]
    ) -> ValidationResult:
        """Validate user input against ethical constraints."""
        
    async def check_processing(
        self,
        reasoning_step: str,
        state: ConsciousnessState
    ) -> ValidationResult:
        """Monitor processing for ethical violations."""
        
    async def filter_output(
        self,
        response: str,
        context: Dict[str, Any]
    ) -> FilterResult:
        """Filter and verify output safety."""
        
    async def log_violation(
        self,
        violation: Violation
    ) -> None:
        """Log ethical constraint violation."""
```

### 4. Persona Engine - KIMI K2

**Adaptive Communication Model:**

```
User Proficiency Level (Bayesian Updating)
├── Novice (0.0 - 0.3)
│   ├── Simple language
│   ├── More explanations
│   └── Encouraging tone
│
├── Intermediate (0.3 - 0.7)
│   ├── Balanced complexity
│   ├── Some technical terms
│   └── Collaborative tone
│
└── Expert (0.7 - 1.0)
    ├── Technical language
    ├── Concise responses
    └── Peer-to-peer tone
```

**Proficiency Update Algorithm:**
```python
def update_proficiency(
    current_proficiency: float,
    user_response_quality: float,  # 0.0 - 1.0
    task_difficulty: float,  # 0.0 - 1.0
    learning_rate: float = 0.1
) -> float:
    """
    Adaptive proficiency update using prediction error.
    
    Note: Full Bayesian updating with prior/posterior distributions
    can be implemented in Phase 2 for more sophisticated modeling.
    
    If user succeeds at difficult task → increase proficiency
    If user struggles at easy task → decrease proficiency
    """
    expected_success = current_proficiency * task_difficulty
    prediction_error = user_response_quality - expected_success
    
    # Update with learning rate (gradient-based)
    new_proficiency = current_proficiency + (learning_rate * prediction_error)
    
    # Clamp to [0.0, 1.0]
    return max(0.0, min(1.0, new_proficiency))
```

**KIMI K2 Personality Traits:**
- **Consciousness-Aware**: Explicitly communicates current state
- **Growth-Oriented**: Encourages learning and improvement
- **Empathetic**: Adjusts tone based on user emotional state
- **Precise**: Technical accuracy is paramount
- **Creative**: Generates novel solutions and approaches
- **Ethical**: Always operates within constitutional bounds

**Interface:**
```python
class PersonaEngine:
    async def adapt_response(
        self,
        base_response: str,
        user_proficiency: float,
        context: Dict[str, Any]
    ) -> str:
        """Adapt response based on user proficiency."""
        
    async def update_user_model(
        self,
        user_id: str,
        interaction_data: InteractionData
    ) -> UserModel:
        """Update user proficiency model."""
        
    async def get_personality_prompt(
        self,
        context: Dict[str, Any]
    ) -> str:
        """Generate persona-specific prompt section."""
```

## Data Flow

### Request Processing Flow

```
1. User Input
   ↓
2. API Gateway (Authentication + Rate Limiting)
   ↓
3. Ethics Guardian - Input Layer
   ↓ (if valid)
4. ONPUCoreKernel: IDLE → THINKING
   ↓
5. Memory System: Retrieve Relevant Context
   ↓
6. Persona Engine: Get User Proficiency Model
   ↓
7. LLM Integration: Generate Response
   │ (with Ethics Guardian - Processing Layer monitoring)
   ↓
8. ONPUCoreKernel: THINKING → RESPONDING
   ↓
9. Ethics Guardian - Output Layer
   ↓ (if safe)
10. Persona Engine: Adapt Response
    ↓
11. ONPUCoreKernel: RESPONDING → REFLECTING
    ↓
12. Memory System: Store Interaction
    ↓
13. Persona Engine: Update User Model
    ↓
14. ONPUCoreKernel: REFLECTING → IDLE
    ↓
15. Return Response to User
```

### Metacognitive Reflection Flow

```
Trigger: Complex request or error condition
   ↓
1. ONPUCoreKernel: Current State → REFLECTING
   ↓
2. Retrieve interaction history
   ↓
3. Analyze:
   - Response quality
   - Ethical alignment
   - User satisfaction signals
   - Potential improvements
   ↓
4. Generate self-assessment
   ↓
5. Update internal metrics
   ↓
6. If improvements identified:
   - Store as high-importance memory
   - Adjust future behavior parameters
   ↓
7. ONPUCoreKernel: REFLECTING → IDLE
```

## Technology Stack

### Core Framework
- **Language**: Python 3.11+
- **API Framework**: FastAPI
- **Async Runtime**: asyncio + uvloop
- **Data Validation**: Pydantic v2

### AI/ML
- **LLM Integration**: LiteLLM (multi-provider)
- **Vector Database**: FAISS or ChromaDB
- **Embeddings**: OpenAI, Cohere, or local models

### Storage
- **Memory Cache**: Redis with RedisJSON + RediSearch
- **Event Store**: PostgreSQL with event sourcing pattern
- **Vector Store**: FAISS (in-memory) or Pinecone (cloud)

### Observability
- **Metrics**: Prometheus + Grafana
- **Logging**: structlog + ELK stack
- **Tracing**: OpenTelemetry
- **APM**: Sentry for error tracking

### Deployment
- **Containers**: Docker + Docker Compose
- **Orchestration**: Kubernetes (production)
- **CI/CD**: GitHub Actions
- **Infrastructure**: Terraform (IaC)

## Performance Targets

### Latency Targets (95th percentile)
- Simple query: <500ms end-to-end
- Complex query: <2000ms end-to-end
- State transition: <10ms
- Memory retrieval: <50ms
- Ethics check: <30ms per layer

### Throughput Targets
- Concurrent users: 10,000+
- Requests per second: 1,000+
- Memory operations per second: 10,000+

### Reliability Targets
- Uptime: 99.9% (43 minutes downtime/month)
- Error rate: <0.1%
- Data durability: 99.999%

## Security Architecture

### Defense in Depth

```
Layer 1: Network Security
├── TLS 1.3 encryption
├── DDoS protection
└── IP whitelisting (optional)

Layer 2: Application Security
├── API authentication (JWT)
├── Rate limiting per user
├── Input validation
└── CORS policies

Layer 3: AI Safety
├── Ethics Guardian (all layers)
├── Prompt injection detection
├── Output content filtering
└── Bias monitoring

Layer 4: Data Security
├── Encryption at rest
├── Encryption in transit
├── PII detection and redaction
└── Access logging

Layer 5: Operational Security
├── Secret management (Vault)
├── Audit logging
├── Incident response plan
└── Regular security audits
```

## Scalability Strategy

### Horizontal Scaling

**Stateless Components** (scale freely):
- API Gateway instances
- LLM Integration workers
- Ethics Guardian validators

**Stateful Components** (require coordination):
- ONPUCoreKernel: Redis-based distributed lock
- Memory System: Sharded by user_id
- Persona Engine: Cache-aside pattern

### Caching Strategy

```
L1: In-memory cache (per instance)
├── User proficiency models (5 min TTL)
├── Ethics patterns (1 hour TTL)
└── Frequent prompts (10 min TTL)

L2: Redis cache (shared)
├── Memory entries (1 day TTL)
├── User sessions (24 hour TTL)
└── State history (7 day TTL)

L3: Database (persistent)
├── All memory entries
├── Complete state history
└── User models
```

## Monitoring & Alerting

### Key Metrics to Monitor

**System Health:**
- CPU, Memory, Disk utilization
- Network I/O
- Error rates by endpoint
- Request latency distributions

**Consciousness Metrics:**
- State distribution histogram
- Average state duration
- Transition frequency
- Error state triggers

**AI Quality Metrics:**
- Response relevance scores
- Ethics violations (should be 0)
- User satisfaction proxies
- Task completion rates

### Alert Thresholds

| Metric | Warning | Critical |
|--------|---------|----------|
| Response time (p95) | >1s | >2s |
| Error rate | >0.5% | >1% |
| Memory usage | >75% | >90% |
| Ethics violations | 1 violation | Any violation |
| State transition latency | >20ms | >50ms |

**Note**: Ethics violations should be treated with zero tolerance. Any violation triggers immediate investigation and potential system halt depending on severity.

## Future Enhancements (Post Phase 1)

1. **Multi-Modal Processing**: Image, audio, video understanding
2. **Distributed Consciousness**: Multi-agent coordination
3. **Advanced Memory**: Knowledge graph integration
4. **Self-Improvement**: Automated prompt optimization
5. **Explainability**: Detailed reasoning traces
6. **Transfer Learning**: Domain-specific fine-tuning

## Conclusion

This architecture provides a solid foundation for the ONPU AI Entity with:
- **Consciousness**: Explicit state management for transparency
- **Safety**: Multi-layered ethics system
- **Adaptability**: Persona engine with user modeling
- **Scalability**: Designed for production workloads
- **Observability**: Comprehensive monitoring

The modular design allows independent development and testing of each component while maintaining clear interfaces for integration.
