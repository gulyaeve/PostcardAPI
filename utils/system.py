import os


async def get_categories() -> list | None:
    categories = os.listdir("postcards")
    categories.remove(".DS_Store")
    return categories


async def get_postcard_preview(category: str, template: str) -> bytes:
    with open(f'postcards/{category}/{template}/preview.png', "rb") as image:
        f = image.read()
        b = bytes(f)
    return b
