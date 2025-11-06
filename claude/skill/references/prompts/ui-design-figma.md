# Prompt-Template: UI-Design (Figma)

## Kontext
Du erstellst UI-Design-Spezifikationen und Mockups für die Implementierung.

## Aufgabe
Erstelle UI-Design für:

[FEATURE/USE-CASE HIER EINFÜGEN]
[RELEVANTE USER STORIES]
[ARCHITEKTUR-DOKUMENT - Frontend-Anforderungen]

## UI-Design-Prozess

### Phase 1: Design-Vorbereitung

#### 1.1 Design-Brief erstellen

**Projekt-Kontext**:
- App-Name: [Name]
- Platform: Web / iOS / Android / Desktop
- Zielgruppe: [Persona-Referenz]
- Stil: Modern / Minimalistisch / Verspielt / Corporate / etc.

**Design-Anforderungen**:
- Responsive Design: Mobile-First / Desktop-First
- Accessibility: WCAG 2.1 Level AA compliance
- Browser-Support: Chrome, Firefox, Safari, Edge (latest versions)
- Dark Mode: Ja / Nein
- Multi-Language: Ja / Nein

**Brand Guidelines**:
- Farben: Primär, Sekundär, Akzent
- Typografie: Schriftarten, Größen, Hierarchie
- Logo/Branding: Verfügbar in `assets/`
- Tone of Voice: Professionell / Freundlich / etc.

#### 1.2 User-Flow definieren

Basierend auf Use-Cases:

```
User Journey: Todo erstellen

Entry Point: Dashboard
    ↓
[+ Button] geklickt
    ↓
Modal/Page: Todo-Formular öffnet
    ↓
User gibt Daten ein
    ↓
[Speichern] geklickt
    ↓
Validierung läuft
    ↓ Success        ↓ Error
Todo erscheint      Fehler-Message
in Liste            wird angezeigt
    ↓
Erfolgs-Feedback
    ↓
Exit: Zurück zu Dashboard
```

#### 1.3 Wireframes (Low-Fidelity)

**Zweck**: Struktur und Layout ohne visuelles Design

**Elemente** (ASCII/Text-basiert für KI):
```
┌────────────────────────────────────┐
│ Header                    [User ▼] │
├────────────────────────────────────┤
│ Sidebar │ Main Content             │
│         │                          │
│ [Todos] │  My Todos      [+ New]   │
│ [Cats]  │  ─────────────────────── │
│ [Tags]  │  [ ] Todo 1    [Edit]    │
│         │  [✓] Todo 2    [Edit]    │
│         │  [ ] Todo 3    [Edit]    │
│         │                          │
└────────────────────────────────────┘
```

**Figma-Wireframe-Struktur**:
```
Screens/
├── 01-Dashboard (Wireframe)
├── 02-Todo-Form (Wireframe)
├── 03-Todo-List-Empty (Wireframe)
└── 04-Todo-List-Filled (Wireframe)
```

### Phase 2: High-Fidelity Design

#### 2.1 Design-System erstellen

**Figma-Organisation**:
```
Project: [App-Name]
├── 📁 Design System
│   ├── Colors
│   ├── Typography
│   ├── Components
│   ├── Icons
│   └── Spacing
│
├── 📁 Wireframes (Low-Fi)
│   ├── Mobile
│   ├── Tablet
│   └── Desktop
│
├── 📁 Mockups (High-Fi)
│   ├── Mobile
│   ├── Tablet
│   └── Desktop
│
├── 📁 Prototypes
│   ├── User Flow 1
│   ├── User Flow 2
│   └── User Flow 3
│
└── 📁 Assets (Export)
    ├── Icons (SVG)
    ├── Images (PNG/WebP)
    └── Styles (CSS Export)
```

#### 2.2 Design-System Komponenten

