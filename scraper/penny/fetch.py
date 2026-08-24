from datetime import date

todayWeek = date.today().isocalendar().week
todayYear = date.today().isocalendar().year

URL=f"https://files.rewe.co.at/PennyIntLeaflet/RO/Pliant_National_KW{todayWeek}_{todayYear}/files/assets/common/downloads/Pliant%20National.pdf"
