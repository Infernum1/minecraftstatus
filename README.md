An async API wrapper around [api.iapetus.me](https://github.com/Iapetus-11/api.iapetus11.me)

#### <u>Example</u>
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