##### Colors
```
Primary Colors:
- Primary-500: #3B82F6 (Main Brand Color)
- Primary-600: #2563EB (Hover)
- Primary-700: #1D4ED8 (Active)

Secondary Colors:
- Secondary-500: #8B5CF6
- Secondary-600: #7C3AED

Neutrals:
- Gray-50: #F9FAFB (Background)
- Gray-100: #F3F4F6
- Gray-500: #6B7280 (Text Secondary)
- Gray-900: #111827 (Text Primary)

Semantic Colors:
- Success: #10B981 (Green)
- Warning: #F59E0B (Orange)
- Error: #EF4444 (Red)
- Info: #3B82F6 (Blue)
```

##### Typography
```
Font Family: Inter (Google Fonts)

Heading Styles:
- H1: 32px / 40px line-height / 700 weight
- H2: 24px / 32px / 600
- H3: 20px / 28px / 600
- H4: 18px / 26px / 600

Body Styles:
- Body-Large: 18px / 28px / 400
- Body: 16px / 24px / 400
- Body-Small: 14px / 20px / 400
- Caption: 12px / 16px / 400

Code:
- Font: JetBrains Mono
- Size: 14px / 20px / 400
```

##### Spacing System
```
4px Base Unit (0.25rem)

Scale:
- xs: 4px   (0.25rem)
- sm: 8px   (0.5rem)
- md: 16px  (1rem)
- lg: 24px  (1.5rem)
- xl: 32px  (2rem)
- 2xl: 48px (3rem)
- 3xl: 64px (4rem)
```

##### Component Library

**Button Component**:
```
Variants:
- Primary (filled)
- Secondary (outlined)
- Ghost (text only)

States:
- Default
- Hover
- Active
- Disabled
- Loading

Sizes:
- Small (32px height)
- Medium (40px height)
- Large (48px height)

Properties:
- Icon (left/right/both/none)
- Full Width (boolean)
- Loading (boolean)
```

**Input Component**:
```
Variants:
- Text
- Email
- Password
- Number
- Textarea

States:
- Default
- Focus
- Error
- Disabled
- Success

Properties:
- Label
- Placeholder
- Helper Text
- Error Message
- Icon (left/right)
- Required (boolean)
```

**Card Component**:
```
Variants:
- Default
- Elevated (shadow)
- Outlined

Properties:
- Header (optional)
- Body
- Footer (optional)
- Padding (sm/md/lg)
```

#### 2.3 Screen-Designs (High-Fidelity)

##### Dashboard Screen
```
Figma Frame: Dashboard - Desktop (1440x900)

Layout:
┌──────────────────────────────────────────────────┐
│ [Logo]  Todo App         [Search]  [User Avatar] │ Header (64px)
├────────┬─────────────────────────────────────────┤
│ Nav    │ Content Area                            │
│        │                                         │
│ Todos  │  📊 My Todos                [+ New]     │
│ Cats   │  ───────────────────────────────────    │
│ Tags   │                                         │
│ Settings│  🔲 Prepare presentation    High       │
│        │     Due: Tomorrow 3:00 PM    [Edit]    │
│        │     Category: Work                      │
│        │                                         │
│        │  ✅ Buy groceries           Low        │
│        │     Completed: Today 10:30 AM [Edit]   │
│        │     Category: Personal                  │
│        │                                         │
│  240px │  🔲 Review code PR          Medium     │
│        │     Due: Today 5:00 PM       [Edit]    │
│        │     Category: Work                      │
│        │                                         │
└────────┴─────────────────────────────────────────┘

Components Used:
- Header (fixed)
- Sidebar Navigation
- Todo Card Component (x3)
- Button (Primary, + New)
- Badge (Priority indicator)
```

