import discord
from discord.ext import commands


class FightClubCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @commands.command(name='fight', description='Auto sorts players for private pvp. !fight <player1 player2 ect...')
        @commands.guild_only()
        async def sort_fighters(ctx, players: str):
            return


# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(FightClubCog(bot))