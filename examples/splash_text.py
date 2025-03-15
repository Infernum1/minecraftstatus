# Getting a custom splash text image.

import asyncio
from minecraftstatus import MCStatus


async def main(text: str):
    async with MCStatus() as client:
        image = await client.splash_text(text)

    print(image.getvalue())


if __name__ == "__main__":
    asyncio.run(main("Also check out terarria"))
