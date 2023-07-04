# Getting a custom achievement image.

import asyncio
import minecraftstatus

client = minecraftstatus.MCStatus()


async def main(achievement: str):
    image = await client.achievement(achievement)
    print(image.getvalue())


if __name__ == "__main__":
    asyncio.run(main("Mom, get the camera!!!"))
