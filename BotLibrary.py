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
from tqdm import tqdm
from dotenv import load_dotenv

# Bot Main Functions
# Init
def CreateBot(TriggerPrefix):
    return Bot(command_prefix=TriggerPrefix)

# Run
def RunBot(client, TOKEN):
    client.run(TOKEN)

# Bot Command Functions
def AddResponseCommand(client, triggerWord, ResponseText):
    NewClientCommandCode = open("ClientCommandCode.txt", 'r').read()
    exec_code = NewClientCommandCode.replace('triggerWord', "'" + triggerWord + "'")
    exec_code = exec_code.replace('ResponseText', "'" + ResponseText + "'")
    exec(exec_code)

def AddCustomResponses(client, file_path=None):
    print("Adding Custom Responses from file", file_path)

    # Read file and add line by line
    n_cmds = 0
    for line in tqdm(open(file_path, 'r').readlines()):
        # Parse
        MessageSplitUp = line.strip().split(' - ')
        if len(MessageSplitUp) == 1 or MessageSplitUp[0] == '':
            continue
        triggerWord = MessageSplitUp[0]
        ResponseText = ' - '.join(MessageSplitUp[1:])
        print(str(n_cmds+1) + ':', triggerWord, '-', ResponseText)

        # Add to client
        AddResponseCommand(client, triggerWord, ResponseText)

        n_cmds += 1
    