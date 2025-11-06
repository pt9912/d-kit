# Prompt-Template: Task-Design-Dokument

## Kontext
Du erstellst ein detailliertes Design-Dokument für eine spezifische Task.

## Aufgabe
Erstelle ein Design-Dokument für:

Task-ID: [TASK-XXX]
[TASK-BESCHREIBUNG HIER EINFÜGEN]

Relevante Dokumente:
[ARCHITEKTUR-DOKUMENT (relevante Teile)]
[PFLICHTENHEFT (relevante Anforderungen)]

## Struktur des Task-Design-Dokuments

### 1. Task-Übersicht
- **Task-ID**: TASK-XXX
- **Titel**: [Kurzer Titel]
- **Ziel**: Was soll diese Task erreichen
- **User Story**: Als [Rolle] möchte ich [Funktion], damit [Nutzen]
- **UI-Design**: [Figma-Link zu relevanten Screens] (falls Frontend)

### 2. Technische Spezifikation

#### 2.1 Betroffene Komponenten
- Komponente 1: [Name und Rolle]
- Komponente 2: [Name und Rolle]

#### 2.2 Änderungen an bestehenden Dateien
```
src/
  ├── components/
  │   └── UserProfile.tsx [MODIFY] - Add avatar display
  ├── services/
  │   └── userService.ts [MODIFY] - Add getAvatar method
  └── types/
      └── user.ts [MODIFY] - Add avatar field to User interface
```

#### 2.3 Neue Dateien
```
src/
  ├── components/
  │   └── Avatar.tsx [NEW] - Reusable avatar component
  └── utils/
      └── imageProcessing.ts [NEW] - Image handling utilities
```

### 3. API-Design (falls relevant)

#### 3.1 Endpoints

##### GET /api/users/:id/avatar
```
Request:
  Headers:
    Authorization: Bearer <token>
  
Response 200:
  {
    "avatarUrl": "https://...",
    "uploadedAt": "2024-01-15T10:30:00Z"
  }

Response 404:
  {
    "error": "User not found"
  }

Response 401:
  {
    "error": "Unauthorized"
  }
```

##### POST /api/users/:id/avatar
```
Request:
  Headers:
    Authorization: Bearer <token>
    Content-Type: multipart/form-data
  Body:
    file: <image file>
    
Response 200:
  {
    "avatarUrl": "https://...",
    "uploadedAt": "2024-01-15T10:30:00Z"
  }

Validations:
  - File size max 5MB
  - Allowed formats: jpg, png, gif
  - Image dimensions: min 100x100, max 2000x2000
```

### 4. Datenmodell-Änderungen (falls relevant)

#### 4.1 Schema-Änderungen
```sql
-- Migration: add_avatar_to_users.sql

ALTER TABLE users 
ADD COLUMN avatar_url VARCHAR(255),
ADD COLUMN avatar_uploaded_at TIMESTAMP;

CREATE INDEX idx_users_avatar ON users(avatar_url) 
WHERE avatar_url IS NOT NULL;
```

#### 4.2 TypeScript Interfaces
```typescript
interface User {
  id: string;
  name: string;
  email: string;
  avatarUrl?: string;  // NEW
  avatarUploadedAt?: Date;  // NEW
}

interface AvatarUploadRequest {
  file: File;
  userId: string;
}

interface AvatarUploadResponse {
  avatarUrl: string;
  uploadedAt: Date;
}
```

### 5. Business-Logik

#### 5.1 Workflow
```
1. User wählt Datei aus
   └─> Validate file (size, format, dimensions)
       ├─> Invalid: Show error message
       └─> Valid:
           2. Upload to storage (S3/Cloud Storage)
              └─> 3. Get public URL
                  └─> 4. Update user record in database
                      └─> 5. Update UI with new avatar
```

#### 5.2 Validation Rules
- File size: 100 KB - 5 MB
- Allowed MIME types: image/jpeg, image/png, image/gif
- Image dimensions: 100x100 - 2000x2000 pixels
- Aspect ratio: flexible

#### 5.3 Error Handling
```
Errors to handle:
- File too large → "Image must be smaller than 5MB"
- Invalid format → "Please upload a JPG, PNG, or GIF image"
- Upload failed → "Upload failed. Please try again"
- Network error → "Network error. Check your connection"
- Server error → "Something went wrong. Please try again later"
```

### 6. Frontend-Implementation (falls relevant)

#### 6.1 UI-Design-Referenz

**Figma-Screens**:
- Main Screen: [Figma-Link]
- Modal/Component: [Figma-Link]
- Mobile Version: [Figma-Link]

**Design-Spezifikationen** (aus Figma):
```css
/* From Figma Design System */
.avatar-container {
  width: 120px;
  height: 120px;
  border-radius: 60px;
  background: var(--color-gray-100);
  border: 2px solid var(--color-gray-300);
}

.avatar-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: inherit;
}

.upload-button {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 36px;
  height: 36px;
  background: var(--color-primary-500);
  border-radius: 18px;
  box-shadow: var(--shadow-md);
}
```

**Component-Hierarchy** (aus Figma):
```
<AvatarUpload>
  ├─ <AvatarDisplay>
  │   ├─ <Image src={avatarUrl} />
  │   └─ <DefaultAvatar /> (wenn kein Bild)
  │
  └─ <UploadButton>
      ├─ <Icon name="camera" />
      └─ <FileInput hidden />
```

