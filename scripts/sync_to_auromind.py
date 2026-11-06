import os
import sys
import subprocess
import shutil

# Ensure utf-8 output on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

def run_cmd(cmd, cwd=None, error_msg=None):
    print(f"--> Running: {cmd} (in {cwd or '.'})")
    result = subprocess.run(cmd, cwd=cwd, shell=True, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if result.returncode != 0:
        print(f"ERROR: {error_msg or 'Command failed'}")
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        sys.exit(1)
    if result.stdout.strip():
        print(result.stdout.strip())
    return result.stdout.strip()

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target_dir = os.path.join(os.path.dirname(base_dir), "AuroMind", "games", "auromatch")

    print("==================================================")
    print("  AUROMATCH ➔ AUROMIND HYBRID SUBPATH DEPLOYMENT ")
    print("==================================================")

    # 1. Run Automated Tests
    print("\n[Step 1/3] Running automated QA test suite...")
    run_cmd("node --test tests/*.test.js", cwd=base_dir, error_msg="QA tests failed! Aborting deployment.")

    # 2. Build Standalone Prototype Fallback
    print("\n[Step 2/3] Compiling standalone web prototype bundle...")
    proto_script = os.path.join(base_dir, "scripts", "build_prototype.py")
    if os.path.exists(proto_script):
        run_cmd(f'python "{proto_script}"', cwd=base_dir, error_msg="Prototype build failed!")

    # 3. Copy Modular Web Application & Assets to AuroMind/games/auromatch
    print(f"\n[Step 3/3] Synchronizing assets to {target_dir}...")
    if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)

    # Entrypoint index.html
    src_index = os.path.join(base_dir, "index.html")
    dest_index = os.path.join(target_dir, "index.html")
    if os.path.exists(src_index):
        shutil.copy2(src_index, dest_index)
        print(f"Copied index.html -> {dest_index}")

    # Modular source trees and styles
    for mod_dir in ["src", "styles"]:
        s_dir = os.path.join(base_dir, mod_dir)
        d_dir = os.path.join(target_dir, mod_dir)
        if os.path.exists(s_dir):
            shutil.copytree(s_dir, d_dir, dirs_exist_ok=True)
            print(f"Synchronized {mod_dir}/ directory -> {d_dir}")

    # Standalone prototype fallback
    src_proto = os.path.join(base_dir, "AuroMatch_Web_Prototype.html")
    dest_proto = os.path.join(target_dir, "AuroMatch_Web_Prototype.html")
    if os.path.exists(src_proto):
        shutil.copy2(src_proto, dest_proto)
        print(f"Copied standalone prototype -> {dest_proto}")

    # PWA assets & manifests
    for f in ["manifest.json", "sw.js", "favicon.ico"]:
        src_f = os.path.join(base_dir, f)
        if os.path.exists(src_f):
            shutil.copy2(src_f, os.path.join(target_dir, f))
            print(f"Copied {f} -> {target_dir}")

    # Assets folder (3D tiles, textures, audio)
    src_assets = os.path.join(base_dir, "Assets")
    dest_assets = os.path.join(target_dir, "Assets")
    if os.path.exists(src_assets):
        shutil.copytree(src_assets, dest_assets, dirs_exist_ok=True)
        print(f"Synchronized Assets/ directory -> {dest_assets}")

    print("\n==================================================")
    print("✅ AUROMATCH DEPLOYMENT TO AUROMIND COMPLETE!")
    print(f"Subpath Location: {target_dir}")
    print("==================================================")

if __name__ == "__main__":
    main()
