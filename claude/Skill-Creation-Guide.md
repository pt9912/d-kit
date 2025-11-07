# Anleitung: .skill Dateien erstellen

## Was ist eine .skill Datei?

Eine `.skill` Datei ist ein ZIP-Archiv mit spezieller Struktur, das von Claude importiert werden kann.

## Methoden zum Erstellen

### Methode 1: Mit package_skill.sh (Empfohlen) ⭐

Das d-kit Repository enthält ein fertiges Script:

```bash
cd d-kit

# Gemeinsame Templates/Prompts/Scripts in den Build kopieren
./tools/sync_skill_assets.sh

# Skill validieren und packen
./claude/tools/package_skill.sh
```

**Ausgabe:**
```
📦 Packaging d-kit skill...
   Version: 1.1.0
   Skill directory: /home/claude/d-kit/claude/skill
   Output directory: /home/claude/d-kit/claude/releases

🔍 Validating skill structure...
✅ Skill structure is valid

📦 Creating package: d-kit-v1.1.0.skill
✅ Successfully packaged skill to: claude/releases/d-kit-v1.1.0.skill
   File size: 45K

✅ Created symlink: d-kit-latest.skill

🎉 Packaging complete!
```

**Was das Script macht:**
1. Liest Version aus `claude/CHANGELOG.md`
2. Validiert Skill-Struktur (SKILL.md vorhanden, etc.)
3. Erstellt ZIP vom `skill/` Ordner
4. Benennt es als `d-kit-vX.X.X.skill`
5. Erstellt Symlink `d-kit-latest.skill`

> Hinweis: Falls noch keine `claude/CHANGELOG.md` existiert, legen Sie eine minimale Datei mit dem aktuellen Release-Eintrag an, da das Script sonst ohne Versionsnummer abbricht.

### Methode 2: Mit Anthropic's offiziellem Tool

Wenn Sie Zugriff auf das offizielle Anthropic Tool haben:

```bash
# Download von Anthropic's skill-creator
# (Pfad kann variieren)
python /path/to/anthropic/package_skill.py d-kit/claude/skill/

# Alternativ: Mit dem im Repository inkludierten Tool
python /mnt/skills/public/skill-creator/scripts/package_skill.py d-kit/claude/skill/
```

### Methode 3: Manuell mit ZIP

Falls Sie es komplett manuell machen möchten:

```bash
cd d-kit

# ZIP erstellen
cd claude
zip -r ../d-kit-v1.1.0.skill skill/ \
    -x "*.pyc" \
    -x "*__pycache__*" \
    -x "*.DS_Store"

# In claude/releases/ verschieben
mkdir -p releases
mv ../d-kit-v1.1.0.skill releases/
```

**Wichtig:** Die Verzeichnisstruktur im ZIP muss so aussehen:
```
d-kit-v1.1.0.skill (ZIP-Archiv)
└── skill/                      ← Root im ZIP
    ├── SKILL.md               ← Pflicht
    ├── scripts/
    │   ├── code_analysis.py
    │   └── run_tests.py
    ├── references/
    │   ├── prompts/
    │   ├── templates/
    │   ├── checklists/
    │   └── learnings.md
    └── assets/
```

**Nicht so:**
```
d-kit-v1.1.0.skill
└── d-kit/              ← FALSCH!
    └── skill/
        └── SKILL.md
```

## Skill-Struktur Validieren

Vor dem Packen validieren:

```bash
cd d-kit

# Validierungs-Script ausführen
./claude/tools/validate_skill.sh
```

**Ausgabe bei Erfolg:**
```
🔍 Validating d-kit skill...

Checking SKILL.md...
✅ SKILL.md found
✅ YAML frontmatter present
✅ SKILL.md has sufficient content (273 lines)

Checking scripts...
✅ scripts/ directory exists
✅ Found 2 Python script(s)

Checking references...
✅ references/ directory exists
✅ Found 10 prompt template(s)
✅ Found 2 document template(s)
✅ Found 2 checklist(s)

════════════════════════════════════════
Validation Summary
════════════════════════════════════════
✅ All checks passed!
```

## Häufige Fehler

### ❌ Fehler 1: Falsche Verzeichnisstruktur

**Problem:** ZIP enthält falschen Root-Ordner

```bash
# FALSCH
zip -r d-kit.skill d-kit/skill/
# Ergibt: d-kit.skill/d-kit/skill/SKILL.md

# RICHTIG
cd d-kit
zip -r d-kit.skill skill/
# Ergibt: d-kit.skill/skill/SKILL.md
```

### ❌ Fehler 2: SKILL.md fehlt

**Problem:** Keine SKILL.md im skill/ Ordner

**Lösung:** Jeder Skill MUSS eine SKILL.md haben:
```markdown
---
name: skill-name
description: What the skill does and when to use it
---

# Skill Content
...
```

### ❌ Fehler 3: Ungültige YAML Frontmatter

**Problem:** Frontmatter fehlt oder fehlerhaft

**Lösung:**
```markdown
---
name: d-kit                    # Pflicht
description: Complete desc...   # Pflicht
---

# Skill Content starts here
```

### ❌ Fehler 4: Unnötige Dateien im ZIP

**Problem:** __pycache__, .pyc, .DS_Store im ZIP

