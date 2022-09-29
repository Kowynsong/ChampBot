import discord
from discord import app_commands
from discord.ext import commands
from helper import *

class Questions(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Questions cog loaded')
    
    @commands.command() 
    @commands.has_permissions(administrator = True)
    async def sync(self, ctx) -> None:
        # for testing specific guild (server): fmt = await ctx.bot.tree.sync(guild=ctx.guild)
        fmt = await ctx.bot.tree.sync()
        await ctx.send(f'Synced {len(fmt)} commands.')

    # ping(self, interaction, input) --> all stage name & dates for given input (tournament name)
    @app_commands.command(name="stages", description = "/stages(tournament name) --> date: stage name (team1 vs team2)")
    async def ping(self, interaction: discord.Interaction, input: str):
        for j in range(len(valTours)):
            if valTours[j].name == input:
                output = []
                for k in valTours[j].stages:
                    output.append(f'{k.dates}: {k.names} ({k.team1} vs {k.team2})')
                await interaction.response.send_message("\n".join(["".join(i) for i in output]))
        await interaction.response.send_message('please check spelling and whitespaces!')

    # same as above but no spoiler version
    @app_commands.command(name="stages2", description = "no spoiler version of /stages")
    async def ping2(self, interaction: discord.Interaction, input: str):
        for j in range(len(valTours)):
            if valTours[j].name == input:
                output = []
                for k in valTours[j].stages:
                    output.append(f'{k.dates}: {k.names}')
                await interaction.response.send_message("\n".join(["".join(i) for i in output]))
        await interaction.response.send_message('please check spelling and whitespaces!')

async def setup(bot):
    # re: "for testing..." await bot.add_cog(Questions(bot), guilds = [discord.Object(id=1024116460500570132)])
    await bot.add_cog(Questions(bot))