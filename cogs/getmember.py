import discord
from discord.ext import commands


def getmember(var: discord.Role):

    member : discord.Member
    member_list = []

    for member in var.members:
        member_list.append(member.display_name)

    return member_list


class Members(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='memberof', description="gets members of a role")
    async def memberof(self, ctx, var: discord.Role):
        members = getmember(var)

        await ctx.send(members)




def setup(client):
    client.add_cog(Members(client))