**Lösung:** Diese excluden:
```bash
zip -r skill.skill skill/ \
    -x "*.pyc" \
    -x "*__pycache__*" \
    -x "*.DS_Store" \
    -x "*.git*"
```

## Version-Nummern

Folgen Sie Semantic Versioning (semver.org):

```
MAJOR.MINOR.PATCH

1.0.0 - Initial Release
1.1.0 - New Features (Progress-Tracking)
1.1.1 - Bugfix
2.0.0 - Breaking Changes
```

**Wo Version setzen:**

1. **CHANGELOG.md:**
```markdown
## [1.1.0] - 2025-11-06
### Added
- New feature
```

2. **Dateiname:**
```
d-kit-v1.1.0.skill
```

3. **Git Tag:**
```bash
git tag -a v1.1.0 -m "Release v1.1.0"
```

## Kompletter Release-Prozess

### Schritt 1: Code fertigstellen
```bash
# Alle Änderungen committen
git add .
git commit -m "feat: add progress tracking"
```

### Schritt 2: Version aktualisieren
```bash
# CHANGELOG.md editieren
# [Unreleased] → [1.1.0] - 2025-11-06
```

### Schritt 3: Validieren
```bash
./claude/tools/validate_skill.sh
```

### Schritt 4: Packen
```bash
./claude/tools/package_skill.sh
# Erstellt: claude/releases/d-kit-v1.1.0.skill
```

### Schritt 5: Testen
```bash
# Skill in Claude importieren
# Testen ob er funktioniert
```

### Schritt 6: Git Tag
```bash
git tag -a v1.1.0 -m "Release v1.1.0: Progress Tracking"
git push origin v1.1.0
```

### Schritt 7: GitHub Release
```bash
# Auf GitHub:
# 1. Neues Release erstellen
# 2. Tag: v1.1.0
# 3. Titel: "d-kit v1.1.0 - Progress Tracking"
# 4. Beschreibung: CHANGELOG-Eintrag kopieren
# 5. Datei anhängen: claude/releases/d-kit-v1.1.0.skill
```

## Testing der .skill Datei

### Vor dem Release:

1. **Struktur prüfen:**
```bash
# ZIP-Inhalt anschauen
unzip -l claude/releases/d-kit-v1.1.0.skill | head -20
```

2. **Extrahieren und testen:**
```bash
# Temporäres Verzeichnis
mkdir -p /tmp/skill-test
unzip claude/releases/d-kit-v1.1.0.skill -d /tmp/skill-test

# SKILL.md vorhanden?
cat /tmp/skill-test/skill/SKILL.md | head -10
```

3. **In Claude importieren:**
   - Claude öffnen
   - Settings → Skills → Import Skill
   - `d-kit-v1.1.0.skill` auswählen
   - Testen: "Ich möchte Software entwickeln"

### Während des Tests:

**Checklist:**
- [ ] Skill wird in Skills-Liste angezeigt
- [ ] Name und Description korrekt
- [ ] Skill triggert bei passenden Anfragen
- [ ] Templates werden korrekt geladen
- [ ] Scripts sind ausführbar
- [ ] Keine Fehler in Console

## Troubleshooting

### Problem: "Invalid skill file"

**Ursache:** Falsche ZIP-Struktur

**Lösung:**
```bash
# Entpacken und prüfen
unzip -l skill.skill

# Sollte zeigen:
# skill/SKILL.md
# skill/scripts/...
# NICHT: d-kit/skill/SKILL.md
```

### Problem: "SKILL.md not found"

**Ursache:** SKILL.md im falschen Ordner

**Lösung:**
```bash
# Korrekt:
skill/SKILL.md

# Nicht:
SKILL.md (im Root)
d-kit/skill/SKILL.md
```

### Problem: "Invalid YAML frontmatter"

**Ursache:** Frontmatter fehlt oder fehlerhaft

**Lösung:**
```markdown
---
name: d-kit
description: Complete description here
---

Content...
```

## Tools im d-kit Repository

### validate_skill.sh
```bash
./claude/tools/validate_skill.sh
```
- Prüft Struktur
- Prüft SKILL.md
- Prüft Frontmatter
- Zählt Scripts/Templates

### package_skill.sh
```bash
./claude/tools/package_skill.sh [output-dir]
```
- Validiert automatisch
- Erstellt versioniertes ZIP
- Erstellt latest-Symlink

## Zusammenfassung

**Schnellster Weg:**
```bash
cd d-kit
./claude/tools/package_skill.sh
# Fertig! → claude/releases/d-kit-v1.1.0.skill
```

**Manueller Weg:**
```bash
cd d-kit/claude
zip -r ../d-kit-v1.1.0.skill skill/ -x "*.pyc"
mkdir -p releases
mv ../d-kit-v1.1.0.skill releases/
```

**Mit Validation:**
```bash
cd d-kit
./claude/tools/validate_skill.sh && ./claude/tools/package_skill.sh
```

---

**Ihre aktuelle Situation:**

✅ `d-kit-v1.1.0.skill` - Aktuelles Release (Shared Assets + Multi-Provider Support)
✅ `d-kit-v1.0.0.skill` - Initial Release (Legacy, nur bei Bedarf verwenden)

Beide verfügbar in: `claude/releases/` oder `/mnt/user-data/outputs/`
