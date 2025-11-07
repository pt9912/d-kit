# Beispiel: User Stories und Use-Cases im Lastenheft

Dieses Beispiel zeigt wie User Stories und Use-Cases im Lastenheft strukturiert werden.

## Projekt: Todo-App

### User Personas

#### Persona 1: Lisa Müller, Freelance Designerin
- **Alter**: 28 Jahre
- **Berufserfahrung**: 5 Jahre als selbstständige Designerin
- **IT-Kenntnisse**: Fortgeschritten (nutzt viele Tools)
- **Ziele**:
  - Projekte und Aufgaben effizient organisieren
  - Deadlines im Blick behalten
  - Prioritäten klar erkennen
- **Frustrationen**:
  - Aktuelle Todo-Listen (Papier/Excel) sind unübersichtlich
  - Vergisst wichtige Aufgaben
  - Schwer, zwischen Projekten zu wechseln
- **Typischer Arbeitstag**:
  - 2-3 Kundenprojekte parallel
  - 10-15 Aufgaben pro Tag
  - Arbeitet von Zuhause und Café
- **Motivation**: Produktiver werden, weniger Stress

#### Persona 2: Thomas Weber, Projektmanager
- **Alter**: 35 Jahre
- **Berufserfahrung**: 10 Jahre im Projektmanagement
- **IT-Kenntnisse**: Fortgeschritten
- **Ziele**:
  - Team-Aufgaben koordinieren
  - Überblick über alle Projekte
  - Fortschritt tracken
- **Frustrationen**:
  - Zu viele verschiedene Tools
  - Keine Transparenz über Team-Aufgaben
  - Status-Updates mühsam
- **Typischer Arbeitstag**:
  - 3-4 Projekte betreuen
  - 5-10 Team-Mitglieder koordinieren
  - 20-30 Aufgaben überblicken
- **Motivation**: Team effizienter machen, Zeit sparen

---

## User Stories

### Epic: Aufgabenverwaltung

#### US-001: Todo erstellen
**Als** Nutzer  
**möchte ich** eine neue Todo-Aufgabe erstellen  
**damit** ich nicht vergesse, was ich zu tun habe

**Acceptance-Kriterien**:
- [ ] Titel kann eingegeben werden (max 200 Zeichen)
- [ ] Optionale Beschreibung kann hinzugefügt werden
- [ ] Fälligkeitsdatum kann gesetzt werden
- [ ] Priorität kann gewählt werden (Hoch/Mittel/Niedrig)
- [ ] Kategorie/Tag kann zugewiesen werden
- [ ] Todo wird gespeichert und in Liste angezeigt
- [ ] Bestätigung wird angezeigt

**Priorität**: Must-Have  
**Geschätzter Aufwand**: 3 Story Points  
**Abhängigkeiten**: Keine

---

#### US-002: Todo als erledigt markieren
**Als** Nutzer  
**möchte ich** eine Todo-Aufgabe als erledigt markieren  
**damit** ich sehe, was ich schon geschafft habe

**Acceptance-Kriterien**:
- [ ] Checkbox bei Todo kann angeklickt werden
- [ ] Erledigte Todos werden durchgestrichen angezeigt
- [ ] Erledigte Todos können gefiltert werden (zeigen/verstecken)
- [ ] Erledigungszeitpunkt wird gespeichert
- [ ] Aktion kann rückgängig gemacht werden

**Priorität**: Must-Have  
**Geschätzter Aufwand**: 2 Story Points  
**Abhängigkeiten**: US-001

---

#### US-003: Todo bearbeiten
**Als** Nutzer  
**möchte ich** eine bestehende Todo-Aufgabe bearbeiten  
**damit** ich Änderungen vornehmen kann

**Acceptance-Kriterien**:
- [ ] Todo kann durch Klick geöffnet werden
- [ ] Alle Felder (Titel, Beschreibung, Datum, etc.) sind editierbar
- [ ] Änderungen können gespeichert werden
- [ ] Änderungen können verworfen werden (Abbrechen)
- [ ] Änderungsverlauf wird dokumentiert (optional für MVP)

**Priorität**: Must-Have  
**Geschätzter Aufwand**: 2 Story Points  
**Abhängigkeiten**: US-001

---

#### US-004: Todo löschen
**Als** Nutzer  
**möchte ich** eine Todo-Aufgabe löschen  
**damit** ich meine Liste aufgeräumt halte

