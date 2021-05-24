import discord
import asyncio
import colorama 
import json
from discord.ext import commands
import os
import random 
from discord import Webhook, AsyncWebhookAdapter
from discord import Permissions



vepczongithub = commands.Bot(command_prefix="=", intents = discord.Intents.all())



token = "TOKEN"

print('''
                 _        
 |\/|  _.  _  _ | \ ._ _  
 |  | (_| _> _> |_/ | | | 
                          
''')
print('Say =sus <message> TO Massdm')
print('> Credit To Vepcz')


@vepczongithub.command()
async def sus(ctx, *, args=None):
    if args != None:
        members = ctx.guild.members
        for member in members:
            try:
                await member.send(args)
                print("[+] SENT DM TO " + member.name)
 
            except:
                print("[-] FAILED DM TO " + member.name)


vepczongithub.run(token)
