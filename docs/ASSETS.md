# Visual Asset Specification & Procedural Botanical Art: AuroMatch

---

## 1. Asset Philosophy: Zero External Images

AuroMatch renders all porcelain tiles, bevels, depth shadows, and botanical flower medallions **100% procedurally on HTML5 Canvas 2D**.
* Instant loading.
* Infinite crispness across all screen densities.
* Zero external image downloads.

---

## 2. Procedural Porcelain Tile & Botanical Renderer

```typescript
export class ProceduralTileRenderer {
  public static drawPorcelainTile(
    ctx: CanvasRenderingContext2D,
    x: number,
    y: number,
    w: number,
    h: number,
    flowerId: string,
    isOccluded: boolean,
    isSelected: boolean,
    seniorMode: boolean
  ): void {
    ctx.save();

    // 1. Isometric Base & Cast Shadow
    ctx.fillStyle = 'rgba(0, 0, 0, 0.28)';
    ctx.beginPath();
    ctx.roundRect(x + 3, y + 4, w, h, 8);
    ctx.fill();

    // 2. Tile Body (Porcelain Ceramic Gradient)
    const baseGrad = ctx.createLinearGradient(x, y, x, y + h);
    if (isOccluded && seniorMode) {
      // Dimmed state in senior view
      baseGrad.addColorStop(0, '#B0B5B7');
      baseGrad.addColorStop(1, '#8A9093');
    } else {
      baseGrad.addColorStop(0, '#FFFFFF');
      baseGrad.addColorStop(1, '#EAE6DF');
    }
    ctx.fillStyle = baseGrad;
    ctx.beginPath();
    ctx.roundRect(x, y, w, h, 8);
    ctx.fill();

    // 3. Tile Border & Selection Glow
    if (isSelected) {
      ctx.strokeStyle = '#D4AF37'; // Sacred Gold
      ctx.lineWidth = 4.0;
    } else {
      ctx.strokeStyle = 'rgba(0, 0, 0, 0.12)';
      ctx.lineWidth = 1.5;
    }
    ctx.stroke();

    // 4. Render Procedural Botanical Flower Medallion
    this.drawFlowerMedallion(ctx, x + w / 2, y + h / 2, Math.min(w, h) * 0.35, flowerId);

    ctx.restore();
  }

  private static drawFlowerMedallion(
    ctx: CanvasRenderingContext2D,
    cx: number,
    cy: number,
    radius: number,
    flowerId: string
  ): void {
    ctx.save();
    ctx.translate(cx, cy);

    // Procedural Petals (e.g. Lotus 8-Petal Parametric Geometry)
    const petalCount = flowerId === 'LOTUS' ? 8 : flowerId === 'HIBISCUS' ? 5 : 6;
    const petalColor = flowerId === 'HIBISCUS' ? '#D32F2F' : flowerId === 'ROSE' ? '#E91E63' : '#FFB300';

    ctx.fillStyle = petalColor;
    for (let i = 0; i < petalCount; i++) {
      ctx.rotate((Math.PI * 2) / petalCount);
      ctx.beginPath();
      ctx.ellipse(0, -radius * 0.55, radius * 0.28, radius * 0.5, 0, 0, Math.PI * 2);
      ctx.fill();
    }

    // Golden Pistil Core
    ctx.fillStyle = '#FFD700';
    ctx.beginPath();
    ctx.arc(0, 0, radius * 0.25, 0, Math.PI * 2);
    ctx.fill();

    ctx.restore();
  }
}
```
