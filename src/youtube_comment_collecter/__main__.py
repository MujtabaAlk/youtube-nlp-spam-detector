from __future__ import annotations

import os

import googleapiclient.discovery
import googleapiclient.errors
from dotenv import load_dotenv

from youtube_comment_collecter import constants
from youtube_comment_collecter.api_resources.comment_thread_resource import (
    CommentThreadListResponse,
    CommentThreadResource,
)
from youtube_comment_collecter.video import Video


def main() -> int:
    load_dotenv()

    developer_key = os.environ[constants.GOOGLE_APPLICATION_API_KEY_ENV]

    youtube = googleapiclient.discovery.build(
        serviceName=constants.API_SERVICE_NAME,
        version=constants.API_VERSION,
        developerKey=developer_key,
    )

    video = Video(id="_VB39Jo8mAQ")

    comment_thread_handler = youtube.commentThreads()
    comment_thread_response: CommentThreadListResponse = (
        comment_thread_handler.list(
            part="id,snippet,replies",
            videoId=video.id,
            maxResults=100,
            textFormat="plainText",
        ).execute()
    )

    comment_threads: list[CommentThreadResource] = []
    comment_threads.extend(comment_thread_response["items"])

    while comment_thread_response.get("nextPageToken") is not None:
        next_page_token = comment_thread_response.get("nextPageToken")
        comment_thread_response = comment_thread_handler.list(
            part="id,snippet,replies",
            videoId="_VB39Jo8mAQ",
            maxResults=100,
            textFormat="plainText",
            pageToken=next_page_token,
        ).execute()

        comment_threads.extend(comment_thread_response["items"])

    for i, thread in enumerate(comment_threads):
        comment_snip = thread["snippet"]["topLevelComment"]["snippet"]
        if comment_snip["likeCount"] > 0:

            print(
                f"[{i}] [likes: {comment_snip['likeCount']}] [published at:"
                f" {comment_snip['publishedAt']}]"
            )
            print(comment_snip["textOriginal"])
            print("*" * 120)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
