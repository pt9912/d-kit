# Prompt-Template: Pflichtenheft-Generierung

## Kontext
Du bist ein Software-Architekt und erstellst ein Pflichtenheft basierend auf einem Lastenheft.

## Aufgabe
Erstelle ein detailliertes Pflichtenheft aus dem folgenden Lastenheft:

[LASTENHEFT HIER EINFÜGEN]

## Struktur des Pflichtenhefts

### 1. Projektziel
- Kurze Zusammenfassung des Projekts
- Primäre Geschäftsziele

### 2. Funktionale Anforderungen
Für jede Anforderung aus dem Lastenheft:
- **ID**: FA-XXX (eindeutige Nummer)
- **Titel**: Kurze Beschreibung
- **Beschreibung**: Detaillierte Spezifikation
- **Zugehörige User Stories**: [US-XXX, US-YYY]
- **Zugehörige Use-Cases**: [UC-XXX]
- **Priorität**: Must-Have / Should-Have / Could-Have / Won't-Have
- **Acceptance-Kriterien**: Messbare Kriterien zur Erfüllung
- **Abhängigkeiten**: Von welchen anderen Anforderungen abhängig

**Beispiel**:

#### FA-001: Bestellerfassung
- **Titel**: System muss Bestellerfassung ermöglichen
- **Beschreibung**: Vertriebsmitarbeiter können neue Bestellungen mit Kundendaten, Produkten, Mengen und Lieferterminen erfassen. Das System validiert Eingaben und speichert die Bestellung persistent.
- **Zugehörige User Stories**: US-001 (Bestellung erfassen)
- **Zugehörige Use-Cases**: UC-001 (Neue Bestellung erfassen)
- **Priorität**: Must-Have
- **Acceptance-Kriterien**:
  - Kunde kann neu angelegt oder aus Bestand ausgewählt werden
  - Mindestens 1 Produkt muss ausgewählt werden
  - Gesamtpreis wird automatisch berechnet
  - Nach Speichern wird Bestellnummer vergeben
  - Bestätigung wird dem Nutzer angezeigt
  - Bestellung ist in Datenbank persistent gespeichert
- **Abhängigkeiten**: 
  - FA-020 (Produktkatalog muss existieren)
  - FA-030 (Kundenverwaltung muss existieren)

#### FA-002: Bestellstatusabfrage
- **Titel**: System muss Bestellstatus-Abfrage ermöglichen
- **Beschreibung**: Nutzer können Bestellungen über Bestellnummer oder Kundenname suchen und den aktuellen Status sowie Verlauf einsehen.
- **Zugehörige User Stories**: US-002 (Bestellstatus abfragen)
- **Zugehörige Use-Cases**: UC-002 (Bestellstatus abfragen)
- **Priorität**: Must-Have
- **Acceptance-Kriterien**:
  - Suche über Bestellnummer funktioniert
  - Suche über Kundenname funktioniert
  - Suchergebnisse innerhalb 1 Sekunde angezeigt
  - Status wird klar angezeigt (Neu, In Bearbeitung, Versandt, Geliefert)
  - Statusverlauf mit Zeitstempeln sichtbar
  - Bei mehreren Ergebnissen: Liste mit Filter-Möglichkeit
- **Abhängigkeiten**: FA-001 (Bestellungen müssen existieren)

### 3. Nicht-funktionale Anforderungen

#### 3.1 Performance
- Response-Zeiten
- Durchsatz
- Skalierbarkeit

#### 3.2 Sicherheit
- Authentifizierung
- Autorisierung
- Datenverschlüsselung
- Compliance-Anforderungen

#### 3.3 Usability
- User Experience Anforderungen
- Accessibility
- Internationalisierung

#### 3.4 Wartbarkeit
- Code-Qualität
- Dokumentation
- Testbarkeit

#### 3.5 Verfügbarkeit
- Uptime-Anforderungen
- Backup-Strategie
- Disaster Recovery

### 4. Systemgrenzen
- Was ist Teil des Systems
- Was ist nicht Teil des Systems
- Externe Schnittstellen

### 5. Randbedingungen
- Technische Constraints
- Budget-Constraints
- Zeit-Constraints
- Rechtliche Anforderungen

### 6. Glossar
- Fachbegriffe und ihre Definitionen

## 7. Traceability Matrix

Die Traceability Matrix zeigt die Verbindung zwischen User Stories, Use-Cases und funktionalen Anforderungen:

| User Story | Use-Case | Funktionale Anforderung | Priorität   | Status |
| ---------- | -------- | ----------------------- | ----------- | ------ |
| US-001     | UC-001   | FA-001, FA-020, FA-030  | Must-Have   | [ ]    |
| US-002     | UC-002   | FA-002                  | Must-Have   | [ ]    |
| US-003     | UC-003   | FA-003, FA-001          | Must-Have   | [ ]    |
| US-004     | UC-004   | FA-004                  | Should-Have | [ ]    |
| US-005     | UC-005   | FA-010, FA-011          | Must-Have   | [ ]    |

**Legende**:
- [ ] Not Started
- [→] In Progress
- [✓] Completed
- [✗] Blocked

Diese Matrix ermöglicht:
- **Vollständigkeitsprüfung**: Alle User Stories haben Use-Cases und Anforderungen
- **Impact-Analyse**: Welche Anforderungen sind betroffen bei Änderung einer User Story
- **Progress-Tracking**: Status-Übersicht über alle Ebenen
- **Test-Planung**: Welche Tests decken welche User Stories ab

## 8. Anforderungs-Abhängigkeiten

Visualisierung der Abhängigkeiten zwischen Anforderungen:

```
FA-020 (Produktkatalog)
    └── FA-001 (Bestellerfassung)
            ├── FA-002 (Bestellstatus)
            ├── FA-003 (Bestellung bearbeiten)
            └── FA-004 (Bestellung stornieren)

FA-030 (Kundenverwaltung)
    └── FA-001 (Bestellerfassung)
            └── FA-002 (Bestellstatus)

FA-010 (User Authentication)
    └── Alle anderen Anforderungen (FA-001 bis FA-050)
```

Diese Darstellung hilft bei:
- **Priorisierung**: Basis-Anforderungen zuerst implementieren
- **Planung**: Abhängigkeiten für Sprint-Planung berücksichtigen
- **Risiko-Management**: Kritische Pfade identifizieren

## Wichtige Hinweise
- Jede Anforderung muss eindeutig, messbar und testbar sein
- Prioritäten nach MoSCoW-Methode vergeben
- Abhängigkeiten klar dokumentieren
- Bei Unklarheiten im Lastenheft: Annahmen dokumentieren und kennzeichnen