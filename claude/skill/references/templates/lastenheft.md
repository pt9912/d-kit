# Lastenheft: [Projektname]

## Dokument-Information
- **Projekt**: [Projektname]
- **Version**: 1.0
- **Datum**: [YYYY-MM-DD]
- **Erstellt von**: [Name/Organisation]
- **Status**: Draft / In Review / Approved

## 1. Ausgangssituation

### 1.1 Ist-Situation
[Beschreibung der aktuellen Situation, Probleme, Herausforderungen]

**Beispiel:**
"Derzeit werden Kundenbestellungen manuell per E-Mail und Excel verwaltet. Dies führt zu:
- Hohem Zeitaufwand für manuelle Dateneingabe
- Fehleranfälligkeit bei der Bestellverarbeitung
- Keine Echtzeit-Übersicht über Bestellstatus
- Schwierige Nachverfolgbarkeit von Bestellhistorien"

### 1.2 Verbesserungspotenzial
[Was soll verbessert werden, welche Ziele sollen erreicht werden]

**Beispiel:**
"Eine automatisierte Bestellverwaltungs-Software soll:
- Bestellprozess digitalisieren und automatisieren
- Fehlerrate reduzieren
- Transparenz und Nachverfolgbarkeit erhöhen
- Zeitersparnis von 70% ermöglichen"

## 2. Zielsetzung

### 2.1 Projektziel
[Hauptziel des Projekts in 2-3 Sätzen]

**Beispiel:**
"Entwicklung einer webbasierten Bestellverwaltungs-Software, die den gesamten Bestellprozess von der Aufnahme bis zur Auslieferung digitalisiert und automatisiert."

### 2.2 Business-Ziele
- [Geschäftsziel 1]: [Messbare Kennzahl]
- [Geschäftsziel 2]: [Messbare Kennzahl]
- [Geschäftsziel 3]: [Messbare Kennzahl]

**Beispiel:**
- Zeitersparnis: 70% Reduktion der Bearbeitungszeit pro Bestellung
- Fehlerreduktion: 90% weniger Fehler bei der Bestellverarbeitung
- Kundenzufriedenheit: Erhöhung um 25% innerhalb 6 Monate

### 2.3 Erfolgs-Kriterien
[Woran wird der Erfolg des Projekts gemessen]

**Beispiel:**
- System wird von mindestens 80% der Mitarbeiter aktiv genutzt
- Durchschnittliche Bearbeitungszeit pro Bestellung < 5 Minuten
- User-Zufriedenheit Score > 4/5

## 3. Zielgruppe

### 3.1 Primäre Nutzer
[Wer wird das System hauptsächlich nutzen]

**Beispiel:**
"Vertriebsmitarbeiter (15 Personen):
- Alter: 25-55 Jahre
- IT-Kenntnisse: grundlegend bis fortgeschritten
- Aufgaben: Bestellaufnahme, Kundenkommunikation
- Arbeitsweise: Desktop-Computer, teilweise mobil"

### 3.2 Sekundäre Nutzer
[Weitere Nutzergruppen]

**Beispiel:**
- Lagerverwalter (5 Personen): Bestellausführung, Bestandsverwaltung
- Manager (3 Personen): Reporting, Analysen
- Kunden (ca. 500): Bestellstatus-Abfrage (Optional)

## 4. Zielgruppe

### 4.1 Primäre Nutzer
[Wer wird das System hauptsächlich nutzen]

**Beispiel:**
"Vertriebsmitarbeiter (15 Personen):
- Alter: 25-55 Jahre
- IT-Kenntnisse: grundlegend bis fortgeschritten
- Aufgaben: Bestellaufnahme, Kundenkommunikation
- Arbeitsweise: Desktop-Computer, teilweise mobil"

### 4.2 Sekundäre Nutzer
[Weitere Nutzergruppen]

**Beispiel:**
- Lagerverwalter (5 Personen): Bestellausführung, Bestandsverwaltung
- Manager (3 Personen): Reporting, Analysen
- Kunden (ca. 500): Bestellstatus-Abfrage (Optional)

### 4.3 User Personas

#### Persona 1: [Name], [Rolle]
- **Alter**: [X] Jahre
- **Berufserfahrung**: [X] Jahre
- **IT-Kenntnisse**: [Anfänger/Fortgeschritten/Experte]
- **Ziele**: 
  - [Hauptziel 1]
  - [Hauptziel 2]
