import os
import re

def strip_esm(code):
    # 1. Remove multiline import statements: import ... from '...';
    code = re.sub(r'import\s+[^;\'"]*?from\s+[\'"][^\'"]+[\'"];?', '', code, flags=re.MULTILINE | re.DOTALL)
    # 2. Remove single bare imports: import 'style.css';
    code = re.sub(r'import\s+[\'"][^\'"]+[\'"];?', '', code)
    # 3. Remove multiline export { ... };
    code = re.sub(r'export\s+\{[^}]*?\};?', '', code, flags=re.MULTILINE | re.DOTALL)
    # 4. Remove export default
    code = re.sub(r'export\s+default\s+', '', code)
    # 5. Remove export async function
    code = re.sub(r'export\s+(async\s+function\b)', r'\1', code)
    # 6. Remove export function, class, const, let, var
    code = re.sub(r'export\s+(function\b|class\b|const\b|let\b|var\b)', r'\1', code)
    return code

def build_standalone_prototype():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Read CSS
    with open(os.path.join(base_dir, 'styles', 'main.css'), 'r', encoding='utf-8') as f:
        css_content = f.read()

    # Read modules
    modules = [
        ('src/models/floraDatabase.js', 'Flora Database'),
        ('src/controllers/storageAdapter.js', 'Storage Adapter'),
        ('src/audio/synthesizer.js', 'Audio Synthesizer'),
        ('src/models/boardGenerator.js', 'Board Generator'),
        ('src/controllers/inputDispatcher.js', 'Input Dispatcher'),
        ('src/ui/boardRenderer.js', 'Board Renderer'),
        ('src/controllers/settings.js', 'Settings'),
        ('src/ui/particles.js', 'Particles'),
        ('src/ui/scriptureCard.js', 'Scripture Card'),
        ('src/ui/constellation.js', 'Constellation Grid'),
        ('src/controllers/themeManager.js', 'Theme Manager'),
        ('src/controllers/gameManager.js', 'Game Manager'),
        ('src/main.js', 'Main Application Initialization')
    ]

    bundle_js = "\n\n// --- BUNDLED AUROMATCH CORE LOGIC ---\n"
    for mod_path, mod_name in modules:
        with open(os.path.join(base_dir, mod_path), 'r', encoding='utf-8') as f:
            code = f.read()
        bundle_js += f"\n// --- {mod_name} ---\n" + strip_esm(code)

    # Read base index.html
    with open(os.path.join(base_dir, 'index.html'), 'r', encoding='utf-8') as f:
        index_html = f.read()

    style_tag = f"<style>\n{css_content}\n</style>"
    index_html = index_html.replace('<link rel="stylesheet" href="./styles/main.css">', style_tag)

    script_tag = f"<script>\n{bundle_js}\n</script>"
    index_html = index_html.replace('<script type="module" src="./src/main.js"></script>', script_tag)

    out_path = os.path.join(base_dir, 'AuroMatch_Web_Prototype.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(index_html)

    # Validate JavaScript bundle syntax with node --check
    import subprocess
    temp_check_path = os.path.join(base_dir, 'test_bundle.js')
    with open(temp_check_path, 'w', encoding='utf-8') as f:
        f.write(bundle_js)
    res = subprocess.run(['node', '--check', temp_check_path], capture_output=True, text=True)
    if os.path.exists(temp_check_path):
        os.remove(temp_check_path)
    if res.returncode != 0:
        print("SYNTAX ERROR in compiled bundle:")
        print(res.stderr)
        raise SystemExit(1)

    size_kb = os.path.getsize(out_path) / 1024
    print(f"AuroMatch_Web_Prototype.html successfully compiled: {size_kb:.2f} KB (Target < 600 KB)")
    print("Bundle syntax validation: PASSED (100% clean).")

if __name__ == '__main__':
    build_standalone_prototype()
