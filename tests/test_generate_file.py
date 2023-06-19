import env
import os
from ytextractor import SpreadSheet, CSV, FileManager

class TestExtractor:
    filename = '0000000test'
    videos = [
        {
            "videoId": "1234abcd",
            "title": "Example Video 1",
            "description": "This is an example video.",
            "publishedAt": "2022-05-01T00:00:00Z",
            "channelId": "abcd1234",
            "channelTitle": "Example Channel"
        },
        {
            "videoId": "5678efgh",
            "title": "Example Video 2",
            "description": "This is another example video.",
            "publishedAt": "2022-05-02T00:00:00Z",
            "channelId": "efgh5678",
            "channelTitle": "Another Example Channel"
        },
        {
            "videoId": "9012ijkl",
            "title": "Example Video 3",
            "description": "This is yet another example video.",
            "publishedAt": "2022-05-03T00:00:00Z",
            "channelId": "ijkl9012",
            "channelTitle": "Yet Another Example Channel"
        }
    ]

    def test_spreadsheet(self):
        spreadsheet = SpreadSheet(self.filename, self.videos)
        spreadsheet.generate()

        assert os.path.exists(fr'{self.filename}.xlsx')

        os.remove(fr'{self.filename}.xlsx')

    def test_csv(self):
        csv = CSV(self.filename, self.videos)
        csv.generate()

        assert os.path.exists(fr'{self.filename}.csv')
        
        os.remove(fr'{self.filename}.csv')

    def test_file_manager(self):
        file_manager = FileManager(self.filename, self.videos)
        file_manager.generate_xlsx()
        file_manager.generate_csv()

        assert os.path.exists(fr'{self.filename}.xlsx')
        assert os.path.exists(fr'{self.filename}.csv')

        os.remove(fr'{self.filename}.xlsx')
        os.remove(fr'{self.filename}.csv')