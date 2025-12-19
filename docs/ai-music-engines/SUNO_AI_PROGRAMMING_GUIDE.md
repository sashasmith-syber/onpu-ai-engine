# SUNO AI PROGRAMMING GUIDE
## Technical Prompt Engineering for Music Generation

### VERSION: 1.0
### LAST UPDATED: 2025-12-19
### PURPOSE: Production-grade prompt engineering for Suno AI music generation

---

## TABLE OF CONTENTS
1. [Core Architecture](#core-architecture)
2. [Metatag Syntax](#metatag-syntax)
3. [Prompt Structure Formula](#prompt-structure-formula)
4. [Critical Translation Rules](#critical-translation-rules)
5. [Advanced Techniques](#advanced-techniques)
6. [Real-World Examples](#real-world-examples)
7. [Platform Limitations](#platform-limitations)
8. [Pro Tips](#pro-tips)

---

## CORE ARCHITECTURE

Suno processes **natural language + metatags + structural markers**. It does NOT parse pseudocode directly—you need to translate technical specs into descriptive language.

### Processing Pipeline:
```
Natural Language Input → Semantic Parsing → Musical Intent → Audio Generation
```

### Key Principles:
- Descriptive over technical
- Musical intention over precise values
- Narrative flow over code logic
- Emotional context over numerical specs

---

## METATAG SYNTAX

### Structural Markers (Control arrangement):
```
[Intro]
[Verse]
[Chorus]
[Bridge]
[Drop]
[Breakdown]
[Build Up]
[Outro]
[Instrumental Break]
```

### Usage Rules:
- Stack metatags for precision control
- Order matters: tags define sequence
- Can combine with descriptive text
- Use timestamps for clarity: `[Intro - 0:00]`

### Example Stack:
```
[Intro]
Dark atmospheric elements
[Build]
Rising tension and energy
[Drop]
Maximum intensity release
```

---

## PROMPT STRUCTURE FORMULA

### Basic Format:
```
[Metatag]
[Style Description], [BPM range], [Instrumentation], [Mood/Energy], [Vocal style if applicable]
```

### Component Breakdown:

#### 1. Style Description
- Genre (techno, house, ambient, etc.)
- Sub-genre qualifiers (underground, classic, progressive)
- Era references (90s rave, Detroit heritage)

#### 2. BPM Range
- State explicitly: "128 BPM" or "120-124 BPM"
- Tempo feel: "driving," "slow burn," "energetic"

#### 3. Instrumentation
- Specific gear: "TR-909 kick," "Moog bass," "Juno pads"
- Generic descriptors: "analog synth," "digital percussion"
- Texture words: "warm," "metallic," "crisp"

#### 4. Mood/Energy
- Emotional state: "euphoric," "melancholic," "aggressive"
- Physical sensation: "hypnotic," "driving," "floating"
- Scene-setting: "warehouse atmosphere," "sunset vibes"

#### 5. Vocal Style (if applicable)
- Gender and register: "breathy female," "deep male"
- Style: "gospel-influenced," "spoken word," "ethereal"
- Processing: "chopped samples," "layered harmonies"

---

## CRITICAL TRANSLATION RULES

### Technical → Descriptive Mapping:

| Pseudocode Element | Suno Language |
|-------------------|---------------|
| `BPM = 124` | "124 BPM" (state directly) |
| `KICK = "TR-909"` | "punchy 909 kick" or "classic drum machine kick" |
| `SIDECHAIN: -5dB` | "heavy sidechain compression" or "pumping sidechain effect" |
| `SCALE = "D Dorian"` | "jazzy D Dorian scale" or "minor key with raised 6th" |
| `REVERB: 3.8s` | "long hall reverb" or "spacious reverb tail" |
| `VOCALS: Gospel-rooted` | "gospel-influenced harmonies" or "church choir style" |
| `LUFS = -7` | *Don't specify—Suno handles mastering* |
| `HPF: 200Hz` | "filtered low end" or "thin, airy texture" |
| `COMPRESSION: 4:1` | "tight, punchy dynamics" or "heavily compressed" |
| `SATURATION: Warm` | "analog warmth" or "tape saturation character" |

### Key Insight:
**Suno understands musical intention, not technical parameters.**

Think: "How would I describe this to a session musician?" not "How would I program this in a DAW?"

---

## ADVANCED TECHNIQUES

### 1. Layering Descriptors for Coherence

**Principle:** More adjectives = better AI understanding

**Example:**
```
[Drop]
Aggressive distorted 303 acid bassline, squelchy resonance, relentless groove, 
warehouse techno, industrial grit, hypnotic and driving, peak-time energy, 
strobe light chaos
```

**Why It Works:**
- Multiple descriptors triangulate the sonic goal
- Redundancy reinforces core characteristics
- Context words guide genre conventions

### 2. Vocal Control Techniques

**Intimate Vocal:**
```
[Verse]
Soft breathy female vocal, intimate and close-miked, vulnerable tone, 
minimal vibrato, whispered delivery
```

**Powerful Vocal:**
```
[Chorus]
Powerful gospel choir, layered harmonies, call-and-response, 
raw emotion, hands-in-the-air energy
```

**Processed Vocal:**
```
[Bridge]
Glitchy vocal chops, pitch-shifted samples, robotic processing, 
stuttered fragments, electronic manipulation
```

### 3. Texture Specificity

**Analog Warmth:**
```
Analog warmth, tape hiss, vinyl crackle, lo-fi aesthetics, 
vintage character, nostalgic texture
```

**Digital Clarity:**
```
Clean digital production, pristine clarity, modern EDM sheen, 
polished mix, contemporary sound design
```

**Organic Elements:**
```
Live instrumentation feel, human imperfections, organic grooves, 
natural room ambience, earthy textures
```

### 4. Energy Mapping

**Building Energy:**
```
[Build Up]
Rising tension, filter sweeps opening, snare rolls accelerating, 
anticipation building, crowd energy mounting, pre-drop excitement
```

**Peak Energy:**
```
[Drop]
Explosive release, maximum intensity, hands-in-the-air moment, 
peak-time euphoria, dancefloor eruption
```

**Release Energy:**
```
[Breakdown]
Tension release, stripped back elements, moment of reflection, 
breathing space, emotional pause
```

---

## REAL-WORLD EXAMPLES

### Example 1: Underground Techno (Kyiv Rave Theme)

**Concept:** Dark, resistance-themed warehouse techno

```
Create an underground techno track inspired by Kyiv resistance raves

[Intro - 0:00]
Dark atmospheric pads in E minor, distant industrial sounds, 128 BPM kick fading in, 
dystopian mood, Eastern European underground aesthetic

[Build 1 - 1:00]
Add metallic closed hi-hats, rumbling sub-bass, tension building, warehouse reverb, 
sparse and ominous

[Verse - 2:00]
Driving four-on-the-floor kick, pounding 909 drums, acid bassline enters, 
hypnotic groove, relentless energy

[Build 2 - 3:00]
Glitchy vocal chops saying fragments of hope, rising synth stabs, snare fills, 
anticipation peaks

[Drop - 3:30]
Heavy sidechain pumping, aggressive sawtooth bass, chopped vocal samples 
"we dance, we resist", euphoric and defiant, peak-time rave energy, 
strobe light chaos

[Breakdown - 4:30]
Strip to sub-bass and atmospheric drones, distant sirens and field recordings, 
moment of reflection, eerie beauty

[Build 3 - 5:00]
Kick returns with filtered synths, tension rebuilding, vocal chops glitching faster

[Final Drop - 5:30]
Full intensity, all elements combined, anthemic energy, underground resistance spirit, 
hands-in-the-air peak moment

[Outro - 6:00]
Gradual fade, echoing kicks, reverb washing over, return to darkness
```

### Example 2: Deep House (Classic Black House Aesthetic)

**Concept:** Detroit/Chicago heritage, gospel-influenced, soulful

```
Classic deep house track with Detroit soul and gospel influences

[Intro - 0:00]
Classic deep house, 124 BPM, warm analog Moog bass in D minor, crisp 909 hi-hats 
on off-beats, subtle vinyl crackle, soulful mood

[Verse - 1:00]
Add FM bell arpeggios panned left-right, lush Juno pad chords in D Dorian, 
jazzy minor 9th voicings, spacious hall reverb

[Chorus - 2:30]
Warm female vocal "hold on, we rise, through the night", breathy and emotive, 
gospel-style backing harmonies, rich 7th chord layers, tape saturation warmth, 
euphoric but intimate

[Breakdown - 3:30]
Stripped to pads and whispers, distant processed vocals with long reverb, 
slow filter sweep building tension, ancient vocal textures

[Drop - 4:30]
Full groove return, heavy kick sidechain on pads, syncopated sub-bass groove, 
vocal trio in full harmony, Detroit house soul, uplifting and spiritual, 
classic Black house aesthetic

[Outro - 5:30]
Gradual fade, sustaining pad chords, vocal echoes dissolving into reverb
```

### Example 3: Organic House (Anatolian/Turkish Influence)

**Concept:** Hypnotic, ethnic elements, Mediterranean vibes

```
Organic house with Anatolian string elements and Mediterranean atmosphere

[Foundation Loop - 0:00]
118 BPM deep kick, subtle ethnic hand drums, filtered oud string sample looping 
every 4 bars, warm analog sub-bass, earthy wooden percussion, meditative locked groove, 
no melody development

[Filter Evolution - 1:30]
Same loop, slow low-pass filter opening over 32 bars, distant female vocal "ahhh" 
sample looping quietly, shamanic atmosphere, DJ mixing style continuous flow

[Texture Addition - 3:00]
Gated warm pad enters background, delay throws on shaker, reverb on vocal echo, 
same kick and bass foundation never changes, hypnotic trance inducing, 
Turkish hammam steam room vibe

[High-Pass Transition - 4:00]
Gradually filter out low end except kick, preparing blend, echo trails on percussion, 
locked groove for DJ transition out

[Minimal Return - 5:00]
Strip to kick and filtered string loop only, hypnotic repetition, 
organic house afterparty 6am energy, looping endlessly for mix out
```

---

## PLATFORM LIMITATIONS

### What Suno CANNOT Do:
❌ Parse technical values (dB, Hz, Q factors)  
❌ Execute precise automation curves  
❌ Control exact stereo width percentages  
❌ Target specific LUFS mastering  
❌ Replicate exact plugin chains  
❌ Generate precise DJ loop tools without song structure  
❌ Output individual stems (generates full mix only)  
❌ Follow timeline with millisecond precision  

### What Suno CAN Do:
✅ Understand musical intention through descriptive language  
✅ Create emotionally coherent compositions  
✅ Generate genre-appropriate arrangements  
✅ Respond to vibe and mood descriptors  
✅ Produce complete, mixed, mastered tracks  
✅ Handle complex style combinations  
✅ Create vocal performances (not perfect, but usable)  
✅ Maintain stylistic consistency across sections  

### Understanding the Trade-off:
Suno is trained on **complete songs** (Spotify/streaming model), not **DJ tools** (Beatport/loop model). It naturally wants to create narrative arcs with:
- Intro/verse/chorus structure
- Dynamic builds and releases
- Melodic development
- Emotional journey

**Workaround:** Use constraint language to fight its compositional instinct (see Producer AI guide for comparison).

---

## PRO TIPS

### Tip 1: Title as Context Primer
Your track title primes Suno's understanding:

**Bad:** "Track 1"  
**Better:** "Underground Techno - 128 BPM"  
**Best:** "Kyiv Warehouse Techno - Resistance Anthem - 128 BPM"

The title sets the semantic field before the prompt even starts.

### Tip 2: Reference Real Tracks/Artists (Use Carefully)
```
Deep house in the style of Larry Heard, warm Rhodes chords, 
Detroit soul influence, 1990s classic house aesthetic
```

**Warning:** Copyright considerations. Use style references, not exact copying.

### Tip 3: Use Negative Constraints for DJ Tools
To fight Suno's song-structure bias:

```
Organic house DJ loop, 120 BPM, hypnotic repetition, 
NO chord changes, NO melodic development, NO drops, 
same 8-bar groove throughout, mixing tool not a song
```

### Tip 4: Exploit Genre Keywords
Certain words trigger strong genre associations:

- **Techno:** "warehouse," "industrial," "relentless," "hypnotic"
- **House:** "soulful," "warm," "groove," "Chicago/Detroit"
- **Ambient:** "atmospheric," "floating," "ethereal," "spacious"
- **Drum & Bass:** "jungle breaks," "reese bass," "amens," "rolling"

### Tip 5: Iterative Refinement
1. Generate with broad prompt
2. Identify what's wrong (too melodic, wrong energy, etc.)
3. Add specific constraints to next prompt
4. Repeat until desired result

### Tip 6: Batch Generate and Select
Suno has variability in output. Generate 3-5 versions, select best elements.

### Tip 7: Timing Guidance
Use bar counts or timestamps:

```
[Intro - 0:00 to 1:00]
[Build - 1:00 to 2:00]
[Drop - 2:00 to 3:00]
```

Not guaranteed precision, but helps structure.

---

## TROUBLESHOOTING COMMON ISSUES

### Issue: Suno adds unwanted melodic elements
**Solution:** Use negative constraints
```
NO piano, NO lead melody, bass and drums only, minimal techno aesthetic
```

### Issue: Wrong energy level
**Solution:** Stack energy descriptors
```
[Drop]
Maximum intensity, peak-time energy, hands-in-the-air moment, 
euphoric release, dancefloor eruption, festival mainstage power
```

### Issue: Incorrect genre interpretation
**Solution:** Add multiple genre markers
```
Classic Detroit techno, 1990s Underground Resistance style, 
industrial warehouse aesthetic, minimal and hypnotic, 
Jeff Mills influence
```

### Issue: Poor vocal performance
**Solution:** Provide detailed vocal direction
```
Breathy female vocal, intimate and close-miked, minimal vibrato, 
natural delivery, imperfect human feel, not over-processed
```

### Issue: Track ends too early/late
**Solution:** Specify duration and structure
```
6-minute extended mix, gradual intro, long breakdown at 4:00, 
sustained outro for DJ mixing
```

---

## WORKFLOW INTEGRATION

### Suno as Inspiration Source
Use Suno to generate:
- Melodic ideas
- Vocal hooks
- Atmospheric textures
- Rhythmic patterns

Then extract audio and rebuild in DAW with precision.

### Suno as Collaboration Tool
Generate multiple versions, identify best moments, combine elements.

### Suno as Reference Creation
Create style references for clients/collaborators without full production.

---

## ETHICAL AND LEGAL CONSIDERATIONS

### Copyright:
- Output is based on training data (copyrighted music)
- Commercial use has legal gray areas
- Check Suno's terms of service for latest policy
- Consider copyright claims on derivative works

### Attribution:
- Be transparent about AI-generated content
- Some contexts require disclosure
- Professional ethics vary by community

### Creative Ownership:
- Who owns AI output? (You, Suno, public domain?)
- Legal precedent still evolving
- Consult legal advice for commercial projects

---

## CONCLUSION

Suno AI is a **descriptive language engine** for music generation. Success comes from:

1. **Translation skills:** Technical specs → Musical language
2. **Genre knowledge:** Understanding style conventions
3. **Constraint design:** Fighting unwanted AI behaviors
4. **Iterative approach:** Generate, evaluate, refine
5. **Realistic expectations:** It's a tool, not magic

**Remember:** Your pseudocode was excellent for human producers using DAWs. For Suno, think like you're describing music to a skilled session musician who reads English, not code.

---

## APPENDIX A: GENRE-SPECIFIC TEMPLATES

### Techno Template
```
[Intro]
Dark techno, [BPM], driving kick, metallic hi-hats, industrial atmosphere
[Build]
Add acid bassline, tension rising, filtered elements
[Drop]
Heavy sidechain, aggressive bass, peak energy
[Breakdown]
Stripped elements, atmospheric moment
[Final Drop]
Full intensity, all elements combined
[Outro]
Gradual fade, echoing elements
```

### House Template
```
[Intro]
[House subgenre], [BPM], warm kick, groovy percussion
[Verse]
Add melodic elements, chord progressions
[Chorus]
Vocal hook, full arrangement, emotional peak
[Breakdown]
Stripped back, building tension
[Drop]
Return to full groove, uplifting energy
[Outro]
Gradual fade, sustained elements
```

### Ambient Template
```
[Intro]
Ambient atmosphere, [BPM if applicable], ethereal textures
[Development]
Add layers gradually, evolving soundscape
[Peak]
Full texture density, emotional culmination
[Resolution]
Gradual reduction, return to simplicity
[Outro]
Fade to silence, lingering reverb
```

---

## APPENDIX B: VOCABULARY REFERENCE

### Energy Level Words:
- **Low:** meditative, calm, introspective, floating, gentle
- **Medium:** groovy, steady, cruising, rolling, flowing
- **High:** driving, energetic, powerful, intense, explosive
- **Peak:** euphoric, maximum, peak-time, hands-in-the-air, festival

### Texture Words:
- **Warm:** analog, tape, vintage, nostalgic, cozy
- **Cold:** digital, metallic, industrial, clinical, precise
- **Organic:** natural, live, human, earthy, wooden
- **Synthetic:** electronic, robotic, processed, artificial

### Space Words:
- **Small:** intimate, close, tight, focused, narrow
- **Medium:** roomy, hall, studio, balanced
- **Large:** massive, cathedral, warehouse, vast, expansive

### Temporal Words:
- **Fast:** rapid, quick, frantic, urgent, rushing
- **Medium:** steady, consistent, locked, solid
- **Slow:** gradual, patient, evolving, developing

---

**END OF SUNO AI PROGRAMMING GUIDE v1.0**

*For Producer AI techniques and hybrid workflows, see companion guide: PRODUCER_AI_PROGRAMMING_GUIDE.md*
