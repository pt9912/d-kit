# d-kit - Development KI Templates

<div align="center">

**Strukturierte KI-gestützte Softwareentwicklung vom Lastenheft bis zum MVP**

[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg)](https://github.com/yourusername/d-kit/releases)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Claude](https://img.shields.io/badge/Claude-Sonnet%204.5+-orange.svg)](https://claude.ai)

[Features](#-features) • [Installation](#-installation) • [Quick Start](#-quick-start) • [Dokumentation](#-dokumentation) • [Contributing](#-contributing)

</div>

---

## 📋 Übersicht

**d-kit** (Development KI Templates) ist ein KI-gestütztes Development-Framework mit strukturiertem 7-Phasen-Prozess. Prompt-Templates, automatische Tests und Quality Gates führen von der Anforderung bis zum Release – systematisch und effizient. Von der Anforderungsanalyse über Design und Implementation bis hin zu Testing und Release – jeder Schritt ist strukturiert, dokumentiert und mit Best Practices versehen.

### Warum d-kit?

- ✅ **Strukturierter Prozess** - 7 klar definierte Phasen mit Validierungs-Checkpoints
- ✅ **Qualitätssicherung** - Integrierte Tests, Code-Analyse und Security-Scans
- ✅ **Zeitersparnis** - 50-60% schnellere Entwicklung bei höherer Qualität
- ✅ **Best Practices** - Clean Code, SOLID-Prinzipien, umfassendes Error-Handling
- ✅ **Kontinuierliche Verbesserung** - Learnings dokumentieren und Prozess optimieren
- ✅ **Prompt-Templates** - 12 ausgereifte Templates für konsistente Outputs

## ✨ Features

### 🎯 Strukturierter 7-Phasen-Prozess

1. **Anforderungsanalyse** - Lastenheft → Pflichtenheft → Architektur
2. **Planung** - MVP-Plan → Test-Strategie
3. **UI-Design** - Design-System → Wireframes → Mockups → Prototype (Figma)
4. **Sprint-Planung** - Sprint-Plan mit Tasks
5. **Iterative Entwicklung** - Design → Code → Tests (Unit-, Integration- und E2E-Tests pro Task)
6. **Sprint-Abschluss** - Review → Retrospektive → Learnings
7. **MVP-Abschluss** - E2E-Tests → UAT → Performance-Tests → Release

### 🛡️ Quality Gates

- **Code-Qualität**: Clean Code, SOLID, Error Handling
- **Test-Coverage**: >80% Ziel, automatisches Tracking
- **Security**: Input-Validierung, Security-Scans, Penetration Testing
- **Performance**: Response-Time-Monitoring, Load-Tests

### 📚 Umfassende Templates

**Prompt-Templates** (`claude/skill/references/prompts/`):
- `pflichtenheft.md` - Anforderungsspezifikation
- `architektur.md` - System-Architektur
- `mvp-plan.md` - MVP-Planung
- `sprint-plan.md` - Sprint-Planung
- `task-design.md` - Detailliertes Task-Design (>300 Zeilen)
- `design-review.md` - Systematisches Review-Framework
- `code-generation.md` - Clean-Code Best Practices
- `test-generation.md` - Testfälle und Coverage-Strategie
- `test-strategie.md` - Umfassende Test-Planung
- `progress-update.md` - Status- und Fortschrittsberichte
- `ui-design-figma.md` - Figma-basierter UI-Design-Flow
- `bug-fix.md` - Systematischer Bug-Fix-Workflow

**Dokument-Templates** (`claude/skill/references/templates/`):
- `lastenheft.md` - Strukturiertes Lastenheft mit Beispielen
- `retrospektive.md` - Sprint-Retrospektive

**Checklists** (`claude/skill/references/checklists/`):
- `sprint-review.md` - >80 Checkpunkte für Sprint-Review
- `e2e-tests.md` - E2E-Test Validierung

### 🤖 Automatisierung

**Scripts** (`claude/skill/scripts/`):
- `code_analysis.py` - Syntax, Linting, Security-Scanning
- `run_tests.py` - Test-Ausführung mit Coverage-Reporting

### 📖 Learnings-Framework

- Häufige KI-Code-Probleme und Lösungen
- Erfolgreiche Prompt-Strategien
- Best Practices und Anti-Patterns
- Kontinuierliche Verbesserung

## 🚀 Installation

### Gemeinsame Ressourcen synchronisieren

Die Claude-, Codex- und Gemini-Skills lesen ihre Templates zur Build-Zeit aus `shared/skill-common/`. Führe deshalb **vor jedem Packaging oder jeder Installation** einmal

```bash
./tools/sync_skill_assets.sh
```

aus. Dadurch werden die Zielordner (`claude/skill/…`, `codex/skills/d-kit/…`, `gemini/context/…`) mit den aktuellen Templates/Checklisten gefüllt.

### Voraussetzungen

- Claude Account (Sonnet 4.5 oder höher empfohlen)
- Skills-Feature aktiviert in Claude

### Installation

1. **Download des Skills**
   ```bash
   # Download der neuesten Version
   wget https://github.com/yourusername/d-kit/releases/download/v1.1.0/d-kit-v1.1.0.skill
   ```

2. **Import in Claude**
   - Öffnen Sie Claude
   - Gehen Sie zu Settings → Skills
   - Klicken Sie auf "Import Skill"
   - Wählen Sie `d-kit-v1.1.0.skill` aus
   - Der Skill ist nun verfügbar!

### Codex (GPT-5 Codex CLI)

1. **Skill-Dateien installieren**
   ```bash
   cd /pfad/zu/d-kit
   ./tools/sync_skill_assets.sh
   ./codex/tools/install_skill.sh
   ```
2. **Bootstrap aktivieren**
   - Inhalt aus `codex/bootstrap/AGENTS-snippet.md` an `~/.codex/AGENTS.md` anhängen.
   - Codex neu starten; der Skill wird automatisch erkannt.
3. **Weitere Hinweise**
   - Details siehe [`codex/README.md`](codex/README.md)

### Gemini CLI (GenKit Extension)

1. **Gemeinsame Assets synchronisieren**
   ```bash
   cd /pfad/zu/d-kit
   ./tools/sync_skill_assets.sh
   ```
2. **Extension lokal installieren**
   ```bash
   gemini extensions install --local /pfad/zu/d-kit/gemini
   ```
3. **Verwendung**
   - Beim Start liest Gemini die Kontextdatei `DKIT.md` und stellt Templates/Checklisten bereit.
   - Details siehe [`gemini/README.md`](gemini/README.md)

### Grok (xAI Collections)

1. **Collection anlegen & Dateien hochladen**
   - Anleitung siehe [`docs/grok-collections.md`](docs/grok-collections.md)
   - Empfohlen: Alle Dateien aus `shared/skill-common/` hochladen.
2. **Grok anweisen**
   - Verwende den bereitgestellten Startprompt, damit Grok jede Aufgabe mit `collections.search` beginnt.
   - Checklisten wie gewohnt per `update_plan` abbilden.

## 🎬 Quick Start

### Beispiel 1: Neue Software entwickeln

```
User: "Ich möchte eine Todo-App mit KI entwickeln"

Claude: "Großartig! Ich nutze den d-kit Skill für einen 
strukturierten Entwicklungsprozess. Lass uns mit einem 
Lastenheft starten..."
```

Claude führt Sie durch:
1. ✅ Anforderungssammlung & Lastenheft
2. ✅ Pflichtenheft & Architektur-Dokument
3. ✅ MVP-Plan & Sprint-Planung
4. ✅ Task-by-Task Implementation mit Tests
5. ✅ Release-Ready Software

### Beispiel 2: Bestehendes Projekt fortsetzen

```
User: "Erstelle ein Design-Dokument für Task: User-Login"

Claude: [Nutzt task-design.md Template]
```

### Beispiel 3: Code-Review

```
User: "Review dieses Design-Dokument"

Claude: [Nutzt design-review.md mit 12 Review-Kriterien]
```

## 📖 Dokumentation

Vollständige Dokumentation finden Sie in [`docs/`](docs/):

- [Getting Started Guide](docs/getting-started.md) - Erste Schritte mit d-kit
- [Process Overview](docs/process-overview.md) - Detaillierte Prozessbeschreibung
- [Improvements](docs/improvements.md) - Verbesserungen gegenüber Ad-Hoc Entwicklung
- [Examples](docs/examples/) - Praxisbeispiele
- [Grok Collections](docs/grok-collections.md) - d-kit in xAI Grok integrieren
- [GitHub Blog: Spec-driven Development Toolkit](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/) – beschreibt die gleiche Philosophie, auf der d-kit basiert
- [GitHub/spec-kit](https://github.com/github/spec-kit) – Open-Source Toolkit für spefikationsgetriebene Entwicklung

## 📊 Erwartete Ergebnisse

| Phase          | Zeit ohne KI | Zeit mit d-kit | Ersparnis |
| -------------- | ------------ | -------------- | --------- |
| Design         | 100%         | 40%            | **60%**   |
| Implementation | 100%         | 45%            | **55%**   |
| Testing        | 100%         | 50%            | **50%**   |
| Dokumentation  | 100%         | 30%            | **70%**   |

**Zusätzliche Vorteile:**
- ~40% weniger Bugs durch systematische Reviews
- >80% Test-Coverage statt typisch 50%
- Production-Ready Code Quality
- Vollständige Dokumentation

## 🏗️ Projekt-Struktur

```
d-kit/
├── claude/
│   ├── skill/                 # Claude Skill Dateien
│   │   ├── SKILL.md           # Haupt-Skill-Definition
│   │   ├── scripts/           # Automatisierungs-Scripts
│   │   ├── references/        # Prompt-Templates, Checklists, etc.
│   │   └── assets/            # Assets (leer in v1.0)
│   └── tools/                 # Build- & Test-Tools für den Skill
├── codex/                     # Codex Skill (inkl. Installer & Bootstrap)
├── docs/                      # Dokumentation
├── shared/skill-common/       # Gemeinsame Templates/Prompts/Scripts für beide Skills
├── tools/                     # Hilfsskripte (z. B. sync_skill_assets.sh)
├── CONTRIBUTING.md            # Beitragenden-Leitfaden
├── LICENSE
└── README.md
```

> **Hinweis:** Änderungen an Templates, Checklists oder Scripts bitte in `shared/skill-common/` vornehmen und danach `./tools/sync_skill_assets.sh` ausführen. Dadurch bleiben der Claude- und der Codex-Skill automatisch konsistent.

## 🔧 Workflow-Varianten

### Quick-Start (kleine Projekte)
Für Projekte mit <5 Tasks:
1. Lastenheft → direkt MVP-Plan
2. Pro Task: Design → Code → Tests
3. Release

### Enterprise (große Projekte)
Mit zusätzlichen Reviews:
- Stakeholder-Reviews nach jeder Phase
- Detailliertere Dokumentation
- Erweiterte Test-Coverage (>90%)
- Security-Reviews nach jedem Sprint

## 🤝 Contributing

Wir freuen uns über Beiträge! Siehe [CONTRIBUTING.md](CONTRIBUTING.md) für Details.

### Wie Sie helfen können:

- 🐛 Bug Reports
- 💡 Feature Requests
- 📝 Dokumentations-Verbesserungen
- 🔧 Neue Prompt-Templates
- 📊 Erfolgsgeschichten teilen

## 📜 Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe [LICENSE](LICENSE) für Details.

## 🙏 Danksagungen

- Inspiriert von modernen Softwareentwicklungs-Best-Practices
- Basiert auf Erfahrungen aus zahlreichen KI-Entwicklungsprojekten
- Claude von Anthropic für die KI-Fähigkeiten

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/d-kit/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/d-kit/discussions)


## 🗺️ Roadmap

### v1.1 (geplant)
- [ ] Zusätzliche Prompt-Templates (Bug-Fix, Refactoring)
- [ ] GitHub Actions Integration
- [ ] Erweiterte Metriken
- [ ] Multi-Language Support

### v2.0 (Zukunft)
- [ ] CI/CD-Integration Templates
- [ ] Docker/Kubernetes Templates
- [ ] API-First Design Templates
- [ ] Microservices-Patterns

---

<div align="center">

**Entwickelt mit ❤️ und KI**

[⬆ Nach oben](#d-kit---development-ki-templates)

</div>