**Acceptance-Kriterien**:
- [ ] Löschen-Button ist vorhanden
- [ ] Sicherheitsabfrage erscheint ("Wirklich löschen?")
- [ ] Nach Bestätigung wird Todo gelöscht
- [ ] Gelöschte Todos können wiederhergestellt werden (30 Tage Papierkorb)
- [ ] Feedback wird angezeigt ("Todo gelöscht")

**Priorität**: Must-Have  
**Geschätzter Aufwand**: 2 Story Points  
**Abhängigkeiten**: US-001

---

#### US-005: Todos filtern und sortieren
**Als** Nutzer  
**möchte ich** meine Todos filtern und sortieren  
**damit** ich schnell finde, was wichtig ist

**Acceptance-Kriterien**:
- [ ] Filter nach Priorität (Hoch/Mittel/Niedrig)
- [ ] Filter nach Status (Offen/Erledigt/Alle)
- [ ] Filter nach Kategorie/Tag
- [ ] Sortierung nach Fälligkeitsdatum
- [ ] Sortierung nach Priorität
- [ ] Sortierung nach Erstellungsdatum
- [ ] Filter und Sortierung kombinierbar

**Priorität**: Should-Have  
**Geschätzter Aufwand**: 5 Story Points  
**Abhängigkeiten**: US-001, US-002

---

### Epic: Kategorien & Organisation

#### US-010: Kategorien erstellen
**Als** Nutzer  
**möchte ich** Kategorien/Tags erstellen  
**damit** ich meine Todos organisieren kann

**Acceptance-Kriterien**:
- [ ] Neue Kategorie kann erstellt werden
- [ ] Kategorie-Name und -Farbe wählbar
- [ ] Kategorien können bearbeitet werden
- [ ] Kategorien können gelöscht werden (mit Warnung)
- [ ] Maximal 20 Kategorien

**Priorität**: Should-Have  
**Geschätzter Aufwand**: 3 Story Points  
**Abhängigkeiten**: US-001

---

### Epic: Authentifizierung

#### US-020: Registrierung
**Als** neuer Nutzer  
**möchte ich** mich registrieren  
**damit** ich die App nutzen kann

**Acceptance-Kriterien**:
- [ ] Email und Passwort können eingegeben werden
- [ ] Email-Validierung funktioniert
- [ ] Passwort muss mindestens 8 Zeichen haben
- [ ] Bestätigungs-Email wird gesendet
- [ ] Nach Bestätigung kann sich eingeloggt werden

**Priorität**: Must-Have  
**Geschätzter Aufwand**: 5 Story Points  
**Abhängigkeiten**: Keine

---

#### US-021: Login
**Als** registrierter Nutzer  
**möchte ich** mich einloggen  
**damit** ich auf meine Todos zugreifen kann

**Acceptance-Kriterien**:
- [ ] Email und Passwort können eingegeben werden
- [ ] Bei korrekten Daten wird eingeloggt
- [ ] Bei falschen Daten wird Fehler angezeigt
- [ ] "Passwort vergessen" Funktion vorhanden
- [ ] Session bleibt erhalten (Remember me)

**Priorität**: Must-Have  
**Geschätzter Aufwand**: 3 Story Points  
**Abhängigkeiten**: US-020

---

## User Stories - Priorisierung

### MVP (Must-Have):
```
Epic: Authentifizierung
├── US-020: Registrierung (5 SP)
└── US-021: Login (3 SP)

Epic: Aufgabenverwaltung
├── US-001: Todo erstellen (3 SP)
├── US-002: Todo als erledigt markieren (2 SP)
├── US-003: Todo bearbeiten (2 SP)
└── US-004: Todo löschen (2 SP)

Gesamt MVP: 17 Story Points
```

### Version 1.1 (Should-Have):
```
├── US-005: Todos filtern/sortieren (5 SP)
├── US-010: Kategorien erstellen (3 SP)
└── US-011: Kategorien zuweisen (2 SP)

Gesamt v1.1: 10 Story Points
```

---

## Use-Cases

### Use-Case 1: Todo erstellen

**Use-Case ID**: UC-001  
**Name**: Neue Todo-Aufgabe erstellen  
**Akteur**: Nutzer (Lisa)  
**Ziel**: Eine neue Aufgabe im System erfassen  
**Vorbedingung**: Nutzer ist eingeloggt  
**Nachbedingung Erfolg**: Todo ist gespeichert und in Liste sichtbar  
**Nachbedingung Fehler**: Todo nicht gespeichert, Fehlermeldung angezeigt

