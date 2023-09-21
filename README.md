# youtube-title-extractor

Extract video titles from a youtube playlist and export the data into a file type of your choice. 

Supported file types: xlsx, csv

# Installation

## Setup Project
> git clone https://github.com/johnpiapian/youtube-title-extractor \
> python3 -m venv virtual\
> source virtual/bin/activate\
> pip install google-api-python-client\
> pip install XlsxWriter

### Alternatively use setup script
> git clone https://github.com/johnpiapian/youtube-title-extractor \
> ./setup.sh

## Configure API
Set YOUTUBE_API in env.txt to your own Youtube api key and then rename env.txt to env.py.

<br>

# Usage

You can interact with the console by running the app like the following:
> python app.py

Alternatively, you can pass the necessary values directly as flags:
> python app.py [playlist_id] [filename] [filetype]

For example (exclude extension from filename):
> app.py PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj video_titles csv

If filename(2nd arg) is not provided, it will be set to a default name(titles). Similarily, if file type(3rd arg) is not provided then it will be set to xlsx.

# Test

The project utilizes Pytest framework for testing. To test run the following command in the root folder:
> pytest  pytest -vv

Or for more detail

> pytest -vv