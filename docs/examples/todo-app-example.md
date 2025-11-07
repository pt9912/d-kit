# Beispiel: Todo-App mit d-kit entwickeln

Dieses Beispiel zeigt, wie Sie mit d-kit eine vollständige Todo-App entwickeln.

## 🎯 Projektziel

Eine webbasierte Todo-App mit:
- Benutzer-Authentifizierung
- Todo-Verwaltung (CRUD)
- Kategorien und Tags
- Responsive Design

## 📋 Phase 1: Anforderungsanalyse

### Schritt 1: Mit d-kit starten

```
User: "Ich möchte eine Todo-App mit KI entwickeln. Die App soll 
Benutzer-Login, Todo-Verwaltung und Kategorien haben."

Claude: "Großartig! Ich nutze den d-kit Skill für strukturierte 
Entwicklung. Lass uns mit einem Lastenheft beginnen. Ich habe 
einige Fragen..."
```

### Schritt 2: Lastenheft erstellen

Claude nutzt das Template `claude/skill/references/templates/lastenheft.md` und fragt:

**Zielgruppe:**
- Wer nutzt die App? → Privatpersonen, Alter 18-65
- Wie viele Nutzer? → Start mit 100-500

**Funktionen:**
- Was sind Must-Have Features? → Login, Todos erstellen/bearbeiten/löschen
- Was ist Nice-to-Have? → Tags, Teilen mit anderen Usern

**Technik:**
- Web oder Mobile? → Web (responsive)
- Gibt es bestehende Systeme? → Nein, Neustart

**Output:**
```markdown
# Lastenheft: Todo-App

## 1. Ausgangssituation
Nutzer verwalten ihre Aufgaben derzeit in verschiedenen Tools 
(Notizen-Apps, Excel, Papier), was zu:
- Unübersichtlichkeit führt
- Wichtige Aufgaben vergessen werden
- Keine Priorisierung möglich ist

## 2. Zielsetzung
Entwicklung einer webbasierten Todo-App, die einfach und 
intuitiv zu bedienen ist...

[vollständiges Lastenheft]
```

### Schritt 3: Pflichtenheft generieren

```
Claude: "Basierend auf dem Lastenheft erstelle ich nun ein 
Pflichtenheft mit detaillierten Anforderungen..."
```

Claude nutzt `claude/skill/references/prompts/pflichtenheft.md`:

**Output:**
```markdown
# Pflichtenheft: Todo-App

## 2. Funktionale Anforderungen

### FA-001: Benutzerregistrierung
- **Beschreibung**: Neuer Nutzer kann Account erstellen
- **Priorität**: Must-Have
- **Acceptance-Kriterien**:
  - [ ] Email und Passwort können eingegeben werden
  - [ ] Email-Validierung funktioniert
  - [ ] Passwort min. 8 Zeichen
  - [ ] Bestätigungs-Email wird versendet
- **Abhängigkeiten**: Keine

[weitere Anforderungen...]

## 3. Nicht-funktionale Anforderungen

### 3.1 Performance
- Response-Zeit < 500ms für CRUD-Operationen
- Seitenaufbau < 2 Sekunden

[vollständiges Pflichtenheft]
```

### Schritt 4: Architektur-Dokument

```
Claude: "Jetzt erstelle ich das Architektur-Dokument..."
```

Claude nutzt `claude/skill/references/prompts/architektur.md`:

**Output:**
```markdown
# Architektur-Dokument: Todo-App

## 2. Architektur-Übersicht

### 2.1 Architekturstil
Monolithic Web Application mit klarer 3-Tier-Architektur

### 2.2 High-Level Diagramm
```
┌─────────────┐
│   Browser   │
└──────┬──────┘
       │ HTTPS
┌──────▼──────────────────┐
│   Frontend (React)      │
└──────┬──────────────────┘
       │ REST API
┌──────▼──────────────────┐
│   Backend (Node.js)     │
│   - Express             │
│   - JWT Auth            │
└──────┬──────────────────┘
       │
