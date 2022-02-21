
# Note: this library is still in development and cannot be used in it's current stage!

An async API wrapper around [api.iapetus.me](https://github.com/Iapetus-11/api.iapetus11.me)

### <u>Example</u>
##### Getting info on a Minecraft Server.

```py
import asyncio
import mcutility

client = mcutility.MCStatus()

async def main(ip_address: str)
  server = await client.get_server(ip_address)
  print(server.motd)
  print(server.players_online)
  print(server.max_players)
  print(server.version) # and many more attributes!

asyncio.run(main("mc.hypixel.net"))
```

##### Getting a custom achievement image.

```py
import asyncio
import mcutility

client = mcutility.MCStatus()

async def main(achievement: str)
  image = await client.achievement(achievement)
  print(await image.getvalue())

asyncio.run(main("Mom, get the camera!!!"))
```

##### Getting a custom splash text image.

```py
import asyncio
import mcutility

client = mcutility.MCStatus()

async def main(text: str)
  image = await client.splash_text(text)
  print(await image.getvalue())

asyncio.run(main("Also check out terarria"))
```

##### Or if you plan to use it in a discord bot

```py
import discord
import mcutility

client = mcutility.MCStatus()
bot = discord.ext.commands.Bot()

@bot.command()
async def achievement(achievement: str)
  image = await client.achievement(achievement)
  file = discord.File(image, "achievement.png")
  await ctx.send(file=file)
```

###### these are just examples! it's upto you how you want to use this lib.