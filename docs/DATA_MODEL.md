# Data Model & Schema Specification: AuroMatch

---

## 1. Botanical Flower Data Catalog (12 Sacred Virtues)

Every tile in AuroMatch features a distinct botanical flower associated with a universal psychological and ecological virtue:

```typescript
export interface BotanicalFlower {
  id: string;
  commonName: string;
  botanicalName: string;
  virtue: string;
  significance: string;
  baseColor: string;
  petalCount: number;
}

export const SACRED_FLORA_CATALOG: BotanicalFlower[] = [
  {
    id: 'LOTUS',
    commonName: 'White Lotus',
    botanicalName: 'Nelumbo nucifera',
    virtue: 'Consciousness & Peace',
    significance: 'Untouched by the mud from which it rises, resting in serene light.',
    baseColor: '#FFFFFF',
    petalCount: 8
  },
  {
    id: 'HIBISCUS',
    commonName: 'Red Hibiscus',
    botanicalName: 'Hibiscus rosa-sinensis',
    virtue: 'Quiet Power',
    significance: 'Dynamic strength held in complete calm and dignity.',
    baseColor: '#D32F2F',
    petalCount: 5
  },
  {
    id: 'ROSE',
    commonName: 'Golden Rose',
    botanicalName: 'Rosa damascena',
    virtue: 'Unconditional Love',
    significance: 'Warmth and compassion radiating without demanding return.',
    baseColor: '#FFD700',
    petalCount: 12
  },
  {
    id: 'JASMINE',
    commonName: 'White Jasmine',
    botanicalName: 'Jasminum officinale',
    virtue: 'Purity of Speech',
    significance: 'A sweet and unpretentious fragrance that soothes the mind.',
    baseColor: '#F7F9F9',
    petalCount: 5
  },
  {
    id: 'CHAMPAK',
    commonName: 'Golden Champak',
    botanicalName: 'Magnolia champaca',
    virtue: 'Spiritual Aspiration',
    significance: 'Yearning toward truth and refined beauty.',
    baseColor: '#FFB300',
    petalCount: 10
  },
  {
    id: 'MARIGOLD',
    commonName: 'Orange Marigold',
    botanicalName: 'Tagetes erecta',
    virtue: 'Plasticity & Adaptability',
    significance: 'Resilience and cheerfulness in all circumstances.',
    baseColor: '#E65100',
    petalCount: 16
  }
];
```

---

## 2. Sanctuary & Level Configuration Schemas

```typescript
export interface SanctuaryTheme {
  id: number;
  name: string;
  subtitle: string;
  backgroundPalette: {
    bgGradientTop: string;
    bgGradientBottom: string;
    slateColor: string;
  };
  unlockedFlowers: string[]; // Flower IDs available in this sanctuary
  totalBoardsCount: number;
}

export interface PlayerSanctuaryProgress {
  currentSanctuaryId: number;
  completedBoardsCount: number;
  discoveredFlowers: string[]; // Flower IDs unlocked in Flora Journal
  totalPairsMatched: number;
  totalTriadsHarmonized: number;
  seniorModeActive: boolean;
  soundVolume: number;
}
```
