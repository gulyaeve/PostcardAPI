import datetime
import os
import re

from pyppeteer import launch
# from utils.postcard_image_generator.page import page_template
# from utils.postcard_image_generator.page1 import page_template_1
# from utils.postcard_image_generator.page2 import page_template_2


def make_text(input_text):
    return re.sub(r'<.*?>', '', input_text)


async def make_postcard(text: str, category: str, template: str) -> bytes:
    current_time = datetime.datetime.now()
    text = make_text(text)
    with open(f"postcards/{category}/{template}/index.html") as index_page:
        page = index_page.read()

    page = page.replace(
        '{{ TEXT }}',
        text
    )
    with open(f'postcards/{category}/{template}/page_temp_{current_time}.html', 'w') as file:
        file.write(page)

    browser = await launch(defaultViewport={'width': 1440, 'height': 100, 'scale': 1},
                           headless=True, ignoreHTTPSErrors=True, executablePath='/usr/bin/chromium',
                           args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto(f'file:///src/postcards/{category}/{template}/page_temp_{current_time}.html')
    await page.screenshot({'path': f'temp/postcard_{category}_{template}_{current_time}.png', 'fullPage': 'true'})
    await browser.close()
    with open(f'temp/postcard_{category}_{template}_{current_time}.png', "rb") as image:
        f = image.read()
        b = bytes(f)
    os.remove(f'postcards/{category}/{template}/page_temp_{current_time}.html')
    os.remove(f'temp/postcard_{category}_{template}_{current_time}.png')
    return b