**States to Implement** (aus Figma):
- Default (no image)
- With Image
- Uploading (loading spinner)
- Error (red border + message)
- Success (green checkmark animation)

#### 6.2 Component Structure
```typescript
// Avatar.tsx - Pseudocode
const Avatar = ({ userId, size = 'medium' }) => {
  const [avatarUrl, setAvatarUrl] = useState(null)
  const [isUploading, setIsUploading] = useState(false)
  
  const handleFileSelect = async (file) => {
    // Validate file
    if (!validateFile(file)) return
    
    // Upload file
    setIsUploading(true)
    try {
      const response = await uploadAvatar(userId, file)
      setAvatarUrl(response.avatarUrl)
    } catch (error) {
      showError(error.message)
    } finally {
      setIsUploading(false)
    }
  }
  
  return (
    <div className="avatar-container">
      {avatarUrl ? (
        <img src={avatarUrl} alt="User avatar" />
      ) : (
        <DefaultAvatar />
      )}
      <FileUpload onSelect={handleFileSelect} disabled={isUploading} />
    </div>
  )
}
```

#### 6.2 State Management
- Local state: current upload progress, errors
- Global state (if Redux/Context): user profile with avatar
- Cache strategy: avatarUrl in user object

### 7. Backend-Implementation (falls relevant)

#### 7.1 Controller/Handler
```python
# users_controller.py - Pseudocode

@router.post("/users/{user_id}/avatar")
async def upload_avatar(
    user_id: str,
    file: UploadFile,
    current_user: User = Depends(get_current_user)
):
    # Authorization check
    if current_user.id != user_id:
        raise HTTPException(status_code=403, detail="Forbidden")
    
    # Validate file
    validate_image_file(file)
    
    # Upload to storage
    avatar_url = await storage_service.upload(
        file, 
        path=f"avatars/{user_id}"
    )
    
    # Update database
    await user_repository.update_avatar(user_id, avatar_url)
    
    return {"avatarUrl": avatar_url, "uploadedAt": datetime.now()}
```

#### 7.2 Service Layer
```python
class StorageService:
    async def upload(self, file: UploadFile, path: str) -> str:
        # Implementation for S3/Cloud Storage upload
        pass
    
    async def delete(self, url: str) -> bool:
        # Delete old avatar when new one is uploaded
        pass
```

### 8. Test-Cases

#### 8.1 Unit-Tests

##### Frontend Tests
```typescript
describe('Avatar Component', () => {
  test('displays default avatar when no avatarUrl', () => { ... })
  test('displays user avatar when avatarUrl provided', () => { ... })
  test('handles file upload successfully', () => { ... })
  test('shows error message on upload failure', () => { ... })
  test('validates file size', () => { ... })
  test('validates file format', () => { ... })
})
```

##### Backend Tests
```python
def test_upload_avatar_success():
    # Test successful upload
    pass

def test_upload_avatar_unauthorized():
    # Test authorization check
    pass

def test_upload_avatar_invalid_file():
    # Test file validation
    pass

def test_upload_avatar_file_too_large():
    # Test file size limit
    pass
```

#### 8.2 Integration Tests
```
Test: Complete avatar upload flow
1. User selects file → Frontend validates
2. Frontend sends request → Backend receives
3. Backend uploads to storage → Storage returns URL
4. Backend updates database → Database confirms
5. Frontend receives response → UI updates
```

#### 8.3 Edge Cases
- User uploads same file twice
- Network fails during upload
- Storage service is unavailable
- Database update fails after upload
- User navigates away during upload

### 9. Performance Considerations
- Image optimization: Resize on server-side
- Caching: CDN for avatar URLs
- Lazy loading: Load avatars only when visible
- Thumbnail generation: Multiple sizes (small, medium, large)

### 10. Security Considerations
- File type validation on both frontend and backend
- Virus scanning for uploaded files
- Authorization: Users can only change their own avatar
- Rate limiting: Max 5 uploads per hour per user
- Sanitize file names

### 11. Dependencies
- External libraries:
  - Frontend: react-dropzone (file upload UI)
  - Backend: Pillow (Python image processing)
- Internal:
  - TASK-001 (User authentication) must be complete
  - Storage service must be configured

### 12. Rollout Strategy
- Feature flag: `feature.avatar_upload.enabled`
- Rollout phases:
  1. Internal testing (beta users)
  2. 10% of users
  3. 50% of users
  4. 100% of users

### 13. Monitoring & Observability
- Metrics to track:
  - Upload success rate
  - Average upload time
  - File size distribution
  - Error rate by error type
- Alerts:
  - Upload success rate < 95%
  - Average upload time > 5 seconds

### 14. Documentation Needs
- API documentation (OpenAPI/Swagger)
- User guide: "How to upload an avatar"
- Developer notes: Storage configuration

## Wichtige Hinweise
- Design muss mit Architektur konsistent sein
- Alle Edge Cases berücksichtigen
- Test-Cases müssen Design vollständig abdecken
- Security nicht vergessen
- Bei Unklarheiten: Fragen dokumentieren
- Code-Beispiele als Pseudocode oder mit Kommentaren