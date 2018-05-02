import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Bot Online - olá Mundo')
    print(client.user.name)
    print(client.user.id)
    print('---------PR------------')

client.run('NDQxMzM3MzIwMDkyNzI5MzY1.DcuzwA.wJcd8h1kJ30GP8VyUa2ytqAlx5U')