with open('src/controllers/gameManager.js', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('diff: Chapter  (50 Levels)', "diff: 'Chapter ' + r.chapter + ' (50 Levels)'")

with open('src/controllers/gameManager.js', 'w', encoding='utf-8') as f:
    f.write(text)

print('Cleaned line 1014!')
