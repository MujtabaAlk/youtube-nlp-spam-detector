from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Config:
    app_name: str
    db_connection_url: str
