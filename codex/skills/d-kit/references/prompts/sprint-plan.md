# Prompt-Template: Sprint-Plan

## Kontext
Du erstellst einen Sprint-Plan basierend auf dem MVP-Plan.

## Aufgabe
Erstelle einen Sprint-Plan für Sprint [NUMMER]:

[MVP-PLAN HIER EINFÜGEN]
[VORHERIGER SPRINT-RETROSPEKTIVE HIER EINFÜGEN (falls vorhanden)]

## Struktur des Sprint-Plans

### 1. Sprint-Ziel
- Klares, messbares Ziel für diesen Sprint
- Welches Feature/Milestone soll erreicht werden

### 2. Sprint Progress Overview

**Sprint**: [Nummer] von [Gesamt]
**Status**: 🟢 On Track / 🟡 At Risk / 🔴 Delayed
**Zeitraum**: [Start] - [Ende]
**Tag**: [X] von [Y]

```
Sprint-Fortschritt: ██████░░░░ 60% (3/5 Tasks)

Completed:    ██████ 3 tasks
In Progress:  ██░░░░ 1 task
Blocked:      ░░░░░░ 0 tasks
Not Started:  ░░░░░░ 1 task
```

**Velocity**: 
- Target: [X] SP/Tag
- Actual: [Y] SP/Tag
- Trend: ↗️ Ahead / → On Track / ↘️ Behind

**Burndown**:
```
Day 1: ████████░░ 15 SP
Day 2: ███████░░░ 13 SP
Day 3: █████░░░░░ 10 SP (Current)
Day 4: ░░░░░░░░░░  ? SP
Day 5: ░░░░░░░░░░  0 SP (Target)
```

**Letzte Aktualisierung**: [Datum, Uhrzeit]

### 3. Sprint-Duration
- Start-Datum: [YYYY-MM-DD]
- End-Datum: [YYYY-MM-DD]
- Anzahl Arbeitstage: [X]

### 3. Task-Liste

#### Task 1: [Titel]
```
ID: TASK-XXX
Status: [ ] Todo / [→] In Progress / [✓] Done / [✗] Blocked / [!] Issue
Progress: ████████░░ 80% (4/5 Subtasks)
Sprint Day: [X]

Beschreibung: [Detaillierte Beschreibung]
User Story: [Falls relevant]
Zugeordnetes Feature: [MVP-M-XXX]

Acceptance-Kriterien:
  - [✓] Kriterium 1 (abgeschlossen am [Datum])
  - [→] Kriterium 2 (in Arbeit)
  - [ ] Kriterium 3
  - [✓] Unit-Tests geschrieben
  - [ ] Code-Review durchgeführt

Technische Details:
  - Komponente: [Welche Architektur-Komponente]
  - Dateien/Module: [Zu erstellende/ändernde Dateien]
  - APIs: [Zu erstellende/ändernde Endpunkte]

Subtasks (für detailliertes Tracking):
  - [✓] Design-Dokument erstellen
  - [✓] Code implementieren
  - [→] Tests schreiben (8/10 tests)
  - [ ] Code-Review
  - [ ] Integration

Abhängigkeiten:
  - [✓] TASK-XXX muss abgeschlossen sein (Done)
  - [→] Externe Dependency [Name] (In Progress)

Zeiterfassung:
  - Geschätzter Aufwand: [X Stunden/Story Points]
  - Tatsächlicher Aufwand: [Y Stunden] (laufend aktualisiert)
  - Verbleibend: [Z Stunden]

Priorität: [High/Medium/Low]
Assignee: [Name]
Started: [Datum]
Target Completion: [Datum]
Actual Completion: [Datum, falls abgeschlossen]

Notizen/Updates:
  - [Datum]: [Wichtiges Update oder Problem]
  - [Datum]: [Fortschritt oder Änderung]

Blockers/Issues:
  - [Falls vorhanden]: Beschreibung des Blockers
```

[Weitere Tasks: 2-4 Tasks pro Sprint empfohlen]

### 4. Definition of Done (für den Sprint)
- [ ] Alle Tasks abgeschlossen
- [ ] Alle Tests erfolgreich
- [ ] Code-Review durchgeführt
- [ ] Dokumentation aktualisiert
- [ ] Integration erfolgreich
- [ ] Demo-fähiger Stand vorhanden

### 5. Task-Dependencies Visualisierung
```
TASK-001 (Setup)
    └── TASK-002 (Backend API)
        ├── TASK-003 (Frontend Integration)
        └── TASK-004 (Tests)
```

### 6. Daily Progress Tracking

**Status-Legende**:
- [ ] Not Started | [→] In Progress | [✓] Done | [✗] Blocked | [!] Issue | [~] Skipped

#### Tag 1: [YYYY-MM-DD] 
**Geplant**: [Task-IDs die heute bearbeitet werden sollen]

**Completed**:
  - [✓] TASK-XXX: [Kurzbeschreibung] ([X] SP)

**In Progress**:
  - [→] TASK-XXX: [Beschreibung] (Progress: XX%)

**Blockers**: 
  - [Falls vorhanden] Beschreibung

**Issues**:
  - [Falls vorhanden] Beschreibung

**Metrics**:
  - Story Points Burned Today: [X] SP
  - Cumulative SP: [Y] SP of [Total] SP
  - Velocity: On Track ✅ / Behind ⚠️ / Ahead ⚡

**Team Notes**: [Wichtige Erkenntnisse, Entscheidungen]

---

#### Tag 2: [YYYY-MM-DD]
[Gleiche Struktur...]

---

#### Tag X: [YYYY-MM-DD] - Aktueller Tag
**Geplant**: [Was heute geplant ist]
**Status**: [Wird laufend aktualisiert]

[Weitere Tage...]

### 7. Risiken für diesen Sprint

#### Risiko 1: [Beschreibung]
- Wahrscheinlichkeit: [Hoch/Mittel/Niedrig]
- Impact: [Hoch/Mittel/Niedrig]
- Mitigation: [Was wird getan]
- Owner: [Wer kümmert sich darum]

### 8. Sprint-Capacity
- Verfügbare Entwicklungstage: [X]
- Geplante Story Points: [Y]
- Buffer für Bugs/Unvorhergesehenes: [20% empfohlen]

### 9. Review & Retrospektive Vorbereitung

#### Review-Fragen
- Wurde das Sprint-Ziel erreicht?
- Welche Features sind demo-fähig?
- Was fehlt noch?

#### Retrospektive-Fragen
- Was lief gut?
- Was lief schlecht?
- Was können wir verbessern?
- Welche KI-generierten Outputs waren problematisch?

## Wichtige Hinweise
- Nicht zu viele Tasks pro Sprint (Qualität > Quantität)
- Jeder Task muss innerhalb des Sprints abschließbar sein
- Tasks müssen klare Acceptance-Kriterien haben
- Dependencies früh identifizieren
- 20% Buffer für unvorhergesehene Probleme einplanen
- Learnings aus vorherigem Sprint berücksichtigen
