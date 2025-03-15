# Welcome to MinecraftStatus Documentation

**MinecraftStatus** is an asynchronous Python wrapper for the [Minecraft Server Status API](https://api.iapetus11.me). It provides an easy-to-use interface to fetch server status, generate server cards, and more.

---

## Getting Started

### Installation

You can install the latest stable release of `minecraftstatus` using pip:

```bash
pip install -U minecraftstatus
```

To install the latest development version directly from the `main` branch, run:

```bash
pip install -U git+https://github.com/Infernum1/minecraftstatus
```

> **Note:** Make sure you have [Git](https://gitforwindows.org) installed to install from the repository.

---

## Examples

### Fetching Server Status

Here’s a quick example to fetch the status of a Minecraft server:

```python
import minecraftstatus

client = minecraftstatus.MCStatus()

async def get_server_status(ip: str):
    server = await client.get_server(ip)
    print(f"Server {server.host} is online with {server.online_player_count} players.")
```

### Generating an Achievement Image

You can generate a Minecraft-style achievement image:

```python
import minecraftstatus

client = minecraftstatus.MCStatus()

async def generate_achievement(text: str):
    image = await client.achievement(text)
    with open("achievement.png", "wb") as f:
        f.write(image.getbuffer())
```

### Using in a Discord Bot

Here’s how you can integrate `minecraftstatus` into a Discord bot:

```python
import discord
from discord.ext import commands
import minecraftstatus

client = minecraftstatus.MCStatus()
bot = commands.Bot(command_prefix="!")

@bot.command()
async def achievement(ctx, *, text: str):
    image = await client.achievement(text)
    file = discord.File(image, "achievement.png")
    await ctx.send(file=file)

bot.run("YOUR_BOT_TOKEN")
```

For more examples, check out the [examples directory](https://github.com/Infernum1/minecraftstatus/tree/main/examples) in the repository.

---

## API Reference

Explore the full API documentation:

- **[Client](api/client.md)**: The main class for interacting with the API.
- **[Errors](api/errors.md)**: Exceptions raised by the library.
- **[Server Status](api/server_status.md)**: Details about the server status response.

---

## Need Help?

If you have any questions or need assistance, feel free to reach out:

- **Discord:** Add `infernum._.` on Discord for direct support.
- **GitHub Issues:** Open an issue on the [GitHub repository](https://github.com/Infernum1/minecraftstatus/issues).

---