import discord
from dotenv import load_dotenv
import os
from bot_1 import MyClient
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents, command_prefix='!')


@client.event
async def on_ready():
    print("i'm ready")


@client.command()
async def hello(context):
    await context.reply('hello')


@client.command()
async def voice(context):
    if not context.message.author.voice:
        await context.reply('You are not in a voice channel, Join a voice channel!')
    else:
        await context.message.author.voice.channel.connect()
@client.command()
async def out_channel(context):
    await context.voice_client.disconnect()

@client.command()
async def play(context):
    song=discord.FFmpegOpusAudio('music\\Estrelar (Remix).mp3')
    context.voice_client.play(song)

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client.run(token)
