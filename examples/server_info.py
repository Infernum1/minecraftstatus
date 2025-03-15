# Getting info on a Minecraft Server.

import asyncio
from minecraftstatus import MCStatus


async def main(ip_address: str):
    async with MCStatus() as client:
        server = await client.get_server(ip_address)

    print(server.clean_motd)
    print(server.max_players)
    print(server.max_players)
    print(server.version_info)  # and many more attributes!


if __name__ == "__main__":
    asyncio.run(main("mc.hypixel.net"))
