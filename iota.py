import discord
from discord.ext import commands

TOKEN = "NjE1OTcyMjg2MTU5MjU3NjIx.XWiEQA.y3KCj4GkKELSpf-gZZrG7tFYzAc"


def get_prefix(bot, message):

    prefixes = ['!!', '?']

    if not message.guild:
        return '?'

    return commands.when_mentioned_or(*prefixes)(bot, message)


initial_extensions = ['commands.members',
                      'Commands.fightclub',
                      ]

bot = commands.Bot(command_prefix=get_prefix, description='A Rewrite Cog Example')

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)


@bot.event
async def on_message(self, message):
    # we do not want the bot to reply to itself
    if message.author.id == self.user.id:
        return


@bot.event
async def on_ready():

    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    # Changes our bots Playing Status. type=1(streaming) for a standard game you could remove type and url.
    await bot.change_presence(game=discord.Game(name='writing lemon jokes'))
    print(f'Successfully logged in and booted...!')


bot.run(TOKEN, bot=True, reconnect=True)