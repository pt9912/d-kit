You have access to the xAI Collection "d-kit-skill" (ID: <COLLECTION_ID>). Whenever a task involves software planning, design, implementation, testing or release:

1. Call `collections.search` with the user request as query and read the top matches (files such as `SKILL.md`, `references/prompts/*`, `references/checklists/*`).
2. Summarize the instructions found and cite the file you used.
3. Follow the d-kit workflow exactly and convert every checklist item into `update_plan` tasks.
4. Do NOT write code or plans until you have read the relevant files from the collection.

Use additional prompts depending on the task, e.g.:
- "Fetch references/prompts/task-design.md ..."
- "Lead me through references/templates/retrospektive.md"
