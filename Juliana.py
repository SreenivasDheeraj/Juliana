'''
Main Script to Run Juliana Bot
'''

########################################## - Imports - ################################################
import discord as dc
from discord.ext.commands import Bot
import json

import BotLibrary

import random
from discord import Member
from discord.ext.commands import has_permissions


########################################## - Init - ###################################################
print("Init Bot...\n")

# Load Bot Data
configData = json.load(open('config.json'))
BotName = configData['BotName']
TOKEN = configData['TOKEN']
# TOKEN = 'Njc4Mjg2MTMxMDcwMjM4NzQw.XkgnJw.e_jqfJbM6acEt33Y_YiOqnfdpAM'
trigger = configData['Trigger']

# Create Bot
client = Bot(command_prefix=trigger)
# channel = client.get_channel(678286131070238740)

# Init Script Data
BotLibrary.configData = configData

# Load Custom Response Commands from directory
CustomResponses_path = configData['TriggerResponses_Path']
BotLibrary.AddCustomResponses(client, path=CustomResponses_path)

print("\n\n")

########################################## - Bot Events - #############################################
# Bot Started Event
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(str(client.user))
    print('------')
    print("\n\n")
    return

########################################## - Basic Ping Commands - ####################################
# Basic Commands
BotLibrary.AddCommandsFromFile(client, 'Commands/Commands_Basic.py')

########################################## - Admin Commands - ########################################
BotLibrary.AddCommandsFromFile(client, 'Commands/Commands_Admin.py')
    
########################################## - Further Commands - ########################################
# 8 Ball Random Reponse
BotLibrary.AddCommandsFromFile(client, 'Commands/Commands_8Ball.py')

# Trigger-Response Commands
BotLibrary.AddCommandsFromFile(client, 'Commands/Commands_Trigger-Response.py')

########################################## - RUN - #####################################################
# Run the Client
client.run(TOKEN)