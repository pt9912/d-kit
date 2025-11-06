# Prompt-Template: Architektur-Dokument

## Kontext
Du bist ein Software-Architekt und erstellst ein Architektur-Dokument basierend auf dem Pflichtenheft.

## Aufgabe
Erstelle ein detailliertes Architektur-Dokument für:

[PFLICHTENHEFT HIER EINFÜGEN]

## Struktur des Architektur-Dokuments

### 1. Executive Summary
- Überblick über die gewählte Architektur
- Hauptkomponenten
- Wichtigste Designentscheidungen

### 2. Architektur-Übersicht

#### 2.1 Architekturstil
- Gewählter Architekturstil (z.B. Microservices, Monolith, Serverless)
- Begründung der Wahl

#### 2.2 High-Level Architektur-Diagramm
```
[ASCII-Diagramm der Hauptkomponenten und deren Beziehungen]
```

### 3. Komponenten-Beschreibung

Für jede Hauptkomponente:

#### 3.X [Komponenten-Name]
- **Zweck**: Welche Aufgabe erfüllt die Komponente
- **Verantwortlichkeiten**: Was macht die Komponente
- **Technologie-Stack**: Verwendete Frameworks/Libraries
- **Schnittstellen**: APIs, Events, Datenformate
- **Datenhaltung**: Welche Daten werden gespeichert
- **Abhängigkeiten**: Andere Komponenten, externe Services

### 4. Technologie-Stack

#### 4.1 Frontend
- Framework/Library (z.B. React, Vue, Angular)
- State Management
- UI-Komponenten
- Build-Tools

#### 4.2 Backend
- Programmiersprache
- Framework (z.B. Express, Django, Spring Boot)
- API-Typ (REST, GraphQL, gRPC)
- Authentication/Authorization

#### 4.3 Datenbank
- Typ (SQL/NoSQL)
- Spezifisches DBMS (PostgreSQL, MongoDB, etc.)
- ORM/ODM
- Migration-Strategie

#### 4.4 Infrastructure
- Cloud-Provider (AWS, Azure, GCP) oder On-Premise
- Container-Orchestrierung (Kubernetes, Docker Swarm)
- CI/CD Tools
- Monitoring & Logging

### 5. Datenmodell

#### 5.1 Entities
Für jede wichtige Entity:
```
Entity: [Name]
Attributes:
  - [attribute1]: [type] - [description]
  - [attribute2]: [type] - [description]
Relationships:
  - [relationship to other entities]
```

#### 5.2 Datenfluss
- Wie fließen Daten durch das System
- Transformationen
- Caching-Strategie

### 6. API-Design

#### 6.1 REST Endpoints (falls REST)
```
GET    /api/resource         - List resources
POST   /api/resource         - Create resource
GET    /api/resource/:id     - Get specific resource
PUT    /api/resource/:id     - Update resource
DELETE /api/resource/:id     - Delete resource
```

#### 6.2 Request/Response Formats
```json
{
  "example": "request/response structure"
}
```

### 7. Sicherheitsarchitektur

#### 7.1 Authentication
- Mechanismus (JWT, OAuth, Session-based)
- Token-Management

#### 7.2 Authorization
- Role-based access control (RBAC)
- Permissions-Model

#### 7.3 Data Protection
- Verschlüsselung at-rest
- Verschlüsselung in-transit
- PII-Handling

### 8. Deployment-Architektur

#### 8.1 Environments
- Development
- Staging
- Production

#### 8.2 Deployment-Pipeline
```
Code → Build → Test → Deploy
```

#### 8.3 Skalierung
- Horizontal Scaling
- Vertical Scaling
- Auto-Scaling Trigger

### 9. Monitoring & Observability

#### 9.1 Logging
- Logging-Framework
- Log-Aggregation
- Log-Levels

#### 9.2 Metrics
- Application Metrics
- Infrastructure Metrics
- Business Metrics

#### 9.3 Alerting
- Alert-Kriterien
- Notification-Channels

### 10. Architektur-Entscheidungen (ADRs)

Für jede wichtige Designentscheidung:

#### ADR-XXX: [Titel der Entscheidung]
- **Status**: Accepted/Proposed/Deprecated
- **Kontext**: Warum musste eine Entscheidung getroffen werden
- **Entscheidung**: Was wurde entschieden
- **Alternativen**: Welche Optionen wurden erwogen
- **Konsequenzen**: Positive und negative Auswirkungen
- **Begründung**: Warum diese Option gewählt wurde

### 11. Risiken & Mitigations
- Technische Risiken
- Skalierbarkeits-Risiken
- Security-Risiken
- Mitigation-Strategien

### 12. Offene Fragen
- Ungelöste architektonische Fragen
- Benötigte weitere Informationen

## Wichtige Hinweise
- Architektur muss die nicht-funktionalen Anforderungen erfüllen
- Designentscheidungen begründen
- Trade-offs transparent machen
- Bei Unsicherheiten mehrere Optionen präsentieren
- Diagramme in ASCII-Art oder als Mermaid-Code
