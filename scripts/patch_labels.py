with open('src/main.js', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    '13 Thematic Realms: 195 Levels with Dedicated 3D Artistic Tiles & Environmental Backdrops!',
    '20 Grand Realms: 1,000 Levels (50 per Chapter) with Dedicated 3D Tile Sets & Environmental Sanctuaries!'
)

old_start = """    window.openRealmsBrowser = () => {
        const modal = document.getElementById('realms-browser-modal');
        const container = document.getElementById('realms-grid-container');
        if (!modal || !container) return;"""

new_start = """    window.openRealmsBrowser = () => {
        const modal = document.getElementById('realms-browser-modal');
        const container = document.getElementById('realms-grid-container');
        if (!modal || !container) return;

        const modalH3 = modal.querySelector('h3');
        if (modalH3) modalH3.innerText = '🗺️ The 20 Grand Realms (1,000 Levels)';
        const modalSub = modal.querySelector('p');
        if (modalSub) modalSub.innerText = '1,000 Levels (50 per Chapter) · 20 Dedicated 3D Tactile Tile Sets & Environmental Sanctuaries';"""

text = text.replace(old_start, new_start)

with open('src/main.js', 'w', encoding='utf-8') as f:
    f.write(text)

print('src/main.js patched cleanly!')
