from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Comment:
    comment_id: str
    author_name: str
    author_id: str
    video_id: str
    text: str
    like_count: int
    parent_id: str = ""

    @classmethod
    def from_youtube_api(
        cls,
        id: str,
        authorDisplayName: str,
        authorChannelId: dict[str, str],
        videoId: str,
        textDisplay: str,
        likeCount: int,
    ) -> Comment:
        return Comment(
            comment_id=id,
            author_name=authorDisplayName,
            author_id=authorChannelId.get("value", ""),
            video_id=videoId,
            text=textDisplay,
            like_count=likeCount,
        )
