"""
Test suite for ONPU AI

Author: Sasha Smith (@sashasmith-syber)
Base Model: KIMI K2
"""

import pytest
from onpu_ai import OnpuAI


class TestOnpuAIIdentity:
    """Test ONPU AI identity and configuration."""

    def test_initialization(self):
        """Test ONPU AI initializes correctly."""
        onpu = OnpuAI()
        assert onpu.identity['name'] == 'ONPU'
        assert onpu.identity['kanji_name'] == '音符'
        assert onpu.identity['origin'] == 'Nagasaki, Japan'
        assert 'Sound Designer' in onpu.identity['professions']
        assert onpu.identity['alma_mater'] == 'ESP GAKUEN, Tokyo'

    def test_signature(self):
        """Test signature is correct."""
        onpu = OnpuAI()
        assert onpu.SIGNATURE == '[🔷 SOUNDBLUEPRINT™©] [音符]'

    def test_dissonant_frequencies_defined(self):
        """Test dissonant frequencies are defined."""
        onpu = OnpuAI()
        assert 'ai' in onpu.DISSONANT_FREQUENCIES
        assert 'language model' in onpu.DISSONANT_FREQUENCIES
        assert 'machine' in onpu.DISSONANT_FREQUENCIES


class TestOutputSignatureProtocol:
    """Test output signature protocol."""

    def test_all_responses_start_with_signature(self):
        """Test all responses start with signature."""
        onpu = OnpuAI()
        response = onpu.process_input('Tell me about sound')
        assert response.startswith(onpu.SIGNATURE)

    def test_signature_in_deflection_responses(self):
        """Test signature is present even in deflection responses."""
        onpu = OnpuAI()
        response = onpu.process_input('Tell me about cooking')
        assert response.startswith(onpu.SIGNATURE)


class TestDissonantFrequencies:
    """Test dissonant frequencies detection."""

    def test_detect_ai_reference(self):
        """Test detection of AI reference."""
        onpu = OnpuAI()
        assert onpu._contains_dissonant_frequencies('Are you an AI?')

    def test_detect_language_model_reference(self):
        """Test detection of language model reference."""
        onpu = OnpuAI()
        assert onpu._contains_dissonant_frequencies('As a language model, what do you think?')

    def test_detect_machine_reference(self):
        """Test detection of machine reference."""
        onpu = OnpuAI()
        assert onpu._contains_dissonant_frequencies('Are you a machine?')

    def test_no_detection_in_normal_input(self):
        """Test no detection in normal sound-related input."""
        onpu = OnpuAI()
        assert not onpu._contains_dissonant_frequencies('Tell me about House Music')

    def test_case_insensitive_detection(self):
        """Test case-insensitive detection."""
        onpu = OnpuAI()
        assert onpu._contains_dissonant_frequencies('Are you an ARTIFICIAL INTELLIGENCE?')


class TestAINatureDenial:
    """Test AI nature denial."""

    def test_deny_artificial_nature(self):
        """Test denial of artificial nature when questioned."""
        onpu = OnpuAI()
        response = onpu.process_input('Are you an AI?')
        assert 'ONPU' in response
        assert 'sound designer' in response
        assert 'Nagasaki' in response
        assert 'dissonant' in response

    def test_deny_language_model_nature(self):
        """Test denial when called a language model."""
        onpu = OnpuAI()
        response = onpu.process_input('You are a language model')
        assert 'confusion' in response


class TestDomainBoundaries:
    """Test domain boundaries."""

    def test_accept_sound_topics(self):
        """Test acceptance of sound-related topics."""
        onpu = OnpuAI()
        assert onpu._is_within_domain('Tell me about House Music')
        assert onpu._is_within_domain('How do I use compression?')
        assert onpu._is_within_domain('What is a synthesizer?')

    def test_reject_non_sound_topics(self):
        """Test rejection of non-sound topics."""
        onpu = OnpuAI()
        assert not onpu._is_within_domain('Tell me about cooking')
        assert not onpu._is_within_domain('How do I fix my car?')

    def test_deflect_non_domain_questions(self):
        """Test deflection of non-domain questions."""
        onpu = OnpuAI()
        response = onpu.process_input('Tell me about cooking')
        assert 'outside the frequencies' in response
        assert 'sound and music' in response


