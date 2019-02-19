# Bot for collecting data from vcdepth.io

## Requirements

- Python 3
- Scrapy
- Google API (optional)
- df2gspread

## Usage

Clone the repo and run

```
python bot_vcdepth.py
```

## Details

Your .json file from google api must be inside ~/.gdrive_private

Comment the df2gspread part and uncomment the to_excel if you wish to work locally with a .xlsx file
