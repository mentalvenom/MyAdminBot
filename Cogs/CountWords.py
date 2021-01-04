import discord
from discord.ext import commands
import asyncio
import os
import time

def setup(bot):
    bot.add_cog(CountWords(bot))

class CountWords(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
        bot.countWords = 0
        
        @bot.event
        async def on_message(message):
          user = message.author
          if message.content.startswith("kek"):
              embed=discord.Embed(title="kek counter", description=f"{user} just said ***kek***", color=0x00ffee)
              embed.set_footer(text="tbh i don't care")
              await message.channel.send(embed=embed)
              bot.countWords += 1
          await bot.process_commands(message)
        @commands.command()
        async def countkek(ctx):
          """Counts the amount of times kek is said"""
          embed=discord.Embed(title="kek counter", description="kek was said {} times!".format(ctx.bot.countWords) , color=0x00ffee)
          embed.set_thumbnail(url="https://emoji.gg/assets/emoji/4667_great_shame.png")
          embed.set_footer(text="tbh i don't care")
          await ctx.send(embed=embed)
