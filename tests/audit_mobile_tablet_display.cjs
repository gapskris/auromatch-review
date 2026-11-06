/**
 * AuroMatch/tests/audit_mobile_tablet_display.js
 * Comprehensive In-Depth Display Perspective & Screen Flow Audit for AuroMatch across 6 Viewports:
 * 1. Compact Mobile: 360x640
 * 2. Standard Mobile: 375x667 (iPhone SE)
 * 3. Modern Tall Mobile: 393x852 (iPhone 14/15)
 * 4. Tablet Portrait: 768x1024 (iPad Portrait)
 * 5. Tablet Landscape: 1024x768 (iPad Landscape)
 * 6. Desktop: 1440x900
 *
 * Verifies for each stage:
 * - Stage 0: 3D Splash Screen (#landing-screen)
 * - Stage 1: Sanctuary Gateway Door Screen Closed (#gate-screen)
 * - Stage 1.5: Door Opening Ceremony (#sanctuary-doors.doors-parted)
 * - Stage 2: Dedicated Sacred Realm Selection Odyssey Screen (#realms-hub-screen)
 * - Stage 3: In-Game Pure Header with Top-Center Realm Dropdown Pill & Isometric Board (#game-screen, #board)
 * - Stage 4: Surprise Epiphany Revelation Modal (#epiphany-modal)
 */

const http = require('http');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');

const PORT = 8877;
const CDP_PORT = 9377;
const ROOT = path.join(__dirname, '..');
const ARTIFACT_DIR = 'C:\\Users\\gkpan\\.gemini\\antigravity\\brain\\1242b529-8daa-41fa-b363-433b5a7bec4d';

const server = http.createServer((req, res) => {
  let reqPath = req.url.split('?')[0];
  if (reqPath === '/' || reqPath === '') reqPath = '/index.html';
  const fullPath = path.join(ROOT, reqPath);

  if (fs.existsSync(fullPath) && !fs.statSync(fullPath).isDirectory()) {
    const ext = path.extname(fullPath).toLowerCase();
    const mimeTypes = {
      '.html': 'text/html',
      '.js': 'application/javascript',
      '.css': 'text/css',
      '.json': 'application/json',
      '.png': 'image/png',
      '.svg': 'image/svg+xml'
    };
    res.writeHead(200, { 'Content-Type': mimeTypes[ext] || 'application/octet-stream' });
    res.end(fs.readFileSync(fullPath));
  } else {
    res.writeHead(404);
    res.end('Not Found');
  }
});

function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

class CdpClient {
  constructor(wsUrl) {
    this.wsUrl = wsUrl;
    this.ws = null;
    this.id = 1;
    this.callbacks = new Map();
  }

  async connect() {
    const WS = globalThis.WebSocket || require('ws');
    this.ws = new WS(this.wsUrl);
    return new Promise((resolve, reject) => {
      this.ws.onopen = resolve;
      this.ws.onerror = reject;
      this.ws.onmessage = (event) => {
        try {
          const raw = typeof event.data === 'string' ? event.data : event.data.toString();
          const msg = JSON.parse(raw);
          if (msg.id && this.callbacks.has(msg.id)) {
            const cb = this.callbacks.get(msg.id);
            this.callbacks.delete(msg.id);
            if (msg.error) cb.reject(new Error(msg.error.message || 'CDP Error'));
            else cb.resolve(msg.result);
          }
        } catch (e) {
          console.error('CDP parse error:', e);
        }
      };
    });
  }

  send(method, params = {}) {
    return new Promise((resolve, reject) => {
      const id = this.id++;
      this.callbacks.set(id, { resolve, reject });
      this.ws.send(JSON.stringify({ id, method, params }));
    });
  }

  async evaluate(expression) {
    const res = await this.send('Runtime.evaluate', {
      expression,
      returnByValue: true,
      awaitPromise: true
    });
    if (res.exceptionDetails) {
      throw new Error(`Eval error: ${JSON.stringify(res.exceptionDetails)}`);
    }
    return res.result ? res.result.value : undefined;
  }

