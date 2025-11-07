# d-kit für Grok (xAI Collections)

Dieser Ordner enthält Skripte und Prompts, um die d-kit Templates über xAI Collections für Grok bereitzustellen.

## Ablauf

1. **Gemeinsame Dateien synchronisieren**
   ```bash
   ./tools/sync_skill_assets.sh
   ```
2. **Collection anlegen**
   - Konsole: xAI → Collections → Create New Collection → Embeddings aktiv lassen
   - oder via Script (siehe unten)
3. **Dateien hochladen**
   ```bash
   python grok/tools/upload_collection.py --collection-id <ID> --root shared/skill-common
   ```
4. **Prompts verwenden**
   - Siehe `grok/prompts/collections-start.md` für System-Prompt / Anweisungen

## Dateien
- `prompts/collections-start.md` – Startprompt, der Grok zwingt, via Collections zu suchen
- `tools/upload_collection.py` – Upload-Script mit xAI SDK
- `README.md` – diese Übersicht

Weitere Details siehe `docs/grok-collections.md`.
