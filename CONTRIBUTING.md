# Contributing to d-kit

Vielen Dank für Ihr Interesse, zu d-kit beizutragen! 🎉

## 📋 Code of Conduct

Dieses Projekt verpflichtet sich zu einem offenen und einladenden Umfeld. Bitte lesen Sie unseren [Code of Conduct](CODE_OF_CONDUCT.md).

## 🤔 Wie kann ich beitragen?

### 🐛 Bug Reports

Bugs werden als [GitHub Issues](https://github.com/yourusername/d-kit/issues) getrackt.

**Bevor Sie einen Bug melden:**
- Prüfen Sie, ob der Bug bereits gemeldet wurde
- Stellen Sie sicher, dass Sie die neueste Version verwenden

**Guter Bug Report enthält:**
- Klare, beschreibende Überschrift
- Schritte zur Reproduktion
- Erwartetes vs. tatsächliches Verhalten
- Screenshots (falls relevant)
- Version von d-kit und Claude
- Relevante Prompt/Context (anonymisiert)

### 💡 Feature Requests

Feature-Wünsche sind ebenfalls willkommen!

**Guter Feature Request enthält:**
- Klare Beschreibung des Features
- Use Case: Warum ist es nützlich?
- Beispiele, wie es verwendet werden würde
- Optional: Implementierungsvorschläge

### 📝 Verbesserung der Dokumentation

Dokumentations-Verbesserungen sind immer willkommen:
- Tippfehler korrigieren
- Beispiele hinzufügen
- Unklare Passagen präzisieren
- Übersetzungen (zukünftig)

### 🔧 Code-Beiträge

#### Prompt-Templates

Neue oder verbesserte Prompt-Templates sind sehr wertvoll!

**Template-Anforderungen:**
- Klare Struktur (Kontext → Aufgabe → Struktur → Hinweise)
- Ausführliche Beispiele
- Best Practices
- Edge-Cases berücksichtigen
- Getestet mit echten Projekten

**Beispiel-Struktur:**
```markdown
# Prompt-Template: [Name]

## Kontext
[Wer ist die KI, was ist die Rolle]

## Aufgabe
[Was soll generiert werden]

## Struktur des Outputs
[Detaillierte Struktur mit Beispielen]

## Wichtige Hinweise
[Spezielle Anforderungen, Edge-Cases]
```

#### Scripts

Scripts für Automatisierung sind willkommen:

**Script-Anforderungen:**
- Python 3.8+ kompatibel
- Docstrings für alle Funktionen
- Error-Handling
- Hilfetexte (`--help`)
- Tests (falls komplex)

#### Checklists

Neue Checklists oder Erweiterungen bestehender:

**Checklist-Anforderungen:**
- Klar strukturiert
- Priorisiert (Must-Have vs. Nice-to-Have)
- Actionable (konkrete Aktionen)
- Messbar (wo möglich)

## 🔄 Pull Request Prozess

### 1. Fork & Clone

```bash
# Fork das Repo auf GitHub
# Dann:
git clone https://github.com/your-username/d-kit.git
cd d-kit
git remote add upstream https://github.com/pt9912/d-kit.git
```

### 2. Branch erstellen

```bash
# Feature Branch
git checkout -b feature/your-feature-name

# Bugfix Branch
git checkout -b fix/issue-number-description

# Docs Branch
git checkout -b docs/what-you-are-documenting
```

### 3. Änderungen machen

- Halten Sie Commits atomar (eine logische Änderung pro Commit)
- Schreiben Sie aussagekräftige Commit-Messages
- Folgen Sie der bestehenden Code-Struktur

**Commit-Message Format:**
```
<type>: <subject>

<body>

<footer>
```

**Types:**
- `feat`: Neues Feature
- `fix`: Bugfix
- `docs`: Dokumentation
- `style`: Formatierung
- `refactor`: Code-Refactoring
- `test`: Tests
- `chore`: Wartung

**Beispiel:**
```
feat: add bug-fix prompt template

Add comprehensive prompt template for systematic bug fixing including:
- Root cause analysis
- Test case generation
- Regression prevention

Closes #42
```

### 4. Testen

```bash
# Validiere Skill-Struktur (wenn Skill-Dateien geändert)
./claude/tools/validate_skill.sh

# Optional: Syntax der Scripts prüfen (Python 3 erforderlich)
python3 -m compileall claude/skill/scripts

# Optional: Eigene Tests/Smoke-Checks ausführen
# (z. B. python3 claude/skill/scripts/code_analysis.py --help)

# Skills synchron halten (gemeinsame Templates/Checklists)
./tools/sync_skill_assets.sh
```

### 5. Pull Request erstellen

**PR-Beschreibung sollte enthalten:**
- Was wurde geändert und warum
- Welches Issue wird addressiert (falls zutreffend)
- Screenshots/Beispiele (falls relevant)
- Breaking Changes (falls zutreffend)
- Checklist der durchgeführten Tests

**PR-Checklist:**
- [ ] Code folgt Projekt-Style
- [ ] Commit-Messages sind aussagekräftig
- [ ] Dokumentation wurde aktualisiert
- [ ] Tests wurden durchgeführt
- [ ] CHANGELOG.md wurde aktualisiert (für Features/Fixes)
- [ ] Keine Merge-Konflikte

### 6. Review-Prozess

- Maintainer werden Ihr PR reviewen
- Konstruktive Diskussion ist erwünscht
- Änderungen können requested werden
- Nach Approval wird gemerged

## 📁 Verzeichnis-Struktur

```
d-kit/
├── shared/skill-common/       # Einzige Quelle für Templates/Prompts/Skripte
├── claude/
│   ├── skill/                 # wird via sync_script befüllt (SKILL.md + assets)
│   └── tools/                 # Build- & Validierungs-Scripts
├── codex/                     # Codex Skill (Installer, Bootstrap)
├── gemini/                    # Gemini CLI Extension
├── grok/                      # Collections-Skripte/Prompts
├── docs/                      # Dokumentation (Getting Started, Grok, Examples …)
├── tools/                     # sync_skill_assets.sh etc.
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## 💡 Tipps für gute Beiträge

### Prompt-Templates

1. **Testen Sie ausführlich**: Verwenden Sie das Template in echten Projekten
2. **Dokumentieren Sie Learnings**: Was funktioniert gut? Was nicht?
3. **Seien Sie spezifisch**: Je detaillierter, desto besser die KI-Outputs
4. **Beispiele sind Gold**: Konkrete Beispiele helfen enorm

### Scripts

1. **Error-Handling**: Scripts sollten robust sein
2. **Dokumentation**: Code sollte selbsterklärend sein
3. **Portabilität**: Auf verschiedenen Systemen getestet
4. **Performance**: Effizient für große Projekte

### Dokumentation

1. **Klar und präzise**: Keine unnötigen Worte
2. **Beispiele**: Zeigen statt nur beschreiben
3. **Aktuell**: Mit Code synchronisiert halten
4. **Struktur**: Leicht scanbar und navigierbar

## 🎓 Learnings teilen

Haben Sie d-kit in einem Projekt verwendet?

**Teilen Sie Ihre Erfahrungen:**
- Was hat gut funktioniert?
- Welche Prompts waren besonders effektiv?
- Welche Probleme sind aufgetreten?
- Welche Verbesserungen würden Sie vorschlagen?

→ Öffnen Sie eine [Discussion](https://github.com/yourusername/d-kit/discussions) oder Issue!

## ❓ Fragen?

- 💬 [GitHub Discussions](https://github.com/yourusername/d-kit/discussions) für Fragen
- 🐛 [GitHub Issues](https://github.com/yourusername/d-kit/issues) für Bugs
- 📧 Email: contribute@d-kit.dev (placeholder)

## 🙏 Danke!

Jeder Beitrag, egal wie klein, wird geschätzt. Sie machen d-kit besser für alle! 🎉

---

**Happy Contributing! 🚀**
