from __future__ import annotations

from dataclasses import dataclass

@dataclass
class Log:
    id: str
    timestamp: str
    message: str