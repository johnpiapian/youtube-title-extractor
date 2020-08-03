import os
from googleapiclient.discovery import build

api_key = os.environ.get('YOUTUBE_API')

youtube = build('youtube', 'v3', developerKey=api_key)

vid_titles = []
nextPageToken = None

while True:
    pl_request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId="PL8ATzBSyrJZxzU9yP_XlJoGIopvo_jivu",
        maxResults=50,
        pageToken=nextPageToken
    )
    pl_response = pl_request.execute()

    vid_ids = []

    # Get all video ids and store in vid_ids
    for item in pl_response['items']:
        vid_ids.append(item['contentDetails']['videoId'])


    v_request = youtube.videos().list(
        part='snippet',
        id=','.join(vid_ids)
    )
    v_response = v_request.execute()

    for item in v_response['items']:
        vid_titles.append(item['snippet']['title'])

    # Get the next token if not stop looping
    nextPageToken = pl_response.get('nextPageToken')

    if not nextPageToken:
        break