# d-kit Skills für OpenAI Codex

Dieser Ordner enthält eine Codex-kompatible Version des d-kit Skill-Bundles. Ziel ist es, denselben strukturierten Entwicklungsprozess wie unter `claude/` auch im OpenAI Codex CLI verfügbar zu machen.

## Ordnerstruktur

```
codex/
├── README.md                      # Diese Anleitung
├── bootstrap/
│   └── AGENTS-snippet.md          # Textbaustein für ~/.codex/AGENTS.md
├── skills/
│   └── d-kit/                     # Skill-Inhalte (SKILL.md, Templates, Scripts, …)
└── tools/
    └── install_skill.sh           # Helferscript zum Installieren/Aktualisieren
```

## Voraussetzungen

- OpenAI Codex CLI (GPT-5 Codex)
- Schreibzugriff auf `~/.codex/`
- macOS oder Linux Shell (Bash) für das Installationsscript

## Installation

1. **Skill-Dateien kopieren**

   ```bash
   cd /pfad/zu/d-kit
   ./codex/tools/install_skill.sh
   ```

   Das Script synchronisiert alle Dateien nach `~/.codex/skills/d-kit/` und zeigt anschließend an, wie der Bootstrap-Snippet übernommen wird.

2. **Bootstrap aktivieren**

   Öffne `~/.codex/AGENTS.md` und füge – falls noch nicht vorhanden – den Inhalt aus `codex/bootstrap/AGENTS-snippet.md` am Ende ein. Dadurch erinnert sich Codex beim Start daran, dass die d-kit Skills verfügbar sind und wie sie genutzt werden.

3. **Codex neu starten**

   Starte deine Codex-Session neu. Beim nächsten Start sollte Codex ankündigen, dass der Skill verfügbar ist. Wenn eine Aufgabe zum strukturierten Softwareprozess passt, wird Codex automatisch `~/.codex/skills/d-kit/SKILL.md` lesen.

## Updates

Bei Änderungen im Repository genügt es, das Installationsscript erneut auszuführen. Es synchronisiert die Dateien inkrementell:

```bash
cd /pfad/zu/d-kit
./codex/tools/install_skill.sh
```

## Manuelle Installation (falls gewünscht)

1. Verzeichnis `~/.codex/skills/d-kit/` anlegen   
2. Inhalt aus `codex/skills/d-kit/` dorthin kopieren   
3. Snippet aus `codex/bootstrap/AGENTS-snippet.md` in `~/.codex/AGENTS.md` übernehmen

## Verwendung in Codex

- Ein Skill wird gelesen, indem Codex die Datei `~/.codex/skills/d-kit/SKILL.md` lädt (`open_file ~/.codex/skills/d-kit/SKILL.md` oder `cat`) und die Anweisungen befolgt.
- Templates liegen unter `~/.codex/skills/d-kit/references/…`.
- Automatisierungsskripte stehen unter `~/.codex/skills/d-kit/scripts/…` zur Verfügung.
- Checklisten sollten in `update_plan` Aufgaben verwandelt werden, damit Codex einen nachvollziehbaren Fortschritt dokumentiert.

## Deinstallation

```bash
rm -rf ~/.codex/skills/d-kit
```

Optional den Eintrag in `~/.codex/AGENTS.md` entfernen.

---

Viel Erfolg beim Einsatz von d-kit Skills in Codex! Feedback oder Erweiterungen sind jederzeit willkommen.

> **Hinweis:** Templates, Prompts und Scripts werden zentral in `shared/skill-common/` gepflegt.  
> Führe nach Anpassungen `./tools/sync_skill_assets.sh` aus, um die Inhalte nach `claude/skill/` und `codex/skills/d-kit/` zu kopieren.
