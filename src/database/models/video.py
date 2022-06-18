from __future__ import annotations

from typing import Any

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from database.models.base import Base


class Video(Base):
    __tablename__ = "video"

    id = Column(Integer, primary_key=True, autoincrement=True)
    youtube_id = Column(String, nullable=False, unique=True)

    def __init__(
        self, *args: tuple[Any], youtube_id: str, **kwargs: dict[str, Any]
    ) -> None:
        self.youtube_id = youtube_id

        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return (
            f"[{self.id}]{type(self).__name__}(youtube_id={self.youtube_id!r})"
        )
