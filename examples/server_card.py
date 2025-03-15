# Getting a custom splash text image.

import asyncio
from minecraftstatus import MCStatus


async def main(ip_address: str):
    async with MCStatus() as client:
        server_card = await client.get_server_card(ip_address, "My Server")

    print(server_card.getvalue())


if __name__ == "__main__":
    asyncio.run(main("mc.hypixel.net"))
