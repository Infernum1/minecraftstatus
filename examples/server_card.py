# Getting a custom splash text image.

import asyncio
import minecraftstatus
from minecraftstatus import MCStatus


async def main(ip_address: str):
    async with MCStatus() as client:
        server = await client.get_server(ip_address)

    print(server.host)


if __name__ == "__main__":
    asyncio.run(main("mc.hypixel.net"))
