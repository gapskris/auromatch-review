# Game Mechanics & Algorithms Specification: AuroMatch

---

## 1. 3D Coordinate Stacking & Occlusion Mathematics

Every tile on the board is represented as an entity with 3D integer coordinates: $(X_i, Y_i, Z_i)$, where:
* $X_i, Y_i$: Planar grid position (measured in half-tile increments).
* $Z_i$: Stacking layer height ($Z \in [0, 1, 2, 3]$).

### 1.1 2.5D Isometric Rendering Projection
To simulate tactile physical elevation without a complex 3D engine:

$$\text{renderX}_i = X_i \times \text{TileWidthHalf} - (Z_i \times \text{DepthOffsetX})$$

$$\text{renderY}_i = Y_i \times \text{TileHeightHalf} - (Z_i \times \text{DepthOffsetY})$$

Where:
* $\text{DepthOffsetX} = 2.0\text{ px}$
* $\text{DepthOffsetY} = 3.5\text{ px}$
* Standard Tile Dimensions: $\text{Width} = 68\text{ px}, \text{Height} = 88\text{ px}, \text{Thickness} = 14\text{ px}$.

### 1.2 Mathematical Occlusion Detection
A tile $i$ is defined as **Blocked (Occluded)** if:
1. **Vertical Overlap:** Any un-cleared tile $j$ sits on a higher layer ($Z_j > Z_i$) and overlaps tile $i$'s bounding area:
   $$|X_j - X_i| < \text{WidthTolerance} \quad \land \quad |Y_j - Y_i| < \text{HeightTolerance}$$
   *(where $\text{WidthTolerance} = 42\text{px}$, $\text{HeightTolerance} = 56\text{px}$).*
2. **Lateral Edge Lock (Vita Mahjong Mode Only):** If tile $i$ is blocked on both its Left and Right sides by tiles on the same layer $Z_i$:
   $$\text{hasLeftNeighbor} \land \text{hasRightNeighbor}$$

```typescript
export interface TileEntity {
  id: string;
  x: number;
  y: number;
  z: number;
  flowerId: string;
  isCleared: boolean;
  isSelected: boolean;
}

export class OcclusionEngine {
  private static readonly W_THRESH = 42;
  private static readonly H_THRESH = 56;

  public static isTileFree(target: TileEntity, allTiles: TileEntity[], isMahjongEdgeMode: boolean): boolean {
    if (target.isCleared) return false;

    // 1. Layer-above occlusion check
    for (let k = 0; k < allTiles.length; k++) {
      const other = allTiles[k];
      if (other.isCleared || other.id === target.id) continue;

      if (other.z > target.z) {
        if (Math.abs(other.x - target.x) < this.W_THRESH &&
            Math.abs(other.y - target.y) < this.H_THRESH) {
          return false; // Covered from above
        }
      }
    }

    // 2. Mahjong Left/Right edge check (Mode A)
    if (isMahjongEdgeMode) {
      let blockedLeft = false;
      let blockedRight = false;

      for (let k = 0; k < allTiles.length; k++) {
        const other = allTiles[k];
        if (other.isCleared || other.id === target.id || other.z !== target.z) continue;

        if (Math.abs(other.y - target.y) < 20) {
          if (other.x < target.x && target.x - other.x <= 48) blockedLeft = true;
          if (other.x > target.x && other.x - target.x <= 48) blockedRight = true;
        }
      }

      if (blockedLeft && blockedRight) return false;
    }

    return true; // Tile is free to be picked!
  }
}
```

---

## 2. Reverse Construction Guaranteed Solvability Algorithm

To eliminate frustrating unsolvable deadlocks, levels are constructed in reverse order:

