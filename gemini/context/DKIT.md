# d-kit Entwicklungs-Extension (Gemini CLI)

## Zweck
Diese Extension bringt der Gemini CLI den d-kit Entwicklungsprozess bei. Verwende sie, sobald eine Aufgabe Struktur, Architektur, Implementierung oder Tests erfordert.

## So verwendest du die Extension
1. Lies dieses Dokument vollständig (`open_file ~/.config/gemini/extensions/d-kit/context/DKIT.md`).
2. Prüfe die verfügbaren Artefakte in `references/`:
   - Prompts: `references/prompts/*.md`
   - Templates: `references/templates/*.md`
   - Checklists: `references/checklists/*.md`
3. Nutze `update_plan`, um jeden Checklistenpunkt als ToDo zu verfolgen und abzuschließen.
4. Führe Scripts bei Bedarf mit `python3 ~/.config/gemini/extensions/d-kit/scripts/...` aus.
5. Dokumentiere Learnings und offene Fragen am Ende jeder Phase.

## Prozess-Übersicht (7 Phasen)
1. **Anforderungsanalyse** – Lastenheft → Pflichtenheft → Architektur
2. **Planung** – MVP-Plan → Test-Strategie
3. **UI-Design** – Design-System → Wireframes → Mockups → Prototype
4. **Sprint-Planung** – Sprint-Plan mit Checkpoint
5. **Iterative Entwicklung** – Design → Code → Tests (pro Task)
6. **Sprint-Abschluss** – Review → Retrospektive → Learnings
7. **MVP-Abschluss** – E2E-Tests → UAT → Performance-Tests → Release

## Phase 1: Anforderungsanalyse
- Falls kein Lastenheft vorhanden ist, mithilfe `references/templates/lastenheft.md` erstellen.
- Pflichtenheft mit `references/prompts/pflichtenheft.md` generieren.
- Architektur mit `references/prompts/architektur.md` definieren.
- **Checkpoint 1**: Vollständigkeit + Konsistenz prüfen, Feedback einholen.

## Phase 2: Planung
- MVP-Plan (`references/prompts/mvp-plan.md`) – inklusive Prioritäten & Abhängigkeiten.
- Test-Strategie (`references/prompts/test-strategie.md`) – Coverage-Ziele >80%.

## Phase 3: UI-Design
- Für Frontend-Projekte `references/prompts/ui-design-figma.md` verwenden.
- Design-System, Wireframes, Mockups, Interaktionen und Handoff dokumentieren.
- **Design-Checkpoint**: States, Responsiveness, Accessibility (WCAG 2.1 AA) prüfen.

## Phase 4: Sprint-Planung
- Sprint-Plan (`references/prompts/sprint-plan.md`) erstellen.
- **Review**: Aufgaben realistisch? Dependencies geklärt? Freigabe einholen.

## Phase 5: Iterative Entwicklung (pro Task)
1. **Design (Schritt 8–10)**  
   - Task-Design (`references/prompts/task-design.md`) erstellen.  
   - Review mit `references/prompts/design-review.md`. Max. 3 Iterationen.
2. **Implementation (Schritt 11–13)**  
   - Code via `references/prompts/code-generation.md`.  
   - Tests mit `references/prompts/test-generation.md`.  
   - Analyse: `scripts/code_analysis.py`.
3. **Testing (Schritt 14–16)**  
   - Tests ausführen: `scripts/run_tests.py`.  
   - Bei Fehlern `references/prompts/bug-fix.md` (liegt in progress-update Prompt?).  
   - Task-Completion nur bei grünen Tests.
4. **Integration (Schritt 17–18)**  
   - Task integrieren, Integrationstests fahren.

## Phase 6: Sprint-Abschluss
- Sprint-Review (`references/checklists/sprint-review.md`) durchführen.
- Retrospektive (`references/templates/retrospektive.md`) dokumentieren.
- Nächsten Sprint-Plan auf Basis der Learnings aktualisieren.

## Phase 7: MVP-Abschluss
- E2E-Tests (`references/checklists/e2e-tests.md`) + Performance messen.
- User Acceptance Tests einplanen.
- Final Review: Alle Must-Haves, Tests, Dokumentation, Performance ok → Release.

## Leitplanken
- Checkpoints **nie** überspringen.
- Vor jedem Coding-Schritt Design & Tests planen.
- Alle Learnings in `references/learnings.md` ergänzen.
- `progress-update.md` für Status-Reports verwenden.

Mit dieser Extension bleibt die Gemini CLI im d-kit Prozess – halte alle Schritte ein und dokumentiere Fortschritt transparent.
