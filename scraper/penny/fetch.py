from datetime import date
import requests
import os
import pdfplumber

todayWeek = date.today().isocalendar().week
todayYear = date.today().isocalendar().year

dURL = "https://files.rewe.co.at/PennyIntLeaflet/RO/Pliant_National_KW36_2026/files/assets/common/downloads/Pliant%20National.pdf"

# resp = requests.get(URL)
# print(resp.status_code)

# curr_dir = os.getcwd()
# entries = os.listdir(curr_dir)
# print(entries)

def catalog_url(week, year):
    return f"https://files.rewe.co.at/PennyIntLeaflet/RO/Pliant_National_KW{week:02d}_{year}/files/assets/common/downloads/Pliant%20National.pdf"

def catalog_dir(week, year):
    return f"data/penny/KW{week:02d}_{year}"

def catalog_filename(week, year):
    return os.path.join(catalog_dir(week,year), "catalog.pdf")

def catalog_exists(week, year):
    file_path = catalog_filename(week, year)
    return os.path.exists(file_path)

def pages_dir(week, year):
    return os.path.join(catalog_dir(week,year),"pages")

def pages_exists(week, year):
    return os.path.exists(os.path.join(pages_dir(week, year), "page_01.png"))



def download_catalog(week, year):
    URL = catalog_url(week, year)
    resp = requests.get(URL)
    if resp.ok:
        os.makedirs(catalog_dir(week, year), exist_ok=True)
        file_path = catalog_filename(week, year)
        with open(file_path, 'wb') as f:
            f.write(resp.content)
    else:
        print("url failed")

def pages_to_image(week, year):
    if pages_exists(week,year):
        print("pages already converted")
    else:
        with pdfplumber.open(catalog_filename(week,year)) as pdf:
            os.makedirs(pages_dir(week,year), exist_ok=True)
            for i, page in enumerate(pdf.pages, start=1):
                im = page.to_image(resolution=150)
                path = os.path.join(pages_dir(week,year), f"page_{i:02d}.png")
                im.save(path)

        
if not catalog_exists(todayWeek, todayYear):
    download_catalog(todayWeek, todayYear)
pages_to_image(todayWeek,todayYear)

# file_path = f"data/penny/penny_KW{todayWeek}_{todayYear}.pdf"
# if os.path.exists(file_path):
#     print("Bine coaie")
# else:
#     print("Nu-i bine coaie")