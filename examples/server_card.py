# Getting a custom splash text image.

import asyncio
import minecraftstatus

client = minecraftstatus.MCStatus()


async def main(ip_address: str):
    image = await client.get_server_card(ip_address, custom_server_name="An Awesome Minecraft Server")
    print(await image.getvalue())


if __name__ == "__main__":
    asyncio.run(main("Also check out terarria"))
