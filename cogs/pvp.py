import discord
import random
from discord.ext import commands
from cogs.getmember import getmember

class Pvp(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def fight(self, ctx, *, players: discord.Role):
        player_list = getmember(players)
        random.shuffle(player_list)

        temp_team_1 = player_list[:len(player_list)//2]
        temp_team_2 = player_list[len(player_list)//2:]

        red_team = ' '.join(temp_team_1)
        blue_team = ' '.join(temp_team_2)

        title = [

            "Let's get ready to Rumble!!!",
            '3....2....1...**FIGHT**',
            'The teams are set!',
            'Remember no OEM...',
            'For the Glory of the Crucible!'

        ]

        embed = discord.Embed(title=random.choice(title), colour=0x6262ff)
        embed.add_field(name="Red Team", value=f'\n {red_team}', inline=False)
        embed.add_field(name="<<<<<<<<<>>>>>>>>>", value=' -  ╔════════╗  -\n-  ║   VS   ║  -\n-  ╚════════╝  -', inline=False)
        embed.add_field(name="Blue Team", value=f'\n {blue_team}', inline=False)

        await ctx.send(content=None, embed=embed)


def setup(client):
    client.add_cog(Pvp(client))




