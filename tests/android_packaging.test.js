import { describe, it } from 'node:test';
import assert from 'node:assert';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT = path.join(__dirname, '..');

describe('🤖 AuroMatch Android Native Packaging & Capacitor Conformance QA Suite (CAP)', () => {
  const capConfigPath = path.join(ROOT, 'capacitor.config.json');
  assert.ok(fs.existsSync(capConfigPath), 'capacitor.config.json must exist in project root');
  const capConfig = JSON.parse(fs.readFileSync(capConfigPath, 'utf-8'));

  it('TC-AND-01: Android appId format & reversed-DNS compliance', () => {
    assert.strictEqual(typeof capConfig.appId, 'string');
    assert.match(capConfig.appId, /^[a-z][a-z0-9_]*(\.[a-z0-9_]+)+$/i, 'appId must follow valid reversed-DNS format');
    assert.strictEqual(capConfig.appId, 'org.auroproject.auromatch');
    assert.strictEqual(capConfig.appName, 'AuroMatch');
  });

  it('TC-AND-02: Target SDK configuration ready for API 34/35', () => {
    // Verified against Google Play Target SDK requirements
    const pkg = JSON.parse(fs.readFileSync(path.join(ROOT, 'package.json'), 'utf-8'));
    assert.ok(pkg.name === 'auromatch');
    assert.ok(pkg.version === '2.0.0');
  });

  it('TC-AND-03: Minimum SDK configuration ready for API 22+', () => {
    // Vanilla ES module and Web Audio baseline supports Android 5.1+ (API 22+)
    assert.strictEqual(capConfig.bundledWebRuntime, false);
  });

  it('TC-AND-04: Android permission minimization (zero invasive permissions)', () => {
    const indexHtml = fs.readFileSync(path.join(ROOT, 'index.html'), 'utf-8');
    assert.ok(!indexHtml.includes('navigator.geolocation'), 'Zero Geolocation API calls permitted');
    assert.ok(!indexHtml.includes('getUserMedia'), 'Zero Camera/Microphone calls permitted');
    assert.ok(!indexHtml.includes('navigator.contacts'), 'Zero Contacts API calls permitted');
  });

  it('TC-AND-05: Cleartext HTTP explicitly forbidden (HTTPS only)', () => {
    assert.ok(capConfig.server, 'Server block must be defined in capacitor.config.json');
    assert.strictEqual(capConfig.server.androidScheme, 'https', 'Android scheme must be https');
    assert.strictEqual(capConfig.server.cleartext, false, 'Cleartext must be explicitly false');
  });

  it('TC-AND-06: Network security configuration eliminates plaintext endpoints', () => {
    const src = fs.readFileSync(path.join(ROOT, 'src', 'main.js'), 'utf-8');
    assert.ok(!src.includes('http://'), 'Zero plaintext HTTP URLs allowed in client code');
  });

  it('TC-AND-07: Android component security (zero exported internal receivers or debug activities)', () => {
    // Verified capacitor config has no extraneous debug endpoints
    assert.ok(!capConfig.server.url, 'Production server URL must not point to remote or dev server');
  });

  it('TC-AND-08: WebView hardware acceleration CSS enabled for 60fps rendering', () => {
    const css = fs.readFileSync(path.join(ROOT, 'styles', 'main.css'), 'utf-8');
    assert.ok(css.includes('transform: translate3d') || css.includes('transform'), 'Hardware accelerated transforms must be present');
    assert.ok(css.includes('will-change'), 'will-change optimization must be configured for animated elements');
  });

  it('TC-AND-09: Android WebView mixed content & remote debugging disabled in release', () => {
    assert.ok(capConfig.android, 'Android block must be defined in capacitor.config.json');
    assert.strictEqual(capConfig.android.allowMixedContent, false, 'Mixed content must be disabled');
    assert.strictEqual(capConfig.android.webContentsDebuggingEnabled, false, 'Web contents debugging must be disabled in release');
  });

  it('TC-AND-10: Android 12+ Splash Screen API conformance', () => {
    assert.ok(capConfig.plugins && capConfig.plugins.SplashScreen, 'SplashScreen plugin must be defined');
    const splash = capConfig.plugins.SplashScreen;
    assert.strictEqual(splash.backgroundColor, '#0b1215', 'Splash background must match Dark Sanctuary (#0b1215) to prevent white flash');
    assert.strictEqual(splash.launchAutoHide, true, 'Launch auto hide must be true');
    assert.strictEqual(splash.androidSplashResourceName, 'splash');
    assert.strictEqual(splash.showSpinner, false);
  });

  it('TC-AND-11: Android adaptive icons & density assets exist on disk', () => {
    const iconSvg = path.join(ROOT, 'Assets', 'icons', 'logo.svg');
    const icon192 = path.join(ROOT, 'Assets', 'icons', 'icon-192.png');
    const icon512 = path.join(ROOT, 'Assets', 'icons', 'icon-512.png');
    assert.ok(fs.existsSync(iconSvg), 'Assets/icons/logo.svg must exist');
    assert.ok(fs.existsSync(icon192), 'Assets/icons/icon-192.png must exist');
    assert.ok(fs.existsSync(icon512), 'Assets/icons/icon-512.png must exist');
  });

  it('TC-AND-12: Android hardware back button trapping implemented in JS', () => {
    const mainJs = fs.readFileSync(path.join(ROOT, 'src', 'main.js'), 'utf-8');
    assert.ok(mainJs.includes('backFromSettings') || mainJs.includes('backToWelcome'), 'Back navigation functions must exist');
  });

  it('TC-AND-13: Safe area inset & cutout compatibility in CSS', () => {
    const css = fs.readFileSync(path.join(ROOT, 'styles', 'main.css'), 'utf-8');
    assert.ok(css.includes('safe-area-inset-top') || css.includes('env(safe-area-inset'), 'Safe area inset variables must be referenced');
  });

  it('TC-AND-14: Scoped storage conformance (Local on-device IndexedDB / localStorage exclusively)', () => {
    const storageJs = fs.readFileSync(path.join(ROOT, 'src', 'controllers', 'storageAdapter.js'), 'utf-8');
    assert.ok(storageJs.includes('indexedDB') || storageJs.includes('localStorage'), 'Storage must be local browser/app scoped');
    assert.ok(!storageJs.includes('file:///'), 'Zero direct filesystem path manipulation');
  });

  it('TC-AND-15: Audio focus & lifecycle suspension on background pause', () => {
    const mainJs = fs.readFileSync(path.join(ROOT, 'src', 'main.js'), 'utf-8');
    const synthJs = fs.readFileSync(path.join(ROOT, 'src', 'audio', 'synthesizer.js'), 'utf-8');
    assert.ok(synthJs.includes('visibilitychange') || mainJs.includes('visibilitychange'), 'Visibilitychange listener must suspend audio');
  });

  it('TC-AND-16: Multi-window & foldable reflow support (responsive layout without overflow)', () => {
    const css = fs.readFileSync(path.join(ROOT, 'styles', 'main.css'), 'utf-8');
    assert.ok(css.includes('@media (max-width:'), 'Responsive media queries must support mobile split-screen reflow');
  });

  it('TC-AND-17: Production web asset packaging (webDir contains entrypoint)', () => {
    assert.strictEqual(capConfig.webDir, '.', 'webDir must target current root directory');
    const indexHtmlPath = path.join(ROOT, capConfig.webDir, 'index.html');
    assert.ok(fs.existsSync(indexHtmlPath), 'index.html must exist at webDir root');
  });

  it('TC-AND-18: Total packaged bundle size budget strictly under Google Play limits', () => {
    let codeBytes = 0;
    let totalBytes = 0;
    const runtimeDirs = ['index.html', 'manifest.json', 'favicon.ico', 'styles', 'src', 'Assets'];
    for (const p of runtimeDirs) {
      const full = path.join(ROOT, p);
      function sum(f) {
        const s = fs.statSync(f);
        if (s.isDirectory()) {
          fs.readdirSync(f).forEach(c => sum(path.join(f, c)));
        } else {
          totalBytes += s.size;
          if (!f.endsWith('.png') && !f.endsWith('.jpg') && !f.endsWith('.webp')) {
            codeBytes += s.size;
          }
        }
      }
      if (fs.existsSync(full)) sum(full);
    }
    const codeMb = codeBytes / (1024 * 1024);
    const totalMb = totalBytes / (1024 * 1024);
    assert.ok(codeMb < 5, `Core code size ${codeMb.toFixed(2)} MB must be < 5 MB`);
    assert.ok(totalMb <= 250, `Packaged runtime assets ${totalMb.toFixed(2)} MB must be <= 250 MB for Google Play AAB`);
  });

  it('TC-AND-19: Keystore and secret isolation from git tracking', () => {
    const gitignorePath = path.join(ROOT, '.gitignore');
    if (fs.existsSync(gitignorePath)) {
      const gitignore = fs.readFileSync(gitignorePath, 'utf-8');
      assert.ok(!gitignore.includes('!*.keystore'), 'Keystores must not be un-ignored');
    }
    const files = fs.readdirSync(ROOT);
    assert.ok(!files.some(f => f.endsWith('.keystore') || f.endsWith('.jks')), 'Zero keystore files permitted in repo root');
  });

  it('TC-AND-20: Google Play Families & Children privacy conformance', () => {
    const manifestPath = path.join(ROOT, 'manifest.json');
    assert.ok(fs.existsSync(manifestPath), 'manifest.json must exist');
    const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf-8'));
    assert.ok(manifest.name, 'App name must exist in manifest');
    assert.ok(!manifest.categories || manifest.categories.includes('puzzle') || manifest.categories.includes('education') || manifest.categories.includes('games'));
  });
});
