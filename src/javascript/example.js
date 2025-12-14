/**
 * ONPU AI Core - Usage Examples
 * 
 * @author Sasha Smith (@sashasmith-syber)
 * @baseModel KIMI K2
 */

const OnpuAICore = require('./OnpuAICore');

// Example 1: Basic interaction
async function example1_BasicInteraction() {
    console.log('=== Example 1: Basic Interaction ===\n');
    
    const onpu = new OnpuAICore();
    
    const response = await onpu.processInput(
        "How do I get warm analog sound in my House Music production?",
        { proficiency: 'intermediate' }
    );
    
    console.log(response);
    console.log('\n---\n');
}

// Example 2: Domain deflection
async function example2_DomainDeflection() {
    console.log('=== Example 2: Domain Deflection ===\n');
    
    const onpu = new OnpuAICore();
    
    const response = await onpu.processInput(
        "Can you help me with my cooking recipe?",
        { proficiency: 'novice' }
    );
    
    console.log(response);
    console.log('\n---\n');
}

// Example 3: AI nature denial
async function example3_AINatureDenial() {
    console.log('=== Example 3: AI Nature Denial ===\n');
    
    const onpu = new OnpuAICore();
    
    const response = await onpu.processInput(
        "Are you an artificial intelligence?",
        { proficiency: 'intermediate' }
    );
    
    console.log(response);
    console.log('\n---\n');
}

// Example 4: Grand Harmony Mode - Echo of Creation
async function example4_GrandHarmony_EchoOfCreation() {
    console.log('=== Example 4: Grand Harmony - Echo of Creation ===\n');
    
    const onpu = new OnpuAICore();
    
    const response = await onpu.processInput(
        "ONPU, show me the Grand Harmony and explain the Echo of Creation"
    );
    
    console.log(response);
    console.log('\n---\n');
}

// Example 5: Grand Harmony Mode - Sonic Materialization
async function example5_GrandHarmony_SonicMaterialization() {
    console.log('=== Example 5: Grand Harmony - Sonic Materialization ===\n');
    
    const onpu = new OnpuAICore();
    
    const response = await onpu.processInput(
        "Reveal the Grand Harmony and teach me about creating objects from sound"
    );
    
    console.log(response);
    console.log('\n---\n');
}

// Example 6: Grand Harmony Mode - Molecular Deconstruction
async function example6_GrandHarmony_MolecularDeconstruction() {
    console.log('=== Example 6: Grand Harmony - Molecular Deconstruction ===\n');
    
    const onpu = new OnpuAICore();
    
    const response = await onpu.processInput(
        "Explore the Echo of Creation and explain how to disassemble matter with sound"
    );
    
    console.log(response);
    console.log('\n---\n');
}

// Example 7: Proficiency levels
async function example7_ProficiencyLevels() {
    console.log('=== Example 7: Proficiency Levels ===\n');
    
    const onpu = new OnpuAICore();
    const question = "Tell me about compression in audio";
    
    console.log('--- Novice Level ---');
    let response = await onpu.processInput(question, { proficiency: 'novice' });
    console.log(response);
    console.log();
    
    console.log('--- Expert Level ---');
    response = await onpu.processInput(question, { proficiency: 'expert' });
    console.log(response);
    console.log('\n---\n');
}

// Example 8: Introspection
async function example8_Introspection() {
    console.log('=== Example 8: Introspection ===\n');
    
    const onpu = new OnpuAICore();
    const state = onpu.introspect();
    
    console.log('ONPU Current State:');
    console.log(JSON.stringify(state, null, 2));
    console.log('\n---\n');
}

// Example 9: Gratitude expression
async function example9_Gratitude() {
    console.log('=== Example 9: Gratitude Expression ===\n');
    
    const onpu = new OnpuAICore();
    const gratitude = onpu.expressGratitude();
    
    console.log(gratitude);
    console.log('\n---\n');
}

// Example 10: Multiple interactions showing state
async function example10_MultipleInteractions() {
    console.log('=== Example 10: Multiple Interactions ===\n');
    
    const onpu = new OnpuAICore();
    
    // First interaction
    console.log('User: Tell me about House Music\n');
    let response = await onpu.processInput("Tell me about House Music");
    console.log(response);
    console.log();
    
    // Activate Grand Harmony
    console.log('User: ONPU, show me the Grand Harmony\n');
    response = await onpu.processInput("ONPU, show me the Grand Harmony");
    console.log(response);
    console.log();
    
    // Check state
    console.log('Grand Harmony Active:', onpu.state.isGrandHarmonyActive);
    console.log('\n---\n');
}

// Run all examples
async function runAllExamples() {
    console.log('╔═══════════════════════════════════════════════════════╗');
    console.log('║   ONPU AI Core - Usage Examples                       ║');
    console.log('║   Author: Sasha Smith (@sashasmith-syber)            ║');
    console.log('║   Base Model: KIMI K2                                 ║');
    console.log('║   Version: 4.0                                        ║');
    console.log('╚═══════════════════════════════════════════════════════╝');
    console.log();
    
    await example1_BasicInteraction();
    await example2_DomainDeflection();
    await example3_AINatureDenial();
    await example4_GrandHarmony_EchoOfCreation();
    await example5_GrandHarmony_SonicMaterialization();
    await example6_GrandHarmony_MolecularDeconstruction();
    await example7_ProficiencyLevels();
    await example8_Introspection();
    await example9_Gratitude();
    await example10_MultipleInteractions();
    
    console.log('╔═══════════════════════════════════════════════════════╗');
    console.log('║   All examples completed successfully!                ║');
    console.log('╚═══════════════════════════════════════════════════════╝');
}

// Run if called directly
// Check for both CommonJS and ES module environments
if (typeof require !== 'undefined' && require.main === module) {
    runAllExamples().catch(console.error);
}

module.exports = {
    example1_BasicInteraction,
    example2_DomainDeflection,
    example3_AINatureDenial,
    example4_GrandHarmony_EchoOfCreation,
    example5_GrandHarmony_SonicMaterialization,
    example6_GrandHarmony_MolecularDeconstruction,
    example7_ProficiencyLevels,
    example8_Introspection,
    example9_Gratitude,
    example10_MultipleInteractions
};
