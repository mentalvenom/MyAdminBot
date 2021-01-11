import discord
from discord.ext import commands
import asyncio
import os
import time

def setup(bot):
    bot.add_cog(CountKek(bot))

class CountKek(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
        bot.message_counter = 0
        
        @bot.event
        async def on_message(message):
            user = message.author
            if message.content.startswith("kek"):
                bot.message_counter += 1
            await bot.process_commands(message)

        @bot.command()
        async def countkek(ctx):
            embed=discord.Embed(title="Kek Counter", description="Kek has been said {} times!".format(ctx.bot.message_counter) , color=0x00fffb)
            await ctx.send(embed=embed)
