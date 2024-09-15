import discord
from dotenv import load_dotenv
import os
from bot_1 import MyClient
from discord.ext import commands
from datetime import date, timedelta, datetime
from dadadadadadadada import you_were_the_chosen_one

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
async def join(context):
    if not context.message.author.voice:
        await context.reply('You are not in a voice channel, join a voice channel!')
    else:
        await context.message.author.voice.channel.connect()


@client.event
async def on_voice_state_update(member, before, after):
    if member.bot:
        return
    if after.channel:
        if after.channel.name == 'Угадай мелодию' and len(member.voice.channel.members) >= 2:
            await member.voice.channel.connect()
@client.event
async def on_message(message):
    you_were_the_chosen_one(message)
    await client.process_commands(message)

@client.command()
async def leave(context):
    await context.voice_client.disconnect()


@client.command()
async def play(context):
    song = discord.FFmpegOpusAudio('music\\Estrelar (Remix).mp3')
    context.voice_client.play(song)


@client.command()
async def pause(context):
    voice = discord.utils.get(client.voice_clients, guild=context.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await context.send('At the moment, there is no audio playing in the voice channel!')


@client.command()
async def resume(context):
    voice = discord.utils.get(client.voice_clients, guild=context.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await context.send("At the moment, no song is paused!")


@client.command()
async def stop(context):
    voice = discord.utils.get(client.voice_clients, guild=context.guild)
    voice.stop()


@client.command()
async def is_paused(context):
    voice = discord.utils.get(client.voice_clients, guild=context.guild)
    if voice.is_paused():
        await context.send('The audio file execution is currently stopped!')
    else:
        await context.send('This audio file is being played!')


@client.command()
async def is_playing(context):
    voice = discord.utils.get(client.voice_clients, guild=context.guild)
    if voice.is_playing():
        await context.send('This audio file is being played!')
    else:
        await context.send('The audio file is not playing right now!')


load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client.run(token)
