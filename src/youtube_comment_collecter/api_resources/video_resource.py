from __future__ import annotations

from typing import TypedDict


class VideoResource(TypedDict):
    kind: str
    etag: str
    id: str
    statistics: _Statistics


class _Statistics(TypedDict):
    viewCount: int
    likeCount: int
    dislikeCount: int
    favoriteCount: int
    commentCount: int
