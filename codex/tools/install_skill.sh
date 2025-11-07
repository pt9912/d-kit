#!/bin/bash

# Installiert oder aktualisiert den d-kit Skill für das OpenAI Codex CLI.

set -euo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
CODEX_ROOT="$(dirname "$SCRIPT_DIR")"
REPO_ROOT="$(dirname "$CODEX_ROOT")"

SKILL_NAME="d-kit"
SOURCE_DIR="$CODEX_ROOT/skills/$SKILL_NAME"
TARGET_ROOT="${HOME}/.codex/skills"
TARGET_DIR="$TARGET_ROOT/$SKILL_NAME"
SNIPPET_FILE="$CODEX_ROOT/bootstrap/AGENTS-snippet.md"

if [ ! -d "$SOURCE_DIR" ]; then
  echo "❌ Quelle für Skill '$SKILL_NAME' nicht gefunden: $SOURCE_DIR" >&2
  exit 1
fi

echo "📦 Installiere d-kit Skill für Codex"
echo "   Quelle : $SOURCE_DIR"
echo "   Ziel   : $TARGET_DIR"
echo ""

mkdir -p "$TARGET_ROOT"

if [ -d "$TARGET_DIR" ]; then
  echo "⚠️  Hinweis: Lokale Änderungen in $TARGET_DIR werden durch '--delete' überschrieben."
  echo "    Eigene Templates bitte vor dem Update sichern!"
fi

# Synchronisiere Dateien (inkl. Entfernen veralteter Dateien)
rsync -a --delete "$SOURCE_DIR/" "$TARGET_DIR/"

echo "✅ Skill-Dateien wurden aktualisiert."
echo ""

if [ -f "$SNIPPET_FILE" ]; then
  echo "📌 Bootstrap-Hinweis"
  echo "   Bitte füge (falls noch nicht vorhanden) den folgenden Abschnitt zu ~/.codex/AGENTS.md hinzu:"
  echo ""
  cat "$SNIPPET_FILE"
  echo ""
else
  echo "⚠️  Hinweis: Bootstrap-Snippet $SNIPPET_FILE wurde nicht gefunden."
fi

echo "✨ Installation abgeschlossen. Starte eine neue Codex-Session, damit der Skill erkannt wird."
