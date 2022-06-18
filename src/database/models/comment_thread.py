from __future__ import annotations

from typing import Any

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from database.models.base import Base
from database.models.comment import Comment
from database.models.video import Video


class CommentThread(Base):
    __tablename__ = "comment_thread"

    id = Column(Integer, primary_key=True, autoincrement=True)
    youtube_id = Column(String, nullable=False, unique=True)

    video_id = Column(String, ForeignKey("video.youtube_id"), nullable=False)
    video: Video = relationship(Video, back_populates="comment_threads")
    top_level_comment_id = Column(
        String, ForeignKey("comment.youtube_id"), nullable=False
    )
    top_level_comment: Comment = relationship(Comment)

    def __init__(
        self,
        *args: tuple[Any],
        youtube_id: str,
        video_id: str,
        **kwargs: dict[str, Any],
    ) -> None:
        self.youtube_id = youtube_id
        self.video_id = video_id

        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        return (
            f"[{self.id}]{type(self).__name__}(youtube_id={self.youtube_id!r},"
            f" video_id={self.video_id!r},"
            f" top_level_comment_id={self.top_level_comment_id!r})"
        )
