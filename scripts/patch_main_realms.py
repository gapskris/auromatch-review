import re

with open('src/main.js', 'r', encoding='utf-8') as f:
    text = f.read()

old_block = text[text.find('    window.openRealmsBrowser = () => {'):text.find('    window.openLevelJumpModal = () => {')]

new_block = """    window.openRealmsBrowser = () => {
        const modal = document.getElementById('realms-browser-modal');
        const container = document.getElementById('realms-grid-container');
        if (!modal || !container) return;

        const realms = ThemeManager.getAllRealms();
        const currentLvl = activeGameManager.player.currentLevel || 1;
        const highestUnlocked = activeGameManager.player.highestUnlockedRealm || Math.max(1, Math.floor((currentLvl - 1) / 50) + 1);

        container.innerHTML = realms.map(r => {
            const isUnlocked = (r.chapter === 1) || (r.chapter <= highestUnlocked);
            const progress = ThemeManager.getRealmProgress(r.id, currentLvl);
            const isActive = isUnlocked && (currentLvl >= r.levelStart && currentLvl <= r.levelEnd);
            const currentLevelInThisRealm = isActive ? (((currentLvl - 1) % 50) + 1) : (isUnlocked ? 1 : 1);
            const currentLevelName = (r.levelNames && r.levelNames[currentLevelInThisRealm - 1]) ? r.levelNames[currentLevelInThisRealm - 1] : `Level ${currentLevelInThisRealm}`;

            if (!isUnlocked) {
                return `
                    <div class="realm-card-item locked" style="display: flex; flex-direction: column; position: relative;">
                        <div class="realm-card-lock-badge">🔒 Ch ${r.chapter} Locked</div>
                        <div class="realm-card-thumb" style="width: 100%; height: 96px; border-radius: 8px; margin-bottom: 8px; background: url('${r.mockupImage || r.bgImage}') center/cover no-repeat; border: 1px solid rgba(255,255,255,0.15);"></div>
                        <div class="realm-card-chapter" style="font-size: 11px; font-weight: 700; color: #94a3b8; text-transform: uppercase;">Chapter ${r.chapter}</div>
                        <div class="realm-card-title" style="font-size: 13px; font-weight: 700; line-height: 1.25; margin: 4px 0 2px 0; color: #cbd5e1;">${r.name}</div>
                        <div class="realm-card-subtitle" style="font-size: 11px; opacity: 0.7; color: #94a3b8; margin-bottom: 6px;">${r.subtitle}</div>
                        <div class="realm-card-levels" style="margin-bottom: 10px; font-size: 11px; color: #f59e0b; font-weight: 600;">🔒 Clear Ch ${r.chapter - 1} (Lvl ${(r.chapter - 1) * 50}) to Unlock</div>
                        <button class="c-btn" disabled style="padding: 6px 8px; font-size: 11px; width: 100%; background: rgba(255,255,255,0.08); color: #64748b; font-weight: 700; border-radius: 8px; margin-top: auto; cursor: not-allowed; border: 1px solid rgba(255,255,255,0.1);">
                            🔒 Locked
                        </button>
                    </div>
                `;
            }

            return `
                <div class="realm-card-item ${isActive ? 'active' : ''}" style="display: flex; flex-direction: column;">
                    <div class="realm-card-thumb" style="width: 100%; height: 96px; border-radius: 8px; margin-bottom: 8px; background: url('${r.mockupImage || r.bgImage}') center/cover no-repeat; border: 1px solid rgba(255,215,0,0.35); box-shadow: 0 4px 12px rgba(0,0,0,0.45);"></div>
                    <div class="realm-card-chapter" style="font-size: 11px; font-weight: 700; color: #f59e0b; text-transform: uppercase; letter-spacing: 0.5px;">Chapter ${r.chapter} · ${progress.isCompleted ? '✅ Complete' : `${progress.completedLevels}/50 Cleared`}</div>
                    <div class="realm-card-title" style="font-size: 13px; font-weight: 700; line-height: 1.25; margin: 4px 0 2px 0;">${r.name}</div>
                    <div class="realm-card-subtitle" style="font-size: 11px; opacity: 0.85; color: #c5a880; margin-bottom: 4px;">${r.subtitle}</div>
                    <div class="realm-progress-bar-bg">
                        <div class="realm-progress-bar-fill" style="width: ${progress.percent}%;"></div>
                    </div>
                    <div class="realm-card-levels" style="margin-bottom: 10px; font-size: 11px; color: #ffd700; font-weight: 600;">Lvl ${currentLevelInThisRealm}: ${currentLevelName}</div>
                    <button class="c-btn" onclick="window.selectRealm('${r.id}', ${isActive ? currentLvl : r.levelStart})" style="padding: 6px 8px; font-size: 11px; width: 100%; background: linear-gradient(135deg, #f59e0b, #d97706); color: #fff; font-weight: 700; border-radius: 8px; margin-top: auto;">
                        ▶ Enter Sanctuary
                    </button>
                </div>
            `;
        }).join('');

        modal.classList.add('active');
    };

    window.closeRealmsBrowser = () => {
        const modal = document.getElementById('realms-browser-modal');
        if (modal) modal.classList.remove('active');
    };

    window.selectRealm = (realmId, startLevel) => {
        const currentLvl = activeGameManager.player.currentLevel || 1;
        const highestUnlocked = activeGameManager.player.highestUnlockedRealm || Math.max(1, Math.floor((currentLvl - 1) / 50) + 1);
        const realm = REALMS.find(r => r.id === realmId);
        if (realm && realm.chapter > highestUnlocked) {
            window.showToastMessage(`🔒 Chapter ${realm.chapter} is locked! Complete Chapter ${realm.chapter - 1} first.`);
            return;
        }
        window.closeRealmsBrowser();
        activeGameManager.loadLevel(startLevel);
        window.showToastMessage(`🗺️ Entered Chapter ${realm ? realm.chapter : ''}: Level ${startLevel}`);
    };

"""

assert len(old_block) > 0, "Could not find old_block in src/main.js"
text = text.replace(old_block, new_block, 1)

with open('src/main.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("src/main.js updated successfully with sequential lock UI!")
