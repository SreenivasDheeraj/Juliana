#############################IMPORT#########################################################
import discord as dc
from discord.ext.commands import Bot
from discord.utils import get as gt
import asyncio
import os
import random
from dotenv import load_dotenv
############################init##############################################################
TOKEN = 'Njc4Mjg2MTMxMDcwMjM4NzQw.XkgnJw.e_jqfJbM6acEt33Y_YiOqnfdpAM'

trigger=['j!']
client = Bot(command_prefix=trigger)
channel= client.get_channel(678286131070238740)


#########################################Further Commands############################################################

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(str(client.user))
    print('------')
    return



@client.command(name= '8ball',pass_context=True)
@asyncio.coroutine
async def eight_ball(context):
    possible_responses=['As I see it, yes',
    'Ask again later',
    'Better not tell you now',
    'Cannot predict now',
    'Concentrate and ask again',
    'Don’t count on it',
    'It is certain',
    'It is decidedly so',
    'Most likely',
    'My reply is no',
    'My sources say no',
    'Outlook not so good',
    'Outlook good',
    'Reply hazy, try again',
    'Signs point to yes',
    'Very doubtful',
    'Without a doubt',
    'Yes',
    'Yes – definitely',
    "You may rely on it"]
    await context.channel.send(random.choice(possible_responses)+ context.message.author.mention)
    return

# @client.event
#########################################RUN#########################################################################
client.run(TOKEN)
