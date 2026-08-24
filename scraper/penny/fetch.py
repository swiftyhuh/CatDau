from datetime import date
import requests
import os

todayWeek = date.today().isocalendar().week
todayYear = date.today().isocalendar().year

dURL = "https://files.rewe.co.at/PennyIntLeaflet/RO/Pliant_National_KW34_2026/files/assets/common/downloads/Pliant%20National.pdf"

# resp = requests.get(URL)
# print(resp.status_code)

# curr_dir = os.getcwd()
# entries = os.listdir(curr_dir)
# print(entries)

def catalog_filename(week, year):
    return f"data/penny/penny_KW{week:02d}_{year}.pdf"

def catalog_url(week, year):
    return f"https://files.rewe.co.at/PennyIntLeaflet/RO/Pliant_National_KW{week:02d}_{year}/files/assets/common/downloads/Pliant%20National.pdf"


def catalog_exists(week, year):
    file_path = catalog_filename(week, year)
    return os.path.exists(file_path)

def download_catalog(week, year):
    URL = catalog_url(week, year)
    resp = requests.get(URL)
    if resp.ok:
        file_path = catalog_filename(week, year)
        with open(file_path, 'wb') as f:
            f.write(resp.content)
    else:
        print("url failed")

        
if not catalog_exists(todayWeek, todayYear):
    download_catalog(todayWeek, todayYear)

# file_path = f"data/penny/penny_KW{todayWeek}_{todayYear}.pdf"
# if os.path.exists(file_path):
#     print("Bine coaie")
# else:
#     print("Nu-i bine coaie")