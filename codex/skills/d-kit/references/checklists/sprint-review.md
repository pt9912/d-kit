# Sprint-Review Checklist

## Sprint-Information
- **Sprint**: [Nummer/Name]
- **Zeitraum**: [Start-Datum] bis [End-Datum]
- **Sprint-Ziel**: [Ziel des Sprints]
- **Review-Datum**: [YYYY-MM-DD]
- **Teilnehmer**: [Liste der Anwesenden]

---

## 1. Sprint-Ziel Review

### 1.1 Wurde das Sprint-Ziel erreicht?
- [ ] ✅ Vollständig erreicht
- [ ] ⚠️ Teilweise erreicht
- [ ] ❌ Nicht erreicht

**Kommentar**:
[Erklärung]

---

## 2. Task-Completion

### 2.1 Alle geplanten Tasks
| Task-ID | Titel | Status | Completion |
|---------|-------|--------|------------|
| TASK-001 | [Name] | ✅ Done | 100% |
| TASK-002 | [Name] | ⚠️ In Progress | 80% |
| TASK-003 | [Name] | 🔴 Blocked | 20% |

### 2.2 Task-Completion Rate
- Geplante Tasks: [X]
- Abgeschlossene Tasks: [Y]
- **Completion Rate**: [Y/X * 100]%

**Ziel**: >80% Completion Rate

---

## 3. Funktionale Anforderungen

### 3.1 Implementierte Features
- [ ] Feature 1: [Name] - Functional ✅
- [ ] Feature 2: [Name] - Functional ✅
- [ ] Feature 3: [Name] - Partial ⚠️

### 3.2 Acceptance-Kriterien
Für jedes implementierte Feature:

#### Feature: [Name]
- [ ] Kriterium 1: Erfüllt
- [ ] Kriterium 2: Erfüllt
- [ ] Kriterium 3: Nicht erfüllt (Grund: ...)

---

## 4. Technische Qualität

### 4.1 Code-Qualität
- [ ] Code-Review durchgeführt für alle Tasks
- [ ] Keine offenen Code-Review-Kommentare
- [ ] Code-Standards eingehalten
- [ ] Refactoring durchgeführt wo nötig

### 4.2 Testing
- [ ] Unit-Tests geschrieben für alle neuen Funktionen
- [ ] Unit-Tests erfolgreich (100% pass rate)
- [ ] Integration-Tests durchgeführt
- [ ] Test-Coverage: [X]% (Ziel: >80%)

**Coverage-Details**:
- Gesamt Coverage: [X]%
- Frontend Coverage: [X]%
- Backend Coverage: [X]%
- Critical Paths Coverage: [X]%

### 4.3 Code-Analyse
- [ ] Keine kritischen Linting-Fehler
- [ ] Keine Syntax-Fehler
- [ ] Keine Security-Warnings (High/Critical)
- [ ] Code-Analysis-Report reviewed

**Issues gefunden**:
- Kritisch: [Anzahl]
- Hoch: [Anzahl]
- Mittel: [Anzahl]
- Niedrig: [Anzahl]

---

## 5. Integration

### 5.1 System-Integration
- [ ] Alle neuen Features integriert
- [ ] Keine Merge-Konflikte
- [ ] Integration-Tests erfolgreich
- [ ] Keine Regressions-Bugs

### 5.2 Datenbank-Migration
- [ ] Migrations-Scripts getestet
- [ ] Rollback-Strategie vorhanden
- [ ] Migration auf Dev erfolgreich
- [ ] Migration auf Staging erfolgreich

---

## 6. Dokumentation

### 6.1 Code-Dokumentation
- [ ] JSDoc/Docstrings für neue Public APIs
- [ ] README aktualisiert
- [ ] CHANGELOG aktualisiert
- [ ] API-Dokumentation aktualisiert (falls relevant)

### 6.2 User-Dokumentation
- [ ] User-Guide aktualisiert (falls relevant)
- [ ] Release-Notes vorbereitet
- [ ] Known Issues dokumentiert

---

## 7. Demo

### 7.1 Demo-Vorbereitung
- [ ] Demo-Environment vorbereitet
- [ ] Test-Daten verfügbar
- [ ] Demo-Script erstellt
- [ ] Demo-Account eingerichtet

### 7.2 Demo-Durchführung
**Demonstrierte Features**:
1. [Feature 1]: [Kurze Beschreibung der Demo]
2. [Feature 2]: [Kurze Beschreibung der Demo]
3. [Feature 3]: [Kurze Beschreibung der Demo]

