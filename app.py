import sys
from ytextractor import ExtractData
from ytextractor import FileManager
import env

def app():
    # filename (app.py), playlist_id, spreadsheet's name, spreadsheet's type
    arguments = sys.argv

    if len(arguments) == 1:
        arguments.append(input("Enter playlist id: "))
        arguments.append(input("Enter file name: "))
        arguments.append(input("Enter file type (xlsx or csv): "))
    elif len(arguments) == 2:
        arguments.append("titles")
        arguments.append("xlsx")
    elif len(arguments) == 3:
        arguments.append("xlsx")
    
    try:
        # Unpack arguments
        playlist_id, file_name, file_type = arguments[1:4]
        
        data_extractor = ExtractData(env.YOUTUBE_API)
        data_extractor.setup(playlist_id)

        file_manager = FileManager(file_name, data_extractor.get_videos())

        if file_type == "xlsx":
            file_manager.generate_xlsx()
        elif file_type == "csv":
            file_manager.generate_csv()
        else:
            print("Invalid file type!")
            return
        
        print("Successfully created!")
    except:
        print("An error occured!")
        raise

app()


