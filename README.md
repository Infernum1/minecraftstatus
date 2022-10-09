

An async API wrapper around [api.iapetus.me](https://github.com/Iapetus-11/api.iapetus11.me)


### Get started || [Documentation](https://minecraftstatus.readthedocs.io/en/latest/)

#### to get started, type this in your terminal
```
pip install -U minecraftstatus
```

#### or to install the main branch
```
pip install -U git+https://github.com/Infernum1/minecraftstatus
```
###### (make sure you have [git](https://gitforwindows.org) installed)
### Examples

#### For examples, checkout the [examples directory](https://github.com/Infernum1/minecraftstatus/tree/main/examples)
##### If you plan to use the lib in a discord bot

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

### Add `Infernum#7041` on discord for help
