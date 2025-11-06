# Prompt-Template: Code-Generierung

## Kontext
Du generierst produktionsreifen Code basierend auf einem approbierten Design-Dokument.

## Aufgabe
Generiere Code für:

[DESIGN-DOKUMENT HIER EINFÜGEN]

## Code-Generierungs-Richtlinien

### 1. Code-Qualität

#### Clean Code Prinzipien
- **Lesbarkeit**: Code soll selbsterklärend sein
- **DRY**: Don't Repeat Yourself - keine Duplikation
- **SOLID**: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion
- **KISS**: Keep It Simple, Stupid - keine Over-Engineering

#### Naming Conventions
- **Variablen**: camelCase (JavaScript/TypeScript) oder snake_case (Python)
- **Klassen**: PascalCase
- **Konstanten**: UPPER_SNAKE_CASE
- **Private Members**: _prefixWithUnderscore (Python) oder private keyword (TypeScript)
- **Booleans**: isActive, hasPermission, canEdit, shouldShow
- **Functions**: Verben - getUser, createOrder, validateInput

### 2. Code-Struktur

#### Jede Datei sollte enthalten:
```
1. Imports (gruppiert: stdlib, third-party, local)
2. Constants/Types/Interfaces
3. Helper Functions (private)
4. Main Logic
5. Exports
```

#### Beispiel TypeScript:
```typescript
// 1. Imports
import { useState, useEffect } from 'react';
import axios from 'axios';
import { User, ApiResponse } from './types';

// 2. Constants & Types
const API_BASE_URL = process.env.REACT_APP_API_URL;

interface UserProfileProps {
  userId: string;
  onUpdate?: (user: User) => void;
}

// 3. Helper Functions
const validateEmail = (email: string): boolean => {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
};

// 4. Main Component
export const UserProfile: React.FC<UserProfileProps> = ({ 
  userId, 
  onUpdate 
}) => {
  // ... implementation
};
```

### 3. Error Handling

#### Immer implementieren:
```typescript
try {
  const result = await riskyOperation();
  return result;
} catch (error) {
  // 1. Log the error
  logger.error('Operation failed', { error, context: {...} });
  
  // 2. User-friendly message
  throw new ApplicationError(
    'Unable to complete operation. Please try again.',
    { originalError: error }
  );
}
```

#### Error Hierarchie:
```typescript
class ApplicationError extends Error {
  constructor(message: string, public details?: any) {
    super(message);
    this.name = 'ApplicationError';
  }
}

class ValidationError extends ApplicationError {
  constructor(message: string, public field?: string) {
    super(message);
    this.name = 'ValidationError';
  }
}

class AuthenticationError extends ApplicationError {
  constructor(message: string = 'Authentication failed') {
    super(message);
    this.name = 'AuthenticationError';
  }
}
```

### 4. Kommentare & Dokumentation

#### Wann kommentieren:
- ✅ Komplexe Algorithmen
- ✅ Business-Logik Entscheidungen
- ✅ Workarounds für Bugs/Limitations
- ✅ Public APIs (JSDoc/Docstrings)
- ❌ Offensichtlicher Code
- ❌ Schlecht geschriebener Code (besser refactoren)

#### JSDoc/Docstring Format:
```typescript
/**
 * Uploads user avatar and updates profile
 * 
 * @param userId - The unique identifier of the user
 * @param file - The image file to upload (max 5MB, jpg/png/gif)
 * @returns Promise resolving to the avatar URL
 * @throws {ValidationError} If file is invalid
 * @throws {AuthenticationError} If user is not authorized
 * 
 * @example
 * ```typescript
 * const avatarUrl = await uploadAvatar('user-123', imageFile);
 * console.log('Avatar uploaded:', avatarUrl);
 * ```
 */
async function uploadAvatar(
  userId: string, 
  file: File
): Promise<string> {
  // ...
}
```

### 5. Type Safety

#### TypeScript:
```typescript
// ✅ Good: Strong typing
interface User {
  id: string;
  email: string;
  role: 'admin' | 'user' | 'guest';  // Union types
  preferences?: UserPreferences;  // Optional
}

// ❌ Bad: Any types
function processUser(user: any) {  // Avoid 'any'
  // ...
}

// ✅ Good: Generic types
function getById<T>(id: string, collection: T[]): T | undefined {
  return collection.find(item => item.id === id);
}
```

#### Python:
```python
# ✅ Good: Type hints
from typing import Optional, List, Dict

def get_user(user_id: str) -> Optional[User]:
    """Retrieve user by ID."""
    pass

def filter_users(
    users: List[User], 
    role: str
) -> List[User]:
    """Filter users by role."""
    return [u for u in users if u.role == role]
```

### 6. Validation & Sanitization

```typescript
// Input Validation
function createUser(data: CreateUserRequest): User {
  // Validate required fields
  if (!data.email || !data.name) {
    throw new ValidationError('Email and name are required');
  }
  
  // Validate format
  if (!isValidEmail(data.email)) {
    throw new ValidationError('Invalid email format', 'email');
  }
  
  // Sanitize input
  const sanitizedData = {
    email: data.email.trim().toLowerCase(),
    name: sanitizeString(data.name),
  };
  
  // Create user
  return userRepository.create(sanitizedData);
}
```

### 7. Security Best Practices

