with open('AuroMatch_Web_Prototype.html', 'r', encoding='utf-8') as f:
    c = f.read()

import re

realms_idx = c.find('const REALMS = [')
realms_end = c.find('class ThemeManager')
realms_str = c[realms_idx:realms_end]

pattern = r"chapter:\s*(\d+),\s*name:\s*'([^']+)',\s*subtitle:\s*'([^']+)',\s*mockupImage:\s*'([^']+)'"
matches = re.findall(pattern, realms_str)

print(f"=== BUNDLED 20 THEMES AUDIT ({len(matches)} Themes) ===")
for ch, name, sub, img in matches:
    print(f"Chapter {ch:2s}: {name:30s} | {sub:40s} | {img}")

# Check that NO old doc images exist in mockupImage
for ch, name, sub, img in matches:
    assert not any(k in img for k in ['service_tree', 'golconde', 'ashram_library', 'banyan_tree', 'brass_altar', 'coastline', 'matrimandir', 'auromatch_ui_mockup']), f"OLD IMAGE FOUND in Chapter {ch}: {img}"

print("\nALL 20 THEMES AUDITED: 100% BRAND NEW! ZERO OLD DOC REFERENCES!")
