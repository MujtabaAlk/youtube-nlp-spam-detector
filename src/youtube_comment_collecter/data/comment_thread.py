from __future__ import annotations

from dataclasses import dataclass

from youtube_comment_collecter.data.comment import Comment
from youtube_comment_collecter.api_resources.comment_resource import (
    CommentResource,
)
from youtube_comment_collecter.api_resources.comment_thread_resource import (
    CommentThreadResource,
)


@dataclass
class CommentThread:
    id: str
    top_level_comment: Comment
    comments: list[Comment]

    @classmethod
    def from_youtube_api(
        cls, comment_thread_resource: CommentThreadResource
    ) -> CommentThread:
        replies = comment_thread_resource.get("replies")
        comment_resource_list: list[CommentResource]
        if replies is not None:
            comment_resource_list = replies["comments"]
        else:
            comment_resource_list = list()
        return cls(
            id=comment_thread_resource["id"],
            top_level_comment=Comment.from_youtube_api(
                comment_thread_resource["snippet"]["topLevelComment"],
            ),
            comments=Comment.list_from_youtube_api(comment_resource_list),
        )

    @classmethod
    def list_from_youtube_api(
        cls, comment_thread_resource_list: list[CommentThreadResource]
    ) -> list[CommentThread]:
        comment_thread_list: list[CommentThread] = list()
        for comment_thread_resource in comment_thread_resource_list:
            new_comment_thread = cls.from_youtube_api(comment_thread_resource)
            comment_thread_list.append(new_comment_thread)
        return comment_thread_list
