from __future__ import annotations

from datetime import datetime
from typing import Any
from typing import Optional

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import relationship

from database.models.base import Base
from database.models.video import Video


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, autoincrement=True)
    youtube_id = Column(String, nullable=False, unique=True)
    author_display_name = Column(String, nullable=False)
    text = Column(Text)
    parent_id = Column(String)
    like_count = Column(Integer, nullable=False)
    published_at = Column(DateTime, nullable=False)

    video_id = Column(String, ForeignKey("video.youtube_id"), nullable=False)
    video: Video = relationship(Video)

    def __init__(
        self,
        *args: tuple[Any],
        youtube_id: str,
        video_id: str,
        author_display_name: str,
        text: str,
        parent_id: Optional[str] = None,
        like_count: int,
        published_at: datetime,
        **kwargs: dict[str, Any],
    ) -> None:
        self.youtube_id = youtube_id
        self.video_id = video_id
        self.author_display_name = author_display_name
        self.text = text
        self.parent_id = parent_id
        self.like_count = like_count
        self.published_at = published_at

        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return (
            f"[{self.id}]{type(self).__name__}(youtube_id={self.youtube_id!r},"
            f" author_display_name={self.author_display_name!r},"
            f" text={self.text!r}, parent_id={self.parent_id!r},"
            f" like_count={self.like_count!r},"
            f" published_at={self.published_at!r}, video_id={self.video_id!r})"
        )

    @property
    def is_top_level_comment(self) -> bool:
        return self.parent_id is None
