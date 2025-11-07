---
name: ki-softwareentwicklung
description: Strukturierter KI-gestützter Softwareentwicklungsprozess vom Lastenheft bis zum MVP. Verwende diesen Skill wenn der Benutzer (1) Software mit KI entwickeln möchte, (2) ein Software-Projekt systematisch planen will, (3) von Anforderungen zu Code kommen möchte, (4) einen MVP entwickeln will, (5) nach einem strukturierten Entwicklungsprozess fragt, oder (6) Design-Dokumente, Pflichtenhefte oder Architektur-Dokumente erstellen möchte.
---

# KI-gestützte Softwareentwicklung

Dieser Skill führt durch einen strukturierten, KI-gestützten Entwicklungsprozess mit Validierungs-Checkpoints, Testing-Integration und iterativen Verbesserungsschleifen.

## Prozess-Übersicht

Der Prozess besteht aus 7 Phasen:
1. **Anforderungsanalyse** - Lastenheft → Pflichtenheft + Architektur
2. **Planung** - MVP-Plan + Test-Strategie
3. **UI-Design** - Design-System → Wireframes → Mockups → Prototype
4. **Sprint-Planung** - Sprint-Plan mit Tasks & Checkpoint
5. **Iterative Entwicklung** - Design → Code → Tests (pro Task)
6. **Sprint-Abschluss** - Review → Retrospektive → Learnings
7. **MVP-Abschluss** - E2E-Tests → UAT → Performance-Tests → Release

## Phase 1: Anforderungsanalyse

### Schritt 1: Lastenheft erstellen/analysieren
- Falls vorhanden: Lastenheft analysieren
- Falls nicht vorhanden: Mit User Anforderungen sammeln und Lastenheft erstellen
- Verwende Template: `references/templates/lastenheft.md`

### Schritt 2: Pflichtenheft generieren
- Prompt-Template verwenden: `references/prompts/pflichtenheft.md`
- Aus Lastenheft ein detailliertes Pflichtenheft erzeugen
- Funktionale und nicht-funktionale Anforderungen spezifizieren

### Schritt 3: Architektur-Dokument generieren
- Prompt-Template verwenden: `references/prompts/architektur.md`
- Technologie-Stack definieren
- Komponenten-Diagramm erstellen
- Schnittstellen definieren

### ✓ Review-Checkpoint 1
**Vor dem Weitergehen validieren:**
- Sind alle Anforderungen aus dem Lastenheft im Pflichtenheft erfasst?
- Ist die vorgeschlagene Architektur angemessen und umsetzbar?
- Gibt es Widersprüche oder Unklarheiten?
- User um Freigabe bitten und Feedback einarbeiten

## Phase 2: Planung

### Schritt 4: MVP-Plan erstellen
- Prompt-Template verwenden: `references/prompts/mvp-plan.md`
- Features priorisieren (MoSCoW-Methode)
- Abhängigkeiten identifizieren
- Zeitabschätzung pro Feature

### Schritt 5: Test-Strategie-Dokument erstellen
- Prompt-Template verwenden: `references/prompts/test-strategie.md`
- Unit-Test-Abdeckung definieren
- Integrationstests planen
- Acceptance-Kriterien festlegen

## Phase 3: UI-Design

### Schritt 6: UI-Design erstellen (Figma)
**Für Frontend-Projekte**:
- Prompt-Template verwenden: `references/prompts/ui-design-figma.md`
- Design-Brief und User-Flows ableiten
- Design-System aufsetzen (Colors, Typography, Components, Spacing)
- Wireframes (Low-Fidelity) vorbereiten
- High-Fidelity Mockups designen (Desktop, Tablet, Mobile)
- Interaktionen und Animationen definieren
- Prototype und Handoff-Dokumentation erstellen

**Deliverables**:
- Figma-Datei mit allen Screens und Flows
- Design-System-Dokumentation inkl. Token/Styles
- Component-Spezifikationen & States
- Exportierte Assets (Icons, Bilder, Stylesheets)

