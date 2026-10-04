# CâtDau ❓

Tells you which supermarket has the cheapest basket for your shopping list, based on this week's discounts and your preferred brands.

# Why I'm building it 🤔

Before every shopping trip I'd go through the catalogs of the supermarkets near me to find the best deals and keep the total low. It took too long, so I decided to automate it.

# About me 🤷‍♂️

I'm a student at FMI UBB Cluj. I like writing code and automating repetitive tasks that waste my time. Flipping through catalogs is one of them, and I've never built a mobile app, so 1+1=2: I'm learning as I go. I'm writing the code myself, using AI only for research.

You can find me on [GitHub](https://github.com/swiftyhuh) / [LinkedIn](https://www.linkedin.com/in/mihaisz/) / [Instagram](https://www.instagram.com/mihai.szabo.o/)

# How it works 🥱

A small Python script downloads the available catalogs and extracts the prices automatically. The products and prices go into a SQLite database, and a FastAPI backend serves them. The mobile app will be built with Flutter.

The idea: you write your list in the app (or paste it from Notes), and the app tells you where your basket comes out cheapest. For now it covers Penny and Profi.

# Status 🤗

- **Done:** downloading the current week's catalog and converting each page to PNG.
- **Done:** OCR. I tried Tesseract, EAST, a Laplacian filter and saturation tweaks, but none of them worked the way I needed. [RapidOCR](https://github.com/RapidAI/RapidOCR) did, and Claude helped me understand it and research the options.

# Roadmap 🗺️

1. Parse the OCR output into structured products and prices.
2. Store them in SQLite.
3. Serve the data through a FastAPI backend.
4. Build the Flutter app: shopping list in, cheapest supermarket out.
5. Add Profi alongside Penny.