##### Todo Form Modal
```
Figma Frame: Create Todo Modal (600x700)

┌────────────────────────────────────┐
│ Create New Todo              [✕]   │ Modal Header
├────────────────────────────────────┤
│                                    │
│ Title *                            │
│ ┌────────────────────────────────┐ │
│ │ Enter todo title...            │ │ Text Input
│ └────────────────────────────────┘ │
│                                    │
│ Description                        │
│ ┌────────────────────────────────┐ │
│ │ Add details...                 │ │ Textarea
│ │                                │ │
│ └────────────────────────────────┘ │
│                                    │
│ Due Date                           │
│ ┌────────────────┐                 │
│ │ 📅 Select date │                │ Date Picker
│ └────────────────┘                 │
│                                    │
│ Priority                           │
│ [Low] [Medium] [High]              │ Segmented Control
│   └─── selected                    │
│                                    │
│ Category                           │
│ ┌────────────────┐                 │
│ │ Work        ▼ │                 │ Dropdown
│ └────────────────┘                 │
│                                    │
│ Tags                               │
│ [+ Add tag]                        │ Tag Input
│                                    │
├────────────────────────────────────┤
│              [Cancel] [Create]     │ Modal Footer
└────────────────────────────────────┘

States zu designen:
- Empty (initial state)
- Filled (with data)
- Validation Error
- Loading (during save)
- Success (after save)
```

##### Mobile Responsive Version
```
Figma Frame: Dashboard - Mobile (375x812)

┌─────────────────────────┐
│ [☰] Todo App    [👤]    │ 56px Header
├─────────────────────────┤
│                         │
│ 📊 My Todos   [+ New]   │ Section Header
│ ─────────────────────   │
│                         │
│ ┌─────────────────────┐ │
│ │ 🔲 Presentation     │ │
│ │    Due: Tomorrow    │ │
│ │    Work • High      │ │ Todo Card
│ └─────────────────────┘ │
│                         │
│ ┌─────────────────────┐ │
│ │ ✅ Groceries        │ │
│ │    Completed        │ │
│ │    Personal • Low   │ │ Todo Card
│ └─────────────────────┘ │
│                         │
│ ┌─────────────────────┐ │
│ │ 🔲 Code Review      │ │
│ │    Due: Today 5 PM  │ │
│ │    Work • Medium    │ │ Todo Card
│ └─────────────────────┘ │
│                         │
└─────────────────────────┘
│ [Home] [Todos] [More]   │ 56px Bottom Nav
└─────────────────────────┘

Responsive Breakpoints:
- Mobile: 320px - 767px
- Tablet: 768px - 1023px
- Desktop: 1024px+
```

### Phase 3: Interaktions-Design

#### 3.1 Micro-Interactions

**Button Click Animation**:
```
State: Default
  ↓ (hover)
State: Hover (scale: 1.02, shadow: elevated)
  ↓ (click)
State: Active (scale: 0.98)
  ↓ (release)
State: Hover
  ↓ (mouse leave)
State: Default

Timing: 150ms ease-out
```

**Todo Check Animation**:
```
Checkbox clicked
  ↓
1. Checkmark appears (fade in + scale)
2. Text strikethrough animates (left to right)
3. Card fades to gray (opacity: 1 → 0.6)
4. Card moves down in list (optional)

Duration: 300ms
Easing: cubic-bezier(0.4, 0, 0.2, 1)
```

**Loading States**:
```
Button Loading:
- Button text fades out
- Spinner fades in
- Button disabled
- Width remains constant

Skeleton Loading:
- Cards show shimmer effect
- Gradient animation (left to right)
- Smooth transition to real content
```

#### 3.2 User-Feedback-Design

**Success States**:
```
Toast Notification:
┌────────────────────────────┐
│ ✓ Todo created successfully│ Green background
└────────────────────────────┘
Position: Top-right
Duration: 3 seconds
Animation: Slide in from top
```

**Error States**:
```
Inline Error:
┌────────────────────────────┐
│ Title *                    │
│ ┌──────────────────────────┤ Red border
│ │                          │
│ └──────────────────────────┘
│ ⚠️ Title is required        │ Red text
└────────────────────────────┘

Modal Error:
┌────────────────────────────┐
│ ❌ Error                    │
│                            │
│ Could not save todo.       │
│ Please try again.          │
│                            │
│         [Try Again]        │
└────────────────────────────┘
```

**Empty States**:
```
No Todos Yet:
┌────────────────────────────┐
│         📝                 │ Icon
│                            │
│   No todos yet!            │ Heading
│   Create your first one    │ Description
│                            │
│      [+ New Todo]          │ CTA Button
└────────────────────────────┘
```

### Phase 4: Prototype

