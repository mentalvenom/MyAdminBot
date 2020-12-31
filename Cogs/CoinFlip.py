import discord
from discord.ext import commands
import random

def setup(bot):
    bot.add_cog(CoinFlip(bot))

class CoinFlip(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['flip', 'coin'])
    async def coinflip(self, ctx):
        """ Coinflip! """
        coinsides = ['Heads', 'Tails']
        await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")
