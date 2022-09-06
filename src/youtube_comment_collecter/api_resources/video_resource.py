from __future__ import annotations

from typing import Optional
from typing import TypedDict


class VideoResource(TypedDict):
    kind: str
    etag: str
    id: str
    snippet: _Snippet
    statistics: _Statistics


class _Statistics(TypedDict):
    viewCount: int
    likeCount: int
    favoriteCount: int
    commentCount: int


class _Snippet(TypedDict):
    publishedAt: str
    channelId: str
    title: str
    description: str


class VideoListResponse(TypedDict):
    kind: str
    etag: str
    nextPageToken: Optional[str]
    prevPageToken: Optional[str]
    pageInfo: _PageInfo
    items: list[VideoResource]


class _PageInfo(TypedDict):
    totalResults: int
    resultsPerPage: int
