# KI-Softwareentwicklung Skill

Ein umfassender Claude-Skill für strukturierte, KI-gestützte Softwareentwicklung vom Lastenheft bis zum MVP.

## 📋 Überblick

Dieser Skill führt Sie durch einen bewährten Entwicklungsprozess mit:
- ✅ Strukturierten Phasen (Anforderungen → Design → Code → Tests → Release)
- ✅ Automatischen Validierungs-Checkpoints
- ✅ Fertigen Prompt-Templates für jeden Schritt
- ✅ Test-Automatisierung und Quality-Gates
- ✅ Kontinuierlicher Verbesserung durch Learnings

## 🚀 Installation

1. Laden Sie die Datei `ki-softwareentwicklung.skill` herunter
2. In Claude: Gehen Sie zu Settings → Skills
3. Klicken Sie auf "Import Skill"
4. Wählen Sie die `.skill` Datei aus
5. Der Skill ist nun verfügbar

## 💡 Verwendung

### Schnellstart

Sagen Sie einfach:
- "Ich möchte eine Software mit KI entwickeln"
- "Hilf mir ein MVP zu planen"
- "Erstelle ein Pflichtenheft aus meinem Lastenheft"
- "Generiere ein Design-Dokument für diese Task"

Der Skill wird automatisch aktiviert und führt Sie durch den Prozess.

### Vollständiger Workflow

#### Phase 1: Anforderungen
```
"Ich möchte eine Bestellverwaltungs-Software entwickeln.
Die Anforderungen sind: [Ihre Anforderungen]"
```

Claude wird:
1. Ein Lastenheft erstellen (falls keines vorhanden)
2. Daraus ein Pflichtenheft generieren
3. Ein Architektur-Dokument erstellen
4. Sie um Review bitten

#### Phase 2: Planung
```
"Erstelle einen MVP-Plan basierend auf dem Pflichtenheft"
```

Claude wird:
1. Features nach MoSCoW priorisieren
2. Einen MVP-Plan erstellen
3. Eine Test-Strategie definieren
4. Einen ersten Sprint-Plan erstellen

#### Phase 3: Entwicklung
```
"Erstelle ein Design-Dokument für Task: User-Login"
```

Claude wird:
1. Ein detailliertes Design-Dokument erstellen
2. Ein automatisches Review durchführen
3. Code generieren (nach Approval)
4. Tests generieren
5. Code-Analyse durchführen

## 📚 Enthaltene Templates

### Prompt-Templates (`claude/skill/references/prompts/`)
- **pflichtenheft.md** - Anforderungsspezifikation
- **architektur.md** - System-Architektur
- **mvp-plan.md** - MVP-Planung
- **sprint-plan.md** - Sprint-Planung
- **task-design.md** - Detailliertes Task-Design
- **design-review.md** - Systematisches Design-Review
- **code-generation.md** - Clean-Code-Generierung
- **test-generation.md** - Testfälle & Coverage-Strategie
- **test-strategie.md** - Umfassende Test-Planung
- **progress-update.md** - Fortschritts- und Statusberichte
- **ui-design-figma.md** - UI-Design-Flow für Figma
- **bug-fix.md** - Strukturierter Bug-Fix-Prozess

### Dokument-Templates (`claude/skill/references/templates/`)
- **lastenheft.md** - Strukturiertes Lastenheft
- **retrospektive.md** - Sprint-Retrospektive

### Checklists (`claude/skill/references/checklists/`)
- **sprint-review.md** - Vollständige Sprint-Review Checklist
- **e2e-tests.md** - End-to-End-Test Validierung

### Scripts (`claude/skill/scripts/`)
- **code_analysis.py** - Automatische Code-Qualitäts-Analyse
- **run_tests.py** - Test-Ausführung mit Coverage

### Learnings (`claude/skill/references/learnings.md`)
- Häufige KI-Code-Probleme und Lösungen
- Erfolgreiche Prompt-Strategien
- Best Practices und Anti-Patterns

## 🎯 Workflow-Varianten

### Für kleine Projekte (<5 Tasks)
```
Quick-Start Modus:
1. Lastenheft → MVP-Plan
2. Pro Task: Design → Code → Tests
3. Release
```