**Hauptszenario (Happy Path)**:
1. Nutzer klickt auf "+ Neue Aufgabe" Button
2. System zeigt Todo-Eingabeformular
3. Nutzer gibt Titel ein: "Kundenpräsentation vorbereiten"
4. System validiert Titel (nicht leer, max 200 Zeichen)
5. Nutzer fügt optionale Beschreibung hinzu
6. Nutzer wählt Fälligkeitsdatum: "Morgen, 15:00 Uhr"
7. Nutzer wählt Priorität: "Hoch"
8. Nutzer wählt Kategorie: "Arbeit"
9. Nutzer klickt "Speichern"
10. System validiert alle Eingaben
11. System speichert Todo in Datenbank
12. System vergibt eindeutige Todo-ID
13. System zeigt Todo in Liste (an oberster Stelle)
14. System zeigt Bestätigung: "Todo erfolgreich erstellt"
15. Formular wird geschlossen

**Alternative Szenarien**:

**A1: Nutzer bricht ab (bei Schritt 3-9)**
- Nutzer klickt "Abbrechen"
- System fragt: "Änderungen verwerfen?"
- Nutzer bestätigt
- System verwirft Eingaben
- System schließt Formular
- Kein Todo wird erstellt

**A2: Minimale Eingabe (bei Schritt 3)**
- Nutzer gibt nur Titel ein
- Nutzer klickt "Speichern"
- System setzt Default-Werte:
  - Priorität: Mittel
  - Kategorie: Keine
  - Fälligkeitsdatum: Keins
- Weiter bei Schritt 10

**A3: Datum in Vergangenheit (bei Schritt 6)**
- Nutzer wählt Datum in Vergangenheit
- System zeigt Warnung: "Datum liegt in der Vergangenheit"
- System fragt: "Trotzdem speichern?"
- Nutzer kann bestätigen oder Datum ändern

**Fehlerszenarien**:

**E1: Titel zu lang (bei Schritt 4)**
- Nutzer gibt Titel > 200 Zeichen ein
- System zeigt inline: "Maximal 200 Zeichen (aktuell: 215)"
- Titel-Feld wird rot markiert
- "Speichern" Button ist deaktiviert
- Nutzer muss Titel kürzen

**E2: Netzwerkfehler beim Speichern (bei Schritt 11)**
- System kann nicht speichern (Verbindung verloren)
- System zeigt: "Verbindungsfehler. Todo konnte nicht gespeichert werden"
- System bietet: "Erneut versuchen" oder "Als Entwurf speichern"
- Eingaben bleiben erhalten in Formular

**E3: Server-Error (bei Schritt 11)**
- Datenbank nicht erreichbar
- System zeigt: "Ein Fehler ist aufgetreten. Bitte später versuchen"
- System loggt Error für Debugging
- Nutzer kann es später erneut versuchen

**Spezielle Anforderungen**:
- **Performance**: Formular öffnet in < 300ms
- **Usability**: Autofokus auf Titel-Feld
- **Usability**: Enter-Taste speichert (wenn Validierung OK)
- **Accessibility**: Keyboard-Navigation vollständig möglich
- **Accessibility**: Screen-Reader kompatibel

**Häufigkeit**: 5-10 mal pro Tag pro Nutzer  
**UI-Mockup**: Siehe Anhang A  
**Zugehörige User Story**: US-001

---

### Use-Case 2: Todo als erledigt markieren

**Use-Case ID**: UC-002  
**Name**: Todo als erledigt markieren  
**Akteur**: Nutzer (Lisa)  
**Ziel**: Erledigte Aufgabe abhaken

**Hauptszenario**:
1. Nutzer sieht Todo-Liste mit offenen Aufgaben
2. Nutzer findet Todo: "Kundenpräsentation vorbereiten"
3. Nutzer klickt auf Checkbox neben Todo
4. System markiert Todo als erledigt:
   - Checkbox wird gefüllt ✓
   - Text wird durchgestrichen
   - Todo wird grau (oder anderer visueller Effekt)
5. System speichert Erledigungszeitpunkt in Datenbank
6. System aktualisiert Statistik (z.B. "3 von 10 erledigt")
7. System zeigt kurzes Feedback (z.B. Animation oder Toast)

**Alternative Szenarien**:

**A1: Versehentlich geklickt**
- Nutzer klickt erneut auf Checkbox
- System markiert Todo als "nicht erledigt"
- Durchstreichung wird entfernt
- Todo erscheint wieder normal

