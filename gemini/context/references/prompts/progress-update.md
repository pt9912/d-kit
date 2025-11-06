# Prompt-Template: Progress-Update

## Kontext
Du aktualisierst den Fortschritt in MVP-Plan und Sprint-Plan basierend auf abgeschlossenen Arbeiten.

## Aufgabe
Aktualisiere den Fortschritt für:

**Completed Work**:
[WAS WURDE ABGESCHLOSSEN - z.B. "TASK-002 Code implementiert und getestet"]

**Current Documents**:
[MVP-PLAN DOKUMENT HIER]
[SPRINT-PLAN DOKUMENT HIER]

## Update-Prozess

### 1. Identifiziere zu aktualisierende Bereiche

**Check in beiden Dokumenten**:
- Task-Status und Progress
- Feature-Progress (im MVP-Plan)
- Milestone-Progress (im MVP-Plan)
- Daily Progress (im Sprint-Plan)
- Burndown Chart
- Acceptance-Kriterien Checkboxen

### 2. Task-Status Update

**Aktualisiere im Sprint-Plan**:

```markdown
#### Task 2: Registration API
Status: [→] In Progress → [✓] Done ✓
Progress: ████████░░ 80% → ██████████ 100%

Acceptance-Kriterien:
  - [✓] API Endpoint erstellt
  - [✓] Request Validation
  - [✓] Password Hashing
  - [✓] Email Uniqueness Check
  - [✓] Send Verification Email (abgeschlossen heute)
  - [✓] Unit Tests (12/12 tests passing)
  - [✓] Integration Tests (5/5 passing)
  - [✓] Code Review (approved by @reviewer)

Subtasks:
  - [✓] Design-Dokument erstellen
  - [✓] Code implementieren
  - [✓] Tests schreiben (12/12 tests)
  - [✓] Code-Review (completed)
  - [✓] Integration (merged to develop)

Zeiterfassung:
  - Geschätzter Aufwand: 6 Stunden
  - Tatsächlicher Aufwand: 5.5 Stunden ✅
  - Abweichung: -0.5h (schneller als geplant)

Actual Completion: 2024-11-05 15:30

Notizen/Updates:
  - 2024-11-05: Task erfolgreich abgeschlossen
  - Email-Service integration ging schneller als erwartet
  - Alle Tests passing, Coverage: 92%
  - Code-Review ohne Änderungen approved
```

### 3. Feature-Progress Update (MVP-Plan)

**Aktualisiere verknüpftes Feature**:

```markdown
### Feature: User Authentication [→ 75%]
Progress: ██████░░░░ 60% → ███████░░░ 75%

Tasks:
  - [✓] TASK-001: User Model & Database (Sprint 1) ✓
  - [✓] TASK-002: Registration API (Sprint 1) ✓ NEW
  - [→] TASK-003: Login API (Sprint 1, in progress)
  - [ ] TASK-004: Frontend Forms (Sprint 2)
  - [ ] TASK-005: Integration Tests (Sprint 2)

Progress: 3/6 Tasks completed → 2/5 Tasks completed
Status: On Track ✅
Current Sprint: Sprint 1
ETA: End of Sprint 2

Notizen:
  - 2024-11-05: Registration API completed ahead of schedule
  - Ready to start Login API
```

### 4. Milestone-Progress Update (MVP-Plan)

```markdown
### Milestone 1: Authentication [→ 67%]
Progress: ████░░░░░░ 50% → ██████░░░░ 67%
Status: In Progress ✅

- [✓] Database Schema (completed Sprint 1, Day 1)
- [✓] User Model (completed Sprint 1, Day 1)
- [✓] Registration API (completed Sprint 1, Day 3) ✓ NEW
- [→] Login API (in progress, Sprint 1, Day 3-4)
- [ ] Frontend Integration (Sprint 2)
- [ ] E2E Tests (Sprint 2)

Progress: 3/6 items (50%) → 4/6 items (67%)
Blockers: None
Risks: None
On Track: Yes ✅
Next: Complete Login API by end of Sprint 1

Letzte Aktualisierung: 2024-11-05 15:35
```

### 5. Daily Progress Update (Sprint-Plan)

**Füge neuen Tag hinzu oder aktualisiere aktuellen Tag**:

```markdown
#### Tag 3: 2024-11-05
**Geplant**: TASK-002 abschließen, TASK-003 starten

**Completed Today**:
  - [✓] TASK-002: Registration API (5 SP) ✅

**In Progress**:
  - [→] TASK-003: Login API (started, 15% complete)

**Blockers**: 
  - Keine

**Issues**:
  - Keine

**Metrics**:
  - Story Points Burned Today: 5 SP
  - Cumulative SP: 8 SP of 15 SP (53%)
  - Velocity: 2.7 SP/day (Target: 1.5 SP/day)
  - Status: Ahead of schedule ⚡

**Team Notes**:
  - TASK-002 completed faster than expected
  - Email-Service integration straightforward
  - All tests passing with high coverage (92%)
  - Team morale: Excellent
  - Started TASK-003 in afternoon
```