### ✓ Design-Review-Checkpoint
**UI-Design validieren**:
- Design-System vollständig & konsistent?
- Alle States abgedeckt (default, hover, error, loading, success)?
- Responsive Varianten vorhanden (Mobile, Tablet, Desktop)?
- Accessibility beachtet (WCAG 2.1 AA)?
- Prototype funktional und getestet?
- User/Stakeholder-Feedback eingeholt?

## Phase 4: Sprint-Planung

### Schritt 7: Ersten Sprint-Plan erstellen
- Prompt-Template verwenden: `references/prompts/sprint-plan.md`
- 2-4 Tasks für ersten Sprint auswählen
- Tasks priorisieren und Dependencies beachten
- Tasks mit klaren Acceptance-Kriterien versehen

### ✓ Review-Checkpoint 2
**Sprint-Plan validieren:**
- Sind die Tasks klar definiert?
- Ist der Sprint-Umfang realistisch?
- User um Freigabe bitten

## Phase 5: Iterative Entwicklung (pro Task)

### Progress-Tracking während der Entwicklung

**Wichtig**: Alle Fortschritte werden direkt in den MVP-Plan und Sprint-Plan Dokumenten getrackt!

**Nach jedem Arbeitsschritt aktualisieren**:
1. Task-Status und Progress-Prozent
2. Checkboxen bei Subtasks und Acceptance-Kriterien
3. Tatsächlicher Aufwand
4. Daily Progress Tracking
5. Notizen zu Problemen oder Änderungen

**Checkpoint-Momente für Updates**:
- ✅ Nach Abschluss eines Subtasks
- ✅ Bei Task-Statusänderung (Todo → In Progress → Done)
- ✅ Bei Problemen oder Blockern
- ✅ Am Ende jedes Arbeitstages
- ✅ Nach Code-Review
- ✅ Nach erfolgreichem Test-Run

### 5.1 Design-Phase

#### Schritt 8: Task-Design-Dokument erstellen
- Prompt-Template verwenden: `references/prompts/task-design.md`
- Technische Spezifikation
- API/Schnittstellen-Definition
- Datenmodell (falls relevant)
- Test-Cases für diese Task

#### Schritt 9: Design Review-Schleife
**Automatische Prüfungen:**
- Konsistenz mit Architektur prüfen
- Best Practices validieren
- Prompt verwenden: `references/prompts/design-review.md`

**Bei Problemen:**
- Design iterativ verbessern
- Zurück zu Schritt 8
- Maximal 3 Iterationen, dann User einbeziehen

#### ✓ Design-Approval (Schritt 10)
- Design-Dokument ist fehlerfrei
- Erst nach Approval weiter zur Implementation

### 5.2 Implementation-Phase

#### Schritt 11: Code generieren
- Prompt-Template verwenden: `references/prompts/code-generation.md`
- Code basierend auf Design-Dokument generieren
- Code-Kommentare und Dokumentation inkludieren

#### Schritt 12: Unit-Tests generieren
- Prompt-Template verwenden: `references/prompts/test-generation.md`
- Tests parallel zum Code erstellen
- Edge-Cases abdecken
- Test-Coverage Ziel: >80%

#### Schritt 13: Code-Analyse durchführen
**Automatische Checks:**
- Syntax-Check durchführen
- Linting (je nach Sprache)
- Security-Scan (statische Analyse)
- Script verwenden: `scripts/code_analysis.py`

### 5.3 Testing-Phase

#### Schritt 14: Tests ausführen
- Unit-Tests laufen lassen
- Code-Coverage prüfen (Ziel: >80%)
- Script verwenden: `scripts/run_tests.py`

#### Schritt 15: Bei Fehlern
- Fehleranalyse durchführen
- Prompt verwenden: `references/prompts/bug-fix.md`
- Code korrigieren (zurück zu Schritt 11)
- Tests erneut durchführen

#### ✓ Task-Completion (Schritt 16)
- Alle Tests erfolgreich
- Code-Coverage erreicht
- Task ist abgeschlossen

### Post-Task-Schritte

#### Schritt 17: Integration
- Task in Gesamtsystem integrieren
- Merge-Konflikte lösen (falls vorhanden)

