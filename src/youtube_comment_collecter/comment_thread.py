from __future__ import annotations

from dataclasses import dataclass

# from youtube_comment_collecter.comment import Comment


@dataclass
class CommentThread:
    id: str
    # top_level_comment: Comment
    # comments: list[Comment]

    @classmethod
    def from_youtube_dict_list(
        cls, dict_list: list[dict[str, str | int]]
    ) -> list[CommentThread]:
        ret: list[CommentThread] = []
        for yt_dict in dict_list:
            cmnt_thrd_id = (
                yt_dict["id"]
                if isinstance(yt_dict["id"], str)
                else str(yt_dict["id"])
            )
            cmnt_thrd = cls(id=cmnt_thrd_id)
            ret.append(cmnt_thrd)
        return ret