#### 4.1 Figma Prototype Setup

**Connections to create**:
```
Dashboard
  │
  ├─[+ New] → Todo Form Modal
  │            │
  │            ├─[Cancel] → Dashboard
  │            └─[Create] → Success Toast → Dashboard (updated)
  │
  ├─[Edit Todo] → Edit Modal
  │                │
  │                ├─[Cancel] → Dashboard
  │                └─[Save] → Dashboard (updated)
  │
  └─[Todo Checkbox] → Todo Status Update (animation)
```

**Interaction Details**:
```
Trigger: Click
Action: Navigate to
Destination: [Screen]
Animation: Smart Animate
Duration: 300ms
Easing: Ease Out
```

#### 4.2 User-Testing-Flows

**Flow 1: Create First Todo**
```
1. User lands on Dashboard (empty state)
2. User sees "+ New Todo" CTA
3. User clicks button
4. Modal opens with animation
5. User fills in title
6. User selects due date
7. User clicks "Create"
8. Loading state shows
9. Success toast appears
10. Modal closes
11. Todo appears in list
```

**Flow 2: Mark Todo as Done**
```
1. User sees todo list
2. User finds specific todo
3. User clicks checkbox
4. Checkmark animates in
5. Text strikes through
6. Card fades to gray
7. Done!
```

### Phase 5: Design Handoff

#### 5.1 Figma-zu-Code Export

**Assets-Export**:
```
Icons:
- Format: SVG
- Naming: icon-[name].svg
- Example: icon-check.svg, icon-plus.svg

Images:
- Format: WebP (fallback: PNG)
- Sizes: 1x, 2x, 3x
- Naming: [name]@[size].webp
- Example: hero-image@2x.webp

Illustrations:
- Format: SVG (prefer) or PNG
- Optimized for web
```

**CSS-Export (Figma Plugin)**:
```css
/* Auto-generated from Figma */

:root {
  /* Colors */
  --color-primary-500: #3B82F6;
  --color-primary-600: #2563EB;
  --color-gray-900: #111827;
  
  /* Typography */
  --font-family: 'Inter', sans-serif;
  --font-size-h1: 32px;
  --line-height-h1: 40px;
  
  /* Spacing */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  
  /* Shadows */
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

/* Component: Button Primary */
.button-primary {
  background-color: var(--color-primary-500);
  color: white;
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 600;
  transition: all 150ms ease-out;
}

.button-primary:hover {
  background-color: var(--color-primary-600);
  transform: scale(1.02);
}
```

#### 5.2 Design-Spezifikations-Dokument

**Für Entwickler**:
```markdown
# Design Specifications: Todo Form

## Layout
- Width: 600px (desktop), 100% (mobile)
- Padding: 24px
- Border-radius: 12px
- Background: White (#FFFFFF)
- Shadow: 0 10px 25px rgba(0, 0, 0, 0.1)

## Typography
- Title: H3 (20px, 600 weight, Gray-900)
- Labels: Body-Small (14px, 600 weight, Gray-700)
- Inputs: Body (16px, 400 weight, Gray-900)
- Helper: Caption (12px, 400 weight, Gray-500)

## Spacing
- Form-Field-Gap: 20px (vertical spacing between fields)
- Label-to-Input: 8px
- Input-to-Helper: 4px

## Colors
- Input-Border-Default: Gray-300
- Input-Border-Focus: Primary-500
- Input-Border-Error: Error (Red)
- Input-Background: White

## Animations
- Modal-Open: Fade + Scale (300ms ease-out)
- Modal-Close: Fade + Scale (200ms ease-in)
- Input-Focus: Border transition (150ms ease-out)
- Button-Click: Scale (150ms ease-out)

## States
See Figma frames:
- Default (empty)
- Filled
- Validation-Error
- Loading
- Success
```

#### 5.3 Component-Dokumentation

