import discord
from discord.ext import commands
from secret import BOT_TOKEN

client = discord.Client()
bot = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


@bot.command()
async def play(ctx, args):
    print(args)


client.run(BOT_TOKEN)
