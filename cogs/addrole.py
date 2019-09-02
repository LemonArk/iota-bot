import discord
from discord.ext import commands

class Roles(commands.Cog):

    def __init__(self, client):
        self.client = client

#TODO revisit the add role command.

def setup(client):
    client.add_cog(Roles(client))