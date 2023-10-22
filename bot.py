import asyncio
import discord

intents = discord.Intents.all()
client = discord.Client(intents=intents, activity=discord.Game(name="Yggdrasil sucks"))

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if "You hung up the userphone" in message.content:
        emoji = '\N{HOURGLASS WITH FLOWING SAND}'
        await message.add_reaction(emoji)
        await asyncio.sleep(50)
        await message.reply('Ready to `--userphone` again!', mention_author=True)
        await message.remove_reaction(emoji,client.user)

    if "The other party hung up the userphone" in message.content:
        emoji = '\N{HOURGLASS WITH FLOWING SAND}'
        await message.add_reaction(emoji)
        await asyncio.sleep(5)
        await message.reply('Ready to `--userphone` again!', mention_author=True)
        await message.remove_reaction(emoji,client.user)

client.run('')