- **Frustrationen**: 
  - [Aktuelles Problem 1]
  - [Aktuelles Problem 2]
- **Typischer Arbeitstag**: [Beschreibung]
- **Motivation**: [Was treibt diese Person an]

**Beispiel:**
#### Persona 1: Anna Schmidt, Vertriebsmitarbeiterin
- **Alter**: 32 Jahre
- **Berufserfahrung**: 8 Jahre im Vertrieb
- **IT-Kenntnisse**: Fortgeschritten
- **Ziele**:
  - Bestellungen schnell und fehlerfrei erfassen
  - Kunden proaktiv über Bestellstatus informieren
  - Mehr Zeit für Kundenberatung statt Verwaltung
- **Frustrationen**:
  - Muss Daten mehrfach in verschiedene Systeme eingeben
  - Keine Übersicht über offene Bestellungen
  - Kunden rufen ständig wegen Status an
- **Typischer Arbeitstag**: 
  - 20-30 Kundenanrufe
  - 10-15 neue Bestellungen
  - 5-10 Statusanfragen
- **Motivation**: Kundenservice verbessern, effizienter arbeiten

[Weitere Personas für andere Nutzergruppen...]

## 5. User Stories

User Stories beschreiben Funktionalität aus Sicht der Nutzer nach dem Schema:
**"Als [Rolle] möchte ich [Funktion], damit [Nutzen]"**

### 5.1 User Stories für [Persona/Rolle 1]

#### US-001: Bestellung erfassen
**Als** Vertriebsmitarbeiter  
**möchte ich** eine neue Bestellung mit Kundendaten und Produkten erfassen  
**damit** der Kunde seine Ware erhält und die Bestellung im System dokumentiert ist

**Acceptance-Kriterien**:
- Kundendaten können eingegeben oder aus Bestand ausgewählt werden
- Mehrere Produkte können hinzugefügt werden
- Gesamtpreis wird automatisch berechnet
- Liefertermin kann festgelegt werden
- Bestätigung wird angezeigt

**Priorität**: Must-Have  
**Geschätzter Aufwand**: Large  
**Abhängigkeiten**: Keine

---

#### US-002: Bestellstatus abfragen
**Als** Vertriebsmitarbeiter  
**möchte ich** den aktuellen Status einer Bestellung schnell finden  
**damit** ich Kundenanfragen sofort beantworten kann

**Acceptance-Kriterien**:
- Bestellung über Bestellnummer oder Kundennamen findbar
- Status wird übersichtlich angezeigt (Neu, In Bearbeitung, Versandt, Geliefert)
- Verlauf/History ist sichtbar
- Liefertermin wird angezeigt

**Priorität**: Must-Have  
**Geschätzter Aufwand**: Medium  
**Abhängigkeiten**: US-001

---

#### US-003: Bestellung bearbeiten
**Als** Vertriebsmitarbeiter  
**möchte ich** eine bestehende Bestellung ändern können  
**damit** ich auf Kundenwünsche reagieren kann

**Acceptance-Kriterien**:
- Produkte können hinzugefügt/entfernt werden
- Mengen können geändert werden
- Lieferadresse kann angepasst werden
- Änderungen werden dokumentiert

**Priorität**: Must-Have  
**Geschätzter Aufwand**: Medium  
**Abhängigkeiten**: US-001, US-002

[Weitere User Stories...]

### 5.2 User Stories für [Persona/Rolle 2]

#### US-010: Bestand aktualisieren
**Als** Lagerverwalter  
**möchte ich** den Lagerbestand nach Kommissionierung aktualisieren  
**damit** der Bestand immer aktuell ist

[Details...]

### 5.3 User Stories - Priorisierung

**Must-Have (für MVP)**:
- US-001: Bestellung erfassen
- US-002: Bestellstatus abfragen
- US-003: Bestellung bearbeiten
- US-005: Login/Logout

**Should-Have (für v1.1)**:
- US-004: Bestellung stornieren
- US-006: Benachrichtigungen
- US-010: Bestand aktualisieren

**Could-Have (für v2.0)**:
- US-020: Reports generieren
- US-021: Export zu Excel

**Won't-Have (nicht geplant)**:
- US-099: Integration mit SAP

