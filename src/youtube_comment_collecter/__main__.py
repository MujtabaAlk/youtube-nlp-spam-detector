from __future__ import annotations

from argparse import ArgumentParser
import asyncio
import os

from dotenv import load_dotenv
import httpx

from youtube_comment_collecter import constants
from youtube_comment_collecter.api_resources.comment_thread_resource import (
    CommentThreadListResponse,
    CommentThreadResource,
)


async def async_main(video_id: str) -> int:
    load_dotenv()

    developer_key = os.environ[constants.GOOGLE_APPLICATION_API_KEY_ENV]

    comment_threads: list[CommentThreadResource] = list()
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
        comment_thread_response: CommentThreadListResponse = response.json()
        comment_threads.extend(comment_thread_response["items"])

        while comment_thread_response.get("nextPageToken") is not None:
            next_page_token = comment_thread_response.get("nextPageToken")
            request_params["pageToken"] = (
                next_page_token if next_page_token is not None else ""
            )
            response = await client.get(
                url=constants.THREADS_API_URL, params=request_params
            )
            comment_thread_response = response.json()
            comment_threads.extend(comment_thread_response["items"])

    for i, thread in enumerate(comment_threads):
        comment_snippent = thread["snippet"]["topLevelComment"]["snippet"]
        if comment_snippent["likeCount"] > 0:
            print(
                f"[{i}] [likes: {comment_snippent['likeCount']}] [published"
                f" at: {comment_snippent['publishedAt']}]"
            )
            print(comment_snippent["textOriginal"])
        else:
            print("Skipping!!!")

        print("*" * 120)

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
