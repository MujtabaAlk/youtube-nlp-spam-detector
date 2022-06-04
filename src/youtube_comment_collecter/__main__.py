from __future__ import annotations

import os

import googleapiclient.discovery
import googleapiclient.errors
from dotenv import load_dotenv

from youtube_comment_collecter import constants


def main() -> int:
    load_dotenv()

    developer_key = os.environ[constants.GOOGLE_APPLICATION_API_KEY_ENV]

    youtube = googleapiclient.discovery.build(
        serviceName=constants.API_SERVICE_NAME,
        version=constants.API_VERSION,
        developerKey=developer_key,
    )

    comment_thread_handler = youtube.commentThreads()
    comment_thread_response = comment_thread_handler.list(
        part="id,snippet,replies",
        videoId="_VB39Jo8mAQ",
        maxResults=100,
        textFormat="plainText",
    ).execute()

    comment_threads = []
    comment_threads.extend(comment_thread_response.get("items"))

    while comment_thread_response.get("nextPageToken") is not None:
        next_page_token = comment_thread_response.get("nextPageToken")
        comment_thread_response = comment_thread_handler.list(
            part="id,snippet,replies",
            videoId="_VB39Jo8mAQ",
            maxResults=100,
            textFormat="plainText",
            pageToken=next_page_token,
        ).execute()

        comment_threads.extend(comment_thread_response.get("items"))

    for thread in comment_threads:
        comment_snip = (
            thread.get("snippet").get("topLevelComment").get("snippet")
        )
        print(comment_snip.get("textDisplay"))
        print("*" * 88)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
