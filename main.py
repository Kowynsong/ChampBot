import discord
import config
import asyncio
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents, application_id=os.getenv('APP_ID'))

@bot.event
async def on_ready():
    print('Online.')

# @bot.event
# async def on_message(message):
#     await bot.process_commands(message)
#     if message.content[0] == '.':
#         return
#     if message.author == bot.user:
#         return 
#     await message.channel.send("hello friend.", ephermeral = True)

async def load():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')

async def main():
    await load()
    await bot.start(os.getenv('TOKEN'))

asyncio.run(main())