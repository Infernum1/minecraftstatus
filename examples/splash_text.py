#Getting a custom splash text image.

import asyncio
import minecraftstatus

client = minecraftstatus.MCStatus()

async def main(text: str):
    image = await client.splash_text(text)
    print(await image.getvalue())

if __name__ == "__main__":
    asyncio.run(main("Also check out terarria"))
