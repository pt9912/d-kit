#!/bin/bash

# validate_skill.sh - Validate d-kit skill structure and content

set -e

echo "🔍 Validating d-kit skill..."
echo ""

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
SKILL_DIR="$PROJECT_ROOT/skill"

ERRORS=0
WARNINGS=0

# Function to report error
error() {
    echo "❌ ERROR: $1"
    ((ERRORS++))
}

# Function to report warning
warning() {
    echo "⚠️  WARNING: $1"
    ((WARNINGS++))
}

# Function to report success
success() {
    echo "✅ $1"
}

# Check SKILL.md exists
echo "Checking SKILL.md..."
if [ -f "$SKILL_DIR/SKILL.md" ]; then
    success "SKILL.md found"
    
    # Check frontmatter
    if grep -q "^name: " "$SKILL_DIR/SKILL.md" && grep -q "^description: " "$SKILL_DIR/SKILL.md"; then
        success "YAML frontmatter present"
    else
        error "YAML frontmatter missing or incomplete"
    fi
    
    # Check minimum content length
    LINES=$(wc -l < "$SKILL_DIR/SKILL.md")
    if [ "$LINES" -gt 100 ]; then
        success "SKILL.md has sufficient content ($LINES lines)"
    else
        warning "SKILL.md seems short ($LINES lines)"
    fi
else
    error "SKILL.md not found"
fi
echo ""

# Check scripts directory
echo "Checking scripts..."
if [ -d "$SKILL_DIR/scripts" ]; then
    success "scripts/ directory exists"
    
    SCRIPT_COUNT=$(find "$SKILL_DIR/scripts" -type f -name "*.py" | wc -l)
    if [ "$SCRIPT_COUNT" -gt 0 ]; then
        success "Found $SCRIPT_COUNT Python script(s)"
        
        # Check if scripts are executable
        for script in "$SKILL_DIR/scripts"/*.py; do
            if [ -x "$script" ]; then
                success "$(basename "$script") is executable"
            else
                warning "$(basename "$script") is not executable"
            fi
        done
    else
        warning "No Python scripts found in scripts/"
    fi
else
    error "scripts/ directory not found"
fi
echo ""

# Check references directory
echo "Checking references..."
if [ -d "$SKILL_DIR/references" ]; then
    success "references/ directory exists"
    
    # Check prompts
    if [ -d "$SKILL_DIR/references/prompts" ]; then
        PROMPT_COUNT=$(find "$SKILL_DIR/references/prompts" -type f -name "*.md" | wc -l)
        if [ "$PROMPT_COUNT" -gt 0 ]; then
            success "Found $PROMPT_COUNT prompt template(s)"
        else
            warning "No prompt templates found"
        fi
    else
        warning "references/prompts/ directory not found"
    fi
    
    # Check templates
    if [ -d "$SKILL_DIR/references/templates" ]; then
        TEMPLATE_COUNT=$(find "$SKILL_DIR/references/templates" -type f -name "*.md" | wc -l)
        if [ "$TEMPLATE_COUNT" -gt 0 ]; then
            success "Found $TEMPLATE_COUNT document template(s)"
        else
            warning "No document templates found"
        fi
    else
        warning "references/templates/ directory not found"
    fi
    
    # Check checklists
    if [ -d "$SKILL_DIR/references/checklists" ]; then
        CHECKLIST_COUNT=$(find "$SKILL_DIR/references/checklists" -type f -name "*.md" | wc -l)
        if [ "$CHECKLIST_COUNT" -gt 0 ]; then
            success "Found $CHECKLIST_COUNT checklist(s)"
        else
            warning "No checklists found"
        fi
    else
        warning "references/checklists/ directory not found"
    fi
else
    error "references/ directory not found"
fi
echo ""

# Check for common issues
echo "Checking for common issues..."

# Check for TODO markers
TODO_COUNT=$(grep -r "TODO" "$SKILL_DIR" --include="*.md" | wc -l)
if [ "$TODO_COUNT" -gt 0 ]; then
    warning "Found $TODO_COUNT TODO marker(s) in documentation"
fi

# Check for placeholder text
PLACEHOLDER_COUNT=$(grep -r "\[PLACEHOLDER\]" "$SKILL_DIR" --include="*.md" | wc -l)
if [ "$PLACEHOLDER_COUNT" -gt 0 ]; then
    error "Found $PLACEHOLDER_COUNT placeholder(s) that need to be replaced"
fi

echo ""

# Summary
echo "════════════════════════════════════════"
echo "Validation Summary"
echo "════════════════════════════════════════"
if [ "$ERRORS" -eq 0 ] && [ "$WARNINGS" -eq 0 ]; then
    echo "✅ All checks passed!"
    exit 0
elif [ "$ERRORS" -eq 0 ]; then
    echo "⚠️  Passed with $WARNINGS warning(s)"
    exit 0
else
    echo "❌ Failed with $ERRORS error(s) and $WARNINGS warning(s)"
    exit 1
fi