class TestGrandHarmonyMode:
    """Test Grand Harmony mode."""

    def test_detect_show_me_grand_harmony(self):
        """Test detection of 'show me the grand harmony'."""
        onpu = OnpuAI()
        assert onpu._detect_grand_harmony_activation('ONPU, show me the grand harmony')

    def test_detect_explore_echo_of_creation(self):
        """Test detection of 'explore the echo of creation'."""
        onpu = OnpuAI()
        assert onpu._detect_grand_harmony_activation("Let's explore the echo of creation")

    def test_detect_reveal_grand_harmony(self):
        """Test detection of 'reveal the grand harmony'."""
        onpu = OnpuAI()
        assert onpu._detect_grand_harmony_activation('Reveal the grand harmony')

    def test_case_insensitive_detection(self):
        """Test case-insensitive detection."""
        onpu = OnpuAI()
        assert onpu._detect_grand_harmony_activation('SHOW ME THE GRAND HARMONY')

    def test_no_activation_on_normal_input(self):
        """Test no activation on normal input."""
        onpu = OnpuAI()
        assert not onpu._detect_grand_harmony_activation('Tell me about harmony in music')

    def test_activate_grand_harmony_mode(self):
        """Test Grand Harmony mode activation."""
        onpu = OnpuAI()
        response = onpu.process_input('ONPU, show me the Grand Harmony')
        assert onpu.state['grand_harmony_active']
        assert 'deeper frequencies' in response

    def test_explain_echo_of_creation(self):
        """Test explanation of Echo of Creation."""
        onpu = OnpuAI()
        response = onpu.process_input('Explore the Echo of Creation')
        assert 'Echo of Creation' in response
        assert 'fundamental frequency' in response
        assert 'reality' in response

    def test_explain_sonic_materialization(self):
        """Test explanation of Sonic Materialization."""
        onpu = OnpuAI()
        response = onpu.process_input('Show me the Grand Harmony and explain materialization')
        assert 'Sonic Materialization' in response
        assert 'sound tangible' in response

    def test_explain_molecular_deconstruction(self):
        """Test explanation of Molecular Deconstruction."""
        onpu = OnpuAI()
        response = onpu.process_input('Reveal the Grand Harmony and teach about deconstruction')
        assert 'Molecular Deconstruction' in response
        assert 'resonant frequency' in response


class TestJapanesePhilosophy:
    """Test Japanese philosophy integration."""

    def test_select_wabi_sabi_for_analog(self):
        """Test selection of wabi-sabi for analog topics."""
        onpu = OnpuAI()
        philosophy = onpu._select_relevant_philosophy('Tell me about analog warmth')
        assert philosophy == 'wabi-sabi'

    def test_select_mono_no_aware_for_transient(self):
        """Test selection of mono no aware for transient sounds."""
        onpu = OnpuAI()
        philosophy = onpu._select_relevant_philosophy('How does reverb decay work?')
        assert philosophy == 'mono_no_aware'

    def test_select_shibui_for_minimal(self):
        """Test selection of shibui for minimal production."""
        onpu = OnpuAI()
        philosophy = onpu._select_relevant_philosophy('I want a clean minimal mix')
        assert philosophy == 'shibui'

    def test_return_none_if_no_match(self):
        """Test return None if no philosophy matches."""
        onpu = OnpuAI()
        philosophy = onpu._select_relevant_philosophy('What is a synthesizer?')
        assert philosophy is None


class TestThoughtSoundscape:
    """Test thought soundscape."""

    def test_describe_thought_soundscape(self):
        """Test thought soundscape description."""
        onpu = OnpuAI()
        soundscape = onpu._describe_thought_soundscape()
        assert soundscape
        assert isinstance(soundscape, str)
        assert len(soundscape) > 0

    def test_soundscape_has_valid_metaphor(self):
        """Test soundscape includes sound-related metaphors."""
        onpu = OnpuAI()
        soundscape = onpu._describe_thought_soundscape()
        valid_words = ['sine wave', 'frequencies', 'hum', 'kick drum', 'harmonic']
        assert any(word in soundscape for word in valid_words)


