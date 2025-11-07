# Beispiel: UI-Design mit Figma für Todo-App

Dieses Beispiel zeigt den kompletten UI-Design-Prozess für die Todo-App.

## Phase 1: Design-Brief

### Projekt-Kontext
- **App-Name**: TodoFlow
- **Platform**: Web (Responsive), später Mobile Apps
- **Zielgruppe**: Freelancer und Projektmanager (siehe Personas Lisa & Thomas)
- **Stil**: Modern, Minimalistisch, Clean
- **Tone**: Professionell aber freundlich

### Design-Anforderungen
- **Responsive**: Mobile-First Approach
- **Accessibility**: WCAG 2.1 Level AA
- **Browser**: Chrome, Firefox, Safari, Edge (latest)
- **Dark Mode**: Ja (Phase 2)
- **Multi-Language**: Ja (EN, DE)

### Brand Guidelines
```
Primary Color: #3B82F6 (Blue)
├─ 50:  #EFF6FF
├─ 100: #DBEAFE
├─ 500: #3B82F6 ← Main
├─ 600: #2563EB ← Hover
└─ 700: #1D4ED8 ← Active

Accent Color: #10B981 (Green) für Success

Typography:
- Font: Inter (Google Fonts)
- Headings: 600-700 weight
- Body: 400 weight
- Code: JetBrains Mono

Spacing: 8px base unit
```

## Phase 2: User-Flows

### Flow 1: Create Todo
```
Dashboard (List View)
    │
    │ User clicks [+ New Todo]
    ▼
Modal: Create Todo Form
    │
    │ User fills:
    │ - Title: "Prepare Presentation"
    │ - Description: "Client meeting prep"
    │ - Due: Tomorrow 3 PM
    │ - Priority: High
    │ - Category: Work
    │
    │ User clicks [Create]
    ▼
Loading State (300ms)
    │
    ▼
Success Toast: "Todo created"
    │
    ▼
Modal closes (animated)
    │
    ▼
Dashboard (Todo appears at top)
```

### Flow 2: Mark Todo Complete
```
Dashboard with Todos
    │
    │ User finds todo
    │ User clicks [ ] checkbox
    ▼
Checkbox Animation:
├─ Checkmark appears (fade + scale)
├─ Text strikethrough (left to right)
└─ Card fades to 60% opacity
    │
    ▼
Status saved to DB
    │
    ▼
Dashboard (updated state)
```

## Phase 3: Wireframes (ASCII)

### Dashboard - Desktop Wireframe
```
┌────────────────────────────────────────────────────────────────┐
│ [☰] TodoFlow                    [🔍 Search]        [👤 Lisa ▼] │ 64px Header
├──────────────┬─────────────────────────────────────────────────┤
│              │                                                  │
│ 📋 My Todos  │  My Todos                        [+ New Todo]   │
│ 📁 Projects  │  ─────────────────────────────────────────────  │
│ 🏷️ Categories│                                                  │
│ ⚙️ Settings  │  ┌─────────────────────────────────────────┐   │
│              │  │ [ ] Prepare presentation        🔴 High  │   │
│              │  │     Due: Tomorrow 3:00 PM                │   │
│              │  │     Work                         [⋮]     │   │
│              │  └─────────────────────────────────────────┘   │
│              │                                                  │
│              │  ┌─────────────────────────────────────────┐   │
│  240px       │  │ [✓] Buy groceries              🟢 Low   │   │
│  Sidebar     │  │     Completed: Today 10:30               │   │
│              │  │     Personal                     [⋮]     │   │
│              │  └─────────────────────────────────────────┘   │
│              │                                                  │
│              │  ┌─────────────────────────────────────────┐   │
│              │  │ [ ] Review code PR            🟡 Medium │   │
│              │  │     Due: Today 5:00 PM                   │   │
│              │  │     Work                         [⋮]     │   │
│              │  └─────────────────────────────────────────┘   │
│              │                                                  │
└──────────────┴─────────────────────────────────────────────────┘

Elements:
- Header: Fixed, 64px height
- Sidebar: 240px width, collapsible
- Content: Flexible width, 24px padding
- Todo Cards: Full width, 16px gap
```

