import os
import re

from pyppeteer import launch
from utils.postcard_image_generator.page import page_template
from utils.postcard_image_generator.page1 import page_template_1
from utils.postcard_image_generator.page2 import page_template_2


def make_text(input_text):
    return re.sub(r'<.*?>', '', input_text)


async def make_postcard(text: str, template: int, tlg_id: str) -> bytes:
# async def make_postcard(text: str, template: int):
    # text = make_text(text)
    new_page = ""
    if template == 0:
        new_page = page_template.format(text=text.replace("\n", "<br>"))
    elif template == 1:
        new_page = page_template_1.format(text=text.replace("\n", "<br>"))
    elif template == 2:
        new_page = page_template_2.format(text=text.replace("\n", "<br>"))
    # return new_page

    # with open(f'utils/postcard_image_generator/picture{template}/page_temp_{tlg_id}.html', 'w') as file:
    with open(f'utils/postcard_image_generator/picture{template}/page_temp_{tlg_id}.html', 'w') as file:
        file.write(new_page)
    browser = await launch(defaultViewport={'width': 1440, 'height': 100, 'scale': 1},
                           headless=True, ignoreHTTPSErrors=True, executablePath='/usr/bin/chromium',
                           args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto(f'file:///src/utils/postcard_image_generator/picture{template}/page_temp_{tlg_id}.html')
    await page.screenshot({'path': f'utils/postcard_image_generator/temp/postcard_{tlg_id}.png', 'fullPage': 'true'})
    await browser.close()
    with open(f'utils/postcard_image_generator/temp/postcard_{tlg_id}.png', "rb") as image:
        f = image.read()
        b = bytes(f)
    os.remove(f'utils/postcard_image_generator/picture{template}/page_temp_{tlg_id}.html')
    os.remove(f'utils/postcard_image_generator/temp/postcard_{tlg_id}.png')
    return b
