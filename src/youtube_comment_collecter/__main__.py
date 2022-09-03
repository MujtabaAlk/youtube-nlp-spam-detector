from __future__ import annotations

from argparse import ArgumentParser
import asyncio
import os

from dotenv import load_dotenv
import httpx

from youtube_comment_collecter import constants
from youtube_comment_collecter.comment_thread import CommentThread
from youtube_comment_collecter.api_resources.comment_thread_resource import (
    CommentThreadListResponse,
    CommentThreadResource,
)
from youtube_comment_collecter.api_resources.error import ErrorResponse


async def async_main(video_id: str) -> int:
    load_dotenv()

    developer_key = os.environ[constants.GOOGLE_APPLICATION_API_KEY_ENV]

    comment_threads_resources: list[CommentThreadResource] = list()
    async with httpx.AsyncClient() as client:
        request_params: dict[str, str | int | bool] = {
            "key": developer_key,
            "videoId": video_id,
            "part": "id,snippet,replies",
            "maxResults": 100,
            "textFormat": "plainText",
            "pageToken": "",
        }
        response = await client.get(
            url=constants.THREADS_API_URL,
            params=request_params,
        )

        if response.status_code != 200:
            print("Unable to retrive comments")
            print(f"Error code: {response.status_code}")
            print("*" * 25)
            print("API error:")
            error_response: ErrorResponse = response.json()
            print(error_response["error"]["message"])
            return len(error_response["error"]["errors"])

        comment_thread_response: CommentThreadListResponse = response.json()
        comment_threads_resources.extend(comment_thread_response["items"])

        while comment_thread_response.get("nextPageToken") is not None:
            next_page_token = comment_thread_response.get("nextPageToken")
            request_params["pageToken"] = (
                next_page_token if next_page_token is not None else ""
            )
            response = await client.get(
                url=constants.THREADS_API_URL, params=request_params
            )
            comment_thread_response = response.json()
            comment_threads_resources.extend(comment_thread_response["items"])

    comment_thread_list: list[
        CommentThread
    ] = CommentThread.list_from_youtube_api(comment_threads_resources)

    for i, thread in enumerate(comment_threads_resources):
        comment_snippent = thread["snippet"]["topLevelComment"]["snippet"]
        replies = thread.get("replies")
        reply_count = 0
        if replies is not None:
            reply_count = len(replies["comments"])

        if comment_snippent["likeCount"] > 0:
            print(
                f"[{i}] [likes: {comment_snippent['likeCount']}] [replies:"
                f" {reply_count}] [published at:"
                f" {comment_snippent['publishedAt']}]"
            )
            print(comment_snippent["textOriginal"])
        else:
            print("Skipping!!!")

        print("*" * 120)

    print(f"Generated {len(comment_thread_list)} CommentThread objects")

    return 0


def main() -> int:
    parser = ArgumentParser()
    parser.add_argument(
        "video_id",
        help="ID of the video to collect comments from",
        type=str,
    )
    args = parser.parse_args()

    return asyncio.run(async_main(args.video_id))


if __name__ == "__main__":
    raise SystemExit(main())