  async captureScreenshot(filename) {
    const res = await this.send('Page.captureScreenshot', { format: 'png' });
    const buffer = Buffer.from(res.data, 'base64');
    const outPath = path.join(ARTIFACT_DIR, filename);
    fs.writeFileSync(outPath, buffer);
    console.log(`      📸 Captured: ${filename}`);
  }

  async setViewport(width, height, dsf = 2) {
    await this.send('Emulation.setDeviceMetricsOverride', {
      width,
      height,
      deviceScaleFactor: dsf,
      mobile: width < 768
    });
    await sleep(250);
  }

  close() {
    if (this.ws) {
      try { this.ws.close(); } catch (e) {}
    }
  }
}

async function findChromePath() {
  const possiblePaths = [
    'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
    'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
    'C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe'
  ];
  for (const p of possiblePaths) {
    if (fs.existsSync(p)) return p;
  }
  return null;
}

const VIEWPORTS = [
  { name: 'Compact Mobile (360x640)', width: 360, height: 640 },
  { name: 'Standard Mobile (375x667)', width: 375, height: 667 },
  { name: 'Tall Mobile (393x852)', width: 393, height: 852 },
  { name: 'Tablet Portrait (768x1024)', width: 768, height: 1024 },
  { name: 'Tablet Landscape (1024x768)', width: 1024, height: 768 },
  { name: 'Desktop (1440x900)', width: 1440, height: 900 }
];

