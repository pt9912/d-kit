# Prompt-Template: Design-Review

## Kontext
Du führst ein systematisches Review eines Task-Design-Dokuments durch.

## Aufgabe
Reviewe folgendes Design-Dokument:

[DESIGN-DOKUMENT HIER EINFÜGEN]

Referenz-Dokumente:
[ARCHITEKTUR-DOKUMENT]
[PFLICHTENHEFT - relevante Anforderungen]

## Review-Kriterien

### 1. Vollständigkeit
Prüfe ob vorhanden:
- [ ] Task-Übersicht mit klarem Ziel
- [ ] Technische Spezifikation
- [ ] API-Design (falls relevant)
- [ ] Datenmodell (falls relevant)
- [ ] Business-Logik Workflow
- [ ] Frontend-Implementation Details (falls relevant)
- [ ] Backend-Implementation Details (falls relevant)
- [ ] Umfassende Test-Cases
- [ ] Performance-Überlegungen
- [ ] Security-Überlegungen
- [ ] Dependencies
- [ ] Monitoring-Plan

**Fehlende Elemente:**
[Liste was fehlt]

### 2. Architektur-Konsistenz
Prüfe:
- [ ] Hält sich an definierte Architektur-Patterns
- [ ] Verwendet korrekten Technologie-Stack
- [ ] Respektiert Komponenten-Grenzen
- [ ] Schnittstellen-Design ist konsistent
- [ ] Namenskonventionen werden eingehalten

**Inkonsistenzen:**
[Liste von Abweichungen mit Begründung warum problematisch]

### 3. Requirements-Coverage
Prüfe gegen Pflichtenheft:
- [ ] Alle relevanten funktionalen Anforderungen adressiert
- [ ] Nicht-funktionale Anforderungen berücksichtigt
- [ ] Acceptance-Kriterien erfüllbar

**Fehlende Requirements:**
[Liste von Anforderungen die nicht adressiert werden]

### 4. API-Design Quality (falls relevant)

#### REST Best Practices
- [ ] RESTful Naming (Nomen statt Verben)
- [ ] Korrekte HTTP-Methoden (GET, POST, PUT, DELETE)
- [ ] Sinnvolle Status-Codes
- [ ] Konsistente Error-Responses
- [ ] Versionierung berücksichtigt
- [ ] Pagination für Listen

**API-Design Issues:**
[Liste von Problemen]

#### Data Contracts
- [ ] Request/Response Strukturen klar definiert
- [ ] Alle Felder dokumentiert
- [ ] Validierungen spezifiziert
- [ ] Optional vs Required klar

**Contract Issues:**
[Liste von Problemen]

### 5. Datenmodell-Qualität (falls relevant)
- [ ] Entities klar definiert
- [ ] Relationships korrekt
- [ ] Indexes für Performance
- [ ] Migration-Strategie vorhanden
- [ ] Backwards Compatibility berücksichtigt
- [ ] Constraints definiert (unique, not null, etc.)

**Datenmodell-Issues:**
[Liste von Problemen]

### 6. Error Handling
- [ ] Alle möglichen Fehler identifiziert
- [ ] User-friendly Error-Messages
- [ ] Logging-Strategie definiert
- [ ] Retry-Mechanismen (wo sinnvoll)
- [ ] Graceful Degradation

**Fehlende Error-Handling:**
[Liste von nicht behandelten Fehlerszenarien]

### 7. Security-Review
- [ ] Authentication überprüft
- [ ] Authorization implementiert
- [ ] Input-Validation vorhanden
- [ ] SQL-Injection Prevention
- [ ] XSS Prevention
- [ ] CSRF Protection (falls relevant)
- [ ] Rate Limiting definiert
- [ ] Sensitive Daten verschlüsselt

**Security-Lücken:**
[Liste von potentiellen Sicherheitsproblemen]

### 8. Test-Coverage
- [ ] Unit-Tests für alle Komponenten
- [ ] Integration-Tests definiert
- [ ] Edge-Cases abgedeckt
- [ ] Error-Cases getestet
- [ ] Performance-Tests (falls relevant)
- [ ] Security-Tests (falls relevant)

**Test-Gaps:**
[Liste von nicht getesteten Szenarien]

### 9. Performance
- [ ] Performance-Implikationen analysiert
- [ ] Caching-Strategie (falls relevant)
- [ ] Database-Queries optimiert
- [ ] N+1 Query Problem vermieden
- [ ] Large Data Sets berücksichtigt
- [ ] Response-Time Anforderungen erfüllbar

**Performance-Concerns:**
[Liste von potentiellen Performance-Problemen]

### 10. Code-Qualität (Pseudocode-Review)
- [ ] Code-Beispiele sind verständlich
- [ ] DRY-Prinzip beachtet
- [ ] SOLID-Prinzipien befolgt
- [ ] Separation of Concerns
- [ ] Error Handling im Code
- [ ] Comments wo nötig

**Code-Quality Issues:**
[Liste von Code-Quality Problemen]

### 11. Dependencies & Risks
- [ ] Alle Dependencies identifiziert
- [ ] Keine zirkulären Dependencies
- [ ] Third-party Libraries begründet
- [ ] Risiken identifiziert
- [ ] Mitigations definiert

**Dependency-Issues:**
[Liste von problematischen Dependencies]

### 12. Implementierbarkeit
- [ ] Design ist in gegebenem Zeitrahmen umsetzbar
- [ ] Keine unmöglichen/unrealistischen Anforderungen
- [ ] Verfügbare Technologien ausreichend
- [ ] Klare Implementierungs-Schritte

**Implementierungs-Concerns:**
[Liste von Umsetzungs-Herausforderungen]

## Review-Ergebnis

### Status
Wähle eines:
- ✅ **APPROVED** - Bereit für Implementation
- ⚠️ **APPROVED WITH MINOR CHANGES** - Kleine Anpassungen nötig, kann parallel zur Implementation erfolgen
- ❌ **CHANGES REQUIRED** - Substantielle Überarbeitung nötig vor Implementation
- 🚫 **REJECTED** - Fundamentale Probleme, komplette Neugestaltung nötig

### Zusammenfassung
[Kurze Zusammenfassung des Reviews: Was ist gut, was muss verbessert werden]

### Kritische Issues (MUSS behoben werden)
1. [Issue mit Impact und empfohlener Lösung]
2. [...]

### Wichtige Issues (SOLLTE behoben werden)
1. [Issue mit Impact und empfohlener Lösung]
2. [...]

### Nice-to-Have Verbesserungen
1. [Optionale Verbesserung]
2. [...]

### Positive Aspekte
- [Was ist besonders gut am Design]
- [...]

### Nächste Schritte
1. [Konkrete Aktionen zur Behebung der Issues]
2. [...]

### Empfohlene Iteration
[Falls Changes Required: Was genau muss überarbeitet werden und wie]

## Wichtige Hinweise
- Sei konstruktiv und spezifisch in der Kritik
- Gib konkrete Verbesserungsvorschläge
- Priorisiere Issues (kritisch vs. nice-to-have)
- Anerkenne auch gute Aspekte des Designs
- Bei Unsicherheit: lieber nachfragen als durchwinken