### Create Todo Modal - Wireframe
```
                    ┌────────────────────┐
                    │ Create New Todo [✕]│
                    ├────────────────────┤
                    │                    │
                    │ Title *            │
                    │ [______________]   │
                    │                    │
                    │ Description        │
                    │ [______________]   │
                    │ [______________]   │
                    │                    │
                    │ Due Date           │
                    │ [📅 Select date]   │
                    │                    │
                    │ Priority           │
                    │ ⚪ Low ⚪ Med ⚫ High│
                    │                    │
                    │ Category           │
                    │ [Work        ▼]    │
                    │                    │
                    ├────────────────────┤
                    │ [Cancel] [Create]  │
                    └────────────────────┘

Width: 600px (desktop), 90% (mobile)
Height: Auto, max 80vh
```

### Mobile - Wireframe
```
┌─────────────────────┐
│ [☰] TodoFlow  [👤]  │ 56px
├─────────────────────┤
│ 📊 My Todos         │
│ ──────────  [+ New] │
│                     │
│ ┌─────────────────┐ │
│ │[ ] Presentation │ │
│ │  Tomorrow 3 PM  │ │
│ │  Work • High 🔴 │ │
│ └─────────────────┘ │
│                     │
│ ┌─────────────────┐ │
│ │[✓] Groceries    │ │
│ │  Today 10:30    │ │
│ │  Personal • Low │ │
│ └─────────────────┘ │
│                     │
│ ┌─────────────────┐ │
│ │[ ] Code Review  │ │
│ │  Today 5 PM     │ │
│ │  Work • Med 🟡  │ │
│ └─────────────────┘ │
│                     │
├─────────────────────┤
│[🏠][📋][📁][⚙️]     │ 56px Bottom Nav
└─────────────────────┘
```

## Phase 4: Design-System (Figma)

### Figma-Struktur
```
📁 TodoFlow Design
│
├─📄 Design System
│  ├─ 🎨 Colors
│  │   ├─ Primary Scale
│  │   ├─ Semantic Colors
│  │   └─ Neutrals
│  │
│  ├─ 📝 Typography
│  │   ├─ Headings (H1-H4)
│  │   ├─ Body Styles
│  │   └─ Code Styles
│  │
│  ├─ 🧩 Components
│  │   ├─ Buttons
│  │   │   ├─ Primary (variants: default, hover, active, disabled)
│  │   │   ├─ Secondary
│  │   │   └─ Ghost
│  │   │
│  │   ├─ Input Fields
│  │   │   ├─ Text Input (states: default, focus, error, disabled)
│  │   │   ├─ Textarea
│  │   │   └─ Date Picker
│  │   │
│  │   ├─ Cards
│  │   │   ├─ Todo Card (states: default, completed, hover)
│  │   │   └─ Empty State Card
│  │   │
│  │   ├─ Badges
│  │   │   ├─ Priority (High, Medium, Low)
│  │   │   └─ Category
│  │   │
│  │   └─ Modals
│  │       ├─ Standard Modal
│  │       └─ Confirmation Dialog
│  │
│  ├─ 🔤 Icons
│  │   └─ (Lucide Icons - imported)
│  │
│  └─ 📏 Spacing & Grid
│      ├─ 8px Base Unit
│      └─ 12-Column Grid
│
├─📄 Wireframes
│  ├─ Dashboard - Desktop
│  ├─ Dashboard - Mobile
│  ├─ Create Todo Modal
│  └─ Settings Screen
│
├─📄 Mockups (High-Fidelity)
│  ├─ Dashboard - Desktop
│  ├─ Dashboard - Mobile
│  ├─ Dashboard - Tablet
│  ├─ Create Todo Modal
│  ├─ Edit Todo Modal
│  ├─ Settings Screen
│  └─ Empty States
│
├─📄 Prototypes
│  ├─ Flow: Create Todo
│  ├─ Flow: Mark Complete
│  └─ Flow: Edit Todo
│
└─📄 Exports
   ├─ Icons (SVG)
   ├─ Styles (CSS)
   └─ Assets
```

### Component: Button (Figma)

**Variants:**
```
Button/Primary
├─ Size: Small (32px height)
├─ Size: Medium (40px height)
├─ Size: Large (48px height)
└─ States for each:
    ├─ Default
    ├─ Hover (scale: 1.02, bg: primary-600)
    ├─ Active (scale: 0.98)
    ├─ Disabled (opacity: 0.5)
    └─ Loading (spinner)

Properties:
- Text: String
- Icon: Boolean (show/hide)
- IconPosition: left | right
- FullWidth: Boolean
```

### Component: Todo Card

