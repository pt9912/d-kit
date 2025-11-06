# Checklist: End-to-End-Test Validierung

## 1. Voraussetzungen
- [ ] Testplan freigegeben (`test-strategie.md` referenziert)
- [ ] Kritische User-Journeys priorisiert und dokumentiert
- [ ] Abnahmekriterien pro Journey eindeutig definiert
- [ ] Testumgebung entspricht Produktionskonfiguration (Infra, Secrets, Feature Flags)
- [ ] Zugänge und Rollenberechtigungen eingerichtet

## 2. Testdaten & Fixtures
- [ ] Realistische Seed-Daten vorhanden / anonymisiert
- [ ] Testnutzer:innen inkl. Rollen angelegt
- [ ] Abhängigkeiten zu Drittsystemen simuliert oder stabil
- [ ] Rollback-Strategie bei Datenänderungen dokumentiert

## 3. Tooling & Automatisierung
- [ ] Test-Skripte aktuell (Versionierung geprüft)
- [ ] CI/CD-Integration konfiguriert
- [ ] Monitoring der Testläufe aktiviert (Logs, Screenshots, Videos)
- [ ] Metriken-Tracking (Durchlaufzeit, Erfolgsquote) eingerichtet

## 4. Testdurchführung
- [ ] Happy Path getestet und erfüllt Akzeptanzkriterien
- [ ] Negative Flows / Fehlerfälle abgedeckt
- [ ] Edge Cases (z. B. Grenzwerte, Timeouts) geprüft
- [ ] Parallelität und Race Conditions adressiert
- [ ] Cross-Browser / Cross-Device Szenarien (falls relevant) getestet

## 5. Qualitätssicherung
- [ ] Assertions für Performance (SLAs) vorhanden
- [ ] Security-relevante Pfade (Auth, Payments, Admin) validiert
- [ ] Accessibility Smoke-Test (WCAG 2.1 AA) ausgeführt
- [ ] Logs frei von schwerwiegenden Fehlern
- [ ] Alerts/Dashboards ohne neue Warnungen

## 6. Ergebnisdokumentation
- [ ] Testergebnisse im Report dokumentiert (Pass/Fail/Blocked)
- [ ] Ticket für gefundene Defekte erstellt inkl. Reproduktion
- [ ] Root Cause für Fehlgeschlagene Tests analysiert
- [ ] Stakeholder Review eingeplant / durchgeführt

## 7. Abschluss
- [ ] Regression-Tests erneut erfolgreich
- [ ] Freigabe durch QA / Product Owner erfolgt
- [ ] Release-Checkliste aktualisiert
- [ ] Lessons Learned in `references/learnings.md` ergänzt
- [ ] Automatisierte Tests in CI aktiviert (nicht nur lokal)
