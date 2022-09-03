from __future__ import annotations

from dataclasses import dataclass

from youtube_comment_collecter.api_resources.comment_resource import (
    CommentResource,
)


@dataclass
class Comment:
    comment_id: str
    author_name: str
    author_id: str
    video_id: str
    text: str
    like_count: int
    parent_id: str

    @classmethod
    def from_youtube_api(cls, comment_resource: CommentResource) -> Comment:
        parent_id = comment_resource["snippet"].get("parentId")
        return cls(
            comment_id=comment_resource["id"],
            author_id=comment_resource["snippet"]["authorChannelId"]["value"],
            author_name=comment_resource["snippet"]["authorDisplayName"],
            text=comment_resource["snippet"]["textDisplay"],
            like_count=comment_resource["snippet"]["likeCount"],
            video_id=comment_resource["snippet"]["videoId"],
            parent_id=parent_id or "",
        )

    @classmethod
    def list_from_youtube_api(
        cls, comment_resource_list: list[CommentResource]
    ) -> list[Comment]:
        comment_list: list[Comment] = list()

        for comment_resource in comment_resource_list:
            new_comment = cls.from_youtube_api(comment_resource)
            comment_list.append(new_comment)

        return comment_list
