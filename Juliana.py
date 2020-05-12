########################################## - Imports - ################################################
import discord as dc
from discord.ext.commands import Bot
from discord.utils import get as gt
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio
import os
import random
from dotenv import load_dotenv

import BotLibrary
########################################## - Init - ###################################################
print("Init Bot...\n")
TOKEN = 'Njc4Mjg2MTMxMDcwMjM4NzQw.XkgnJw.e_jqfJbM6acEt33Y_YiOqnfdpAM'
trigger = ['j!']
client = Bot(command_prefix=trigger)
# channel = client.get_channel(678286131070238740)

# Load Custom Response Commands from file
CustomResponses_path = 'CustomResponseCommands.txt'
BotLibrary.AddCustomResponses(client, CustomResponses_path)

print("\n\n")

########################################## - Basic ping commands - ####################################
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(str(client.user))
    print('------')
    print("\n\n")
    return
    

@client.command(name='hello',pass_context=True)
async def on_hello(message):
    # Bot should not reply to itself
    if message.author == client.user:
        return

    print("Trigerred Hello Response to", message)
    msg = 'Hello {0.author.mention}'.format(message)
    await message.channel.send(msg)
    return

@client.command(name='addresp', pass_context=True)
async def on_addresp(context, *, message=None):
    if message == None:
        await context.channel.send("Give in format: TriggerWord - ResponseText " + context.message.author.mention)
        return

    print("Trigerred Add Reponse ", message)
    # Parse to get triggerWord and ResponseText
    MessageSplitUp = message.strip().split(' - ')
    if len(MessageSplitUp) == 1 or MessageSplitUp[0] == '':
        await context.channel.send("Give in format: TriggerWord - ResponseText " + context.message.author.mention)
        return
    triggerWord = MessageSplitUp[0]
    ResponseText = ' - '.join(MessageSplitUp[1:])
    print("TriggerWord - ", triggerWord)
    print("ResponseText - ", ResponseText)

    # Add to Response
    BotLibrary.AddResponseCommand(client, triggerWord, ResponseText)
    await context.channel.send("Added Response " + context.message.author.mention)
    return

########################################## - Admin Commands - ########################################
@client.command(name='ban',pass_context=True)
@has_permissions(ban_members=True)
async def ban(context,user:dc.Member,*,reasons=None):
    if reasons==None:
        reasons= "no reason :person_shrugging:"
    await user.ban(reason=reasons)
    embed=dc.Embed(title="User banned!", description=("**"+user.mention+"** was banned by **"+str(context.message.author.mention)+"** because "+reasons).format(user, context.message.author), color=0xff00f6)
    await context.send(embed=embed)
    await user.send(embed=embed)

@client.command(name='kick',pass_context=True)
@has_permissions(kick_members=True)
async def kick(context,user:dc.Member,*,reasons=None):
    try:
        if reasons==None:
            reasons= "no reason :person_shrugging:"
        
        await user.kick(reason=reasons)
        embed=dc.Embed(title="User Kicked!", description=("**"+user.mention+"** was kicked by **"+str(context.message.author.mention)+"** because "+reasons).format(user, context.message.author), color=0xff00f6)
        await context.send(embed=embed)
        await user.send(embed=embed)
    except dc.Forbidden:
        await context.send("Nice try but you do not have permission qt :stuck_out_tongue_winking_eye:"+context.message.author.mention)
    
    return
       #mute does not work
@client.command(name='mute',pass_context = True)
async def mute(ctx, member: dc.Member):
     if ctx.message.author.guild_permissions.administrator:
        role = dc.utils.get(member.guild.roles, name='Muted')
        await member.add_roles(member, role)
        embed=dc.Embed(title="User Muted!", description=("**"+member+"** was muted by **"+str(ctx.message.author)+"**!").format(member, ctx.message.author), color=0xff00f6)
        await ctx.send(embed=embed)
     else:
        embed=dc.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await ctx.say(embed=embed)
#unban does not work
@client.command(name='unban',pass_context=True)
async def unban(context,user:dc.Member,*,reasons=None):
    if reasons==None:
        reasons= "no reason :person_shrugging:"
    await user.unban(reason=reasons)
    embed=dc.Embed(title="User Unbanned!", description="**{0}** was Unbanned by **{1}** because "+reasons.format(user, context.message.author), color=0xff00f6)
    await context.say(embed=embed)
    await user.send(embed=embed)
    return
    
########################################## - Further Commands - ########################################
# 8 Ball Random Reponse
@client.command(name='8ball', pass_context=True)
async def eight_ball(context):
    print("Trigerred 8ball Reponse to", context)
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
    await context.channel.send(random.choice(possible_responses) + context.message.author.mention)
    return



########################################## - RUN - #####################################################
# Run the Client
client.run(TOKEN)