┌──────▼──────────────────┐
│   Database (PostgreSQL) │
└─────────────────────────┘
```

## 4. Technologie-Stack

### 4.1 Frontend
- React 18
- TypeScript
- Tailwind CSS
- React Router
- Axios

### 4.2 Backend
- Node.js 20
- Express
- JWT für Authentication
- bcrypt für Password-Hashing

[vollständiges Architektur-Dokument]
```

### ✓ Review-Checkpoint 1

```
Claude: "Bitte reviewen Sie:

1. Pflichtenheft:
   - Sind alle Anforderungen vollständig?
   - Sind die Prioritäten richtig?

2. Architektur:
   - Ist der Tech-Stack angemessen?
   - Gibt es Bedenken?

Feedback?"
```

**User:** "Sieht gut aus! PostgreSQL ist OK, go ahead."

## 📋 Phase 2: Planung

### Schritt 5: MVP-Plan

```
Claude: "Erstelle MVP-Plan..."
```

Claude nutzt `claude/skill/references/prompts/mvp-plan.md`:

**Output:**
```markdown
# MVP-Plan: Todo-App

## 2. Feature-Priorisierung (MoSCoW)

### Must-Have Features (MVP)
1. **MVP-M-001: User Registration & Login**
   - User Story: Als Nutzer möchte ich mich registrieren 
     und anmelden können
   - Aufwand: Medium (3 SP)
   - Dependencies: Keine

2. **MVP-M-002: Todo CRUD Operations**
   - User Story: Als Nutzer möchte ich Todos erstellen, 
     bearbeiten, und löschen können
   - Aufwand: Large (5 SP)
   - Dependencies: MVP-M-001

3. **MVP-M-003: Todo-Status Management**
   - User Story: Als Nutzer möchte ich Todos als 
     erledigt markieren können
   - Aufwand: Small (2 SP)
   - Dependencies: MVP-M-002

[weitere Features...]

## 5. Technische Meilensteine

### Milestone 1: Authentication (Woche 1-2)
- Ziel: User kann sich registrieren und einloggen
- Features: MVP-M-001
- Definition of Done:
  - [ ] Registration funktioniert
  - [ ] Login funktioniert
  - [ ] JWT-Tokens werden erstellt
  - [ ] Protected Routes funktionieren
```

### Schritt 6: Test-Strategie

Claude nutzt `claude/skill/references/prompts/test-strategie.md`:

**Output** (Auszug):
```markdown
# Test-Strategie: Todo-App

## 2. Unit-Testing-Strategie

### 2.1 Coverage-Ziele
- Minimum: 80% Code Coverage
- Backend API Functions: 90%
- Frontend Components: 80%

### 2.2 Frameworks
- Frontend: Jest + React Testing Library
- Backend: Jest + Supertest

## 3. Integration-Testing

### 3.1 API-Tests
```typescript
describe('POST /api/todos', () => {
  test('should create todo when authenticated', async () => {
    const response = await request(app)
      .post('/api/todos')
      .set('Authorization', `Bearer ${token}`)
      .send({ title: 'Test Todo', description: 'Test' });
    
    expect(response.status).toBe(201);
    expect(response.body.title).toBe('Test Todo');
  });
  
  test('should return 401 when not authenticated', async () => {
    // ...
  });
});
```
[weitere Test-Spezifikationen...]
```

### Schritt 7: Sprint-Plan

Claude nutzt `claude/skill/references/prompts/sprint-plan.md`:

**Output:**
```markdown
# Sprint-Plan: Sprint 1 (Todo-App)

## 1. Sprint-Ziel
Authentication-System implementieren: User kann sich 
registrieren und einloggen.

## 3. Task-Liste

### Task 1: Backend - User Model & Database Setup
```
ID: TASK-001
Beschreibung: PostgreSQL-Schema und User-Model erstellen

Acceptance-Kriterien:
  - [ ] Database-Schema erstellt
  - [ ] User-Model mit Validierung
  - [ ] Migrations-Scripts vorhanden
  - [ ] Unit-Tests für Model

