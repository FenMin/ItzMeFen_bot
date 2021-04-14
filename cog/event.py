import discord
from discord.ext import commands


class event():
    def __init__(self,bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(event(bot))

