import discord
from discord.ext import commands


class Pvp(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fight(self, ctx):
        await ctx.send()


def setup(client):
    client.add_cog(Pvp(client))