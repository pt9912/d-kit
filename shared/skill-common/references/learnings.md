# Learnings & Best Practices

Dieses Dokument sammelt Erfahrungen aus der KI-gestützten Softwareentwicklung.

## Häufige KI-generierte Code-Probleme

### 1. Over-Engineering
**Problem**: KI generiert zu komplexe Lösungen für einfache Probleme.

**Symptome**:
- Zu viele Abstraktionsschichten
- Premature Optimization
- Unnötige Design Patterns

**Lösung**:
- Im Prompt explizit "KISS-Prinzip" betonen
- Einfachste Lösung verlangen
- Code-Review mit Fokus auf Simplizität

**Verbessertes Prompt-Pattern**:
```
Generiere Code nach dem KISS-Prinzip (Keep It Simple, Stupid):
- Wähle die einfachste Lösung die funktioniert
- Keine vorzeitige Optimierung
- Nur notwendige Abstraktionen
```

### 2. Inkonsistente Namenskonventionen
**Problem**: KI wechselt zwischen verschiedenen Naming-Styles.

**Symptome**:
- camelCase und snake_case gemischt
- Inkonsistente Variablennamen
- Unklare Funktionsnamen

**Lösung**:
- Explizite Naming-Conventions im Prompt
- Referenz auf Projekt-Standards
- Automated Linting

**Verbessertes Prompt-Pattern**:
```
Verwende folgende Namenskonventionen:
- Variablen/Funktionen: camelCase
- Klassen: PascalCase
- Konstanten: UPPER_SNAKE_CASE
- Booleans: is/has/can Präfix
- Funktionen: Verb am Anfang (get, create, update, delete)
```

### 3. Fehlende Error-Handling
**Problem**: KI generiert "Happy Path" Code ohne Fehlerbehandlung.

**Symptome**:
- Keine try-catch Blöcke
- Keine Input-Validierung
- Unbehandelte Promise-Rejections

**Lösung**:
- Explizit Error-Handling verlangen
- Error-Cases im Design-Dokument auflisten
- Review-Checklist für Error-Handling

**Verbessertes Prompt-Pattern**:
```
WICHTIG: Implementiere comprehensive Error-Handling:
- Try-catch für alle async Operationen
- Input-Validierung für alle Funktionen
- User-friendly Error-Messages
- Logging für alle Errors
```

### 4. Tests mit zu geringer Coverage
**Problem**: KI generiert nur offensichtliche Tests.

**Symptome**:
- Nur Happy-Path Tests
- Keine Edge-Case Tests
- Keine Error-Case Tests

**Lösung**:
- Explizite Liste von Test-Szenarien
- Test-Coverage-Requirement im Prompt
- Review der Test-Qualität

**Verbessertes Prompt-Pattern**:
```
Generiere Tests für folgende Szenarien:
1. Happy Path (normale Verwendung)
2. Edge Cases (Grenzwerte, leere Arrays, etc.)
3. Error Cases (ungültige Inputs, Netzwerkfehler, etc.)
4. Null/Undefined Handling
5. Boundary Conditions

Ziel: >90% Code Coverage
```

### 5. Performance-Ignoranz
**Problem**: KI ignoriert Performance-Implikationen.

**Symptome**:
- N+1 Queries
- Unnötige Loops
- Fehlende Indizes
- Memory Leaks

**Lösung**:
- Performance-Requirements explizit nennen
- Beispiele für Performance-Patterns
- Profiling nach Code-Generation

**Verbessertes Prompt-Pattern**:
```
Achte auf Performance:
- Vermeide N+1 Query Problem (verwende JOINs/Includes)
- Verwende Pagination für große Datensets
- Implementiere Caching wo sinnvoll
- Cleanup Resources (Event Listeners, Timers)
```

## Erfolgreiche Prompt-Strategien

### 1. Kontext ist König
**Best Practice**:
```
Guter Prompt:
"Du bist ein Senior-Entwickler und arbeitest an einem E-Commerce-System.
Das System verwendet React, TypeScript, und PostgreSQL.
Die Codebasis folgt Clean-Code-Prinzipien und hat >85% Test-Coverage.

Aufgabe: Implementiere eine Product-Search-Funktion..."

Schlechter Prompt:
"Implementiere eine Suchfunktion"
```

### 2. Beispiele statt Erklärungen
**Best Practice**:
```
Gut: "Verwende diesen Style:
```typescript
// Good example
const user = await userRepository.findById(id);
if (!user) {
  throw new NotFoundError('User not found');
}
```"

Schlecht: "Verwende defensive Programmierung"
```

### 3. Iteratives Refinement
**Best Practice**:
- Erste Iteration: Basic Implementation
- Zweite Iteration: Error-Handling hinzufügen
- Dritte Iteration: Tests hinzufügen
- Vierte Iteration: Performance-Optimierung

### 4. Design-First Approach
**Best Practice**:
- Erst Design-Dokument erstellen und reviewen
- Dann Code generieren basierend auf Design
- Nicht direkt Code generieren ohne Design

## Lessons-Learned pro Projektphase

### Phase 1: Anforderungsanalyse
✅ **Was funktioniert gut**:
- Detaillierte Lastenheft-Templates
- Strukturierte Anforderungs-Kataloge
- MoSCoW-Priorisierung

⚠️ **Was zu beachten ist**:
- KI kann Business-Domain nicht kennen - User-Input essentiell
- Annahmen müssen explizit validiert werden
- Stakeholder-Interviews nicht durch KI ersetzbar

