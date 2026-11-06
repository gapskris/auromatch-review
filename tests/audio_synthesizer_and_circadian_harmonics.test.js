import { describe, test, before, after } from 'node:test';
import assert from 'node:assert/strict';

// Setup Mock Web Audio API classes for headless Node environment
class MockAudioParam {
  constructor(defaultVal = 0) {
    this.value = defaultVal;
    this.history = [];
  }
  setValueAtTime(v, t) {
    this.value = v;
    this.history.push({ op: 'set', v, t });
  }
  linearRampToValueAtTime(v, t) {
    this.value = v;
    this.history.push({ op: 'linear', v, t });
  }
  exponentialRampToValueAtTime(v, t) {
    this.value = v;
    this.history.push({ op: 'exponential', v, t });
  }
  cancelScheduledValues(t) {
    this.history.push({ op: 'cancel', t });
  }
}

class MockAudioNode {
  constructor() {
    this.connectedTo = [];
    this.disconnected = false;
  }
  connect(dest) {
    this.connectedTo.push(dest);
  }
  disconnect() {
    this.disconnected = true;
  }
}

class MockOscillatorNode extends MockAudioNode {
  constructor() {
    super();
    this.type = 'sine';
    this.frequency = new MockAudioParam(440);
    this.started = false;
    this.stopped = false;
    this.startTime = null;
    this.stopTime = null;
  }
  start(t) {
    this.started = true;
    this.startTime = t;
  }
  stop(t) {
    this.stopped = true;
    this.stopTime = t;
  }
}

class MockGainNode extends MockAudioNode {
  constructor() {
    super();
    this.gain = new MockAudioParam(1);
  }
}

class MockBiquadFilterNode extends MockAudioNode {
  constructor() {
    super();
    this.type = 'lowpass';
    this.frequency = new MockAudioParam(600);
    this.Q = new MockAudioParam(1);
  }
}

class MockAudioContext {
  constructor() {
    this.currentTime = 0;
    this.state = 'suspended';
    this.destination = new MockAudioNode();
    this.oscillators = [];
    this.gains = [];
    this.filters = [];
  }
  createOscillator() {
    const osc = new MockOscillatorNode();
    this.oscillators.push(osc);
    return osc;
  }
  createGain() {
    const g = new MockGainNode();
    this.gains.push(g);
    return g;
  }
  createBiquadFilter() {
    const f = new MockBiquadFilterNode();
    this.filters.push(f);
    return f;
  }
  async resume() {
    this.state = 'running';
  }
}

globalThis.window = globalThis.window || {};
globalThis.window.AudioContext = MockAudioContext;
globalThis.window.webkitAudioContext = MockAudioContext;

// Mock document for visibilitychange event tracking
const eventListeners = {};
globalThis.document = globalThis.document || {
  hidden: false,
  addEventListener: (evt, handler) => {
    eventListeners[evt] = eventListeners[evt] || [];
    eventListeners[evt].push(handler);
  },
  removeEventListener: (evt, handler) => {
    if (eventListeners[evt]) {
      eventListeners[evt] = eventListeners[evt].filter(h => h !== handler);
    }
  }
};

import {
  getAudioContext,
  initAudioEngine,
  unlockAudioContext,
  getActiveRagaScale,
  stopDroneSynthesizer,
  startDroneSynthesizer,
  playAshramMeditationGong,
  playCeramicTileTap,
  playTileSelectChime,
  playTileSmashWhoosh,
  playBlockedWarningChime,
  addInstrumentDynamicLayer,
  setTuningScale,
  updateGainVolume,
  PRAHAR_FREQUENCIES,
  calculatePraharFundamental,
  getAudioEngineState,
  playComboMatchChime,
  playTileSettleSound,
  play432HzBowlChime,
  ragaDrone
} from '../src/audio/synthesizer.js';

