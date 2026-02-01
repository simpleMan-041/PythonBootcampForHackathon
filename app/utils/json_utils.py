from __future__ import annotations

import json
from pathlib import Path
from typing import Any

def read_json(path: Path) -> Any:
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        return None
    return json.loads(text)

def write_json(path: Path, data: Any) -> None:
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=4),
        encoding="utf-8"
    )