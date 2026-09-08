# fails because penny catalog its actually just photos merged as pdf fuck penny for this one

import pdfplumber
from pypdf import PdfReader

with pdfplumber.open("data/penny/penny_KW34_2026.pdf") as pdf:
    first_page = pdf.pages[0]
    print(len(first_page.images))
    print(len(first_page.rects))
    print(len(first_page.curves))

# with pdfplumber.open("data/penny/penny_KW34_2026.pdf") as pdf:
#     for i, page in enumerate(pdf.pages):
#         text = page.extract_text()
#         print(i, len(text) if text else 0)


reader = PdfReader("data/penny/penny_KW34_2026.pdf")
print(reader.pages[0].extract_text())