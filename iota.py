import discord
import os
import random
from discord.ext import commands, tasks


TOKEN = "NjE1OTcyMjg2MTU5MjU3NjIx.XWiEQA.y3KCj4GkKELSpf-gZZrG7tFYzAc"

client = commands.Bot(command_prefix='!')

# manual load command for extensions
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

# manual Unload command for extensions
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


# automatically load all extensions from the cogs folder
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


# List of possible status's
status = [

        'Writing new Lemon Jokes',
        'Quickplay',
        'Waiting for ShadowKeep',
        'Hacking the Planet',
        'Convincing DeeDee to come back',
        'Chatting with Benedict',
        'Petting the Colonel',
        'Hodor',
        'Vanguard Strikes',
        'Sparrow Racing League',
        'Huwu',
        'KingsFall',
        'Last Wish',
        'Crown of Sorrows',
        'Destiny 2 Comp',
        'Trials',
        'Prison of Elders',
        'Chatting with Rasputin',
        'In Orbit',
        'Patrolling on EDZ',
        'Patrolling on Titan',
        'Patrolling on Mars',
        'Patrolling on Io',
        'Gambit Prime',

    ]


@client.event
async def on_ready():
    change_status.start()
    print(f'bot {client.user.name} is online')


# loop the bot's 'Playing' status
@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(random.choice(status)))


client.run(TOKEN)