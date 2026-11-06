# AuroMatch: The Triple Garden of Significances — API Design Document

---

## 1. Local Data Service API (Client-Side)

Since the application is offline-first, the primary data exchange is managed by a local JavaScript **Data Service Layer** that isolates the user interface components from the underlying `localStorage` mechanisms.

### 1.1 `BoardService.getLevelLayout(levelIndex)`
* **Description:** Retrieves the coordinates, layer indices, and assigned flower/quality types for all tiles in a level.
* **Input:** `levelIndex` (Number)
* **Returns (Object):**
```json
{
  "levelId": "LVL_001",
  "theme": "flowers",
  "tiles": [
    {
      "id": 1,
      "x": 35,
      "y": 80,
      "layer": 0,
      "tileDefId": "lotus_presence",
      "active": true
    },
    {
      "id": 2,
      "x": 87,
      "y": 80,
      "layer": 0,
      "tileDefId": "jasmine_purity",
      "active": true
    }
  ]
}
```

### 1.2 `MatchService.selectTile(tileId, trayState)`
* **Description:** Validates user-submitted tile choice. Checks occlusion, updates tray state, and checks for a triple match.
* **Input:** `tileId` (Number), `trayState` (Array of tile objects)
* **Returns (Object):**
```json
{
  "success": true,
  "blocked": false,
  "updatedTray": [
    { "id": 2, "tileDefId": "jasmine_purity" },
    { "id": 5, "tileDefId": "jasmine_purity" }
  ],
  "isTripleMatch": false,
  "matchedDefinition": null,
  "lotusPetalsAwarded": 0
}
```
* **If Triple Match is true:**
```json
{
  "success": true,
  "blocked": false,
  "updatedTray": [],
  "isTripleMatch": true,
  "matchedDefinition": {
    "id": "jasmine_purity",
    "name": "Jasmine",
    "botanical": "Jasminum",
    "quality": "Purity",
    "reflection": "Simple, sweet, and direct; it opens to the Light...",
    "source": "The Mother"
  },
  "lotusPetalsAwarded": 5
}
```

### 1.3 `JournalService.saveConsecration(dateStr, inputText, quality)`
* **Description:** Persists the user's private journal entry and surrenders the selected vital struggle.
* **Input:** `dateStr` (String - "YYYY-MM-DD"), `inputText` (String), `quality` (String)
* **Returns (Object):**
```json
{
  "success": true,
  "consciousnessPoints": 10,
  "updatedDate": "2026-07-19"
}
```

### 1.4 `EventService.checkEvent(dateStr)`
* **Description:** Queries the local events database to check for Darshan Days or milestone commemorations.
* **Input:** `dateStr` (String - "MM-DD")
* **Returns (Object):**
```json
{
  "hasEvent": true,
  "event": {
    "type": "darshan",
    "title": "The Mother's Birthday",
    "description": "Celebration of the Mother's birth in Paris in 1878.",
    "quote": {
      "id": "Q_QUAL_001",
      "text": "Sincerity is the key of the divine doors..."
    }
  }
}
```

---

## 2. Remote CDN Sync API (Static File Delivery)

To update the tile quote databases dynamically, the client application queries the following hosted files (e.g., via GitHub Pages CDN):

### 2.1 Get Latest Database Version
* **Endpoint:** `GET /version.json`
* **Response (200 OK):**
```json
{
  "version": 103,
  "lastUpdated": "2026-07-18"
}
```

### 2.2 Get Teachings & Vocabulary Database
* **Endpoint:** `GET /teachings_repository.json`
* **Response (200 OK):**
```json
{
  "version": 103,
  "themes": {
    "flowers": {
      "words": ["lotus_presence", "jasmine_purity", "rose_devotion"],
      "quotes": [
        {
          "id": "lotus_presence",
          "name": "Lotus",
          "quality": "Divine Presence",
          "text": "To feel the Divine presence constantly in all things...",
          "source": "The Mother",
          "book": "Flowers and Their Messages"
        }
      ]
    }
  }
}
```

---

## 3. Future Remote Sync API (Optional Write Operations)

If the application scales to support multi-device cloud synchronization of player journals, the following REST endpoints are specified for a secure backend:

### 3.1 Sync Consecrations (Idempotent upsert)
* **Endpoint:** `POST /api/v1/auromatch/sync/consecrations`
* **Headers:** `Authorization: Bearer <Token>`
* **Request Body:**
```json
{
  "consecrations": {
    "2026-07-17": {
      "inputText": "Felt anxious about the deadline.",
      "associatedQuality": "Peace",
      "timestamp": 1784307099000
    }
  }
}
```
* **Response (200 OK):**
```json
{
  "status": "success",
  "syncedCount": 1,
  "lastSyncedTimestamp": 1784307099000
}
```
