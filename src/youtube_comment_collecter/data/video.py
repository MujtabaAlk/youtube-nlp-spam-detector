from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field

from youtube_comment_collecter.data.comment_thread import CommentThread


@dataclass
class Video:
    id: str
    title: str = field(default_factory=str)
    description: str = field(default_factory=str)
    comment_threads: list[CommentThread] = field(default_factory=list)
