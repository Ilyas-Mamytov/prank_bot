import argparse

import discord
from dotenv import load_dotenv
import os

from discord.ext import commands
from datetime import date, timedelta, datetime
from classes import get_random_elements
from classes import load_music, Out, Game

NAME_BOT = 'guess the melody bot#9057'

MUSIC_PATH = '.\\music\\'


intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(intents=intents, command_prefix='!')
GAME = None

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
    if message.author.bot == NAME_BOT:
        return
    if GAME:
        GAME.process_guess(message.content, str(message.author.global_name))
    await client.process_commands(message)



@client.command()
async def leave(context):
    await context.voice_client.disconnect()


@client.command()
async def play(context, args):
    players = [player.global_name for player in context.voice_client.channel.members if not player.bot]
    args = int(args)
    global GAME
    GAME = Game(players, '.\\music\\', args)
    song = discord.FFmpegOpusAudio(MUSIC_PATH+GAME.songs.current_song.link, options='-frames:a 500')
    context.voice_client.play(song)


@client.command()
async def next(context):
    await context.send(GAME.output_players_dictionary())
    await context.send(GAME.songs.current_song.author + GAME.songs.current_song.name)
    try:
        song = discord.FFmpegOpusAudio(MUSIC_PATH + GAME.songs.next_song().link, options='-frames:a 500')
        context.voice_client.play(song)
    except Out:
        await context.send('Игра заканчивается, ' + GAME.end())


@client.command()
async def end_game(context):
    results = GAME.end()
    print(results)
    await context.send(results)


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

