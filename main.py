import discord
from discord.ext import commands
import random
import time
import datetime
import json
import youtube_dl
import os
import sys
from cog import command
from cog import embed
from cog import event



with open('cog\id.json') as f:
    data = json.load(f)



intents = discord.Intents.all()

bot = commands.Bot(command_prefix='#',intents=intents)

path = 'C:\\Users\\user\\Desktop\\DiscordBOT\\ItzMeFen_bot\\cog'
dir = os.listdir(path)
print (dir)                                           #search path 

cogs = ["command" , "embed" , "event"]
#---------------------------------------------------------------------------------

@bot.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command()
async def leave(ctx):
    print("hi")



@bot.command()
async def apex(ctx):
    embed=discord.Embed(title="APEX", url="https://apex.tracker.gg/apex/profile/origin/", description="Your Apex Informantion", color=0xe90101 , timestamp=datetime.datetime.today())
    embed.set_author(name="FenMin", url="https://apex.tracker.gg/apex/profile/origin/FenMin/overview", icon_url="https://i.imgur.com/A8J8ngD.gif")
    embed.set_thumbnail(url="https://i.imgur.com/ctpVWoS.png")
    embed.add_field(name="Kills", value="6965", inline=True)
    embed.set_footer(text="")
    await ctx.send(embed=embed)
    



if __name__ == "__main__":
    for extension in cogs:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))
    bot.run(data['botid'])



@bot.event
async def on_ready():
    print('Ready!')

