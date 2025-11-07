# Grok-Integration mit xAI Collections

Mit xAI **Collections** können wir die d-kit Templates, Checklisten und Scripts als Wissensbasis für Grok verfügbar machen. Dieses Dokument beschreibt, wie Sie die Inhalte hochladen und Grok dazu bringen, sie bei jeder Aufgabe einzusetzen.

## 1. Voraussetzungen
- xAI Account (Grok) mit Zugriff auf die Verwaltungskonsole
- `XAI_API_KEY` und `XAI_MANAGEMENT_API_KEY`
- Python ≥3.10 und das offizielle `xai-sdk` Paket
- Dieses Repository (z. B. geklont nach `/path/to/d-kit`)

## 2. Inhalte vorbereiten
Die relevanten Dateien liegen gebündelt unter `shared/skill-common/`. Optional können Sie nur ausgewählte Dateien hochladen (z. B. `SKILL.md`, `references/prompts/*.md`).

```bash
# Alle gemeinsamen Assets aktualisieren
./tools/sync_skill_assets.sh
```

> Tipp: Für Grok empfiehlt es sich, jede Prompt/Checklist als eigene Datei hochzuladen, damit die semantische Suche gezielte Treffer liefert.

## 3. Collection anlegen
### Via Konsole
1. xAI Console → Tab **Collections** → *Create new collection*
2. Namen vergeben, „Generate embeddings“ aktiviert lassen

### Via Python
```python
from xai_sdk import Client
import os

client = Client(
    api_key=os.environ["XAI_API_KEY"],
    management_api_key=os.environ["XAI_MANAGEMENT_API_KEY"],
    timeout=3600,
)

collection = client.collections.create(name="d-kit-skill")
print(collection.id)
```
Notieren Sie die `collection_id` – sie wird später im Prompt benötigt.

## 4. Dateien hochladen
> Aktuell (Nov 2025) unterstützt xAI Uploads nur über SDK/Console, nicht via REST.

```python
from pathlib import Path

collection_id = "collection_xxxxx"
shared_root = Path("/path/to/d-kit/shared/skill-common")

for file_path in shared_root.rglob("*.md"):
    with open(file_path, "rb") as fh:
        document = client.collections.upload_document(
            collection_id=collection_id,
            name=str(file_path.relative_to(shared_root)),
            data=fh.read(),
            content_type="text/markdown",
        )
        print("Uploaded", document.id)
```
Optional können Sie auch die Python-Skripte (z. B. `code_analysis.py`) hochladen – setzen Sie dann `content_type="text/x-python"`.

## 5. Relevante Dokumente suchen
```python
response = client.collections.search(
    query="Wie lautet der d-kit Prozess?",
    collection_ids=[collection_id],
)
print(response)
```
Der Response enthält `results` mit `file_id`, `score` und Ausschnitten, die Sie Grok als Kontext übergeben können.

## 6. Prompts für Grok
Damit Grok die Collection ernst nimmt, nutzen Sie einen Startprompt in jeder Session. Beispiel:

```
You have access to the xAI Collection "d-kit-skill" (ID: collection_xxxxx).
Whenever a task involves software planning, design, implementation, testing or release:
1. Call `collections.search` with the user request as query and read the top matches.
2. Summarize the instructions contained in the files (e.g., SKILL.md, references/prompts/*, references/checklists/*).
3. Follow the d-kit workflow exactly and cite which file/chapter you used.
4. Convert every checklist item into update_plan tasks and tick them off.
Do NOT write code or plans before you have read the relevant files from the collection.
```

Weitere spezialisierte Prompts:
- **Dokumente abrufen:**
  ```
  First run `collections.search` with query "task-design" in collection_xxxxx and read the file references/prompts/task-design.md. Summarize the steps and then apply them to the current task.
  ```
- **Retrospektive:**
  ```
  Fetch references/templates/retrospektive.md from collection_xxxxx and lead me through the template. Ask me for each section.
  ```

## 7. Workflows absichern
- Hinterlegen Sie den Startprompt als „System Prompt“ in Grok Codex / Desktop.
- Alternativ können Sie Collections mit `get_usage_guide`-ähnlichen Anweisungen kombinieren, indem Sie Grok vorgeben: „Wenn Du d-kit hörst, suche zuerst in collection_xxxxx“. 
- Bei Team-Nutzung empfiehlt sich, Collection-IDs sowie Beispielprompts in einem Handbuch zu teilen.

## 8. Pflege
- Wenn sich Templates ändern, erneut `./tools/sync_skill_assets.sh` ausführen und die betroffenen Dateien neu hochladen. 
- Über `client.collections.remove_document` können Sie alte Dateien löschen, bevor Sie die aktualisierte Version einspielen.

Mit diesem Setup kann Grok jederzeit auf den vollständigen d-kit Skill zugreifen und bleibt synchron mit den Claude/Codex/Gemini-Versionen.