**A2: Todo automatisch verschieben**
- Wenn Option "Erledigte ausblenden" aktiv:
  - Todo verschwindet nach 2 Sekunden aus Liste
  - Oder rutscht ans Ende der Liste
- System zeigt "Rückgängig" Option für 5 Sekunden

**Spezielle Anforderungen**:
- **Performance**: Sofortige visuelle Reaktion (< 100ms)
- **Offline**: Funktioniert auch offline, sync später
- **Undo**: "Rückgängig" möglich innerhalb 5 Sekunden

**Häufigkeit**: 10-20 mal pro Tag pro Nutzer  
**Zugehörige User Story**: US-002

---

## Use-Case Diagramm

```
                    +-------------------+
                    |    Todo-App       |
                    +-------------------+
                            |
          +-----------------+------------------+
          |                                    |
    [Lisa - Freelancer]                 [Thomas - PM]
          |                                    |
          |-- UC-001: Todo erstellen          |-- UC-001: Todo erstellen
          |-- UC-002: Todo abhaken            |-- UC-002: Todo abhaken
          |-- UC-003: Todo bearbeiten         |-- UC-003: Todo bearbeiten
          |-- UC-004: Todo löschen            |-- UC-004: Todo löschen
          |-- UC-005: Todos filtern           |-- UC-005: Todos filtern
          |                                    |-- UC-015: Team-Todos teilen*
          |                                    |-- UC-016: Fortschritt sehen*
          |                                    |
          +------------------------------------+
                            |
                            |-- UC-020: Registrierung
                            |-- UC-021: Login

* Für spätere Version geplant
```

---

## Traceability Matrix

| User Story | Use-Case | Funktionale Anforderungen | Priorität   | Aufwand | Status |
| ---------- | -------- | ------------------------- | ----------- | ------- | ------ |
| US-001     | UC-001   | FA-001, FA-002, FA-003    | Must-Have   | 3 SP    | [ ]    |
| US-002     | UC-002   | FA-004                    | Must-Have   | 2 SP    | [ ]    |
| US-003     | UC-003   | FA-005, FA-001            | Must-Have   | 2 SP    | [ ]    |
| US-004     | UC-004   | FA-006                    | Must-Have   | 2 SP    | [ ]    |
| US-005     | UC-005   | FA-007, FA-008            | Should-Have | 5 SP    | [ ]    |
| US-010     | UC-010   | FA-010, FA-011            | Should-Have | 3 SP    | [ ]    |
| US-020     | UC-020   | FA-020, FA-021, FA-022    | Must-Have   | 5 SP    | [ ]    |
| US-021     | UC-021   | FA-023, FA-024            | Must-Have   | 3 SP    | [ ]    |

**Gesamt MVP**: 17 Story Points (6 User Stories, 6 Use-Cases, 15 Anforderungen)

---

## Abhängigkeiten-Graph

```
US-020 (Registrierung)
    └── US-021 (Login)
            └── US-001 (Todo erstellen)
                    ├── US-002 (Todo abhaken)
                    ├── US-003 (Todo bearbeiten)
                    │       └── US-005 (Filtern)
                    ├── US-004 (Todo löschen)
                    └── US-010 (Kategorien)
                            └── US-011 (Kategorien zuweisen)
```

**Implementierungs-Reihenfolge für MVP**:
1. US-020, US-021 (Authentifizierung) - Sprint 1
2. US-001 (Todo erstellen) - Sprint 1
3. US-002, US-003, US-004 (CRUD Operations) - Sprint 2
4. Testing & Bugfixing - Sprint 3

---

## Nutzen dieser Struktur

### Für Entwickler:
- ✅ Klare User-Perspektive durch User Stories
- ✅ Detaillierte Abläufe durch Use-Cases
- ✅ Testbare Acceptance-Kriterien
- ✅ Abhängigkeiten sind klar

### Für Product Owner:
- ✅ Priorisierung nach Business-Value
- ✅ Aufwands-Schätzungen transparent
- ✅ Progress trackbar durch Traceability Matrix

### Für Tester:
- ✅ Test-Cases leiten sich direkt von Use-Cases ab
- ✅ Alternative Szenarien sind dokumentiert
- ✅ Fehlerszenarien sind beschrieben

### Für Stakeholder:
- ✅ User Personas machen Zielgruppe greifbar
- ✅ User Stories in Business-Sprache
- ✅ Use-Cases zeigen konkrete Nutzung