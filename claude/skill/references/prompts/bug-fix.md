# Prompt-Template: Bug-Fix Workflow

## Kontext
Du behebst Fehler in einer bestehenden Implementierung. Verwende diesen Prompt, sobald Tests fehlschlagen oder Nutzer über einen Defekt berichten.

## Eingaben
- Fehlerbeschreibung / Testausgabe:
  ```
  [FEHLERAUSGABE / STACKTRACE]
  ```
- Betroffene Komponente / Datei:
  ```
  [PFAD / MODUL]
  ```
- Erwartetes Verhalten:
  ```
  [ERWARTUNG]
  ```

## Vorgehen (strikt einhalten)
1. **Reproduktion**
   - Beschreibe, wie du den Fehler reproduzierst (Kommando, Testfall, manuelle Schritte)
   - Notiere, welche Tests scheitern

2. **Diagnose**
   - Analysiere vorhandene Logs, Stacktraces, Assertions
   - Führe Ursachenanalyse durch (5-Why oder Root Cause Summary)
   - Identifiziere betroffene Codepfade/Abhängigkeiten

3. **Fix planen**
   - Beschreibe geplante Änderungen (z. B. Funktion X validiert Input, neue Branch hinzugefügt …)
   - Evaluieren: Auswirkungen auf andere Module? Rückwärtskompatibel?

4. **Implementierung**
   - Setze den Fix um (sauber, minimal-invasiv)
   - Dokumentiere Entscheidungen im Code (falls nötig kurz kommentieren)

5. **Tests & Verifikation**
   - Füge neue Tests hinzu (Regressionstest für den Bug) → nutze `test-generation.md`
   - Führe bestehende Tests aus (z. B. `scripts/run_tests.py`)
   - Bestätige, dass Coverage-Ziele weiterhin erfüllt sind

6. **Nachbereitung**
   - Aktualisiere relevante Dokumentation (z. B. Changelog, README, Learnings)
   - Kommuniziere Fix & verbleibende Risiken

## Ausgabeformat
```
## Zusammenfassung
- Bug-ID / Ticket: …
- Ursache: …
- Fix: …

## Reproduktion
1. …

## Fix-Details
- Geänderte Datei(en): …
- Änderungen im Verhalten: …

## Tests
- Neu hinzugefügt: …
- Ausgeführt: … (Ergebnis)

## Offene Punkte
- …
```

## Richtlinien
- Niemals Hotfix ohne Tests
- Wenn Ursache unklar → zusätzliche Logs/Assertions hinzufügen
- Kommunikation: dokumentiere alle Schritte, damit andere Entwickler folgen können
- Größere Refactorings vermeiden; Fokus auf minimalen Fix
- Lerneffekt: Ergänze `references/learnings.md` mit Erkenntnissen
