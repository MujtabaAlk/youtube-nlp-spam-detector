from __future__ import annotations

from typing import Optional
from typing import TypedDict

from youtube_comment_collecter.api_resources.comment_resource import (
    CommentResource,
)


class CommentThreadResource(TypedDict):
    kind: str
    etag: str
    id: str
    snippet: _Snippet
    replies: Optional[_Replies]


class _Snippet(TypedDict):
    channelId: str
    videoId: str
    topLevelComment: CommentResource
    canReply: bool
    totalReplyCount: int
    isPublic: bool


class _Replies(TypedDict):
    comments: list[CommentResource]


class CommentThreadListResponse(TypedDict):
    kind: str
    etag: str
    nextPageToken: Optional[str]
    pageInfo: _PageInfo
    items: list[CommentThreadResource]


class _PageInfo(TypedDict):
    totalResults: int
    resultsPerPage: int
