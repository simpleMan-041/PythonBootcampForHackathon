from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime
from uuid import uuid4

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data" 
LOG_FILE = DATA_DIR / "logs.json"

def now_str() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def load_logs() -> list[dict]:
    if not LOG_FILE.exists():
        return []
    
    text = LOG_FILE.read_text(encoding="utf-8")
    if not text.strip():
        return []
    
    return json.loads(text)

def save_logs(logs: list[dict]) -> None:
    LOG_FILE.write_text(
        json.dumps(logs, indent=4), 
        encoding="utf-8"
        )

def add_log(message: str) -> dict:
    return {
        "id": str(uuid4()),
        "timestamp": now_str(),
        "message": message
    }

def main() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    
    logs = load_logs()
    logs.append(add_log("Day3: uuid/json/datetime を学習"))
    save_logs(logs)
    
    print(f"保存先: {LOG_FILE}")
    print(f"件数: {len(logs)}")
    print(json.dumps(logs[-1], ensure_ascii=False, indent=4))
    
if __name__ == "__main__":
    main()