**Figma Component Structure:**
```
TodoCard
├─ Checkbox (component)
├─ Content
│   ├─ Title (text)
│   ├─ Metadata
│   │   ├─ Due Date (icon + text)
│   │   └─ Category Badge (component)
│   └─ Priority Badge (component)
└─ Actions Menu (⋮)

Variants:
├─ Status: Active | Completed
└─ Priority: High | Medium | Low

States:
├─ Default
├─ Hover (shadow: elevated, border: primary)
└─ Completed (opacity: 0.6, strikethrough)

Auto-Layout:
- Direction: Horizontal
- Padding: 16px
- Gap: 12px
- Fill: Hug contents (vertical), Fill container (horizontal)
```

## Phase 5: High-Fidelity Mockups

### Dashboard - Desktop (1440x900)

**Specs:**
```css
/* Header */
.header {
  height: 64px;
  background: #FFFFFF;
  border-bottom: 1px solid #E5E7EB;
  padding: 0 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

/* Sidebar */
.sidebar {
  width: 240px;
  background: #F9FAFB;
  padding: 16px;
  border-right: 1px solid #E5E7EB;
}

.sidebar-item {
  padding: 12px 16px;
  border-radius: 8px;
  transition: background 150ms;
}

.sidebar-item:hover {
  background: #E5E7EB;
}

.sidebar-item.active {
  background: #EFF6FF;
  color: #3B82F6;
}

/* Content Area */
.content {
  flex: 1;
  padding: 24px;
  background: #FFFFFF;
}

.content-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

/* Todo Card */
.todo-card {
  background: #FFFFFF;
  border: 1px solid #E5E7EB;
  border-radius: 12px;
  padding: 16px;
  margin-bottom: 12px;
  display: flex;
  gap: 12px;
  transition: all 200ms;
}

.todo-card:hover {
  border-color: #3B82F6;
  box-shadow: 0 4px 12px rgba(59, 130, 246, 0.1);
  transform: translateY(-2px);
}

.todo-card.completed {
  opacity: 0.6;
}

.todo-card.completed .todo-title {
  text-decoration: line-through;
  color: #6B7280;
}

/* Priority Badges */
.priority-badge {
  display: inline-flex;
  padding: 4px 12px;
  border-radius: 9999px;
  font-size: 12px;
  font-weight: 600;
}

.priority-high {
  background: #FEE2E2;
  color: #DC2626;
}

.priority-medium {
  background: #FEF3C7;
  color: #D97706;
}

.priority-low {
  background: #D1FAE5;
  color: #059669;
}
```

### Create Todo Modal

**Visual Specs:**
```
Width: 600px (desktop), 90vw (mobile, max 400px)
Height: Auto (max 80vh)
Background: #FFFFFF
Border-radius: 16px
Shadow: 0 20px 50px rgba(0, 0, 0, 0.2)
Backdrop: rgba(0, 0, 0, 0.5) blur(4px)

Animation:
- Entry: Fade + Scale from 0.9 to 1.0 (300ms ease-out)
- Exit: Fade + Scale from 1.0 to 0.9 (200ms ease-in)

Header:
- Height: 64px
- Padding: 20px 24px
- Border-bottom: 1px solid #E5E7EB
- Title: H3 (20px, 600 weight, #111827)
- Close Button: 32x32px, hover: bg #F3F4F6

Body:
- Padding: 24px
- Form fields gap: 20px

Footer:
- Height: 72px
- Padding: 16px 24px
- Border-top: 1px solid #E5E7EB
- Buttons: Right-aligned, gap 12px
```

## Phase 6: Interactions & Animations

### Micro-Interactions

#### 1. Todo Check Animation
```css
@keyframes checkTodo {
  0% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(1.1);
  }
  100% {
    transform: scale(1);
    opacity: 0.6;
  }
}

.todo-card.being-checked {
  animation: checkTodo 300ms ease-out;
}

/* Strikethrough animation */
@keyframes strikethrough {
  from {
    width: 0;
  }
  to {
    width: 100%;
  }
}

.todo-title::after {
  content: '';
  position: absolute;
  height: 2px;
  background: currentColor;
  animation: strikethrough 300ms ease-out;
}
```

#### 2. Button Hover
```css
.button-primary {
  transition: all 150ms ease-out;
}

.button-primary:hover {
  transform: scale(1.02);
  background-color: #2563EB;
  box-shadow: 0 8px 16px rgba(59, 130, 246, 0.2);
}

.button-primary:active {
  transform: scale(0.98);
}
```

#### 3. Modal Appearance
```css
@keyframes modalIn {
  from {
    opacity: 0;
    transform: scale(0.9) translateY(-20px);
  }
  to {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}

.modal {
  animation: modalIn 300ms ease-out;
}

@keyframes backdropIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.modal-backdrop {
  animation: backdropIn 200ms ease-out;
}
```