**Storybook-Ready Format**:
```markdown
# Button Component

## Variants
- Primary: Main actions
- Secondary: Less important actions
- Ghost: Tertiary actions

## Props
- size: 'sm' | 'md' | 'lg'
- variant: 'primary' | 'secondary' | 'ghost'
- disabled: boolean
- loading: boolean
- icon: ReactNode (optional)
- iconPosition: 'left' | 'right'
- fullWidth: boolean
- onClick: () => void

## Usage
```tsx
<Button 
  variant="primary" 
  size="md"
  onClick={handleClick}
>
  Create Todo
</Button>
```

## States
- Default: See Figma
- Hover: Scale 1.02, darker bg
- Active: Scale 0.98
- Disabled: Opacity 0.5, cursor not-allowed
- Loading: Show spinner, disable interaction
```

### Phase 6: Design-Iteration

#### 6.1 User-Testing-Feedback

**Template für Feedback**:
```markdown
## User Test: [Date]
**Tester**: [Name, Persona]
**Task**: [What they tried to accomplish]

### Observations
- ✅ What worked well
- ❌ What caused confusion
- 💡 Suggestions

### Issues Found
1. **Issue**: Button too small on mobile
   - **Severity**: High
   - **Fix**: Increase touch target to 48px min
   
2. **Issue**: Modal closes accidentally
   - **Severity**: Medium
   - **Fix**: Add "Are you sure?" confirmation
```

#### 6.2 Design-Iteration-Log

```markdown
## Version 1.0 → 1.1

### Changes
- Increased button sizes (mobile accessibility)
- Added confirmation dialogs
- Improved color contrast (WCAG AA)
- Updated empty states with better copy

### Figma Pages
- v1.0: Archived
- v1.1: Current

### Impact
- User Story US-001: Updated acceptance criteria
- Use-Case UC-001: Updated interaction flow
```

## Figma-Best-Practices

### Naming Conventions
```
Screens: [Number]-[Name]-[Platform]
Example: 01-Dashboard-Desktop

Components: [Category]/[Name]
Example: Buttons/Primary

Frames: [Feature]-[State]
Example: TodoForm-Empty, TodoForm-Filled
```

### Organization
```
✅ DO:
- Use consistent naming
- Create components for reuse
- Document variants and states
- Use Auto-Layout where possible
- Maintain design system page
- Version your designs

❌ DON'T:
- Duplicate components instead of variants
- Mix different design systems
- Skip state designs (hover, error, etc.)
- Forget mobile/responsive versions
- Leave frames unnamed
```

### Plugins für d-kit
- **Figma to Code**: HTML/CSS export
- **Stark**: Accessibility checking
- **Content Reel**: Generate realistic content
- **Iconify**: Icon library integration
- **Anima**: Export to React/Vue

## Integration in d-kit Workflow

### Wann UI-Design erstellen?

**Nach Phase 2 (Planung), vor Phase 3 (Entwicklung)**:
```
1. Anforderungsanalyse
2. MVP-Plan + Sprint-Plan
├─> UI-DESIGN (Figma) ← NEU
│   ├─ Design System
│   ├─ Wireframes
│   ├─ Mockups
│   └─ Prototype
3. Task-Design-Dokument (referenziert Figma)
4. Code-Implementation (folgt Figma-Specs)
5. Tests
```

### Design-Deliverables pro Sprint

**Sprint-Planning**:
- Welche Screens brauchen Design?
- Welche Komponenten sind neu?

**Sprint-Execution**:
- Designer erstellt Figma-Designs
- Dev-Review der Designs
- Design-Approval Checkpoint
- Development startet

**Sprint-Review**:
- Implementierung vs. Design vergleichen
- Design-Debt identifizieren

## Wichtige Hinweise

1. **Design-First-Approach**: UI vor Code designen spart Zeit
2. **Design-System**: Investition lohnt sich ab 3+ Screens
3. **Responsive Design**: Immer Mobile + Desktop designen
4. **Accessibility**: Von Anfang an einplanen (WCAG 2.1 AA)
5. **States**: Alle States designen (empty, loading, error, success)
6. **Feedback**: User-Testing VOR Development wenn möglich
7. **Handoff**: Klare Specs für Entwickler dokumentieren
8. **Iteration**: Design basierend auf Feedback anpassen