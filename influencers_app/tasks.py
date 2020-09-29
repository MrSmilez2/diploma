# Create your tasks here
from __future__ import absolute_import, unicode_literals
from django.conf import settings
from googleapiclient.discovery import build
from .models import VideoInformation
from datetime import timedelta

from celery import shared_task

import re
import time


@shared_task
def test_task():
    time.sleep(5)
    return "It works"


@shared_task
def video_information_update():
    queryset = VideoInformation.objects.values()
    for el in queryset:
        video_id = el.get("video_id")
        new_video = queryset.filter(video_id=video_id)
        if len(video_id) > 11:
            video_id = re.sub(r"https://www\.youtube\.com/watch\?v=", "", video_id)
        api_key = settings.API_KEY
        youtube = build("youtube", "v3", developerKey=api_key)
        request = youtube.videos().list(part="statistics", id=video_id)
        response = request.execute()
        print(response)
        views_count = response["items"][0]["statistics"]["viewCount"]
        likes_count = response["items"][0]["statistics"]["likeCount"]
        dislikes_count = response["items"][0]["statistics"]["dislikeCount"]
        comments_count = response["items"][0]["statistics"]["commentCount"]
        new_video.update(
            views_count=views_count,
            comments_count=comments_count,
            likes_count=likes_count,
            dislikes_count=dislikes_count,
        )


SCHEDULE = {
    "video_information_update": {
        "task": "influencers_app.tasks.video_information_update",
        "args": (),
        "options": {},
        "schedule": timedelta(seconds=5),
    }
}
