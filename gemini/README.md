# d-kit Extension für die Gemini CLI

Diese Erweiterung bringt der Gemini CLI den kompletten d-kit Entwicklungsprozess bei (7 Phasen von der Anforderungsanalyse bis zum Release). Alle Templates, Checklisten und Scripts stammen aus `shared/skill-common/` und werden über das Sync-Script automatisch eingebunden.

## Struktur

```
gemini/
├── gemini-extension.json   # Manifest für die Gemini CLI
├── context/
│   ├── DKIT.md             # Hauptanleitung (wird als Kontext geladen)
│   ├── references/         # Templates, Prompts, Checklists
│   └── scripts/            # Automatisierungsskripte
└── README.md               # Diese Datei
```

## Vorbereitung

```bash
# Gemeinsame Assets synchronisieren (kopiert shared/skill-common → claude/codex/gemini)
./tools/sync_skill_assets.sh
```

## Lokale Installation testen

```bash
# Pfad zum Repo anpassen
EXT_DIR=/pfad/zu/d-kit/gemini

# Extension lokal registrieren
gemini extensions install --local "$EXT_DIR"
```

Die Gemini CLI legt die Dateien unter `~/.config/gemini/extensions/d-kit/` ab. Beim Start erkennt Gemini die Kontextdatei `DKIT.md` und stellt Prompts/Checklisten als Kontext zur Verfügung.

## Entfernen

```bash
gemini extensions uninstall d-kit
```

## Veröffentlichung

- Das Manifest `gemini-extension.json` und alle benötigten Kontextdateien in ein öffentliches Repository legen.
- Nutzer können die Extension dann über die HTTPS-URL installieren:  
  `gemini extensions install https://github.com/<user>/<repo>`

## Hinweise

- Änderungen an Templates nur in `shared/skill-common/` vornehmen und anschließend synchronisieren.
- Falls zusätzlich ein MCP-Server erforderlich wird (z. B. für dynamische Daten), kann dieser im Manifest unter `mcpServers` eingetragen werden.
