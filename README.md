A (work in progress) async API wrapper around [api.iapetus.me](https://github.com/Iapetus-11/api.iapetus11.me)

### <u>Example</u>
###### Getting info on a Minecraft Server.

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

###### Getting a custom achievement image.

```py
import asyncio
import mcutility

client = mcutility.MCStatus()
async def main(achievement: str)
  image = await client.achievement(achievement)
  print(await image.getvalue())

asyncio.run(main("Mom, get the camera!!!"))
```

###### Or if you plan to use it in a discord bot

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
