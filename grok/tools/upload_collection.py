#!/usr/bin/env python3
import argparse
import os
from pathlib import Path
from xai_sdk import Client

def upload_files(collection_id: str, root: Path):
    client = Client(
        api_key=os.environ["XAI_API_KEY"],
        management_api_key=os.environ["XAI_MANAGEMENT_API_KEY"],
        timeout=3600,
    )
    for file_path in root.rglob("*"):
        if file_path.is_file():
            rel = file_path.relative_to(root)
            content_type = "text/markdown" if file_path.suffix in {".md"} else "text/plain"
            with file_path.open("rb") as fh:
                document = client.collections.upload_document(
                    collection_id=collection_id,
                    name=str(rel),
                    data=fh.read(),
                    content_type=content_type,
                )
                print("Uploaded", rel, "->", document.id)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--collection-id", required=True)
    parser.add_argument("--root", default="shared/skill-common")
    args = parser.parse_args()
    upload_files(args.collection_id, Path(args.root))
