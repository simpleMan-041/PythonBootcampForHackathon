from __future__ import annotations

import json
import logging
from pathlib import Path
from uuid import uuid4

from models.log import Log
from utils.time_utils import now_str
from utils.json_utils import read_json, write_json

class LogService:
    def __init__(self, data_dir: Path):
        self.log_file = data_dir / "logs.json"
    
    def load(self) -> list[Log]:
        raw = read_json(self.log_file)
        if raw is None:
            logging.info("ログファイルが存在しないか空です。")
            return []
        return [Log(**item) for item in raw] # Logクラスのリストに変換している
    
    def save(self, logs: list[Log]) -> None:
        write_json(self.log_file, [log.__dict__ for log in logs])
        logging.info("ログファイルを保存しました。全体で %d 件のログがあります。", len(logs))
    
    def add(self, message: str) -> Log:
        return Log(
            id=str(uuid4()),
            timestamp=now_str(),
            message=message,
        )
    
    def delete_by_id(self, logs: list[Log], log_id: str) -> tuple:
        before = len(logs)
        logs = [ x for x in logs if x.id != log_id ]
        deleted = len(logs) != before
        return logs, deleted