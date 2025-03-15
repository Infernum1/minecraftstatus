# Getting a custom achievement image.

import asyncio
from minecraftstatus import MCStatus


async def main(achievement: str):
    async with MCStatus() as client:
        image = await client.achievement(achievement)

    print(image.getvalue())


if __name__ == "__main__":
    asyncio.run(main("Mom, get the camera!!!"))