### Für große Projekte
```
Enterprise Modus:
- Zusätzliche Stakeholder-Reviews
- Detailliertere Dokumentation
- Erweiterte Test-Coverage (>90%)
- Security-Reviews nach jedem Sprint
```

## ✨ Hauptfeatures

### 1. Strukturierter Prozess
- 5 klare Phasen mit definierten Outputs
- Validierungs-Checkpoints verhindern Fehler
- Iterative Verbesserungsschleifen

### 2. Qualitätssicherung
- Automatische Code-Analyse
- Test-Coverage >80% Ziel
- Security-Scans
- Design-Reviews vor Implementation

### 3. Best Practices
- Clean-Code-Prinzipien
- SOLID-Prinzipien
- Error-Handling
- Performance-Optimierung
- Security-First

### 4. Dokumentation
- Automatische Code-Dokumentation
- API-Dokumentation
- User-Guides
- Change-Logs

### 5. Continuous Improvement
- Learnings-Dokument pflegen
- Prompt-Templates verbessern
- Metriken tracken
- Retrospektiven durchführen

## 📊 Erwartete Zeitersparnis

| Phase | Ohne KI | Mit Skill | Ersparnis |
|-------|---------|-----------|-----------|
| Design | 100% | 40% | 60% |
| Implementation | 100% | 45% | 55% |
| Testing | 100% | 50% | 50% |
| Dokumentation | 100% | 30% | 70% |

## ⚠️ Wichtige Hinweise

### Do's ✅
- Checkpoints nicht überspringen
- Design vor Code erstellen
- Tests sind Pflicht
- Learnings dokumentieren
- Review-Schleifen ernst nehmen

### Don'ts ❌
- Nicht blind Copy-Paste von Code
- Nicht direkt von Requirements zu Code
- Review-Schritte nicht überspringen
- KI-Output nicht als "final" betrachten
- Nicht ohne Tests releasen

## 🔧 Anpassung

Der Skill kann an Ihre Bedürfnisse angepasst werden:

1. **Prompt-Templates bearbeiten**: Passen Sie die Templates in `claude/skill/references/prompts/` an
2. **Eigene Checklists**: Fügen Sie projektspezifische Checklists in `claude/skill/references/checklists/` hinzu
3. **Scripts erweitern**: Ergänzen Sie Automatisierungs-Scripts unter `claude/skill/scripts/`
4. **Learnings pflegen**: Dokumentieren Sie Erfahrungen in `claude/skill/references/learnings.md`

## 📞 Support

Bei Fragen oder Problemen:
1. Schauen Sie in `claude/skill/references/learnings.md` für häufige Probleme
2. Prüfen Sie die Prompt-Templates unter `claude/skill/references/prompts/` für Beispiele
3. Nutzen Sie die Checklists in `claude/skill/references/checklists/` für systematische Reviews

## 🎓 Beispiel-Session

```
User: "Ich möchte eine Todo-App entwickeln"

Claude: "Großartig! Ich nutze den KI-Softwareentwicklung-Skill, 
um Sie systematisch durch den Entwicklungsprozess zu führen.

Lass uns mit einem Lastenheft starten. Ich habe einige Fragen:

1. Wer sind die Hauptnutzer der App?
2. Welche Kernfunktionen soll die App haben?
3. Gibt es besondere Anforderungen (z.B. Offline-Fähigkeit)?
..."

[Nach Beantwortung]

Claude: "Basierend auf Ihren Antworten habe ich ein Lastenheft erstellt.
[zeigt Lastenheft]

Möchten Sie das reviewen, bevor ich das Pflichtenheft erstelle?"

[User approved]

Claude: "Perfekt! Ich erstelle nun:
1. Pflichtenheft mit detaillierten Anforderungen
2. Architektur-Dokument mit Technologie-Empfehlungen
..."
```

## 📈 Version

- **Version**: 1.0
- **Erstellt**: 2024
- **Kompatibel mit**: Claude Sonnet 4.5+

## 📝 Lizenz

Siehe LICENSE.txt im Skill-Paket.

---

**Viel Erfolg bei Ihrer KI-gestützten Softwareentwicklung! 🚀**
