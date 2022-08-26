from __future__ import annotations

from typing import TypedDict


class CommentResource(TypedDict):
    kind: str
    etag: str
    id: str
    snippet: _Snippet


class _Snippet(TypedDict):
    authorDisplayName: str
    authorProfileImageUrl: str
    authorChannelUrl: str
    authorChannelId: _AuthorChannelId
    channelId: str
    videoId: str
    textDisplay: str
    textOriginal: str
    parentId: str
    canRate: bool
    viewerRating: str
    likeCount: int
    moderationStatus: str
    publishedAt: str
    updatedAt: str


class _AuthorChannelId(TypedDict):
    value: str