#### Schritt 18: Integrationstests
- Integrationstests ausführen
- Interaktion mit anderen Komponenten testen

## Phase 6: Sprint-Abschluss

### Nach allen Sprint-Tasks

#### Schritt 19: Sprint-Review
- Funktionale Tests des implementierten Features
- Demo-fähigen Stand erstellen
- Dokumentation aktualisieren
- Checklist verwenden: `references/checklists/sprint-review.md`

#### Schritt 20: Sprint-Retrospektive
**Analyse:**
- Was lief gut?
- Was lief schlecht?
- Welche KI-generierten Outputs waren problematisch?
- Template verwenden: `references/templates/retrospektive.md`

**Verbesserungen:**
- Prompt-Templates anpassen
- Lessons-Learned dokumentieren
- Qualitätsmetriken tracken

#### Schritt 21: Nächster Sprint-Plan
- Prompt-Template verwenden: `references/prompts/sprint-plan.md`
- Learnings aus Retrospektive einbeziehen
- Zurück zu Phase 4, Schritt 7

## Phase 7: MVP-Abschluss

### Wenn alle Sprints abgeschlossen

#### Schritt 22: End-to-End Tests
- Komplette User-Journeys testen
- Performance-Tests durchführen
- Checklist: `references/checklists/e2e-tests.md`

#### Schritt 23: User Acceptance Testing
- Mit echten Usern testen
- Feedback sammeln
- Kritische Bugs fixen

#### Schritt 24: Performance-Tests
- Load-Tests durchführen
- Bottlenecks identifizieren
- Optimierungen vornehmen (falls nötig)

#### ✓ Final Review (Schritt 25)
**MVP Release-Kriterien:**
- Alle Must-Have Features implementiert
- Alle Tests erfolgreich
- Dokumentation vollständig
- Performance-Anforderungen erfüllt

## Best Practices

### Qualitätsmetriken tracken
- Code-Coverage pro Sprint
- Bug-Rate und Schweregrad
- Review-Zyklen pro Design-Dokument
- Velocity (Tasks pro Sprint)

### Kontinuierliche Verbesserung
- Typische KI-Fehler dokumentieren
- Prompt-Templates basierend auf Erfahrungen anpassen
- Learning-Dokument führen: `references/learnings.md`

### Risikomanagement
- Kritische Komponenten kennzeichnen (mehr manueller Review)
- Technische Schulden tracken
- Rollback-Strategie bei fundamentalen Design-Fehlern

## Workflow-Varianten

### Quick-Start für kleine Projekte
Für einfache Projekte (<5 Tasks):
1. Lastenheft → direkt MVP-Plan (Schritte 1, 4, 7)
2. Pro Task: Design → Code → Tests (Schritte 8-16)
3. Release (Schritte 22-25)

### Enterprise-Variante
Für große Projekte mit Team:
- Zusätzliche Stakeholder-Reviews nach jeder Phase
- Detailliertere Dokumentation
- Erweiterte Test-Coverage (>90%)
- Security-Reviews nach jedem Sprint

## Ressourcen

### Prompt-Templates (`references/prompts/`)
Fertige Prompts für jeden Schritt - siehe Dateien im references/prompts/ Verzeichnis

### Document-Templates (`references/templates/`)
Strukturierte Vorlagen für Dokumente

### Checklists (`references/checklists/`)
Validierungs-Checklists für Reviews

### Scripts (`scripts/`)
Hilfs-Scripts für Automatisierung

### Learnings (`references/learnings.md`)
Dokumentation von Erfahrungen und typischen Problemen

## Wichtige Hinweise

1. **Checkpoints nicht überspringen** - Validierung spart Zeit bei späteren Bugfixes
2. **Review-Schleifen begrenzen** - Max. 3 Iterationen, dann User einbeziehen
3. **Tests sind Pflicht** - Keine Task ohne Tests abschließen
4. **Dokumentation aktuell halten** - Nach jedem Sprint aktualisieren
5. **Learnings dokumentieren** - Typische KI-Fehler festhalten für bessere Prompts
6. **Progress kontinuierlich tracken** - MVP-Plan und Sprint-Plan täglich aktualisieren mit Checkboxen
