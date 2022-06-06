import os
import constants
from googleapiclient.discovery import build

# API Secret key
# api_key = os.environ.get('YOUTUBE_API')
api_key = constants.YOUTUBE_API

# API connection
youtube = build('youtube', 'v3', developerKey=api_key)


def getTitles(playlist_id):

    vid_titles = []

    nextPageToken = None

    while True:
        pl_request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=playlist_id,
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

    return vid_titles