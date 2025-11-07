#!/bin/bash

# Synchronisiert gemeinsame Skill-Ressourcen im Build (Claude, Codex, Gemini).

set -euo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

SHARED_DIR="$REPO_ROOT/shared/skill-common"
CLAUDE_DIR="$REPO_ROOT/claude/skill"
CODEX_DIR="$REPO_ROOT/codex/skills/d-kit"
GEMINI_DIR="$REPO_ROOT/gemini/context"

if [ ! -d "$SHARED_DIR" ]; then
  echo "❌ Gemeinsamer Skill-Ordner nicht gefunden: $SHARED_DIR" >&2
  exit 1
fi

sync_dir() {
  local source="$1"
  local target="$2"
  local label="$3"

  echo "➡️  Befülle $label aus gemeinsamen Quellen"
  rm -rf "$target/references" "$target/scripts"
  rsync -a "$source/references/" "$target/references/"
  rsync -a "$source/scripts/" "$target/scripts/"
}

sync_dir "$SHARED_DIR" "$CLAUDE_DIR" "Claude Skill"
sync_dir "$SHARED_DIR" "$CODEX_DIR" "Codex Skill"
sync_dir "$SHARED_DIR" "$GEMINI_DIR" "Gemini Extension"

echo "✅ Skill-Ressourcen aktualisiert."