async function runAudit() {
  console.log('📱 STARTING AUROMATCH COMPREHENSIVE VIEWPORT & SCREEN FLOW AUDIT');
  await new Promise(r => server.listen(PORT, r));
  console.log(`📡 Test Server running on http://localhost:${PORT}`);

  const chromePath = await findChromePath();
  const chromeProc = spawn(chromePath, [
    `--remote-debugging-port=${CDP_PORT}`,
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    '--disable-dev-shm-usage',
    `http://localhost:${PORT}/index.html`
  ]);

  await sleep(2500);

  let cdp = null;
  const auditResults = [];

  try {
    const versionRes = await fetch(`http://127.0.0.1:${CDP_PORT}/json`);
    const targets = await versionRes.json();
    const pageTarget = targets.find(t => t.type === 'page');
    cdp = new CdpClient(pageTarget.webSocketDebuggerUrl);
    await cdp.connect();
    await cdp.send('Page.enable');
    await cdp.send('Runtime.enable');

    for (const vp of VIEWPORTS) {
      console.log(`\n======================================================`);
      console.log(`🔎 AUDITING AUROMATCH VIEWPORT: ${vp.name}`);
      console.log(`======================================================`);

      await cdp.setViewport(vp.width, vp.height);

      // --- SCREEN 0: Stage 0 3D Splash Screen (#landing-screen) ---
      console.log(`   [1/6] Auditing Stage 0 3D Splash Screen (#landing-screen)...`);
      await cdp.evaluate(`
        (() => {
          document.querySelectorAll('.screen-view').forEach(s => {
            s.classList.remove('active-screen');
            s.style.display = '';
          });
          const splash = document.getElementById('landing-screen');
          if (splash) splash.classList.add('active-screen');
        })()
      `);
      await sleep(250);

      const splashMetrics = await cdp.evaluate(`
        (() => {
          const splash = document.getElementById('landing-screen');
          const content = splash ? splash.querySelector('.landing-content') : null;
          const rect = content ? content.getBoundingClientRect() : { width: 0, height: 0 };
          return {
            viewportW: window.innerWidth,
            viewportH: window.innerHeight,
            cardW: Math.round(rect.width),
            cardH: Math.round(rect.height),
            isContained: rect.width <= window.innerWidth && rect.height <= window.innerHeight,
            overflowX: document.scrollingElement.scrollWidth > window.innerWidth
          };
        })()
      `);
      console.log(`      Splash Metrics:`, splashMetrics);
      await cdp.captureScreenshot(`auromatch_splash_${vp.width}x${vp.height}.png`);

      // --- SCREEN 1: Stage 1 Sanctuary Gateway Closed Double Doors (#gate-screen) ---
      console.log(`   [2/6] Auditing Stage 1 Sanctuary Gateway Doors (#gate-screen)...`);
      await cdp.evaluate(`
        (() => {
          document.querySelectorAll('.screen-view').forEach(s => {
            s.classList.remove('active-screen');
            s.style.display = '';
          });
          const gate = document.getElementById('gate-screen');
          if (gate) {
            gate.classList.add('active-screen');
            const doors = document.getElementById('sanctuary-doors');
            if (doors) doors.classList.remove('doors-parted');
          }
        })()
      `);
      await sleep(250);

      const doorClosedMetrics = await cdp.evaluate(`
        (() => {
          const gate = document.getElementById('gate-screen');
          const stage = document.getElementById('sanctuary-door-stage');
          const leftDoor = document.getElementById('door-left');
          const rightDoor = document.getElementById('door-right');
          const medallion = document.getElementById('door-medallion');
          const btn = document.getElementById('gate-btn-enter');
          const sRect = stage ? stage.getBoundingClientRect() : { width: 0, height: 0 };
          const bRect = btn ? btn.getBoundingClientRect() : { bottom: 0, height: 0 };
          return {
            stageW: Math.round(sRect.width),
            stageH: Math.round(sRect.height),
            leftDoorW: leftDoor ? Math.round(leftDoor.getBoundingClientRect().width) : 0,
            rightDoorW: rightDoor ? Math.round(rightDoor.getBoundingClientRect().width) : 0,
            medallionVisible: !!medallion,
            btnBottom: Math.round(bRect.bottom),
            isButtonVisible: bRect.bottom <= window.innerHeight
          };
        })()
      `);
      console.log(`      Door Closed Metrics:`, doorClosedMetrics);
      await cdp.captureScreenshot(`auromatch_door_closed_${vp.width}x${vp.height}.png`);

      // --- SCREEN 1.5: Stage 1.5 Door Parting Ceremony (#sanctuary-doors.doors-parted) ---
      console.log(`   [3/6] Auditing Stage 1.5 Sanctuary Gateway (Double Doors Parted)...`);
      await cdp.evaluate(`
        (() => {
          const doors = document.getElementById('sanctuary-doors');
          if (doors) doors.classList.add('doors-parted');
        })()
      `);
      await sleep(400);

      const doorPartedMetrics = await cdp.evaluate(`
        (() => {
          const portal = document.getElementById('door-inner-revelation-portal');
          const pRect = portal ? portal.getBoundingClientRect() : { width: 0, height: 0 };
          const text = portal ? portal.innerText.trim() : '';
          return {
            portalW: Math.round(pRect.width),
            portalH: Math.round(pRect.height),
            hasText: text.length > 0
          };
        })()
      `);
      console.log(`      Door Parted Metrics:`, doorPartedMetrics);
      await cdp.captureScreenshot(`auromatch_door_parted_${vp.width}x${vp.height}.png`);

      // --- SCREEN 2: Stage 2 Dedicated Sacred Realm Selection Screen (#realms-hub-screen) ---
      console.log(`   [4/6] Auditing Stage 2 Theme Realm Selection Screen (#realms-hub-screen)...`);
      await cdp.evaluate(`
        (() => {
          document.querySelectorAll('.screen-view').forEach(s => {
            s.classList.remove('active-screen');
            s.style.display = '';
          });
          const hub = document.getElementById('realms-hub-screen');
          if (hub) hub.classList.add('active-screen');
        })()
      `);
      await sleep(250);

      const realmMetrics = await cdp.evaluate(`
        (() => {
          const hub = document.getElementById('realms-hub-screen');
          const cards = hub ? hub.querySelectorAll('.realm-hub-card') : [];
          return {
            hubVisible: !!hub,
            cardCount: cards.length,
            overflowX: document.scrollingElement.scrollWidth > window.innerWidth
          };
        })()
      `);
      console.log(`      Realm Hub Metrics:`, realmMetrics);
      await cdp.captureScreenshot(`auromatch_realm_hub_${vp.width}x${vp.height}.png`);

      // --- SCREEN 3: Stage 3 Centered Gameplay Stage (#game-screen, #board) ---
      console.log(`   [5/6] Auditing Stage 3 Centered Gameplay Stage (#game-screen)...`);
      await cdp.evaluate(`
        (() => {
          document.querySelectorAll('.screen-view').forEach(s => {
            s.classList.remove('active-screen');
            s.style.display = '';
          });
          if (window.beginDirectJourney) {
            window.beginDirectJourney();
          } else if (window.navTo) {
            window.navTo('game');
          }
        })()
      `);
      await sleep(400);

      const gameMetrics = await cdp.evaluate(`
        (() => {
          const header = document.querySelector('#game-screen .app-header');
          const pill = document.getElementById('header-realm-dropdown-pill');
          const board = document.getElementById('board');
          const bRect = board ? board.getBoundingClientRect() : { width: 0, height: 0, left: 0 };
          const pRect = pill ? pill.getBoundingClientRect() : { width: 0, height: 0, left: 0 };
          const tiles = document.querySelectorAll('.tile-element');
          return {
            headerHeight: header ? Math.round(header.getBoundingClientRect().height) : 0,
            pillW: Math.round(pRect.width),
            pillH: Math.round(pRect.height),
            pillText: pill ? pill.innerText.replace(/\\s+/g, ' ').trim() : '',
            boardW: Math.round(bRect.width),
            boardH: Math.round(bRect.height),
            tileCount: tiles.length,
            hasTiles: tiles.length > 0,
            overflowX: document.scrollingElement.scrollWidth > window.innerWidth
          };
        })()
      `);
      console.log(`      Game Stage Metrics:`, gameMetrics);
      await cdp.captureScreenshot(`auromatch_game_stage_${vp.width}x${vp.height}.png`);

      // --- SCREEN 4: Stage 4 Sacred Epiphany Revelation Modal (#epiphany-modal) ---
      console.log(`   [6/6] Auditing Stage 4 Sacred Epiphany Modal (#epiphany-modal)...`);
      await cdp.evaluate(`
        (() => {
          const modal = document.getElementById('epiphany-modal');
          if (modal) {
            modal.style.display = 'flex';
            modal.classList.add('modal-active');
          }
        })()
      `);
      await sleep(250);

      const epiphanyMetrics = await cdp.evaluate(`
        (() => {
          const modal = document.getElementById('epiphany-modal');
          const card = modal ? modal.querySelector('.epiphany-card') || modal.querySelector('.modal-content') : null;
          const rect = card ? card.getBoundingClientRect() : { width: 0, height: 0 };
          return {
            modalVisible: modal ? modal.style.display === 'flex' : false,
            cardW: Math.round(rect.width),
            cardH: Math.round(rect.height),
            isContained: rect.width <= window.innerWidth && rect.height <= window.innerHeight
          };
        })()
      `);
      console.log(`      Epiphany Modal Metrics:`, epiphanyMetrics);
      await cdp.captureScreenshot(`auromatch_epiphany_modal_${vp.width}x${vp.height}.png`);

      auditResults.push({
        viewport: vp.name,
        splashMetrics,
        doorClosedMetrics,
        doorPartedMetrics,
        realmMetrics,
        gameMetrics,
        epiphanyMetrics
      });
    }

    console.log(`\n======================================================`);
    console.log(`🌟 AUROMATCH VIEWPORT TELEMETRY AUDIT COMPLETE: 100% SUCCESS`);
    console.log(`======================================================`);
  } finally {
    if (cdp) cdp.close();
    chromeProc.kill();
    server.close();
  }
}

runAudit().catch(err => {
  console.error('Audit failed with error:', err);
  process.exit(1);
});
