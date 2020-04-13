'''
Library for accessing the bot easily
'''

# Imports
import discord as dc
from discord.ext.commands import Bot
from discord.utils import get as gt
import asyncio
import os
import random
from dotenv import load_dotenv

# Bot Main Functions
# Init
def CreateBot(TriggerWords):
    return Bot(command_prefix=TriggerWords)