**Feedback aus Demo**:
- [Positives Feedback 1]
- [Positives Feedback 2]
- [Verbesserungsvorschlag 1]
- [Verbesserungsvorschlag 2]

---

## 8. Bugs & Issues

### 8.1 Neue Bugs (während Sprint entdeckt)
| Bug-ID | Titel | Severity | Status | Assignee |
|--------|-------|----------|--------|----------|
| BUG-001 | [Beschreibung] | High | Fixed | [Name] |
| BUG-002 | [Beschreibung] | Medium | Open | [Name] |

### 8.2 Offene Bugs
- Critical: [Anzahl]
- High: [Anzahl]
- Medium: [Anzahl]
- Low: [Anzahl]

**Action Items**:
- [ ] Critical Bugs müssen vor Release gefixt werden
- [ ] High-Priority Bugs für nächsten Sprint einplanen

---

## 9. Performance & Skalierung

### 9.1 Performance-Metrics
- [ ] Response-Zeiten gemessen
- [ ] Performance-Anforderungen erfüllt
- [ ] Keine Performance-Regressions

**Messungen**:
- API Response Time (avg): [X]ms (Ziel: <500ms)
- Page Load Time (avg): [X]s (Ziel: <2s)
- Database Query Time (avg): [X]ms (Ziel: <100ms)

### 9.2 Last-Tests (falls durchgeführt)
- [ ] Load-Tests durchgeführt
- [ ] System stabil unter Last
- [ ] Skalierungs-Strategie funktioniert

---

## 10. Deployment & Release

### 10.1 Deployment-Readiness
- [ ] Code auf Staging deployed
- [ ] Staging-Tests erfolgreich
- [ ] Rollback-Plan vorhanden
- [ ] Deployment-Dokumentation aktuell

### 10.2 Release-Kriterien
- [ ] Alle Must-Have Features implementiert
- [ ] Keine offenen Critical/High Bugs
- [ ] Test-Coverage > 80%
- [ ] Performance-Anforderungen erfüllt
- [ ] Security-Review durchgeführt
- [ ] Dokumentation vollständig

**Release-Status**:
- [ ] ✅ Ready for Production
- [ ] ⚠️ Ready with minor issues
- [ ] ❌ Not ready (Blocker: ...)

---

## 11. Metrics & KPIs

### 11.1 Sprint-Velocity
- Geplante Story Points: [X]
- Completed Story Points: [Y]
- **Velocity**: [Y] SP

### 11.2 Sprint-Burndown
- Verlief gemäß Plan: [ ] Ja [ ] Nein
- Falls Nein, Grund: [Erklärung]

### 11.3 Team-Capacity
- Geplante Verfügbarkeit: [X] Personentage
- Tatsächliche Verfügbarkeit: [Y] Personentage
- Abweichung: [Y-X] Tage

---

## 12. Stakeholder-Feedback

### 12.1 Feedback vom Product Owner
[Kommentare und Bewertung]

### 12.2 Feedback von Usern (falls vorhanden)
[Kommentare aus User-Testing]

### 12.3 Feedback vom Team
[Kommentare zur Sprint-Durchführung]

---

## 13. Action Items für nächsten Sprint

### 13.1 Carry-Over Tasks
- [ ] TASK-XXX: [Grund warum nicht fertig]
- [ ] TASK-XXX: [Grund warum nicht fertig]

### 13.2 Bug-Fixes
- [ ] BUG-XXX: [Priorität]
- [ ] BUG-XXX: [Priorität]

### 13.3 Technical Debt
- [ ] Refactoring: [Beschreibung]
- [ ] Performance-Optimierung: [Beschreibung]

### 13.4 Verbesserungen
- [ ] [Verbesserungsmaßnahme aus Retrospektive]
- [ ] [Verbesserungsmaßnahme aus Retrospektive]

---

## 14. Gesamt-Bewertung

### 14.1 Sprint-Erfolg
**Rating**: [1-5 Sterne] ⭐⭐⭐⭐⭐

**Begründung**:
[Zusammenfassung des Sprint-Erfolgs]

### 14.2 Haupterfolge
1. [Erfolg 1]
2. [Erfolg 2]
3. [Erfolg 3]

### 14.3 Hauptherausforderungen
1. [Herausforderung 1]
2. [Herausforderung 2]

### 14.4 Learnings
1. [Learning 1]
2. [Learning 2]

---

## Unterschriften

| Name | Rolle | Datum | Unterschrift |
|------|-------|-------|--------------|
| | Product Owner | | |
| | Tech Lead | | |
| | QA Lead | | |

---

**Nächstes Review**: [Datum des nächsten Sprint-Reviews]