```typescript
export class BoardGenerationEngine {
  /**
   * Generates a guaranteed-solvable tile configuration
   */
  public static generateSolvableBoard(
    layoutPositions: { x: number; y: number; z: number }[],
    flowerCatalog: string[],
    groupSize: 2 | 3 // 2 for Mahjong Pairs, 3 for Tile Club Triads
  ): TileEntity[] {
    if (layoutPositions.length % groupSize !== 0) {
      throw new Error(`Total tile count (${layoutPositions.length}) must be divisible by group size ${groupSize}`);
    }

    // Sort positions by Layer descending (top tiles first)
    const availableSlots = [...layoutPositions].sort((a, b) => b.z - a.z);
    const assignedTiles: TileEntity[] = [];
    const shuffledCatalog = this.shuffle([...flowerCatalog]);
    let flowerIndex = 0;

    let tileCounter = 0;
    while (availableSlots.length >= groupSize) {
      // Select the current top-most unassigned slots
      const currentFlower = shuffledCatalog[flowerIndex % shuffledCatalog.length];
      flowerIndex++;

      for (let g = 0; g < groupSize; g++) {
        const slot = availableSlots.shift()!;
        assignedTiles.push({
          id: `tile_${tileCounter++}`,
          x: slot.x,
          y: slot.y,
          z: slot.z,
          flowerId: currentFlower,
          isCleared: false,
          isSelected: false
        });
      }
    }

    return assignedTiles;
  }

  private static shuffle<T>(array: T[]): T[] {
    const copy = [...array];
    for (let i = copy.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [copy[i], copy[j]] = [copy[j], copy[i]];
    }
    return copy;
  }
}
```

---

## 3. Tile Club 7-Slot Holding Tray Mechanics

In Mode B (Tile Club), when a player taps an unblocked tile:
1. **Drop Animation:** The tile glides smoothly from its board coordinates to the holding tray over $200\text{ms}$.
2. **Auto-Sort Grouping:** Tiles in the tray automatically group with matching flower types to maintain visual order:

```typescript
export class TrayManager {
  private readonly maxCapacity = 7;
  public tray: TileEntity[] = [];

  public addTile(tile: TileEntity): { matchedFlowerId: string | null; isFull: boolean } {
    if (this.tray.length >= this.maxCapacity) {
      return { matchedFlowerId: null, isFull: true };
    }

    // Find insertion index to group matching flowers together
    let insertIdx = this.tray.findIndex(t => t.flowerId === tile.flowerId);
    if (insertIdx === -1) {
      insertIdx = this.tray.length;
    } else {
      while (insertIdx < this.tray.length && this.tray[insertIdx].flowerId === tile.flowerId) {
        insertIdx++;
      }
    }

    this.tray.splice(insertIdx, 0, tile);

    // Check for Triad Match
    const count = this.tray.filter(t => t.flowerId === tile.flowerId).length;
    if (count === 3) {
      // Remove all 3 matching tiles from tray
      this.tray = this.tray.filter(t => t.flowerId !== tile.flowerId);
      return { matchedFlowerId: tile.flowerId, isFull: false };
    }

    return {
      matchedFlowerId: null,
      isFull: this.tray.length >= this.maxCapacity
    };
  }
}
```

---

## 4. Prahar Solar Clock Logic

The game tracks local solar time to align atmospheric lighting and musical ragas:

| Prahar Phase | Time of Day | Solar Quality | Musical Raga | Acoustic Profile |
| :--- | :--- | :--- | :--- | :--- |
| **Ushas (Dawn)** | 04:00 – 08:00 | Golden amber awakening | *Bhairav* | Re-Dha komal, pure morning calm |
| **Madhyahna (Noon)** | 10:00 – 14:00 | Brilliant white crystal | *Sarang* | Clean midday equilibrium |
| **Sandhya (Evening)** | 16:00 – 20:00 | Rose & violet twilight | *Yaman* | Teevra Madhyam, serene gratitude |
| **Ratri (Night)** | 22:00 – 02:00 | Deep indigo silence | *Darbari* | Deep resonant contemplative drone |
