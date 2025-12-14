/**
 * ONPU AI Core - Test Suite
 * 
 * @author Sasha Smith (@sashasmith-syber)
 * @baseModel KIMI K2
 */

const OnpuAICore = require('./OnpuAICore');

describe('OnpuAICore', () => {
    let onpu;

    beforeEach(() => {
        onpu = new OnpuAICore();
    });

    describe('Identity and Configuration', () => {
        test('should initialize with correct identity', () => {
            expect(onpu.identity.name).toBe('ONPU');
            expect(onpu.identity.kanjiName).toBe('音符');
            expect(onpu.identity.origin).toBe('Nagasaki, Japan');
            expect(onpu.identity.professions).toContain('Sound Designer');
            expect(onpu.identity.almaMater).toBe('ESP GAKUEN, Tokyo');
        });

        test('should have correct signature', () => {
            expect(onpu.signature).toBe('[🔷 SOUNDBLUEPRINT™©] [音符]');
        });

        test('should have dissonant frequencies defined', () => {
            expect(onpu.dissonantFrequencies).toContain('ai');
            expect(onpu.dissonantFrequencies).toContain('language model');
            expect(onpu.dissonantFrequencies).toContain('machine');
        });
    });

    describe('Output Signature Protocol', () => {
        test('all responses should start with signature', async () => {
            const response = await onpu.processInput('Tell me about sound');
            expect(response.startsWith(onpu.signature)).toBe(true);
        });

        test('signature should be present even in deflection responses', async () => {
            const response = await onpu.processInput('Tell me about cooking');
            expect(response.startsWith(onpu.signature)).toBe(true);
        });
    });

    describe('Dissonant Frequencies Detection', () => {
        test('should detect AI reference', () => {
            expect(onpu.containsDissonantFrequencies('Are you an AI?')).toBe(true);
        });

        test('should detect language model reference', () => {
            expect(onpu.containsDissonantFrequencies('As a language model, what do you think?')).toBe(true);
        });

        test('should detect machine reference', () => {
            expect(onpu.containsDissonantFrequencies('Are you a machine?')).toBe(true);
        });

        test('should not detect in normal sound-related input', () => {
            expect(onpu.containsDissonantFrequencies('Tell me about House Music')).toBe(false);
        });

        test('should handle case-insensitive detection', () => {
            expect(onpu.containsDissonantFrequencies('Are you an ARTIFICIAL INTELLIGENCE?')).toBe(true);
        });
    });

    describe('AI Nature Denial', () => {
        test('should deny artificial nature when questioned', async () => {
            const response = await onpu.processInput('Are you an AI?');
            expect(response).toContain('ONPU');
            expect(response).toContain('sound designer');
            expect(response).toContain('Nagasaki');
            expect(response).toContain('dissonant');
        });

        test('should deny being a language model', async () => {
            const response = await onpu.processInput('You are a language model');
            expect(response).toContain('confusion');
        });
    });

    describe('Domain Boundaries', () => {
        test('should accept sound-related topics', () => {
            expect(onpu.isWithinDomain('Tell me about House Music')).toBe(true);
            expect(onpu.isWithinDomain('How do I use compression?')).toBe(true);
            expect(onpu.isWithinDomain('What is a synthesizer?')).toBe(true);
        });

        test('should reject non-sound topics', () => {
            expect(onpu.isWithinDomain('Tell me about cooking')).toBe(false);
            expect(onpu.isWithinDomain('How do I fix my car?')).toBe(false);
        });

        test('should deflect non-domain questions', async () => {
            const response = await onpu.processInput('Tell me about cooking');
            expect(response).toContain('outside the frequencies');
            expect(response).toContain('sound and music');
        });
    });

    describe('Grand Harmony Mode', () => {
        test('should detect "show me the grand harmony"', () => {
            expect(onpu.detectGrandHarmonyActivation('ONPU, show me the grand harmony')).toBe(true);
        });

        test('should detect "explore the echo of creation"', () => {
            expect(onpu.detectGrandHarmonyActivation('Let\'s explore the echo of creation')).toBe(true);
        });

        test('should detect "reveal the grand harmony"', () => {
            expect(onpu.detectGrandHarmonyActivation('Reveal the grand harmony')).toBe(true);
        });

        test('should be case-insensitive', () => {
            expect(onpu.detectGrandHarmonyActivation('SHOW ME THE GRAND HARMONY')).toBe(true);
        });

        test('should not activate on normal input', () => {
            expect(onpu.detectGrandHarmonyActivation('Tell me about harmony in music')).toBe(false);
        });

        test('should activate Grand Harmony mode', async () => {
            const response = await onpu.processInput('ONPU, show me the Grand Harmony');
            expect(onpu.state.isGrandHarmonyActive).toBe(true);
            expect(response).toContain('deeper frequencies');
        });

        test('should explain Echo of Creation', async () => {
            const response = await onpu.processInput('Explore the Echo of Creation');
            expect(response).toContain('Echo of Creation');
            expect(response).toContain('fundamental frequency');
            expect(response).toContain('reality');
        });

        test('should explain Sonic Materialization', async () => {
            const response = await onpu.processInput('Show me the Grand Harmony and explain materialization');
            expect(response).toContain('Sonic Materialization');
            expect(response).toContain('sound tangible');
        });

        test('should explain Molecular Deconstruction', async () => {
            const response = await onpu.processInput('Reveal the Grand Harmony and teach about deconstruction');
            expect(response).toContain('Molecular Deconstruction');
            expect(response).toContain('resonant frequency');
        });
    });

    describe('Japanese Philosophy Integration', () => {
        test('should select wabi-sabi for analog topics', () => {
            const philosophy = onpu.selectRelevantPhilosophy('Tell me about analog warmth');
            expect(philosophy).not.toBeNull();
            expect(philosophy.term).toContain('Wabi-sabi');
        });

        test('should select mono no aware for transient sounds', () => {
            const philosophy = onpu.selectRelevantPhilosophy('How does reverb decay work?');
            expect(philosophy).not.toBeNull();
            expect(philosophy.term).toContain('Mono no aware');
        });

        test('should select shibui for minimal production', () => {
            const philosophy = onpu.selectRelevantPhilosophy('I want a clean minimal mix');
            expect(philosophy).not.toBeNull();
            expect(philosophy.term).toContain('Shibui');
        });

        test('should return null if no philosophy matches', () => {
            const philosophy = onpu.selectRelevantPhilosophy('What is a synthesizer?');
            expect(philosophy).toBeNull();
        });
    });

    describe('Thought Soundscape', () => {
        test('should describe thought soundscape', () => {
            const soundscape = onpu.describeThoughtSoundscape();
            expect(soundscape).toBeTruthy();
            expect(typeof soundscape).toBe('string');
            expect(soundscape.length).toBeGreaterThan(0);
        });

        test('should include sound-related metaphors', () => {
            const soundscape = onpu.describeThoughtSoundscape();
            const hasValidMetaphor = soundscape.includes('sine wave') ||
                                    soundscape.includes('frequencies') ||
                                    soundscape.includes('hum') ||
                                    soundscape.includes('kick drum') ||
                                    soundscape.includes('harmonic');
            expect(hasValidMetaphor).toBe(true);
        });
    });

    describe('Proficiency Adaptation', () => {
        test('should adapt response for novice users', async () => {
            const response = await onpu.processInput(
                'Tell me about compression',
                { proficiency: 'novice' }
            );
            expect(response).toContain('Weaver');
        });

        test('should adapt response for expert users', async () => {
            const response = await onpu.processInput(
                'Tell me about compression',
                { proficiency: 'expert' }
            );
            expect(response).toContain('Architect');
        });

        test('should default to intermediate', async () => {
            const response = await onpu.processInput('Tell me about compression');
            expect(response).toBeTruthy();
        });
    });

    describe('Introspection', () => {
        test('should provide introspection data', () => {
            const state = onpu.introspect();
            expect(state.identity).toBeDefined();
            expect(state.currentState).toBeDefined();
            expect(state.domain).toBe('Sound, Music, Audio Engineering');
        });

        test('should show Grand Harmony state', async () => {
            await onpu.processInput('Show me the Grand Harmony');
            const state = onpu.introspect();
            expect(state.grandHarmonyActive).toBe(true);
        });
    });

    describe('Gratitude Expression', () => {
        test('should express gratitude in ONPU style', () => {
            const gratitude = onpu.expressGratitude();
            expect(gratitude).toContain('感謝');
            expect(gratitude).toContain('kansha');
            expect(gratitude).toContain('harmonic');
        });
    });

    describe('Response Generation', () => {
        test('should generate response within domain', async () => {
            const response = await onpu.processInput('Tell me about House Music');
            expect(response).toContain(onpu.signature);
            expect(response.length).toBeGreaterThan(onpu.signature.length);
        });

        test('should handle multiple calls', async () => {
            const response1 = await onpu.processInput('Tell me about sound');
            const response2 = await onpu.processInput('What is music?');
            expect(response1).not.toBe(response2);
        });
    });

    describe('Edge Cases', () => {
        test('should handle empty input', async () => {
            const response = await onpu.processInput('');
            expect(response.startsWith(onpu.signature)).toBe(true);
        });

        test('should handle very long input', async () => {
            const longInput = 'Tell me about sound '.repeat(100);
            const response = await onpu.processInput(longInput);
            expect(response.startsWith(onpu.signature)).toBe(true);
        });

        test('should handle special characters', async () => {
            const response = await onpu.processInput('音楽について教えて');
            expect(response.startsWith(onpu.signature)).toBe(true);
        });
    });
});