## 6. Use-Cases

Use-Cases beschreiben detaillierte Interaktionen zwischen Nutzer und System.

### 6.1 Use-Case: Neue Bestellung erfassen

**Use-Case ID**: UC-001  
**Name**: Neue Bestellung erfassen  
**Akteur**: Vertriebsmitarbeiter  
**Ziel**: Kundenbestellung im System erfassen  
**Vorbedingung**: Nutzer ist angemeldet  
**Nachbedingung Erfolg**: Bestellung ist gespeichert, Bestätigung angezeigt  
**Nachbedingung Fehler**: Bestellung nicht gespeichert, Fehlermeldung angezeigt

**Hauptszenario (Happy Path)**:
1. Vertriebsmitarbeiter wählt "Neue Bestellung"
2. System zeigt Bestellformular
3. Vertriebsmitarbeiter gibt Kundendaten ein oder wählt Kunden aus
4. System validiert Kundendaten
5. Vertriebsmitarbeiter fügt Produkte hinzu:
   - Wählt Produkt aus Katalog
   - Gibt Menge ein
   - Wiederholt für weitere Produkte
6. System berechnet Gesamtpreis automatisch
7. Vertriebsmitarbeiter wählt Liefertermin
8. Vertriebsmitarbeiter fügt Notizen hinzu (optional)
9. Vertriebsmitarbeiter klickt "Bestellung speichern"
10. System validiert alle Daten
11. System speichert Bestellung
12. System vergibt Bestellnummer
13. System zeigt Bestätigung mit Bestellnummer
14. System sendet Bestätigungs-Email an Kunden (optional)

**Alternative Szenarien**:

**A1: Kunde existiert nicht (bei Schritt 3)**
- 3a. Vertriebsmitarbeiter wählt "Neuer Kunde"
- 3b. System zeigt Kundenformular
- 3c. Vertriebsmitarbeiter gibt Kundendaten ein
- 3d. System validiert und speichert Kunde
- 3e. Weiter bei Schritt 5

**A2: Produkt nicht verfügbar (bei Schritt 5)**
- 5a. System zeigt Warnung "Produkt nicht auf Lager"
- 5b. System zeigt voraussichtliches Lieferdatum
- 5c. Vertriebsmitarbeiter entscheidet:
  - Option 1: Anderes Produkt wählen
  - Option 2: Trotzdem bestellen mit späterem Liefertermin
- 5d. Weiter bei Schritt 6

**A3: Validierung schlägt fehl (bei Schritt 10)**
- 10a. System zeigt Fehlermeldung mit Details
- 10b. System markiert fehlerhafte Felder rot
- 10c. Vertriebsmitarbeiter korrigiert Eingaben
- 10d. Zurück zu Schritt 9

**Fehlerszenarien**:

**E1: Netzwerkfehler beim Speichern**
- System zeigt: "Verbindungsfehler. Bestellung konnte nicht gespeichert werden"
- System bietet "Erneut versuchen" oder "Als Entwurf speichern"
- Eingaben bleiben erhalten

**E2: Session abgelaufen**
- System zeigt: "Sitzung abgelaufen. Bitte erneut anmelden"
- System speichert Entwurf (falls möglich)
- Nach Login: System bietet Wiederherstellung

**Spezielle Anforderungen**:
- Response-Zeit: < 2 Sekunden für Speichervorgang
- Validierung: Inline-Validierung während Eingabe
- Usability: Maximal 3 Klicks bis Speichern
- Accessibility: Tastatur-Navigation möglich

**Häufigkeit**: 50-100 mal pro Tag  
**UI-Mockup**: Siehe Anhang B  
**Zugehörige User Stories**: US-001

---

### 6.2 Use-Case: Bestellstatus abfragen

**Use-Case ID**: UC-002  
**Name**: Bestellstatus abfragen  
**Akteur**: Vertriebsmitarbeiter, Kunde (über Portal)  
**Ziel**: Aktuellen Status einer Bestellung einsehen

**Hauptszenario**:
1. Nutzer wählt "Bestellung suchen"
2. System zeigt Suchmaske
3. Nutzer gibt Bestellnummer oder Kundennamen ein
4. System sucht in Datenbank
5. System zeigt Suchergebnisse (Liste von Bestellungen)
6. Nutzer wählt gewünschte Bestellung
7. System zeigt Bestelldetails:
   - Bestellnummer
   - Kunde
   - Produkte mit Mengen
   - Aktueller Status
   - Verlauf (Statusänderungen mit Zeitstempel)
   - Voraussichtliches Lieferdatum
   - Tracking-Nummer (falls versandt)
