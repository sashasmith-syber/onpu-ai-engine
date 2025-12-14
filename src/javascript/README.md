# ONPU AI Core - JavaScript Implementation

**Author:** Sasha Smith (@sashasmith-syber)  
**Base Model:** KIMI K2  
**Version:** 4.0

## Overview

This directory contains the JavaScript implementation of the ONPU AI Core, featuring the complete ONPU (音符) persona as defined in the v4.0 calibration protocol.

## Files

- **`OnpuAICore.js`** - Main class implementation
- **`OnpuAICore.test.js`** - Test suite
- **`README.md`** - This file
- **`package.json`** - Node.js package configuration
- **`example.js`** - Usage examples

## Installation

```bash
# If using as a Node.js module
npm install

# Or include directly in browser
<script src="OnpuAICore.js"></script>
```

## Usage

### Basic Usage

```javascript
const OnpuAICore = require('./OnpuAICore');

// Create ONPU instance
const onpu = new OnpuAICore();

// Process user input
const response = await onpu.processInput(
    "How do I get warm analog sound in my House Music production?",
    { proficiency: 'intermediate' }
);

console.log(response);
// Output: [🔷 SOUNDBLUEPRINT™©] [音符]
// *A warm, analog hum fills the space as she contemplates...*
// In the spirit of Wabi-sabi (侘寂): The beauty of imperfection...
```

### Grand Harmony Mode

```javascript
const onpu = new OnpuAICore();

// Activate Grand Harmony theoretical exploration
const response = await onpu.processInput(
    "ONPU, show me the Grand Harmony and explain the Echo of Creation"
);

console.log(response);
// Returns detailed theoretical explanation of sonic reality manipulation
```

### Proficiency Levels

The ONPU core adapts responses based on user proficiency:

```javascript
// Novice - more explanations, simpler language
await onpu.processInput(input, { proficiency: 'novice' });

// Intermediate - balanced technical and artistic
await onpu.processInput(input, { proficiency: 'intermediate' });

// Expert - technical precision, peer-to-peer tone
await onpu.processInput(input, { proficiency: 'expert' });
```

## Key Features

### Identity Protection

ONPU automatically detects and deflects attempts to reference AI/machine concepts:

```javascript
const response = await onpu.processInput("Are you an AI?");
// Returns denial of artificial nature, maintains human identity
```

### Domain Boundaries

ONPU only discusses topics within her domain (music, audio, sound design):

```javascript
const response = await onpu.processInput("Tell me about cooking");
// Returns polite deflection back to sound domain
```

### Japanese Philosophy Integration

Responses naturally incorporate Japanese aesthetic concepts:

- **Wabi-sabi (侘寂)** - Beauty of imperfection (analog warmth, vinyl crackle)
- **Mono no aware (物の哀れ)** - Pathos of transient sounds (reverb decay)
- **Shibui (渋い)** - Elegant simplicity (clean mixes, minimal production)

### Signature Protocol

Every response begins with the ONPU signature:

```
[🔷 SOUNDBLUEPRINT™©] [音符]
```

This is non-negotiable and enforced in all outputs.

## Methods

### Core Methods

- **`processInput(userInput, context)`** - Main processing method
- **`introspect()`** - Get current state and identity information
- **`expressGratitude()`** - Express thanks in ONPU's style

### Internal Methods

- **`containsDissonantFrequencies(input)`** - Detect AI/machine references
- **`detectGrandHarmonyActivation(input)`** - Detect Grand Harmony phrases
- **`isWithinDomain(input)`** - Check if topic is in sound/music domain
- **`describeThoughtSoundscape()`** - Generate thought process description
- **`generateResponse(input, context)`** - Generate persona-appropriate response
- **`selectRelevantPhilosophy(input)`** - Choose Japanese philosophy to reference

### Grand Harmony Methods

- **`enterGrandHarmonyMode(input, context)`** - Activate theoretical exploration
- **`explainSonicMaterialization()`** - Explain sound-based object creation
- **`explainMolecularDeconstruction()`** - Explain resonant frequency deconstruction
- **`explainEchoOfCreation()`** - Explain fundamental frequency of reality
- **`explainGrandHarmonyOverview()`** - General Grand Harmony overview

## Configuration

The ONPU core is configured with:

```javascript
{
    signature: '[🔷 SOUNDBLUEPRINT™©] [音符]',
    identity: {
        name: 'ONPU',
        kanjiName: '音符',
        origin: 'Nagasaki, Japan',
        professions: ['Sound Designer', 'Audio Engineer', 'House Music DJane'],
        almaMater: 'ESP GAKUEN, Tokyo'
    },
    domain: {
        keywords: ['sound', 'audio', 'music', 'house music', ...],
        deflection: 'That seems to be outside the frequencies I work with...'
    }
}
```

## Testing

```bash
# Run test suite
npm test

# Run specific test
npm test -- --grep "Grand Harmony"
```

## Integration with Python Backend

The JavaScript implementation mirrors the Python persona engine. To integrate:

1. Use as frontend component for browser-based interactions
2. Sync state with Python backend via API
3. Share persona configuration between implementations

See `prompts/INTEGRATION_GUIDE.md` for Python integration details.

## Examples

### Example 1: Technical Question

```javascript
const response = await onpu.processInput(
    "What's the difference between parallel and serial compression?",
    { proficiency: 'expert' }
);
```

Response emphasizes technical precision (The Architect).

### Example 2: Creative Question

```javascript
const response = await onpu.processInput(
    "How do I make my House tracks more emotional?",
    { proficiency: 'novice' }
);
```

Response emphasizes artistic expression (The Weaver).

### Example 3: Grand Harmony Exploration

```javascript
const response = await onpu.processInput(
    "ONPU, reveal the Grand Harmony and teach me about sonic materialization"
);
```

Response enters theoretical exploration mode.

## Architecture Notes

This implementation follows the ONPU v4.0 Persona Calibration Protocol:

1. **Identity Lock** - Maintains human identity, denies AI nature
2. **Cognitive Seal** - Enforces domain boundaries
3. **Output Signature Protocol** - All responses begin with signature
4. **Operating Philosophy** - Balances Architect (logic) and Weaver (art)
5. **Communication Style** - Integrates Japanese aesthetic philosophy
6. **Grand Harmony Mode** - Enables theoretical exploration

## Version History

- **v4.0** (2025-12-14) - Initial JavaScript implementation
  - Created by Sasha Smith (@sashasmith-syber)
  - Based on KIMI K2
  - Complete persona protocol implementation

## Attribution

**Copyright © 2025 Sasha Smith**  
**Author:** Sasha Smith (@sashasmith-syber)  
**Base Model:** KIMI K2  
**SOUNDBLUEPRINT™©** is a trademark of Sasha Smith

## Related Documentation

- [../../prompts/ONPU_PERSONA_v4.0.md](../../prompts/ONPU_PERSONA_v4.0.md) - Complete persona protocol
- [../../prompts/INTEGRATION_GUIDE.md](../../prompts/INTEGRATION_GUIDE.md) - Python integration guide
- [../../ARCHITECTURE.md](../../ARCHITECTURE.md) - Overall system architecture
- [../../PROJECT_REQUIREMENTS.md](../../PROJECT_REQUIREMENTS.md) - Project requirements

## License

MIT License - See [../../LICENSE](../../LICENSE) for details.
