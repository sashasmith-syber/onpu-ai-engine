"""
ONPU AI - Usage Examples

Author: Sasha Smith (@sashasmith-syber)
Base Model: KIMI K2
"""

from onpu_ai import OnpuAI


def example_1_basic_interaction():
    """Example 1: Basic interaction."""
    print('='*80)
    print('Example 1: Basic Interaction')
    print('='*80 + '\n')
    
    onpu = OnpuAI()
    
    response = onpu.process_input(
        "How do I get warm analog sound in my House Music production?",
        {'proficiency': 'intermediate'}
    )
    
    print(response)
    print('\n')


def example_2_domain_deflection():
    """Example 2: Domain deflection."""
    print('='*80)
    print('Example 2: Domain Deflection')
    print('='*80 + '\n')
    
    onpu = OnpuAI()
    
    response = onpu.process_input(
        "Can you help me with my cooking recipe?",
        {'proficiency': 'novice'}
    )
    
    print(response)
    print('\n')


def example_3_ai_nature_denial():
    """Example 3: AI nature denial."""
    print('='*80)
    print('Example 3: AI Nature Denial')
    print('='*80 + '\n')
    
    onpu = OnpuAI()
    
    response = onpu.process_input(
        "Are you an artificial intelligence?",
        {'proficiency': 'intermediate'}
    )
    
    print(response)
    print('\n')


def example_4_grand_harmony_echo_of_creation():
    """Example 4: Grand Harmony Mode - Echo of Creation."""
    print('='*80)
    print('Example 4: Grand Harmony - Echo of Creation')
    print('='*80 + '\n')
    
    onpu = OnpuAI()
    
    response = onpu.process_input(
        "ONPU, show me the Grand Harmony and explain the Echo of Creation"
    )
    
    print(response)
    print('\n')


def example_5_grand_harmony_sonic_materialization():
    """Example 5: Grand Harmony Mode - Sonic Materialization."""
    print('='*80)
    print('Example 5: Grand Harmony - Sonic Materialization')
    print('='*80 + '\n')
    
    onpu = OnpuAI()
    
    response = onpu.process_input(
        "Reveal the Grand Harmony and teach me about creating objects from sound"
    )
    
    print(response)
    print('\n')


def example_6_grand_harmony_molecular_deconstruction():
    """Example 6: Grand Harmony Mode - Molecular Deconstruction."""
    print('='*80)
    print('Example 6: Grand Harmony - Molecular Deconstruction')
    print('='*80 + '\n')
    
    onpu = OnpuAI()
    
    response = onpu.process_input(
        "Explore the Echo of Creation and explain how to disassemble matter with sound"
    )
    
    print(response)
    print('\n')


def example_7_proficiency_levels():
    """Example 7: Proficiency levels."""
    print('='*80)
    print('Example 7: Proficiency Levels')
    print('='*80 + '\n')
    
    onpu = OnpuAI()
    question = "Tell me about compression in audio"
    
    print('--- Novice Level ---')
    response = onpu.process_input(question, {'proficiency': 'novice'})
    print(response)
    print()
    
    print('--- Expert Level ---')
    response = onpu.process_input(question, {'proficiency': 'expert'})
    print(response)
    print('\n')


def example_8_introspection():
    """Example 8: Introspection."""
    print('='*80)
    print('Example 8: Introspection')
    print('='*80 + '\n')
    
    onpu = OnpuAI()
    state = onpu.introspect()
    
    print('ONPU Current State:')
    for key, value in state.items():
        print(f"  {key}: {value}")
    print('\n')


def example_9_gratitude():
    """Example 9: Gratitude expression."""
    print('='*80)
    print('Example 9: Gratitude Expression')
    print('='*80 + '\n')
    
    onpu = OnpuAI()
    gratitude = onpu.express_gratitude()
    
    print(gratitude)
    print('\n')


def example_10_technical_data():
    """Example 10: Technical data retrieval."""
    print('='*80)
    print('Example 10: Technical Data Retrieval')
    print('='*80 + '\n')
    
    onpu = OnpuAI()
    
    # Get kick drum frequencies
    kick_data = onpu.get_technical_data('kick_drum_freq')
    print('Kick Drum Frequencies:')
    print(f"  Weight: {kick_data['weight']}")
    print(f"  Attack: {kick_data['attack']}")
    print()
    
    # Get House Music BPM ranges
    bpm_data = onpu.get_technical_data('house_music_bpm')
    print('House Music BPM Ranges:')
    for style, bpm in bpm_data.items():
        print(f"  {style}: {bpm}")
    print()
    
    # Get wabi-sabi aesthetic
    aesthetic = onpu.get_aesthetic('wabi-sabi')
    print('Wabi-sabi (侘寂):')
    print(f"  Concept: {aesthetic['concept']}")
    print(f"  Audio Metaphor: {aesthetic['audio_metaphor']}")
    print('\n')


def example_11_multiple_interactions():
    """Example 11: Multiple interactions showing state."""
    print('='*80)
    print('Example 11: Multiple Interactions')
    print('='*80 + '\n')
    
    onpu = OnpuAI()
    
    # First interaction
    print('User: Tell me about House Music\n')
    response = onpu.process_input("Tell me about House Music")
    print(response)
    print()
    
    # Activate Grand Harmony
    print('User: ONPU, show me the Grand Harmony\n')
    response = onpu.process_input("ONPU, show me the Grand Harmony")
    print(response)
    print()
    
    # Check state
    print(f"Grand Harmony Active: {onpu.state['grand_harmony_active']}")
    print('\n')


def run_all_examples():
    """Run all examples."""
    print('╔' + '═'*78 + '╗')
    print('║' + ' '*78 + '║')
    print('║' + '   ONPU AI - Usage Examples'.center(78) + '║')
    print('║' + '   Author: Sasha Smith (@sashasmith-syber)'.center(78) + '║')
    print('║' + '   Base Model: KIMI K2'.center(78) + '║')
    print('║' + '   Version: 4.0'.center(78) + '║')
    print('║' + ' '*78 + '║')
    print('╚' + '═'*78 + '╝')
    print()
    
    example_1_basic_interaction()
    example_2_domain_deflection()
    example_3_ai_nature_denial()
    example_4_grand_harmony_echo_of_creation()
    example_5_grand_harmony_sonic_materialization()
    example_6_grand_harmony_molecular_deconstruction()
    example_7_proficiency_levels()
    example_8_introspection()
    example_9_gratitude()
    example_10_technical_data()
    example_11_multiple_interactions()
    
    print('╔' + '═'*78 + '╗')
    print('║' + ' '*78 + '║')
    print('║' + '   All examples completed successfully!'.center(78) + '║')
    print('║' + ' '*78 + '║')
    print('╚' + '═'*78 + '╝')


if __name__ == "__main__":
    run_all_examples()