Technische Details:
  - Komponente: Backend / Models
  - Dateien: 
    - models/User.js
    - migrations/001_create_users.sql
  - Dependencies: Keine

Aufwand: 4 Stunden
Priorität: High
```

[weitere Tasks: Backend API, Frontend Components, Integration]
```

### ✓ Review-Checkpoint 2

```
Claude: "Sprint-Plan Review:
- 4 Tasks definiert
- Aufwand: 16 Stunden (2 Arbeitstage)
- Alle Tasks haben klare Acceptance-Kriterien

Bereit für Implementation?"
```

**User:** "Ja, let's go!"

## 📋 Phase 3: Iterative Entwicklung

### Task 1: User Model & Database

#### Schritt 8: Design-Dokument erstellen

```
User: "Erstelle Design-Dokument für TASK-001"

Claude: [nutzt claude/skill/references/prompts/task-design.md]
```

**Output** (Auszug):
```markdown
# Task-Design: User Model & Database Setup

## 1. Task-Übersicht
- **Task-ID**: TASK-001
- **Titel**: User Model & Database Setup
- **Ziel**: PostgreSQL Schema und User-Model mit Validierung

## 4. Datenmodell-Änderungen

### 4.1 Schema-Änderungen
```sql
-- Migration: 001_create_users.sql

CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  name VARCHAR(100) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_users_email ON users(email);
```

### 4.2 Model Interface
```typescript
interface User {
  id: string;
  email: string;
  passwordHash: string;
  name: string;
  createdAt: Date;
  updatedAt: Date;
}

interface CreateUserDto {
  email: string;
  password: string;
  name: string;
}
```

## 5. Business-Logik

### 5.1 Validation Rules
- Email: Valid email format, unique
- Password: Min 8 characters, 1 uppercase, 1 number
- Name: 2-100 characters, no special chars

### 5.2 Error Handling
```typescript
class ValidationError extends Error {
  constructor(message: string, field: string) {
    super(message);
    this.name = 'ValidationError';
    this.field = field;
  }
}
```

## 8. Test-Cases

### 8.1 Unit-Tests
```typescript
describe('User Model', () => {
  test('should create user with valid data', async () => {
    const user = await User.create({
      email: 'test@example.com',
      password: 'SecurePass123',
      name: 'Test User'
    });
    expect(user.id).toBeDefined();
    expect(user.email).toBe('test@example.com');
  });
  
  test('should hash password before saving', async () => {
    const user = await User.create({
      email: 'test@example.com',
      password: 'SecurePass123',
      name: 'Test User'
    });
    expect(user.passwordHash).not.toBe('SecurePass123');
    expect(user.passwordHash).toMatch(/^\$2[aby]\$/);
  });
  
  test('should throw error for invalid email', async () => {
    await expect(User.create({
      email: 'invalid-email',
      password: 'SecurePass123',
      name: 'Test'
    })).rejects.toThrow(ValidationError);
  });
  
  test('should throw error for duplicate email', async () => {
    // ...
  });
});
```

[vollständiges Design-Dokument...]
```

#### Schritt 9: Design Review

```
Claude: [nutzt claude/skill/references/prompts/design-review.md]
       [führt automatisches Review durch]

✓ Vollständigkeit: Alle Elemente vorhanden
✓ Architektur-Konsistenz: PostgreSQL wie geplant
✓ Requirements-Coverage: FA-001 adressiert
✓ Datenmodell-Qualität: Normalisiert, Indizes vorhanden
✓ Security: Password-Hashing mit bcrypt
✓ Test-Coverage: Happy Path, Edge Cases, Error Cases

Status: ✅ APPROVED - Bereit für Implementation
```

#### Schritt 10-11: Code & Tests generieren

```
User: "Generiere Code für TASK-001"

Claude: [nutzt claude/skill/references/prompts/code-generation.md]
```

**Generierte Dateien:**

