#!/bin/bash

# package_skill.sh - Package the d-kit skill for distribution

set -e

echo "📦 Packaging d-kit skill..."

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
SKILL_DIR="$PROJECT_ROOT/skill"
RELEASES_DIR="$PROJECT_ROOT/releases"
REPO_ROOT="$(dirname "$PROJECT_ROOT")"

# Gemeinsame Skill-Ressourcen synchronisieren
SYNC_SCRIPT="$REPO_ROOT/tools/sync_skill_assets.sh"
if [ -x "$SYNC_SCRIPT" ]; then
    echo "🔄 Synchronisiere gemeinsame Skill-Ressourcen..."
    "$SYNC_SCRIPT"
    echo ""
else
    echo "⚠️  Sync-Script $SYNC_SCRIPT nicht gefunden oder nicht ausführbar."
    echo "    Bitte sicherstellen, dass gemeinsame Ressourcen konsistent sind."
    echo ""
fi

# Get version from CHANGELOG
VERSION=$(grep -m 1 "^## \[" "$PROJECT_ROOT/CHANGELOG.md" | sed 's/.*\[\(.*\)\].*/\1/')

if [ -z "$VERSION" ]; then
    echo "❌ Error: Could not determine version from CHANGELOG.md"
    exit 1
fi

echo "   Version: $VERSION"
echo "   Skill directory: $SKILL_DIR"
echo "   Output directory: $RELEASES_DIR"
echo ""

# Validate skill structure
echo "🔍 Validating skill structure..."

if [ ! -f "$SKILL_DIR/SKILL.md" ]; then
    echo "❌ Error: SKILL.md not found in $SKILL_DIR"
    exit 1
fi

if [ ! -d "$SKILL_DIR/scripts" ] || [ ! -d "$SKILL_DIR/references" ]; then
    echo "❌ Error: Required directories (scripts, references) not found"
    exit 1
fi

echo "✅ Skill structure is valid"
echo ""

# Create releases directory if it doesn't exist
mkdir -p "$RELEASES_DIR"

# Package the skill
OUTPUT_FILE="$RELEASES_DIR/d-kit-v${VERSION}.skill"

echo "📦 Creating package: d-kit-v${VERSION}.skill"

cd "$PROJECT_ROOT"
zip -r "$OUTPUT_FILE" skill/ -x "*.pyc" -x "*__pycache__*" -x "*.DS_Store" > /dev/null

if [ $? -eq 0 ]; then
    echo "✅ Successfully packaged skill to: $OUTPUT_FILE"
    
    # Show file size
    FILE_SIZE=$(du -h "$OUTPUT_FILE" | cut -f1)
    echo "   File size: $FILE_SIZE"
    echo ""
    
    # Create latest symlink
    ln -sf "d-kit-v${VERSION}.skill" "$RELEASES_DIR/d-kit-latest.skill"
    echo "✅ Created symlink: d-kit-latest.skill"
    
    echo ""
    echo "🎉 Packaging complete!"
    echo ""
    echo "Next steps:"
    echo "  1. Test the skill by importing it into Claude"
    echo "  2. Create a GitHub release with this file"
    echo "  3. Update documentation if needed"
else
    echo "❌ Error: Failed to create package"
    exit 1
fi