### Phase 2: Architektur
✅ **Was funktioniert gut**:
- Architektur-Pattern Vorschläge
- Technology-Stack Bewertungen
- Trade-Off Analysen

⚠️ **Was zu beachten ist**:
- KI-Vorschläge müssen auf Projekt-Kontext geprüft werden
- Nicht-funktionale Anforderungen explizit nennen
- Skalierungs-Anforderungen konkretisieren

### Phase 3: Design
✅ **Was funktioniert gut**:
- API-Design (OpenAPI/Swagger)
- Datenmodell-Entwürfe
- Detaillierte Pseudocode

⚠️ **Was zu beachten ist**:
- Design-Review ist Pflicht (nicht überspringen!)
- Security-Aspekte oft unvollständig
- Performance-Implikationen oft ignoriert

### Phase 4: Implementation
✅ **Was funktioniert gut**:
- Boilerplate-Code-Generierung
- Standard-Patterns-Implementation
- Refactoring-Vorschläge

⚠️ **Was zu beachten ist**:
- Code muss getestet werden (nicht blind vertrauen)
- Linting und Static Analysis durchführen
- Dependency-Versions überprüfen

### Phase 5: Testing
✅ **Was funktioniert gut**:
- Test-Case-Generierung
- Test-Data-Fixtures
- E2E-Test-Scripts

⚠️ **Was zu beachten ist**:
- Test-Qualität > Test-Quantität
- Edge-Cases müssen explizit genannt werden
- Flaky Tests sofort adressieren

## Anti-Patterns (Was vermeiden)

### ❌ 1. Blind Copy-Paste
**Problem**: Code ohne Review übernehmen

**Besser**: 
- Code verstehen
- Testen
- An Projekt-Standards anpassen

### ❌ 2. Zu große Tasks
**Problem**: KI mit 1000-Zeilen-Task überfordern

**Besser**:
- Tasks in kleinere Subtasks splitten
- Maximal 300-400 Zeilen pro Task

### ❌ 3. Fehlende Context-Information
**Problem**: KI kennt Projekt-Kontext nicht

**Besser**:
- Relevante Code-Teile mitliefern
- Architektur-Entscheidungen wiederholen
- Abhängigkeiten explizit nennen

### ❌ 4. Review-Schritte überspringen
**Problem**: Von Requirements direkt zu Code

**Besser**:
- Immer Design-Phase einschieben
- Design reviewen und approven
- Dann erst Code generieren

### ❌ 5. KI-Output als "Final"
**Problem**: KI-generierten Code nicht hinterfragen

**Besser**:
- Kritisch reviewen
- Testen
- Verbessern wo nötig

## Erfolgreiche Projekt-Patterns

### Pattern 1: "Design-First"
```
1. Anforderungen sammeln
2. Design-Dokument erstellen (mit KI)
3. Design reviewen (menschlich)
4. Design iterieren bis approved
5. Code generieren basierend auf Design
```

**Erfolgsrate**: Hoch ✅
**Zeitersparnis**: 50-60%

### Pattern 2: "Test-Driven"
```
1. Test-Cases definieren (mit KI)
2. Tests schreiben (mit KI)
3. Code implementieren um Tests zu erfüllen (mit KI)
4. Refactoring (mit KI)
```

**Erfolgsrate**: Sehr hoch ✅✅
**Zeitersparnis**: 40-50%

### Pattern 3: "Incremental"
```
1. Minimal-Implementation (mit KI)
2. Testen
3. Feature hinzufügen (mit KI)
4. Testen
5. Wiederholen
```

**Erfolgsrate**: Hoch ✅
**Zeitersparnis**: 45-55%

## Metrik-Tracking

### Code-Quality Metrics
| Metrik | Ziel | Typical | Notes |
|--------|------|---------|-------|
| Test Coverage | >80% | 75-85% | Höher mit expliziten Test-Prompts |
| Bug Density | <5 per KLOC | 8-12 per KLOC | Reduziert durch Review-Prozess |
| Code Review Cycles | <3 | 2-4 | Abhängig von Task-Komplexität |

### Time Savings
| Phase | Zeit ohne KI | Zeit mit KI | Ersparnis |
|-------|--------------|-------------|-----------|
| Design | 100% | 40% | 60% |
| Implementation | 100% | 45% | 55% |
| Testing | 100% | 50% | 50% |
| Documentation | 100% | 30% | 70% |

## Continuous Improvement

### Monatliches Review
- [ ] Prompt-Templates basierend auf Erfahrungen updaten
- [ ] Neue Anti-Patterns dokumentieren
- [ ] Erfolgreiche Strategien teilen
- [ ] Metriken analysieren und Trends identifizieren

### Projekt-Retrospektive
Nach jedem Projekt:
1. Was hat gut funktioniert mit KI?
2. Wo gab es Probleme?
3. Welche Prompts waren besonders effektiv?
4. Welche Prompts müssen verbessert werden?
5. Neue Patterns erkannt?

## Nützliche Ressourcen

### Prompt-Engineering
- Best Practices für Code-Generation Prompts
- Context-Window Management
- Few-Shot Learning Techniken

### Code-Quality
- Static Analysis Tools
- Linting-Configurations
- Security-Scanning Tools

### Testing
- Test-Framework-Dokumentationen
- Coverage-Tool Setups
- CI/CD Best Practices

---

**Letzte Aktualisierung**: [Datum]
**Nächstes Review**: [Datum]
