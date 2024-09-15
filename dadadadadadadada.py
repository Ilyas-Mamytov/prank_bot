from datetime import date, timedelta, datetime
import asyncio
import os
import discord

async def you_were_the_chosen_one(message):

    if str(message.author) == 'chelhfj':  #fugu35
        msg = 'figus moment'

        if message.content.lower().find('инет') != - 1:
            filename = 'light.png'
            date_file = 'fuggus_not_unet_day.txt'

        elif message.content.lower().find('свет') != - 1:
            filename = 'dark.jpg'
            date_file = 'fuggus_last_day.txt'
        else:
            return

        if not os.path.exists(date_file):
            with open(date_file, 'w') as f:
                vchera = date.today() - timedelta(days=1)
                f.write(vchera.strftime('%d %b %y'))

        with open(date_file, 'r') as f:
            last_day = f.read()
            last_day = datetime.strptime(last_day, '%d %b %y').date()

        today = date.today()
        if not last_day == today:
            print(last_day, today)
            file = discord.File(filename)
            embed = discord.Embed()
            embed.set_image(url=f'attachment://{filename}')
            last_day = today

            with open(date_file, 'w') as f:
                f.write(last_day.strftime('%d %b %y'))

            await message.reply(msg, file=file, embed=embed)

    if str(message.author) == 'kz213.': #'lpodok':
        msg = 'плачь, дурень'
        if not os.path.exists('lpodok_last_day.txt'):
            with open('lpodok_last_day.txt', 'w') as f:
                vchera = date.today() - timedelta(days=1)
                f.write(vchera.strftime('%d %b %y'))

        with open('lpodok_last_day.txt', 'r') as f:
            last_day = f.read()
            last_day = datetime.strptime(last_day, '%d %b %y').date()

        today = date.today()
        print(today, last_day)
        print(type(today), type(last_day))
        if not last_day == today:
            last_day = today

            with open('lpodok_last_day.txt', 'w') as f:
                f.write(last_day.strftime('%d %b %y'))

            await message.reply(msg)
