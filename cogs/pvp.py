import discord
import random
from discord.ext import commands
from cogs.getmember import getmember

# Declare lists to be used later

title = [

    "Let's get ready to Rumble!!!",
    '3....2....1...**FIGHT**',
    'The teams are set!',
    'My bet is on Blue.',
    'My bet is on Red',
    'For the Glory of the Crucible!',


]


class Pvp(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(name="fight", description="Randomly sorts users into teams for private pvp matches.")
    async def fight(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("invalid fight command, please specify a subcommand.")

    @fight.command(description="Sorts all the users in a role. fight role <rolename>")
    async def role(self, ctx, *, players: discord.Role):
        player_list = getmember(players)
        random.shuffle(player_list)

        temp_team_1 = player_list[:len(player_list) // 2]
        temp_team_2 = player_list[len(player_list) // 2:]

        red_team = ' -- '.join(temp_team_1)
        blue_team = ' -- '.join(temp_team_2)

        embed = discord.Embed(title=random.choice(title), colour=0x6262ff)
        embed.add_field(name="Red Team", value=f'\n {red_team}', inline=False)
        embed.add_field(name='\u200b',
                        value=' -  ╔════════╗  -\n-  ║ ------VS----- ║  -\n-  ╚════════╝  -\n \u200b ',
                        inline=False)
        embed.add_field(name="Blue Team", value=f'\n {blue_team}', inline=False)

        await ctx.send(content=None, embed=embed)

    @fight.command(description="Sorts users that are passed to this subcommand. fight add <users")
    async def add(self, ctx, *, players):
        player_list = players.split(" ")
        random.shuffle(player_list)

        temp_team_1 = player_list[:len(player_list)//2]
        temp_team_2 = player_list[len(player_list)//2:]

        red_team = ' -- '.join(temp_team_1)
        blue_team = ' -- '.join(temp_team_2)

        embed = discord.Embed(title=random.choice(title), colour=0x6262ff)
        embed.add_field(name="Red Team", value=f'\n {red_team}', inline=False)
        embed.add_field(name='\u200b',
                        value=' -  ╔════════╗  -\n-  ║ ------VS----- ║  -\n-  ╚════════╝  -\n \u200b ',
                        inline=False)
        embed.add_field(name="Blue Team", value=f'\n {blue_team}', inline=False)

        await ctx.send(content=None, embed=embed)


def setup(client):
    client.add_cog(Pvp(client))