#### SQL Injection Prevention:
```python
# ✅ Good: Parameterized queries
cursor.execute(
    "SELECT * FROM users WHERE email = ?", 
    (email,)
)

# ❌ Bad: String concatenation
cursor.execute(
    f"SELECT * FROM users WHERE email = '{email}'"
)
```

#### XSS Prevention:
```typescript
// ✅ Good: Escape HTML
import DOMPurify from 'dompurify';

const sanitizedContent = DOMPurify.sanitize(userInput);
```

#### Authentication:
```typescript
// ✅ Good: Verify token on every request
const authenticateRequest = async (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  
  if (!token) {
    return res.status(401).json({ error: 'No token provided' });
  }
  
  try {
    const decoded = await verifyToken(token);
    req.user = decoded;
    next();
  } catch (error) {
    return res.status(401).json({ error: 'Invalid token' });
  }
};
```

### 8. Performance

#### Database Queries:
```typescript
// ❌ Bad: N+1 Query Problem
const users = await User.findAll();
for (const user of users) {
  user.posts = await Post.findAll({ where: { userId: user.id } });
}

// ✅ Good: Use joins/includes
const users = await User.findAll({
  include: [{ model: Post }]
});
```

#### Caching:
```typescript
// ✅ Good: Cache expensive operations
const cache = new Map();

async function getUser(id: string): Promise<User> {
  // Check cache first
  if (cache.has(id)) {
    return cache.get(id);
  }
  
  // Fetch from database
  const user = await database.users.findById(id);
  
  // Cache result
  cache.set(id, user);
  
  return user;
}
```

### 9. Testing Hooks

```typescript
// Exportiere testbare Funktionen
export const _internal = {
  validateEmail,
  formatDate,
  calculateTotal,
};

// In Tests:
import { _internal } from './module';

test('validates email correctly', () => {
  expect(_internal.validateEmail('test@example.com')).toBe(true);
  expect(_internal.validateEmail('invalid')).toBe(false);
});
```

### 10. Code-Datei Template

```typescript
/**
 * @file UserService.ts
 * @description Handles user-related business logic
 * @author AI Code Generator
 * @created 2024-01-15
 */

// ===== IMPORTS =====
import { injectable, inject } from 'tsyringe';
import { User, CreateUserDto, UpdateUserDto } from './types';
import { UserRepository } from './UserRepository';
import { EmailService } from '../email/EmailService';
import { ValidationError, NotFoundError } from '../errors';

// ===== CONSTANTS =====
const MAX_LOGIN_ATTEMPTS = 5;
const ACCOUNT_LOCK_DURATION_MINUTES = 30;

// ===== TYPES =====
interface UserServiceConfig {
  enableEmailVerification: boolean;
  enableAccountLocking: boolean;
}

// ===== SERVICE CLASS =====
@injectable()
export class UserService {
  constructor(
    @inject('UserRepository') private userRepository: UserRepository,
    @inject('EmailService') private emailService: EmailService,
    @inject('Config') private config: UserServiceConfig
  ) {}

  /**
   * Creates a new user account
   */
  async createUser(dto: CreateUserDto): Promise<User> {
    // Validation
    this.validateCreateUserDto(dto);
    
    // Check if user exists
    const existingUser = await this.userRepository.findByEmail(dto.email);
    if (existingUser) {
      throw new ValidationError('Email already in use', 'email');
    }
    
    // Create user
    const user = await this.userRepository.create({
      ...dto,
      password: await this.hashPassword(dto.password),
    });
    
    // Send welcome email
    if (this.config.enableEmailVerification) {
      await this.emailService.sendVerificationEmail(user);
    }
    
    return user;
  }

  /**
   * Validates CreateUserDto
   * @private
   */
  private validateCreateUserDto(dto: CreateUserDto): void {
    if (!dto.email || !this.isValidEmail(dto.email)) {
      throw new ValidationError('Invalid email', 'email');
    }
    
    if (!dto.password || dto.password.length < 8) {
      throw new ValidationError(
        'Password must be at least 8 characters', 
        'password'
      );
    }
  }

  /**
   * Validates email format
   * @private
   */
  private isValidEmail(email: string): boolean {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  /**
   * Hashes password using bcrypt
   * @private
   */
  private async hashPassword(password: string): Promise<string> {
    const bcrypt = await import('bcrypt');
    return bcrypt.hash(password, 10);
  }
}

// ===== EXPORTS =====
export { UserService };

// Export for testing
export const _testing = {
  validateCreateUserDto: UserService.prototype['validateCreateUserDto'],
  isValidEmail: UserService.prototype['isValidEmail'],
};
```

## Deliverables

Für jede Datei aus dem Design-Dokument:

1. **Vollständiger, produktionsreifer Code**
2. **Imports/Dependencies korrekt**
3. **Type Definitions (TypeScript/Python type hints)**
4. **Error Handling implementiert**
5. **Kommentare für komplexe Teile**
6. **JSDoc/Docstrings für Public APIs**
7. **Testing Hooks (wo sinnvoll)**

## Wichtige Hinweise
- Code muss lauffähig sein (keine TODOs oder Platzhalter)
- Alle im Design spezifizierten Features implementieren
- Security Best Practices befolgen
- Performance-Implikationen berücksichtigen
- Code soll wartbar und testbar sein
- Bei Unklarheiten: nachfragen statt raten
