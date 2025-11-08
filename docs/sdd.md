# Spezifikationsgetriebene Entwicklung (SDD)

Spezifikationsgetriebene Softwareentwicklung (Spec-Driven Development, SDD) bedeutet, dass **formale oder semiformale Spezifikationen die Single Source of Truth** für den gesamten Lebenszyklus sind: Planung, Code, Tests, Dokumentation. Statt „Code first“ entsteht zuerst eine klare Beschreibung des gewünschten Verhaltens, gegen die alles Weitere abgeleitet oder validiert wird.

## Warum SDD?
- **Klarheit:** Fachliche und technische Anforderungen sind versieht.
- **Konsistenz:** Änderungen an der Spec propagieren über alle Artefakte hinweg.
- **Qualität:** Tests und Reviews können direkt gegen die Spezifikation arbeiten.

## Grundprinzipien
1. **„Die Spezifikation ist die Wahrheit“** – Implementierungen müssen sich daran messen lassen.
2. **Automatisierung** – Was sich aus der Spec ableiten lässt (Code-Stubs, API-Definitionen, Tests), wird automatisch generiert.
3. **Iterative Verfeinerung** – Anpassungen passieren zuerst auf Spec-Ebene und werden dann in Code übertragen.

## KI-gestützte SDD
Moderne KI-Modelle (z. B. Claude, Gemini, Grok) erweitern SDD:
- **Spec-Generierung:** Natürlichsprachliche Anforderungen werden in OpenAPI, JSON Schema, Datenmodelle usw. übersetzt.
- **„Chat with your Spec“:** Stakeholder können Lücken oder Konflikte durch Fragen aufdecken, bevor Code geschrieben wird.
- **Code- und Test-Generierung:** KI erzeugt Implementierungen, Testfälle und Dokumentation aus der Spec – über CRUD-Services bis hin zu UI-Komponenten.
- **Kontinuierliche Conformance-Checks:** Abweichungen zwischen Code und Spec lassen sich automatisiert erkennen.

## Beispiel-Workflow (SDD + KI)
1. **Anforderungsdialog:** Produktidee wird in natürlicher Sprache beschrieben.
2. **Spec-Entwurf:** KI erzeugt formalisierte Artefakte (z. B. OpenAPI, ER-Modelle, Checklisten).
3. **Review & Refinement:** Mensch und KI prüfen Konsistenz, Sicherheitsaspekte, Randfälle.
4. **Implementierung & Tests:** KI generiert Code/Tests; Entwickler validieren und ergänzen.
5. **Änderungen:** Anpassungen starten wieder in der Spec und propagieren automatisch in Code & Tests.

## Vorteile
- **Geschwindigkeit:** Von der Idee zum funktionsfähigen Code in Stunden statt Wochen.
- **Konsistenz:** KI vergisst keine Validierungen oder States, wendet Patterns gleichmäßig an.
- **Lebende Dokumentation:** Specs bleiben synchron mit dem System.
- **Niedrige Einstiegshürde:** Auch Nicht-Techniker können auf Spec-Ebene arbeiten.

## Herausforderungen
- **Spec-Qualität:** Schlechte oder widersprüchliche Anforderungen führen zu fehlerhaften Outputs.
- **Vertrauen & Kontrolle:** Entwickler müssen verstehen, was die KI erzeugt – Review bleibt Pflicht.
- **Balance der Abstraktion:** Spezifikationen dürfen weder zu vage noch zu detailliert sein.
- **Domänentraining:** KI benötigt Kontext oder Feintuning für spezielle Geschäftslogiken.

## Einsatzszenarien
- APIs und Mikroservices mit klaren Schnittstellen
- Business-Anwendungen (CRUD, Workflows, Reporting)
- Legacy-Modernisierung auf Basis extrahierter Specs
- MVPs und Prototyping, wenn schnelle Iterationen nötig sind

## Fazit
SDD verschiebt den Fokus vom „Wie“ zum „Was“. In Kombination mit KI werden Entwickler zu **Spezifikations-Ingenieuren**, die den fachlichen Rahmen definieren, während KI bei Umsetzung, Tests und Konsistenzprüfungen unterstützt. d-kit folgt exakt diesem Paradigma: Spezifikationen (Lasten-/Pflichtenheft, Task-Design, Checklisten) bilden die Grundlage; KI-Tools greifen darauf zu, um Code systematisch und reproducierbar zu generieren.
