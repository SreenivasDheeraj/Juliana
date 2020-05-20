'''
Main Script to Run Juliana Bot
'''

########################################## - Imports - ################################################
import discord as dc
from discord.ext.commands import Bot
import json

import BotLibrary
from Utils import FirebaseLibrary

import random
from discord import Member
from discord.ext.commands import has_permissions


########################################## - Init - ###################################################
print("Init Bot...\n")

# Load Bot Data
configData = json.load(open('config.json'))
BotName = configData['bot_name']
TOKEN = configData['bot_token']
# TOKEN = 'Njc4Mjg2MTMxMDcwMjM4NzQw.XkgnJw.e_jqfJbM6acEt33Y_YiOqnfdpAM'
trigger = configData['bot_trigger']

# Create Bot
client = Bot(command_prefix=trigger)
# channel = client.get_channel(678286131070238740)

# Init Script Data
# BotLibrary
BotLibrary.configData = configData
BotLibrary.client = client
# FirebaseLibrary
FirebaseLibrary.configData = configData
FirebaseLibrary.DBInit()


# Load Custom Response Commands from directory
CustomResponses_path = configData['trigger-response_path']
BotLibrary.AddCustomResponses(path=CustomResponses_path)
# Load Custom Response Commands from Cloud
for tr in FirebaseLibrary.GetAllTriggerResponses():
    tr = tr.to_dict()
    if 'trigger' in tr.keys() and 'response' in tr.keys():
        BotLibrary.AddResponseCommand(tr['trigger'], tr['response'])

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