### 6. Sprint Progress Overview Update

**Aktualisiere Gesamt-Übersicht**:

```markdown
### 2. Sprint Progress Overview

Sprint: 1 von 3
Status: 🟢 On Track → 🟢 Ahead of Schedule ⚡
Zeitraum: 2024-11-01 - 2024-11-10
Tag: 3 von 10

Sprint-Fortschritt: ██████░░░░ 60% → █████████░ 90%

Completed:    ██████████ 2 tasks → 3 tasks
In Progress:  ████░░░░░░ 1 task → 1 task
Blocked:      ░░░░░░░░░░ 0 tasks
Not Started:  ████░░░░░░ 2 tasks → 1 task

Velocity:
- Target: 1.5 SP/Tag
- Actual: 2.7 SP/Tag ⚡
- Trend: ↗️ Ahead of Schedule

Burndown:
Day 1: ████████████████ 15 SP (started)
Day 2: █████████████░░░ 12 SP
Day 3: ████████░░░░░░░░  7 SP (Current) ⚡
Day 4: ░░░░░░░░░░░░░░░░  ? SP
---
Target: ─────────────── 0 SP (Day 10)

Letzte Aktualisierung: 2024-11-05 15:40
```

### 7. Acceptance-Kriterien Update

**Wenn Acceptance-Kriterien erfüllt wurden**:

```markdown
## Acceptance Criteria Progress (MVP-Plan)

### Feature: User Authentication

#### Functional Criteria
- [✓] User can register with email and password
- [✓] User receives verification email ✓ NEW
- [ ] User can verify email via link
- [✓] User can login with credentials
- [ ] User receives JWT token
- [ ] Invalid credentials show error message
- [ ] Duplicate email shows error

Progress: 3/7 criteria met (43%) → 4/7 criteria met (57%)

#### Technical Criteria
- [✓] Password hashing with bcrypt
- [✓] Email validation
- [✓] Email sending implemented ✓ NEW
- [ ] JWT token generation
- [ ] Token expiry handling
- [ ] Refresh token support
- [✓] Rate limiting on auth endpoints

Progress: 4/7 criteria met (57%)

Overall Progress: 8/14 criteria (57%)
```

## Update-Regeln

### Wann Updates durchführen

**Sofort aktualisieren bei**:
- ✅ Task-Statusänderung (Started, Completed, Blocked)
- ✅ Subtask abgeschlossen
- ✅ Blocker aufgetreten oder aufgelöst
- ✅ Acceptance-Kriterium erfüllt

**Am Ende des Tages aktualisieren**:
- Daily Progress Tracking
- Zeiterfassung (tatsächlicher Aufwand)
- Sprint Progress Overview
- Team Notes

**Bei Completion aktualisieren**:
- Task-Status auf Done
- Alle Checkboxen
- Tatsächlicher Aufwand vs. Geschätzt
- Feature-Progress
- Milestone-Progress
- Sprint Burndown

### Konsistenz-Checks

**Stelle sicher dass**:
1. Task-Status in Sprint-Plan und MVP-Plan übereinstimmen
2. Prozent-Angaben mit Checkbox-Count übereinstimmen
3. Story Points in Burndown korrekt addiert werden
4. Datum-Stempel aktuell sind
5. Abhängigkeiten reflektiert werden (wenn Task A done, wird Task B unblocked)

### Progress-Calculation

**Automatische Berechnung**:
```
Task Progress = (Completed Subtasks / Total Subtasks) * 100
Feature Progress = (Completed Tasks / Total Tasks) * 100
Milestone Progress = (Completed Items / Total Items) * 100
Sprint Progress = (Completed SP / Total SP) * 100
```

## Beispiel: Komplettes Update nach Task-Completion

**Ausgangslage**: TASK-002 wurde gerade abgeschlossen

**Updates durchführen**:

1. ✅ Sprint-Plan: Task-Status → Done, alle Checkboxen
2. ✅ Sprint-Plan: Daily Progress für Tag 3
3. ✅ Sprint-Plan: Sprint Progress Overview aktualisieren
4. ✅ MVP-Plan: Feature-Progress aktualisieren
5. ✅ MVP-Plan: Milestone-Progress aktualisieren
6. ✅ MVP-Plan: Acceptance-Kriterien abhaken
7. ✅ Beide: Datum-Stempel setzen

**Ergebnis**: Konsistentes Bild des Fortschritts in allen Dokumenten

## Wichtige Hinweise

- **Ehrlich sein**: Realistische Progress-Zahlen, keine Schönfärberei
- **Aktuell halten**: Tägliche Updates, nicht erst am Sprint-Ende
- **Notizen machen**: Wichtige Erkenntnisse dokumentieren
- **Trends erkennen**: Velocity-Änderungen beobachten
- **Kommunizieren**: Blockers sofort melden, nicht verstecken
- **Lernen**: Abweichungen (Zeit, Aufwand) für Retrospektive nutzen
