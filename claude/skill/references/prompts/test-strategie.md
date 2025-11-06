# Prompt-Template: Test-Strategie

## Kontext
Du erstellst ein Test-Strategie-Dokument basierend auf dem MVP-Plan und der Architektur.

## Aufgabe
Erstelle eine Test-Strategie für:

[MVP-PLAN HIER EINFÜGEN]
[ARCHITEKTUR-DOKUMENT HIER EINFÜGEN]

## Struktur der Test-Strategie

### 1. Test-Pyramide

```
        /\
       /E2E\         End-to-End Tests (10%)
      /______\
     /        \
    /Integration\    Integration Tests (30%)
   /______________\
  /                \
 /   Unit Tests     \ Unit Tests (60%)
/____________________\
```

**Verteilung**:
- Unit Tests: 60% - Schnell, isoliert, viele
- Integration Tests: 30% - Mittel, Komponenten-Interaktion
- E2E Tests: 10% - Langsam, komplett, kritische Pfade

### 2. Unit-Testing-Strategie

#### 2.1 Scope
Was wird mit Unit-Tests abgedeckt:
- Alle Business-Logic-Funktionen
- Alle Utility-Functions
- Alle Data-Transformations
- Alle Validierungs-Logik
- Alle Error-Handling-Pfade

#### 2.2 Frameworks & Tools
**Frontend**:
- Test-Framework: Jest / Vitest
- React Testing: React Testing Library
- Mocking: Jest mock functions

**Backend**:
- Test-Framework: pytest / Jest (Node.js)
- Mocking: pytest-mock / sinon

#### 2.3 Coverage-Ziele
- **Minimum**: 80% Code Coverage
- **Ziel**: 90% Code Coverage
- **Critical Paths**: 100% Coverage

#### 2.4 Test-Naming Convention
```
describe('[ComponentName] - [Functionality]', () => {
  test('should [expected behavior] when [condition]', () => {
    // Arrange
    // Act
    // Assert
  });
});
```

**Beispiele**:
```typescript
describe('UserService - createUser', () => {
  test('should create user successfully when valid data provided', () => {});
  test('should throw ValidationError when email is invalid', () => {});
  test('should throw ConflictError when email already exists', () => {});
});
```

#### 2.5 Zu testende Szenarien pro Funktion
- ✅ Happy Path (normale Verwendung)
- ✅ Edge Cases (Grenzwerte)
- ✅ Error Cases (Fehlerszenarien)
- ✅ Null/Undefined/Empty Inputs
- ✅ Invalid Inputs
- ✅ Boundary Conditions

### 3. Integration-Testing-Strategie

#### 3.1 Scope
Was wird mit Integration-Tests abgedeckt:
- API-Endpunkt Tests (Request → Response)
- Datenbank-Interaktionen
- Service-zu-Service Kommunikation
- External API Calls (gemockt)
- File System Operations

#### 3.2 Test-Environment
- **Test-Database**: Separate Test-DB mit Fixtures
- **API-Server**: Test-Server Instance
- **Mock-Services**: Gemockte externe Dependencies

#### 3.3 Frameworks & Tools
**API-Testing**:
- Supertest (Node.js) / requests (Python)
- Postman/Newman (optional)

**Database Testing**:
- Test-Fixtures für bekannte Zustände
- Transactions mit Rollback nach Test
- In-Memory DB für schnellere Tests (z.B. SQLite)

#### 3.4 Test-Szenarien
Für jede API:
```
GET /api/users/:id
  ✅ should return user when ID exists
  ✅ should return 404 when ID not found
  ✅ should return 401 when not authenticated
  ✅ should return 403 when not authorized
  ✅ should include related data when requested

POST /api/users
  ✅ should create user when valid data
  ✅ should return 400 when missing required fields
  ✅ should return 400 when invalid data format
  ✅ should return 409 when email already exists
  ✅ should hash password before storing
  ✅ should send welcome email
```

### 4. End-to-End Testing-Strategie

#### 4.1 Scope
Kritische User-Journeys:
1. **User-Registration-Flow**
   - Sign up → Email verification → Login → Profile completion
2. **Order-Placement-Flow**
   - Browse products → Add to cart → Checkout → Payment → Confirmation
3. **Admin-Dashboard-Flow**
   - Login as admin → View analytics → Manage users → Export report

#### 4.2 Frameworks & Tools
- **Frontend E2E**: Playwright / Cypress
- **API E2E**: Postman Collections / REST-Assured

#### 4.3 Test-Environment
- Staging-Environment mit Production-ähnlicher Konfiguration
- Test-User-Accounts mit verschiedenen Rollen
- Test-Daten-Set (anonymisierte Production-Daten)

#### 4.4 Test-Execution
- Automatisch nach jedem Release-Candidate Build
- Täglich scheduled auf Staging
- Vor jedem Production-Deployment

### 5. Performance-Testing

#### 5.1 Load-Testing
**Tools**: k6 / JMeter / Locust

**Szenarien**:
- **Normal Load**: 50 gleichzeitige User
- **Peak Load**: 200 gleichzeitige User
- **Stress Test**: Bis System-Limit

**Metrics**:
- Response Time: p50, p95, p99
- Requests per Second
- Error Rate
- Resource Utilization (CPU, Memory, DB connections)

#### 5.2 Performance-Kriterien
- **API Response Time**:
  - p95 < 500ms (Read-Operations)
  - p95 < 1000ms (Write-Operations)
- **Page Load Time**:
  - p95 < 2s (First Contentful Paint)
- **Error Rate**: < 0.1% under normal load

### 6. Security-Testing

