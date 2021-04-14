import discord
from discord.ext import commands
import time

class command():
    def __init__(self,bot):
        self.bot = bot



    @commands.command()
    async def clean(self , ctx , num:int):
        await ctx.channel.purge(limit=num+1)
        await ctx.channel.send(f'已移除 ***{num}*** 則訊息')
        time.sleep(2)
        await ctx.channel.purge(limit=1)


def setup(bot):
    bot.add_cog(command(bot))