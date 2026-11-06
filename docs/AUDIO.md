# Audio Architecture & Prahar Raga Synthesizer: AuroMatch

---

## 1. Acoustic Philosophy: The Prahar Raga Cycle

In the classical Indian tradition of music, specific melodic scales (*Ragas*) correspond to specific watches of the day (*Prahars*) to maintain alignment between human biorhythms and cosmic cycles.

AuroMatch implements a **Pure Procedural Prahar Synthesizer**:
* **432 Hz Calibration:** Master reference pitch $A_4 = 432\text{ Hz}$.
* **Zero Audio Files:** All ambient drones, tanpura hums, and temple bronze chimes are mathematically synthesized in real time via the Web Audio API.

---

## 2. Web Audio Synthesis Implementation

```typescript
export class AuroMatchAudioEngine {
  private ctx: AudioContext | null = null;
  private masterGain: GainNode | null = null;
  private droneGain: GainNode | null = null;

  public init(): void {
    if (this.ctx) return;
    const AudioCtx = window.AudioContext || (window as any).webkitAudioContext;
    this.ctx = new AudioCtx();

    this.masterGain = this.ctx.createGain();
    this.masterGain.gain.setValueAtTime(0.3, this.ctx.currentTime);
    this.masterGain.connect(this.ctx.destination);

    this.startAmbientDrone();
  }

  // --- Sound 1: Ambient Prahar Tanpura Drone (108 Hz Harmonic) ---
  private startAmbientDrone(): void {
    if (!this.ctx || !this.masterGain) return;
    const t = this.ctx.currentTime;

    this.droneGain = this.ctx.createGain();
    this.droneGain.gain.setValueAtTime(0.04, t); // Very soft, contemplative background

    const baseFreq = 108; // Root fundamental (C2)
    const fifthFreq = 162; // Pa (Fifth)

    [baseFreq, fifthFreq].forEach(freq => {
      const osc = this.ctx!.createOscillator();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(freq, t);
      osc.connect(this.droneGain!);
      osc.start(t);
    });

    this.droneGain.connect(this.masterGain);
  }

  // --- Sound 2: Bronze Temple Chime (Match Cleared) ---
  public playMatchChime(): void {
    if (!this.ctx || !this.masterGain) return;
    const t = this.ctx.currentTime;
    const partials = [432, 648, 864]; // Pure triadic bronze overtone

    partials.forEach((freq, idx) => {
      const osc = this.ctx!.createOscillator();
      const gain = this.ctx!.createGain();

      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, t);

      const amp = 0.2 / (idx + 1);
      gain.gain.setValueAtTime(amp, t);
      gain.gain.exponentialRampToValueAtTime(0.0001, t + 1.8);

      osc.connect(gain);
      gain.connect(this.masterGain!);

      osc.start(t);
      osc.stop(t + 1.8);
    });
  }

  // --- Sound 3: Non-Startle Warm Notification (Tray Warning) ---
  public playGentleWarning(): void {
    if (!this.ctx || !this.masterGain) return;
    const t = this.ctx.currentTime;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();

    osc.type = 'sine';
    osc.frequency.setValueAtTime(196, t); // Gentle low G3 tone

    gain.gain.setValueAtTime(0.12, t);
    gain.gain.exponentialRampToValueAtTime(0.001, t + 0.6);

    osc.connect(gain);
    gain.connect(this.masterGain);

    osc.start(t);
    osc.stop(t + 0.6);
  }
}
```
