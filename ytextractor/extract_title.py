import os
from googleapiclient.discovery import build

class ExtractData:
    def __init__(self, api_key):
        self.youtube = build('youtube', 'v3', developerKey=api_key) # API connection
        self.playlist_items = [] # List of playlist items

    def setup(self, playlist_id):
        items = []
        nextPageToken = None

        while True:

            # set video ids from playlist
            pl_request = self.youtube.playlistItems().list(
                part='contentDetails',
                playlistId=playlist_id,
                maxResults=50,
                pageToken=nextPageToken
            )
            pl_response = pl_request.execute()

            # store video ids in the list
            video_ids = []
            for item in pl_response['items']:
                video_ids.append(item['contentDetails']['videoId'])

            # get video information using video ids
            v_request = self.youtube.videos().list(
                part='snippet',
                id=','.join(video_ids)
            )
            v_response = v_request.execute()

            # store video information in the list
            for item in v_response['items']:
                values = {
                    "videoId": item['id'],
                    "title": item['snippet']['title'],
                    "description": item['snippet']['description'],
                    "publishedAt": item['snippet']['publishedAt'],
                    "channelId": item['snippet']['channelId'],
                    "channelTitle": item['snippet']['channelTitle']
                }
                items.append(values)

            # Get the next token if not stop looping
            nextPageToken = pl_response.get('nextPageToken')

            if not nextPageToken:
                break

        # assign items to object variable
        self.playlist_items = items

    def get_videos(self):
        return self.playlist_items

    def get_titles(self):
        titles = []
        for item in self.playlist_items:
            titles.append(item['title'])
        
        return titles







