import os


async def get_categories() -> list | None:
    categories = os.listdir("postcards")
    categories.remove(".DS_Store")
    return categories


async def get_postcards_list(category: str) -> list | None:
    postcards_list = os.listdir(f"postcards/{category}")
    postcards_list.remove(".DS_Store")
    return postcards_list


async def get_postcard_preview(category: str, template: str) -> bytes:
    with open(f'postcards/{category}/{template}/preview.png', "rb") as image:
        f = image.read()
        b = bytes(f)
    return b
