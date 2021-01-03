import discord
from discord.ext import commands
import random

def setup(bot):
    bot.add_cog(DickSize(bot))

class DickSize(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dicksize(self, ctx):
        """How large is your dick? Find out!"""
        if ctx.message.author.id==440231799533338634:
            size = 12
        elif ctx.message.author.id==307243110998605824:
            size = 12
        else:
            size = random.randint(3,10)
        await ctx.send(f"{ctx.author.name} has a **{size}-inch** dick!")