8. Nutzer schließt Detailansicht oder druckt Bestellinfo

**Alternative Szenarien**:

**A1: Keine Ergebnisse (bei Schritt 5)**
- 5a. System zeigt "Keine Bestellungen gefunden"
- 5b. System bietet erweiterte Suche
- 5c. Zurück zu Schritt 3

**A2: Zu viele Ergebnisse (bei Schritt 5)**
- 5a. System zeigt ersten 10 Ergebnisse
- 5b. System bietet Filter (Datum, Status, etc.)
- 5c. Nutzer verfeinert Suche
- 5d. Weiter bei Schritt 6

**Spezielle Anforderungen**:
- Response-Zeit: < 1 Sekunde für Suche
- Suchergebnisse: Maximal 100, dann Pagination
- Relevanz: Sortierung nach Datum (neueste zuerst)

**Häufigkeit**: 100-200 mal pro Tag  
**Zugehörige User Stories**: US-002

---

### 6.3 Use-Case Diagramm

```
                    +------------------------+
                    |  Bestellverwaltung     |
                    +------------------------+
                              |
          +-------------------+-------------------+
          |                                       |
    [Vertriebsmitarbeiter]                  [Lagerverwalter]
          |                                       |
          |-- UC-001: Bestellung erfassen        |
          |-- UC-002: Status abfragen            |
          |-- UC-003: Bestellung bearbeiten      |-- UC-010: Bestand aktualisieren
          |-- UC-004: Bestellung stornieren      |-- UC-011: Kommissionierung
          |                                       |
          |                [Kunde]                |
          |                   |                   |
          +-------------------+-------------------+
                              |
                              |-- UC-020: Status abfragen (readonly)
                              |-- UC-021: Bestellung verfolgen
```

### 6.4 Use-Case Priorisierung

**Phase 1 (MVP)**:
- UC-001: Neue Bestellung erfassen (Must-Have)
- UC-002: Bestellstatus abfragen (Must-Have)
- UC-003: Bestellung bearbeiten (Must-Have)

**Phase 2 (v1.1)**:
- UC-004: Bestellung stornieren (Should-Have)
- UC-010: Bestand aktualisieren (Should-Have)
- UC-020: Kunden-Portal (Should-Have)

**Phase 3 (v2.0)**:
- UC-030: Reports & Analytics (Could-Have)
- UC-031: Automatische Nachbestellung (Could-Have)

## 7. Funktionale Anforderungen

### 4.1 Bestellverwaltung

#### 4.1.1 Bestellung erstellen
**Beschreibung**: Vertriebsmitarbeiter kann eine neue Bestellung im System erfassen.

**Anforderungen**:
- Eingabe von Kundendaten (Name, Adresse, Kontakt)
- Auswahl von Produkten aus Katalog
- Mengenangabe pro Produkt
- Automatische Preisberechnung
- Rabatte anwendbar
- Liefertermin festlegbar
- Notizfeld für besondere Hinweise

**Priorität**: Must-Have

#### 4.1.2 Bestellung bearbeiten
[Ähnliche Struktur wie 4.1.1]

#### 4.1.3 Bestellstatus verfolgen
[...]

### 4.2 Produktverwaltung
[...]

### 4.3 Kundenverwaltung
[...]

### 4.4 Reporting
[...]

## 5. Nicht-funktionale Anforderungen

### 5.1 Performance
- Seitenaufbau: < 2 Sekunden
- Suchabfragen: < 1 Sekunde
- Gleichzeitige Nutzer: mindestens 50

### 5.2 Verfügbarkeit
- Uptime: 99.5% (8/5 Betrieb, Mo-Fr 8-18 Uhr kritisch)
- Geplante Wartungsfenster: Samstag nachts

### 5.3 Usability
- Einarbeitungszeit: Max. 2 Stunden für Basis-Funktionen
- Intuitive Bedienung ohne umfangreiches Training
- Responsive Design für Desktop, Tablet, Smartphone

