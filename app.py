import sys
from ytextractor import ExtractTitle
from ytextractor import FileManager
import constants

def app():
    # filename (app.py), playlist_id, spreadsheet's name
    arguments = sys.argv

    if len(arguments) == 1:
        arguments.append(input("Enter playlist id: "))
        arguments.append(input("Enter spreadsheet's name: "))
    elif len(arguments) == 2:
        arguments.append("titles")
    
    # Unpack arguments
    playlist_id, spreadsheet_name = arguments[1:3]

    try:
        title_extractor = ExtractTitle(constants.YOUTUBE_API)
        titles = title_extractor.get_titles(playlist_id)

        file_manager = FileManager(spreadsheet_name, titles)
        file_manager.generate_xlsx()
        file_manager.generate_csv()

        print("Successfully created!")
    except:
        print("An unexpected error occurred!")
        raise

app()


