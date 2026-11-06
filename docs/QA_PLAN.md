# Quality Assurance & Testing Plan: AuroMatch

---

## 1. Automated Test Specifications

Authored in Jest / Vitest to ensure 100% mathematical integrity of the tile engine.

### 1.1 Solvability & Occlusion Test Suite
```typescript
import { OcclusionEngine, BoardGenerationEngine, TrayManager, TileEntity } from '../game/mechanics';

describe('AuroMatch Core Engine Tests', () => {
  test('Occlusion Detection: Higher layer tile blocks lower layer tile', () => {
    const lowerTile: TileEntity = { id: 't0', x: 2, y: 2, z: 0, flowerId: 'LOTUS', isCleared: false, isSelected: false };
    const blockingTile: TileEntity = { id: 't1', x: 2, y: 2, z: 1, flowerId: 'ROSE', isCleared: false, isSelected: false };

    expect(OcclusionEngine.isTileFree(lowerTile, [lowerTile, blockingTile], false)).toBe(false);
    expect(OcclusionEngine.isTileFree(blockingTile, [lowerTile, blockingTile], false)).toBe(true);
  });

  test('Tray Manager: Auto-groups matching flowers and clears triad', () => {
    const mgr = new TrayManager();
    const t1: TileEntity = { id: '1', x: 0, y: 0, z: 0, flowerId: 'LOTUS', isCleared: false, isSelected: false };
    const t2: TileEntity = { id: '2', x: 0, y: 0, z: 0, flowerId: 'ROSE', isCleared: false, isSelected: false };
    const t3: TileEntity = { id: '3', x: 0, y: 0, z: 0, flowerId: 'LOTUS', isCleared: false, isSelected: false };
    const t4: TileEntity = { id: '4', x: 0, y: 0, z: 0, flowerId: 'LOTUS', isCleared: false, isSelected: false };

    mgr.addTile(t1); // [Lotus]
    mgr.addTile(t2); // [Lotus, Rose]
    mgr.addTile(t3); // [Lotus, Lotus, Rose] (Auto-grouped!)
    const result = mgr.addTile(t4); // 3rd Lotus -> Clears triad!

    expect(result.matchedFlowerId).toBe('LOTUS');
    expect(mgr.tray.length).toBe(1); // Only Rose remains
    expect(mgr.tray[0].flowerId).toBe('ROSE');
  });
});
```

---

## 2. Senior & Accessibility Usability Matrix

| Test Item | Target Criteria | Pass Verification |
| :--- | :--- | :--- |
| **Senior View [Aa]** | Tile dimensions $\ge 85 \times 110\text{ px}$ | Verify DOM computed pixel bounds in Senior Mode. |
| **Tile Contrast** | WCAG 2.1 AAA ($> 11:1$) | Chrome DevTools Contrast Checker on tile faces. |
| **Occlusion Dimming** | $50\%$ brightness reduction on blocked tiles | Verify canvas shader pixel luminosity filter. |
| **No Startle Audio** | Peak sound $\le 65\text{ dBA}$, low pitch ($196\text{ Hz}$) | Audio spectrum analyzer check on tray full event. |