#### 6.1 Automatische Security-Scans
**Tools**:
- OWASP ZAP / Burp Suite
- npm audit / pip audit
- Bandit (Python) / ESLint security plugins

**Checks**:
- SQL Injection vulnerabilities
- XSS vulnerabilities
- CSRF vulnerabilities
- Authentication/Authorization flaws
- Known vulnerabilities in dependencies

#### 6.2 Manuelle Security-Tests
- Penetration Testing (vor Production-Release)
- Security Code Review für kritische Features
- Threat Modeling für sensible Datenflüsse

### 7. Test-Data-Management

#### 7.1 Test-Fixtures
```python
# Beispiel: Fixture für User-Tests
@pytest.fixture
def test_user():
    return {
        "id": "test-user-123",
        "email": "test@example.com",
        "name": "Test User",
        "role": "user"
    }

@pytest.fixture
def admin_user():
    return {
        "id": "admin-123",
        "email": "admin@example.com",
        "name": "Admin User",
        "role": "admin"
    }
```

#### 7.2 Test-Database Seeds
- Minimum-Datensatz für alle Tests
- Spezifische Seeds für verschiedene Szenarien
- Automatisches Reset zwischen Tests

### 8. Continuous Integration

#### 8.1 CI-Pipeline
```
Code Push → Build → Unit Tests → Integration Tests → E2E Tests → Deploy to Staging
                     ↓              ↓                  ↓
                   FAIL           FAIL               FAIL
                     ↓              ↓                  ↓
                  Notify         Notify             Notify
```

#### 8.2 Test-Stages
1. **PR-Tests** (bei Pull Request):
   - Lint
   - Unit Tests
   - Quick Integration Tests
   
2. **Main-Branch Tests** (bei Merge):
   - Full Unit Tests
   - Full Integration Tests
   - Code Coverage Report
   
3. **Pre-Deployment Tests** (vor Staging):
   - E2E Tests
   - Performance Tests (subset)
   - Security Scans

4. **Post-Deployment Tests** (nach Staging):
   - Smoke Tests
   - Full E2E Tests

### 9. Test-Automation

#### 9.1 Was wird automatisiert
- ✅ Unit Tests (alle)
- ✅ Integration Tests (alle)
- ✅ E2E Tests (kritische Pfade)
- ✅ Code Coverage Reporting
- ✅ Security Scans
- ⚠️ Performance Tests (subset)
- ❌ Explorative Tests (manuell)
- ❌ Usability Tests (manuell)

#### 9.2 Test-Execution-Frequency
- **Unit + Integration Tests**: Bei jedem Commit
- **E2E Tests**: Täglich + vor jedem Release
- **Performance Tests**: Wöchentlich + vor jedem Release
- **Security Scans**: Täglich

### 10. Defect-Management

#### 10.1 Bug-Severity-Levels
| Severity | Beschreibung | Response Time |
|----------|--------------|---------------|
| Critical | System down, data loss | Sofort |
| High | Major feature broken | 4 Stunden |
| Medium | Feature partially broken | 1 Tag |
| Low | Minor issue, cosmetic | 1 Woche |

#### 10.2 Bug-Workflow
```
Found → Reported → Triaged → Assigned → Fixed → Verified → Closed
```

#### 10.3 Regression-Test-Suite
- Alle fixed Bugs bekommen einen Regression-Test
- Regression-Suite läuft bei jedem Release

### 11. Test-Metrics & Reporting

#### 11.1 Tracked Metrics
- **Test Coverage**: Zeile, Branch, Function
- **Test Results**: Pass/Fail Rate
- **Test Duration**: Execution Time
- **Defect Density**: Bugs per 1000 LOC
- **Mean Time To Detect** (MTTD)
- **Mean Time To Resolve** (MTTR)

#### 11.2 Test-Reports
- Täglich: Test-Execution-Summary
- Wöchentlich: Coverage-Report + Trend-Analysis
- Pro Sprint: Quality-Report für Sprint-Review

### 12. Acceptance-Kriterien

Für jedes Feature im MVP müssen definiert sein:

#### Feature: [Name]
```
Given [context/precondition]
When [action/trigger]
Then [expected result]

Beispiel:
Feature: User Login

Scenario: Successful login
  Given a registered user with email "user@example.com" and password "SecurePass123"
  When the user submits login form with correct credentials
  Then the user is redirected to dashboard
  And a session token is created
  And "Welcome back" message is displayed

Scenario: Failed login - wrong password
  Given a registered user with email "user@example.com"
  When the user submits login form with wrong password
  Then an error message "Invalid credentials" is displayed
  And no session token is created
  And the user remains on login page
```

### 13. Test-Schedule für MVP

#### Phase 1: Development (Sprints 1-5)
- Unit Tests: Parallel zur Entwicklung
- Integration Tests: Am Ende jedes Sprints
- Code Reviews: Bei jedem PR

#### Phase 2: Integration (Sprint 6)
- Full Integration Testing
- Initial E2E Tests
- Performance Baseline

#### Phase 3: Hardening (Sprint 7-8)
- Bug Fixing basierend auf Tests
- Full E2E Testing
- Performance Testing
- Security Testing

#### Phase 4: Pre-Release (Sprint 9)
- User Acceptance Testing
- Final E2E Run
- Load Testing
- Production-Readiness Review

## Wichtige Hinweise
- Test-first Approach empfohlen (TDD wo sinnvoll)
- Tests sind lebende Dokumentation
- Flaky Tests sofort fixen oder löschen
- Test-Coverage als Metrik, nicht als Ziel (Qualität > Quantität)
- Regelmäßig Test-Suite aufräumen (obsolete Tests entfernen)
