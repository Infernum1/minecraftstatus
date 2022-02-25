

An async API wrapper around [api.iapetus.me](https://github.com/Iapetus-11/api.iapetus11.me)


### Get started

#### to get started, type this in your terminal
```py
pip install minecraftstatus
```

#### or to install the main branch
```py
pip install git+https://github.com/Infernum1/MCUtility
```
###### (make sure you have git installed)
### Example
##### Getting info on a Minecraft Server.

```py
import asyncio
import minecraftstatus

client = minecraftstatus.MCStatus()

async def main(ip_address: str):
    server = await client.get_server(ip_address)
    print(server.motd)
    print(server.players_online)
    print(server.max_players)
    print(server.version) # and many more attributes!

if __name__ == "__main__":
    asyncio.run(main("mc.hypixel.net"))
```

##### Getting a custom achievement image.

```py
import asyncio
import minecraftstatus

client = minecraftstatus.MCStatus()

async def main(achievement: str):
    image = await client.achievement(achievement)
    print(await image.getvalue())

if __name__ == "__main__":
    asyncio.run(main("Mom, get the camera!!!"))
```

##### Getting a custom splash text image.

```py
import asyncio
import minecraftstatus

client = minecraftstatus.MCStatus()

async def main(text: str):
    image = await client.splash_text(text)
    print(await image.getvalue())

if __name__ == "__main__":
    asyncio.run(main("Also check out terarria"))
```

##### Or if you plan to use it in a discord bot

```py
import discord
import minecraftstatus

client = minecraftstatus.MCStatus()
bot = discord.ext.commands.Bot()

@bot.command()
async def achievement(achievement: str):
  image = await client.achievement(achievement)
  file = discord.File(image, "achievement.png")
  await ctx.send(file=file)
```

###### these are just examples! it's upto you how you want to use this lib.

### Join the [discord server](https://discord.gg/jJqJ3rjgqg) for support.