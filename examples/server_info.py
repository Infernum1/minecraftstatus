# Getting info on a Minecraft Server.

import asyncio
import minecraftstatus

client = minecraftstatus.MCStatus()


async def main(ip_address: str):
    server = await client.get_server(ip_address)
    print(server.motd)
    print(server.max_players)
    print(server.max_players)
    print(server.version_info)  # and many more attributes!


if __name__ == "__main__":
    asyncio.run(main("mc.hypixel.net"))