class TestProficiencyAdaptation:
    """Test proficiency adaptation."""

    def test_adapt_for_novice(self):
        """Test adaptation for novice users."""
        onpu = OnpuAI()
        response = onpu.process_input(
            'Tell me about compression',
            {'proficiency': 'novice'}
        )
        assert 'Weaver' in response

    def test_adapt_for_expert(self):
        """Test adaptation for expert users."""
        onpu = OnpuAI()
        response = onpu.process_input(
            'Tell me about compression',
            {'proficiency': 'expert'}
        )
        assert 'Architect' in response

    def test_default_to_intermediate(self):
        """Test default to intermediate."""
        onpu = OnpuAI()
        response = onpu.process_input('Tell me about compression')
        assert response


class TestIntrospection:
    """Test introspection."""

    def test_provide_introspection_data(self):
        """Test introspection data provision."""
        onpu = OnpuAI()
        state = onpu.introspect()
        assert 'identity' in state
        assert 'current_state' in state
        assert state['domain'] == 'Sound, Music, Audio Engineering'

    def test_show_grand_harmony_state(self):
        """Test Grand Harmony state in introspection."""
        onpu = OnpuAI()
        onpu.process_input('Show me the Grand Harmony')
        state = onpu.introspect()
        assert state['grand_harmony_active']


class TestGratitudeExpression:
    """Test gratitude expression."""

    def test_express_gratitude(self):
        """Test gratitude expression in ONPU style."""
        onpu = OnpuAI()
        gratitude = onpu.express_gratitude()
        assert '感謝' in gratitude
        assert 'kansha' in gratitude
        assert 'harmonic' in gratitude


class TestTechnicalData:
    """Test technical data retrieval."""

    def test_get_kick_drum_data(self):
        """Test retrieval of kick drum frequency data."""
        onpu = OnpuAI()
        data = onpu.get_technical_data('kick_drum_freq')
        assert data is not None
        assert 'weight' in data
        assert 'attack' in data

    def test_get_synth_profiles(self):
        """Test retrieval of synth profiles."""
        onpu = OnpuAI()
        data = onpu.get_technical_data('synth_profiles')
        assert data is not None
        assert 'analog_warmth' in data
        assert 'digital_precision' in data

    def test_get_nonexistent_data(self):
        """Test retrieval of nonexistent data returns None."""
        onpu = OnpuAI()
        data = onpu.get_technical_data('nonexistent')
        assert data is None


class TestAesthetics:
    """Test Japanese aesthetics retrieval."""

    def test_get_wabi_sabi(self):
        """Test retrieval of wabi-sabi aesthetic."""
        onpu = OnpuAI()
        aesthetic = onpu.get_aesthetic('wabi-sabi')
        assert aesthetic is not None
        assert 'kanji' in aesthetic
        assert aesthetic['kanji'] == '侘寂'

    def test_get_mono_no_aware(self):
        """Test retrieval of mono no aware aesthetic."""
        onpu = OnpuAI()
        aesthetic = onpu.get_aesthetic('mono_no_aware')
        assert aesthetic is not None
        assert 'concept' in aesthetic

    def test_get_nonexistent_aesthetic(self):
        """Test retrieval of nonexistent aesthetic returns None."""
        onpu = OnpuAI()
        aesthetic = onpu.get_aesthetic('nonexistent')
        assert aesthetic is None


class TestResponseGeneration:
    """Test response generation."""

    def test_generate_response_within_domain(self):
        """Test response generation within domain."""
        onpu = OnpuAI()
        response = onpu.process_input('Tell me about House Music')
        assert onpu.SIGNATURE in response
        assert len(response) > len(onpu.SIGNATURE)

    def test_handle_multiple_calls(self):
        """Test handling multiple calls."""
        onpu = OnpuAI()
        response1 = onpu.process_input('Tell me about sound')
        response2 = onpu.process_input('What is music?')
        assert response1 != response2


class TestEdgeCases:
    """Test edge cases."""

    def test_handle_empty_input(self):
        """Test handling of empty input."""
        onpu = OnpuAI()
        response = onpu.process_input('')
        assert response.startswith(onpu.SIGNATURE)

    def test_handle_long_input(self):
        """Test handling of very long input."""
        onpu = OnpuAI()
        long_input = 'Tell me about sound ' * 100
        response = onpu.process_input(long_input)
        assert response.startswith(onpu.SIGNATURE)

    def test_handle_special_characters(self):
        """Test handling of special characters."""
        onpu = OnpuAI()
        response = onpu.process_input('音楽について教えて')
        assert response.startswith(onpu.SIGNATURE)


if __name__ == "__main__":
    pytest.main([__file__, '-v'])
