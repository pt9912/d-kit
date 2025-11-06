# Prompt-Template: MVP-Plan

## Kontext
Du erstellst einen MVP-Plan basierend auf dem Pflichtenheft und Architektur-Dokument.

## Aufgabe
Erstelle einen MVP-Plan für:

[PFLICHTENHEFT HIER EINFÜGEN]
[ARCHITEKTUR-DOKUMENT HIER EINFÜGEN]

## Struktur des MVP-Plans

### 1. MVP-Vision
- Was ist das Minimum Viable Product
- Welches Kernproblem löst der MVP
- Zielgruppe für den MVP

### 2. MVP Progress Overview

**Aktueller Stand**: [Datum]
```
Gesamt-Fortschritt: ████████░░ 80% (12/15 Features)

Must-Have:  ███████░░░ 70% (7/10)
Should-Have: ████████░░ 80% (4/5)  
Could-Have:  █████░░░░░ 50% (1/2)
```

**Status**: 🟢 On Track / 🟡 At Risk / 🔴 Delayed
**Sprint**: [Aktueller Sprint] von [Gesamt-Sprints]
**Verbleibende Zeit**: [X Wochen]

**Letzte Aktualisierung**: [Datum]

### 3. Feature-Priorisierung (MoSCoW)

#### Must-Have Features (Kern-Features für MVP)
Für jedes Must-Have Feature:
```
Feature: [Name]
ID: MVP-M-XXX
Status: [ ] Todo / [→] In Progress / [✓] Done / [✗] Blocked
Progress: [X/Y Tasks] ███░░░ XX%
Sprint: [Sprint-Nummer]

User Story: Als [Rolle] möchte ich [Funktion], damit [Nutzen]
Beschreibung: [Detaillierte Beschreibung]

Acceptance-Kriterien:
  - [ ] Kriterium 1
  - [ ] Kriterium 2
  - [ ] Kriterium 3

Tasks:
  - [✓] TASK-001: [Beschreibung] (Sprint 1)
  - [→] TASK-002: [Beschreibung] (Sprint 1)
  - [ ] TASK-003: [Beschreibung] (Sprint 2)

Geschätzter Aufwand: [Small/Medium/Large oder Story Points]
Tatsächlicher Aufwand: [Falls abgeschlossen]
Abhängigkeiten: [Liste von Feature-IDs]
Zugeordnete Anforderungen: [FA-XXX aus Pflichtenheft]

Notizen: [Wichtige Erkenntnisse, Probleme, Änderungen]
```

#### Should-Have Features (Wichtig, aber nicht MVP-kritisch)
[Gleiche Struktur wie Must-Have]

#### Could-Have Features (Nice-to-Have für spätere Releases)
[Gleiche Struktur wie Must-Have]

#### Won't-Have Features (Explizit ausgeschlossen)
- Liste von Features die bewusst nicht im MVP sind
- Begründung für Ausschluss

### 3. MVP-Umfang

#### 3.1 In-Scope
- Detaillierte Liste was im MVP enthalten ist
- Technische Komponenten
- Features

#### 3.2 Out-of-Scope
- Was explizit NICHT im MVP ist
- Was in späteren Versionen kommt

### 4. Feature-Dependencies Graph
```
MVP-M-001 (Login)
    └── MVP-M-002 (Dashboard)
        ├── MVP-M-003 (Data Display)
        └── MVP-M-004 (User Settings)
```

### 5. Technische Meilensteine

#### Milestone 1: [Name]
**Status**: [ ] Not Started / [→] In Progress / [✓] Completed / [✗] Blocked
**Progress**: ████░░░░░░ XX%
**Ziel**: [Was soll erreicht werden]
**Features**: [Liste der Features]
**Dauer**: [Geschätzt] | **Tatsächlich**: [Falls abgeschlossen]
**Sprint**: [Sprint-Nummer(n)]

Definition of Done:
  - [✓] Kriterium 1 (abgeschlossen)
  - [→] Kriterium 2 (in Arbeit)
  - [ ] Kriterium 3

**Risiken/Issues**: [Falls vorhanden]
**Notizen**: [Wichtige Updates]
**Letzte Aktualisierung**: [Datum]

[Weitere Milestones...]

### 6. MVP-Timeline

```
Woche 1-2:   [Milestone 1]
Woche 3-4:   [Milestone 2]
Woche 5-6:   [Milestone 3]
Woche 7-8:   Testing & Bug Fixing
Woche 9:     MVP Release
```

### 7. Risiken & Mitigation

#### Risiko 1: [Beschreibung]
- Wahrscheinlichkeit: [Hoch/Mittel/Niedrig]
- Impact: [Hoch/Mittel/Niedrig]
- Mitigation: [Wie wird das Risiko adressiert]

[Weitere Risiken...]

### 8. MVP Success-Kriterien

#### 8.1 Funktionale Kriterien
- [ ] Alle Must-Have Features implementiert
- [ ] Alle Acceptance-Kriterien erfüllt
- [ ] Core User Journey funktioniert

#### 8.2 Technische Kriterien
- [ ] Test-Coverage > 80%
- [ ] Keine kritischen Bugs
- [ ] Performance-Anforderungen erfüllt

#### 8.3 Business-Kriterien
- [ ] MVP löst definiertes Kernproblem
- [ ] Feedback von Zielgruppe eingeholt
- [ ] Bereit für erste User

### 9. Post-MVP Roadmap (Ausblick)

#### Version 1.1 (nach MVP)
- Should-Have Features

#### Version 1.2
- Could-Have Features

#### Version 2.0
- Major neue Features

### 10. Team & Resources

#### Erforderliche Skills
- Frontend Development
- Backend Development
- DevOps
- Testing/QA

#### Geschätzter Gesamtaufwand
- [X] Wochen / [Y] Sprints
- [Z] Story Points

## Wichtige Hinweise
- MVP muss echten Mehrwert liefern (nicht nur ein "Hello World")
- Features müssen testbar und messbar sein
- Realistische Zeitschätzungen
- Dependencies klar identifizieren
- Bei Unsicherheiten: mehrere Szenarien (Best/Worst/Realistic Case)