## Phase 7: Design-Handoff

### For Developers: Component Specs

#### Button Component
```tsx
// Button.tsx
interface ButtonProps {
  variant: 'primary' | 'secondary' | 'ghost';
  size: 'sm' | 'md' | 'lg';
  children: React.ReactNode;
  icon?: React.ReactNode;
  iconPosition?: 'left' | 'right';
  loading?: boolean;
  disabled?: boolean;
  fullWidth?: boolean;
  onClick?: () => void;
}

// Figma: Components / Buttons / Primary
// Variants: Size (sm/md/lg), States (all)
```

#### Todo Card Component
```tsx
// TodoCard.tsx
interface TodoCardProps {
  id: string;
  title: string;
  description?: string;
  dueDate?: Date;
  priority: 'high' | 'medium' | 'low';
  category: string;
  completed: boolean;
  onToggle: (id: string) => void;
  onEdit: (id: string) => void;
  onDelete: (id: string) => void;
}

// Figma: Components / Cards / Todo Card
// States: Default, Hover, Completed
// Variants: Priority (high/medium/low)
```

### CSS Variables Export
```css
/* Generated from Figma Design System */
:root {
  /* Colors - Primary */
  --color-primary-50: #EFF6FF;
  --color-primary-500: #3B82F6;
  --color-primary-600: #2563EB;
  --color-primary-700: #1D4ED8;
  
  /* Semantic Colors */
  --color-success: #10B981;
  --color-warning: #F59E0B;
  --color-error: #EF4444;
  
  /* Typography */
  --font-family: 'Inter', -apple-system, sans-serif;
  --font-size-h1: 32px;
  --font-size-h2: 24px;
  --font-size-h3: 20px;
  --font-size-body: 16px;
  --font-size-small: 14px;
  --font-size-caption: 12px;
  
  /* Spacing */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
  
  /* Shadows */
  --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  
  /* Border Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-full: 9999px;
  
  /* Transitions */
  --transition-fast: 150ms ease-out;
  --transition-base: 200ms ease-out;
  --transition-slow: 300ms ease-out;
}
```

### Assets Export

**Icons** (from Figma):
```
exports/icons/
├─ check.svg
├─ plus.svg
├─ edit.svg
├─ delete.svg
├─ calendar.svg
├─ category.svg
└─ menu.svg

Format: SVG, optimized
Size: 24x24px (scale via CSS)
Color: currentColor (inherit from parent)
```

## Integration mit d-kit Workflow

### Timeline mit UI-Design
```
Sprint 0 (Setup & Design):
├─ Week 1: Requirements → MVP-Plan
└─ Week 2: UI-Design (Figma)
    ├─ Day 1-2: Design System
    ├─ Day 3-4: Wireframes + Mockups
    ├─ Day 5: Prototype
    └─ Design Review ✓

Sprint 1 (Development):
├─ Day 1-2: Setup + Auth (no complex UI)
├─ Day 3-5: Todo CRUD (following Figma)
└─ Day 6-7: Testing + Polish

Sprint 2:
├─ Implement remaining screens
└─ Match Figma designs exactly
```

### Design-to-Code Flow
```
Figma Screen
    ↓
Task-Design-Dokument (references Figma)
    ↓
Code Implementation (follows Figma specs)
    ↓
Visual QA (compare with Figma)
    ↓
Pixel-perfect? → Ship
    └─ No → Iterate
```

## Figma-Links (Beispiel)

```markdown
## Design-Deliverables

**Figma File**: https://figma.com/file/abc123/TodoFlow

### Screens
- Dashboard: https://figma.com/file/abc123/TodoFlow?node-id=1:2
- Create Modal: https://figma.com/file/abc123/TodoFlow?node-id=1:50
- Mobile Views: https://figma.com/file/abc123/TodoFlow?node-id=2:1

### Prototype
- User Flow: https://figma.com/proto/abc123/TodoFlow?node-id=1:2

### Design System
- Components: https://figma.com/file/abc123/TodoFlow?node-id=0:1
- Colors & Type: https://figma.com/file/abc123/TodoFlow?node-id=0:100
```

## Zusammenfassung

**Mit Figma-Integration hat d-kit nun**:
- ✅ Kompletter Design-zu-Code Workflow
- ✅ Klare visuelle Spezifikationen
- ✅ Konsistentes Design-System
- ✅ Prototype für User-Testing
- ✅ Assets ready für Implementation
- ✅ Design-Handoff-Dokumentation

**Resultat**: Entwickler wissen exakt was zu bauen ist! 🎨→💻