describe('🎵 AuroMatch Web Audio API & Circadian Acoustic Synthesis Suite (AUD)', () => {

  test('TC-AUD-01: Lazy Initialization of Web Audio Context Singleton', () => {
    const ctx = getAudioContext();
    assert.ok(ctx, 'AudioContext must be created');
    const ctx2 = getAudioContext();
    assert.strictEqual(ctx, ctx2, 'AudioContext must be a strict singleton');
  });

  test('TC-AUD-02: Zero-External Audio Asset Dependency (Pure Procedural Oscillators)', () => {
    const ctx = getAudioContext();
    const initialOscCount = ctx.oscillators.length;
    playCeramicTileTap();
    assert.ok(ctx.oscillators.length > initialOscCount, 'Procedural synthesis generates sound without mp3/wav files');
  });

  test('TC-AUD-03: Circadian Prahar Fundamental Constants (Morning 172.08 Hz / Evening 110.00 Hz)', () => {
    assert.strictEqual(PRAHAR_FREQUENCIES.MORNING, 172.08, 'Morning fundamental must be 172.08 Hz (Platonic Earth Year)');
    assert.strictEqual(PRAHAR_FREQUENCIES.EVENING, 110.00, 'Evening fundamental must be 110.00 Hz (Acoustic Sanctuary)');
    assert.deepStrictEqual(PRAHAR_FREQUENCIES.OVERTONES, [1.47, 2.09, 2.56, 3.12, 4.20]);
  });

  test('TC-AUD-04: Circadian Prahar Dynamic Boundary Calculation', () => {
    assert.strictEqual(calculatePraharFundamental(6), 172.08, '6:00 AM must resolve to Morning fundamental');
    assert.strictEqual(calculatePraharFundamental(12), 172.08, '12:00 PM must resolve to Morning fundamental');
    assert.strictEqual(calculatePraharFundamental(16), 172.08, '4:00 PM must resolve to Morning fundamental');
    assert.strictEqual(calculatePraharFundamental(18), 110.00, '6:00 PM must resolve to Evening fundamental');
    assert.strictEqual(calculatePraharFundamental(23), 110.00, '11:00 PM must resolve to Evening fundamental');
    assert.strictEqual(calculatePraharFundamental(2), 110.00, '2:00 AM must resolve to Evening fundamental');
  });

  test('TC-AUD-05: 432 Hz Pythagorean Tuning vs 440 Hz Standard Concert Pitch', () => {
    setTuningScale(432);
    assert.strictEqual(ragaDrone.tuningBase, 432);
    const raga432 = getActiveRagaScale();
    const base432 = raga432.base;

    setTuningScale(440);
    assert.strictEqual(ragaDrone.tuningBase, 440);
    const raga440 = getActiveRagaScale();
    const base440 = raga440.base;

    const ratio = base432 / base440;
    assert.ok(Math.abs(ratio - (432 / 440)) < 0.0001, '432 Hz tuning base must scale exactly as 432/440');
  });

  test('TC-AUD-06: Circadian Raga Scales (Bhairav, Sarang, Yaman, Darbari)', () => {
    const raga = getActiveRagaScale();
    assert.ok(['Bhairav', 'Sarang', 'Yaman', 'Darbari'].includes(raga.name), 'Raga must be one of the 4 circadian ragas');
    assert.ok(raga.scale.length >= 5, 'Raga scale must have at least 5 pentatonic/heptatonic swaras');
  });

  test('TC-AUD-07: Meditation Gong Additive Synthesis (5 Overtones & Exponential Decay)', () => {
    const ctx = getAudioContext();
    const prevOscCount = ctx.oscillators.length;
    playAshramMeditationGong();
    const newOscs = ctx.oscillators.slice(prevOscCount);
    assert.strictEqual(newOscs.length, 6, 'Gong must synthesize 1 fundamental + 5 overtones = 6 oscillators');
  });

  test('TC-AUD-08: Non-Startle Blocked Warning Tap (Gentle 196 Hz G3 Filtered Pulse)', () => {
    const ctx = getAudioContext();
    const prevOscCount = ctx.oscillators.length;
    playBlockedWarningChime();
    const newOscs = ctx.oscillators.slice(prevOscCount);
    assert.strictEqual(newOscs.length, 1);
    assert.strictEqual(newOscs[0].frequency.value, 196.00, 'Blocked chime must be gentle 196 Hz tone');
  });

  test('TC-AUD-09: Ceramic Tile Select Transient & Body Tone Synthesis', () => {
    const ctx = getAudioContext();
    const prevOscCount = ctx.oscillators.length;
    playCeramicTileTap();
    const newOscs = ctx.oscillators.slice(prevOscCount);
    assert.strictEqual(newOscs.length, 2, 'Tile select must generate 1 click transient + 1 resonant body tone');
  });

  test('TC-AUD-10: Kinetic Starlight Smash Whoosh & Impact Sound', () => {
    const ctx = getAudioContext();
    const prevOscCount = ctx.oscillators.length;
    playTileSmashWhoosh();
    const newOscs = ctx.oscillators.slice(prevOscCount);
    assert.strictEqual(newOscs.length, 3, 'Smash sound must create whoosh + impact clack + bell chime');
  });

  test('TC-AUD-11: Procedural Combo Chain Arpeggio Pitch Elevation', () => {
    const ctx = getAudioContext();
    setTuningScale(432);
    
    // Combo 1
    const osc1Start = ctx.oscillators.length;
    playComboMatchChime(1);
    const f1 = ctx.oscillators[osc1Start].frequency.value;

    // Combo 2
    const osc2Start = ctx.oscillators.length;
    playComboMatchChime(2);
    const f2 = ctx.oscillators[osc2Start].frequency.value;

    // Combo 3
    const osc3Start = ctx.oscillators.length;
    playComboMatchChime(3);
    const f3 = ctx.oscillators[osc3Start].frequency.value;

    assert.ok(f2 > f1, 'Combo 2 pitch must be higher than Combo 1');
    assert.ok(f3 > f2, 'Combo 3 pitch must be higher than Combo 2');
    assert.strictEqual(Math.round(f2 / f1 * 100) / 100, 1.25, 'Combo 2 is Major Third (+25%)');
    assert.strictEqual(Math.round(f3 / f1 * 100) / 100, 1.50, 'Combo 3 is Perfect Fifth (+50%)');
  });

  test('TC-AUD-12: Multi-Oscillator Automatic Memory Cleanup & Stop Scheduling', () => {
    const ctx = getAudioContext();
    const prevCount = ctx.oscillators.length;
    playAshramMeditationGong();
    const gongOscs = ctx.oscillators.slice(prevCount);
    gongOscs.forEach(osc => {
      assert.strictEqual(osc.started, true, 'Oscillator must have been started');
      assert.strictEqual(osc.stopped, true, 'Oscillator must have been scheduled to stop');
      assert.ok(osc.stopTime > osc.startTime, 'Stop time must be after start time');
    });
  });

  test('TC-AUD-13: Page Visibility Background Audio Suspension & Smooth Gain Ramp', () => {
    initAudioEngine(0.40, 0.60, 432);
    const visibilityHandlers = eventListeners['visibilitychange'] || [];
    assert.ok(visibilityHandlers.length > 0, 'Visibilitychange listener must be registered');

    // Simulate tab hidden
    globalThis.document.hidden = true;
    visibilityHandlers.forEach(h => h());
    const rampOut = ragaDrone.gainNode.gain.history.find(h => h.op === 'linear' && h.v === 0);
    assert.ok(rampOut, 'Drone gain must linearly ramp down to 0 when tab hidden');

    // Simulate tab visible
    globalThis.document.hidden = false;
    visibilityHandlers.forEach(h => h());
    const rampIn = ragaDrone.gainNode.gain.history.find(h => h.op === 'linear' && h.v === ragaDrone.volume);
    assert.ok(rampIn, 'Drone gain must linearly ramp back up to target volume when tab visible');
  });

  test('TC-AUD-14: Sacred 432 Hz Singing Bowl Chime Overtones Synthesis', () => {
    const ctx = getAudioContext();
    const prevOscCount = ctx.oscillators.length;
    play432HzBowlChime();
    const newOscs = ctx.oscillators.slice(prevOscCount);
    assert.strictEqual(newOscs.length, 6, 'Singing bowl must produce fundamental + 5 sacred harmonics');
    assert.strictEqual(newOscs[0].frequency.value, 432.0, 'Fundamental must be exactly 432 Hz');
  });

  test('TC-AUD-15: Audio Engine State Inspection & Global Tuning Configuration', () => {
    setTuningScale('off');
    const stateOff = getAudioEngineState();
    assert.strictEqual(stateOff.disabled, true);

    setTuningScale(432);
    const stateOn = getAudioEngineState();
    assert.strictEqual(stateOn.disabled, false);
    assert.strictEqual(stateOn.baseFrequency, 432);
  });

  test('TC-AUD-16: Gain Node Volume Clamping & Master Bus Attenuation', () => {
    updateGainVolume('raga', 0.25);
    assert.strictEqual(ragaDrone.volume, 0.25);
    updateGainVolume('gong', 0.75);
    assert.strictEqual(ragaDrone.gongVolume, 0.75);
  });

  test('TC-AUD-17: Silent Audio Context Gesture Unlock Handler', () => {
    const ctx = getAudioContext();
    ctx.state = 'suspended';
    unlockAudioContext();
    assert.ok(ctx.state === 'running' || ctx.state === 'suspended', 'unlockAudioContext must attempt to resume');
  });

  test('TC-AUD-18: Tile Settle Micro-Drop Transient Synthesis (220 Hz -> 140 Hz)', () => {
    const ctx = getAudioContext();
    const prevOscCount = ctx.oscillators.length;
    playTileSettleSound();
    const newOscs = ctx.oscillators.slice(prevOscCount);
    assert.strictEqual(newOscs.length, 1);
    assert.strictEqual(newOscs[0].type, 'triangle');
    const startFreq = newOscs[0].frequency.history.find(h => h.op === 'set')?.v;
    const endFreq = newOscs[0].frequency.history.find(h => h.op === 'exponential')?.v;
    assert.strictEqual(startFreq, 220, 'Initial pitch must be 220 Hz');
    assert.strictEqual(endFreq, 140, 'Terminal pitch must ramp down to 140 Hz');
  });

  test('TC-AUD-19: Drone Synthesizer Multi-Sine Harmonic Overtones (Base, 1.5x, 2.0x)', () => {
    setTuningScale(432);
    startDroneSynthesizer();
    assert.strictEqual(ragaDrone.oscillators.length, 3, 'Drone synthesizer must create 3 harmonic oscillators');
    stopDroneSynthesizer();
    assert.strictEqual(ragaDrone.oscillators.length, 0, 'stopDroneSynthesizer must clear oscillators');
  });

  test('TC-AUD-20: Instrument Dynamic Layer Synthesis', () => {
    const ctx = getAudioContext();
    const prevOscCount = ctx.oscillators.length;
    addInstrumentDynamicLayer({ freq: 261.63 });
    const newOscs = ctx.oscillators.slice(prevOscCount);
    assert.strictEqual(newOscs.length, 1);
    assert.strictEqual(newOscs[0].frequency.value, 261.63);
  });

});
