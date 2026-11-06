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

def deploy_all(commit_msg=None):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    public_dir = os.path.join(os.path.dirname(base_dir), "auromatch-play")

    if not commit_msg:
        commit_msg = "chore: automated sync and live deployment"

    print("==================================================")
    print("[PIPELINE] AUROMATCH FULL DUAL-REPO DEPLOYMENT")
    print("==================================================")

    # 1. Run Tests
    print("\n[Step 1/5] Running automated QA test suite...")
    run_cmd("node --test tests/*.test.js", cwd=base_dir, error_msg="QA tests failed! Aborting deployment.")

    # 2. Build Standalone Prototype
    print("\n[Step 2/5] Compiling lightweight web bundle...")
    run_cmd(f"python \"{os.path.join(base_dir, 'scripts', 'build_prototype.py')}\"", cwd=base_dir, error_msg="Build failed!")

    # 3. Commit & Push Private Repository
    print("\n[Step 3/5] Syncing Private Repository (gapskris/AuroMatch)...")
    run_cmd("git add .", cwd=base_dir)
    status_out = subprocess.run("git status --porcelain", cwd=base_dir, shell=True, capture_output=True, text=True, encoding="utf-8", errors="replace").stdout.strip()
    if status_out:
        run_cmd(f'git commit -m "{commit_msg}"', cwd=base_dir)
    else:
        print("No new changes in private repo to commit.")
    run_cmd("git push origin main", cwd=base_dir, error_msg="Failed to push private repo!")

    # 4. Copy Modular Web Application, Assets and Metadata to Public Repository
    print("\n[Step 4/5] Synchronizing modern modular application and assets to Public Repository...")
    
    # Modular entrypoint
    src_index = os.path.join(base_dir, "index.html")
    dest_index = os.path.join(public_dir, "index.html")
    if os.path.exists(src_index):
        shutil.copy2(src_index, dest_index)
        print(f"Synchronized modular index.html -> {dest_index}")

    # Modular source tree and styles
    for mod_dir in ["src", "styles"]:
        s_dir = os.path.join(base_dir, mod_dir)
        d_dir = os.path.join(public_dir, mod_dir)
        if os.path.exists(s_dir):
            shutil.copytree(s_dir, d_dir, dirs_exist_ok=True)
            print(f"Synchronized {mod_dir}/ directory -> public repository")

    # Standalone prototype bundle fallback
    src_proto = os.path.join(base_dir, "AuroMatch_Web_Prototype.html")
    dest_proto = os.path.join(public_dir, "AuroMatch_Web_Prototype.html")
    if os.path.exists(src_proto):
        shutil.copy2(src_proto, dest_proto)
        print(f"Copied standalone prototype -> {dest_proto}")

    # Copy manifest and icons
    src_manifest = os.path.join(base_dir, "manifest.json")
    if os.path.exists(src_manifest):
        shutil.copy2(src_manifest, os.path.join(public_dir, "manifest.json"))
        print("Copied manifest.json -> public repository")

    src_sw = os.path.join(base_dir, "sw.js")
    if os.path.exists(src_sw):
        shutil.copy2(src_sw, os.path.join(public_dir, "sw.js"))
        print("Copied sw.js -> public repository")

    src_favicon = os.path.join(base_dir, "favicon.ico")
    if os.path.exists(src_favicon):
        shutil.copy2(src_favicon, os.path.join(public_dir, "favicon.ico"))
        print("Copied favicon.ico -> public repository")

    src_assets = os.path.join(base_dir, "Assets")
    dest_assets = os.path.join(public_dir, "Assets")
    if os.path.exists(src_assets):
        shutil.copytree(src_assets, dest_assets, dirs_exist_ok=True)
        print("Synchronized Assets/ directory -> public repository")

    # 5. Commit & Push Public Repository
    print("\n[Step 5/5] Syncing Public Repository (gapskris/auromatch-play)...")
    run_cmd("git add .", cwd=public_dir)
    status_public = subprocess.run("git status --porcelain", cwd=public_dir, shell=True, capture_output=True, text=True, encoding="utf-8", errors="replace").stdout.strip()
    if status_public:
        run_cmd(f'git commit -m "{commit_msg}"', cwd=public_dir)
    else:
        print("No new changes in public repo to commit.")
    run_cmd("git push origin main", cwd=public_dir, error_msg="Failed to push public repo!")

    print("\n==================================================")
    print("[SUCCESS] DEPLOYMENT COMPLETE!")
    print("Private Repo: https://github.com/gapskris/AuroMatch")
    print("Public Repo:  https://github.com/gapskris/auromatch-play")
    print("Live Game:    https://gapskris.github.io/auromatch-play/")
    print("==================================================")

if __name__ == "__main__":
    msg = sys.argv[1] if len(sys.argv) > 1 else None
    deploy_all(msg)