1. `migrations/001_create_users.sql`
2. `models/User.js`
3. `tests/models/User.test.js`

#### Schritt 12: Code-Analyse

```
Claude: [führt automatisch aus: scripts/code_analysis.py]

🐍 Analyzing files...
  ✅ models/User.js: Syntax OK
  ✅ No linting issues
  ✅ No security issues

═══════════════════════════════════
CODE ANALYSIS REPORT
═══════════════════════════════════
Total Issues Found: 0
✅ All checks passed!
```

#### Schritt 13: Tests ausführen

```
Claude: [führt aus: scripts/run_tests.py]

🐍 Running tests...
  ✅ User Model - create user with valid data
  ✅ User Model - hash password
  ✅ User Model - validate email
  ✅ User Model - reject duplicate email
  ✅ User Model - validate password strength

═══════════════════════════════════
TEST REPORT
═══════════════════════════════════
Tests Run: 12
Tests Passed: 12 ✅
Tests Failed: 0 ❌
Code Coverage: 94.2%

✅ Coverage target met (≥80%)
✅ All checks passed! Ready for deployment.
```

#### ✓ Task-Completion

```
Claude: "TASK-001 ist abgeschlossen:
✅ Code generiert und reviewed
✅ Alle Tests erfolgreich (12/12)
✅ Coverage: 94.2% (Ziel: 80%)
✅ Keine Security-Issues

Bereit für nächste Task!"
```

### [Tasks 2-4 analog...]

## 📋 Phase 4: Sprint-Abschluss

### Sprint-Review

```
Claude: [nutzt claude/skill/references/checklists/sprint-review.md]

Sprint-Review Sprint 1:
✅ Sprint-Ziel erreicht: Authentication-System funktioniert
✅ Alle 4 Tasks abgeschlossen
✅ Test-Coverage: 91.3% (Ziel: >80%)
✅ Keine kritischen Bugs
✅ Demo-fähiger Stand vorhanden

Demo:
1. User-Registration ✅
2. Email-Validation ✅
3. Login mit JWT ✅
4. Protected Routes ✅
```

### Sprint-Retrospektive

```
Claude: [nutzt claude/skill/references/templates/retrospektive.md]

Was lief gut:
- Design-Review hat 2 Sicherheitslücken verhindert
- Test-First Approach funktionierte gut
- Code-Quality durchgehend hoch

Was lief schlecht:
- Email-Validation-Prompt musste 2x angepasst werden
- Password-Hashing-Tests fehlschlugen initial

Verbesserungen:
- Email-Validation-Prompt optimiert
- Learnings dokumentiert in claude/skill/references/learnings.md

Action Items für Sprint 2:
- Security-Best-Practices-Prompt erweitern
- Test-Generation-Prompt präzisieren
```

## 📋 Phasen 5: MVP-Abschluss

Nach 4-5 Sprints:

```
Claude: [nutzt claude/skill/references/checklists/e2e-tests.md]

E2E-Tests:
✅ Complete User Journey: Register → Login → Create Todos → Logout
✅ Performance: Response times < 500ms
✅ Security: No vulnerabilities found
✅ All Must-Have Features implemented

🚀 Todo-App ist Release-Ready!
```

## 📊 Projekt-Ergebnis

**Zeitaufwand:**
- Ohne d-kit geschätzt: ~40 Stunden
- Mit d-kit tatsächlich: ~22 Stunden
- **Ersparnis: 45%**

**Qualität:**
- Test-Coverage: 91% (Ziel: 80%)
- Bugs in Production: 0 (erste Woche)
- Code-Quality: A (SonarQube)

**Learnings:**
- Design-Review-Checkpoint hat 3 Architekturfehler verhindert
- Test-First-Approach reduzierte Bugs um 60%
- Prompt-Templates sorgten für konsistenten Code-Style

---

**💡 Tipp:** Dieses Beispiel zeigt den idealen Workflow. In der Praxis werden Sie iterieren und anpassen. Das ist normal und erwünscht!
