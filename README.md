# youtube-title-extractor

Extract video titles from a youtube playlist and export the data into a spreadsheet file.

## Installation

> git clone [url]\
> python3 -m venv virtual\
> source virtual/bin/activate\
> pip install google-api-python-client\
> pip install XlsxWriter

## Usage

app.py [playlist_id] [filename]
> app.py PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj video_titles

If the second argument(filename) is not provided, it will be set to a default name(titles.xlsx).  

**Do not include the extension name when setting a name for the file.

For API key, create a python file called constants.py and initialize a variable called YOUTUBE_API with the value as your API key.
