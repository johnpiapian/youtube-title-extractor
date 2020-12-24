# youtube-title-extractor
Extract video titles from a youtube playlist and export the data into a spreadsheet file. 

<br/>

## Installation

> python3 -m venv virtual

> source virtual/bin/activate

> pip install google-api-python-client

> pip install XlsxWriter

<br/>

## Usage

app.py [playlist_id] [filename]
> app.py PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj video_titles

<br/>

If the second argument[filename] is not provided, it will be set to a default name(titles.xlsx).  

<br/><br/>
**Do not include the extension name when setting a name for the spreadsheet.
