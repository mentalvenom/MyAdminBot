import discord
from discord.ext import commands
from AntiSpam import AntiSpamHandler

bot = commands.Bot(command_prefix="+")

def setup(bot):
    bot.add_cog(SpamHandler(bot))

class SpamHandler(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

warn_embed_dict = {
    "title": "**Attention $USERNAME**",
    "description": "You are being warned for spam",
    "timestamp": True,
    "color": 0xFF0000,
    "footer": {"text": "$BOTNAME", "icon_url": "$BOTAVATAR"},
    "author": {"name": "$GUILDNAME", "icon_url": "$GUILDICON"},
    "fields": [
        {"name": "Current warns:", "value": "$WARNCOUNT", "inline": False},
        {"name": "Current kicks:", "value": "$KICKCOUNT", "inline": False},
    ],
}
bot.handler = AntiSpamHandler(bot, 1, ignore_bots=False, ignore_roles=["794690719888834561","770782107034845204","774077932963627009","774077162080436244"], guild_warn_message=warn_embed_dict)

@bot.event
async def on_message(message):
    bot.handler.propagate(message)
    await bot.process_commands(message)
    await user.add_roles("772566718438309890")
