# Prompt-Template: Test-Generierung

## Kontext
Du erzeugst Tests (Unit, Integration oder E2E) für zuvor definierten Code.

## Aufgabe
Erstelle aussagekräftige Tests für die folgende Implementierung:

```
[CODE SNIPPET EINSETZEN]
```

### Rahmenbedingungen
- Programmiersprache / Framework: [z. B. TypeScript + Jest]
- Anzahl Tests: [z. B. mind. 5]
- Coverage-Ziel: >80% Branch & Statement Coverage
- Test-Typen: [Unit | Integration | E2E]
- Kritische Pfade / Edge Cases: [Auflisten]
- Mocking / Stubs: [Erlaubt / Nicht erlaubt]

## Struktur des Outputs

1. **Test-Strategie** (kurz)
   - Welche Szenarien werden abgedeckt?
   - Welche Randfälle werden getestet?
   - Welche Hilfsfunktionen/Mocks sind nötig?

2. **Testsuite**
   - Codeblock mit vollständigen Tests (inkl. Imports/Setup)
   - Benutze idiomatische Test-Framework-APIs
   - Dokumentiere (Kommentar) warum der Test existiert

3. **Verifikation**
   - Wie wird die Coverage gemessen? (`npm test -- --coverage` …)
   - Weitere manuelle Checks?

4. **Follow-up**
   - Wo Coverage <80%? Welche zusätzlichen Tests wären möglich?
   - Welche Risiken bleiben offen?

## Richtlinien
- Schreibe deterministische Tests (keine Zufallswerte ohne Seeding)
- Tests müssen unabhängig voneinander laufen
- Nutze Arrange/Act/Assert-Struktur
- Prüfe sowohl Happy Path als auch Fehlerfälle
- Dokumentiere Annahmen direkt im Testcode (Kommentare)
- Falls externe Ressourcen nötig wären: Funktion mocken oder Dependency Injection nutzen

## Beispiel
```
# Testsuite für calculateInvoiceTotal()

1. Strategie
   - Happy Path: Standard-Warenkorb
   - Edge Case: Leerer Warenkorb → 0
   - Fehlerfall: Ungültige Items werfen Error

2. Testsuite (Jest)
```
