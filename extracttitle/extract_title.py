import os
from googleapiclient.discovery import build

class ExtractTitle:
    def __init__(self, api_key):
        self.api_key = api_key # API Secret key
        self.youtube = build('youtube', 'v3', developerKey=api_key) # API connection

    def get_titles(self, playlist_id):
        vid_titles = []

        nextPageToken = None

        while True:
            pl_request = self.youtube.playlistItems().list(
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

            v_request = self.youtube.videos().list(
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






