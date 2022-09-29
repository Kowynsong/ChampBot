import discord
from discord.ext import commands
from helper import *

class TourButtons(discord.ui.View):
    def __init__(self, *, timeout=10):
        super().__init__(timeout=timeout)

    @discord.ui.button(label="Tournaments", style = discord.ButtonStyle.gray)
    async def tours(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(("\n".join(["".join(i) for i in uniqueTours])), ephemeral = True)

class Valo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('valo cog loaded')

    @commands.command()
    async def vtours(self, ctx):
        await ctx.send("View upcoming tournaments", view = TourButtons())

async def setup(bot):
    await bot.add_cog(Valo(bot))


#current test
"""
stages = []
for i in range(len(res)):
    if (res[i]['event']['name'] + ": " + res[i]['event']['stage']) not in stages:
        date.append(res[i]['date'])
        stages.append(res[i]['event']['name'] + ": " + res[i]['event']['stage'])

for i in range(len(currentTournaments)):
    print(date[i] + ": " + stages[i])
"""