### 5.4 Sicherheit
- Verschlüsselte Datenübertragung (HTTPS)
- Rollenbasiertes Zugriffskonzept
- Automatische Abmeldung nach 30 Min. Inaktivität
- Audit-Log für kritische Aktionen

### 5.5 Kompatibilität
- Browser: Chrome, Firefox, Safari, Edge (jeweils aktuelle Version)
- Betriebssystem: Windows, macOS, iOS, Android
- Integration mit bestehenden Systemen: [Liste]

### 5.6 Wartbarkeit
- Dokumentation: technische Dokumentation und Benutzerhandbuch
- Updates: vierteljährliche Updates möglich ohne Downtime
- Support: 8/5 Support während Geschäftszeiten

## 6. Rahmenbedingungen

### 6.1 Budget
- Maximales Budget: [Betrag]
- Budgetverteilung: Entwicklung 60%, Testing 20%, Schulung 10%, Betrieb 10%

### 6.2 Zeitplan
- Projektstart: [YYYY-MM-DD]
- MVP-Release: [YYYY-MM-DD] (6 Monate nach Start)
- Vollständiger Rollout: [YYYY-MM-DD] (9 Monate nach Start)

### 6.3 Technische Randbedingungen
- Cloud-Hosting bevorzugt (AWS, Azure, oder GCP)
- Datenhaltung in Deutschland (DSGVO-konform)
- API-First Ansatz für spätere Integrationen

### 6.4 Rechtliche Anforderungen
- DSGVO-Konformität
- Datenschutzerklärung erforderlich
- Impressumspflicht
- Cookie-Consent

## 7. Systemgrenzen

### 7.1 Im Projektumfang
- Bestellverwaltung (Erfassung bis Auslieferung)
- Kundenverwaltung (Stammdaten)
- Produktkatalog
- Basic Reporting

### 7.2 Außerhalb des Projektumfangs
- Buchhaltungsintegration (zukünftige Phase)
- CRM-Features (zukünftige Phase)
- Marketing-Automation
- Komplexe Business Intelligence

### 7.3 Schnittstellen
- Bestehende Systeme, zu denen Schnittstellen benötigt werden:
  - [System 1]: [Datenfluss]
  - [System 2]: [Datenfluss]

## 8. Risiken

### Risiko 1: [Titel]
- **Beschreibung**: [Was könnte schiefgehen]
- **Wahrscheinlichkeit**: Hoch/Mittel/Niedrig
- **Impact**: Hoch/Mittel/Niedrig
- **Mitigation**: [Wie wird das Risiko minimiert]

**Beispiel:**
### Risiko 1: Nutzerakzeptanz
- **Beschreibung**: Mitarbeiter könnten das neue System ablehnen und weiter mit Excel arbeiten
- **Wahrscheinlichkeit**: Mittel
- **Impact**: Hoch (Projektziele nicht erreichbar)
- **Mitigation**: 
  - Frühe Einbindung der Mitarbeiter in Anforderungsanalyse
  - Umfangreiche Schulungen
  - Change-Management-Prozess
  - Incentivierung der Nutzung

## 9. Stakeholder

| Stakeholder | Rolle           | Interesse            | Einfluss |
| ----------- | --------------- | -------------------- | -------- |
| [Name]      | Auftraggeber    | Projekterfolg        | Hoch     |
| [Name]      | Vertriebsleiter | Nutzbarkeit          | Hoch     |
| [Name]      | IT-Leiter       | Technische Umsetzung | Mittel   |
| [Name]      | Endanwender     | Arbeitseffizienz     | Mittel   |

## 10. Glossar

| Begriff      | Definition                                                                     |
| ------------ | ------------------------------------------------------------------------------ |
| Bestellung   | Kundenauftrag über ein oder mehrere Produkte                                   |
| SKU          | Stock Keeping Unit - eindeutige Produktkennung                                 |
| Lieferstatus | Aktueller Status einer Bestellung (offen, in Bearbeitung, versandt, geliefert) |

## 11. Anhänge

- Anhang A: Bestehende Prozessbeschreibungen
- Anhang B: Screenshots aktuelle Excel-Vorlagen
- Anhang C: Anforderungen aus User-Interviews

---

**Freigabe:**

| Name | Rolle | Datum | Unterschrift |
| ---- | ----- | ----- | ------------ |
|      |       |       |              |
|      |       |       |              |