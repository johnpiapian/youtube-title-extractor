import sys
from extracttitle import ExtractTitle
from extracttitle import SpreadSheet
import constants

def app():
    # 1st: filename, 2nd: playlist_id, 3rd: spreadsheet's name
    arguments = sys.argv
    playlist_id = None
    spreadsheet_name = None

    # if empty give spreadsheet a default name
    if len(arguments) == 2:
        arguments.append("titles")

    if len(arguments) >= 3:
        playlist_id = arguments[1]
        spreadsheet_name = arguments[2]

        try:
            # createSpreadsheet(spreadsheet_name, playlist_id)
            extract_titles = ExtractTitle(constants.YOUTUBE_API)
            titles = extract_titles.get_titles(playlist_id)

            spreadsheet = SpreadSheet(spreadsheet_name)
            spreadsheet.generate(titles)
            print("Successfully created!")
        except:
            print("An unexpected error occurred!")
            raise
    else:
        print("Invalid input!")  

app()