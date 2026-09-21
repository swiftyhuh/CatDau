from datetime import date
import requests
import os
import pdfplumber

# -=-=-=-=-=-=
# current date
# -=-=-=-=-=-=

todayWeek = date.today().isocalendar().week
todayYear = date.today().isocalendar().year

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# debug url (hardcoded to current catalog)
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

dURL = "https://files.rewe.co.at/PennyIntLeaflet/RO/Pliant_National_KW36_2026/files/assets/common/downloads/Pliant%20National.pdf"

# -=-=-=-
# HELPERS
# -=-=-=-

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

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Downloading current week catalog
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

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

# -=-=-=-=-=-=-=-=-=-=-
# convert pages to pngs
# -=-=-=-=-=-=-=-=-=-=-

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

# -=-=-=-=-=-=
# running code
# -=-=-=-=-=-=

if not catalog_exists(todayWeek, todayYear):
    download_catalog(todayWeek, todayYear)
pages_to_image(todayWeek,todayYear)
