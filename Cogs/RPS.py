
import discord
from discord.ext import commands
import random

def setup(bot):
	# Add the bot
	bot.add_cog(RPS(bot))
	
class RPS(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

	@commands.command(description="Rock Paper Scissors")
	    async def rps(self, msg: str):
		"""Rock paper scissors. Example : /rps Rock if you want to use the rock."""
		print('Rock Paper Scissors!')
		t = ["rock", "paper", "scissors"]
		computer = t[random.randint(0, 2)]
		player = msg.lower()
		print(msg)
		if player == computer:
		    await self.bot.say("Tie!")
		elif player == "rock":
		    if computer == "paper":
			await self.bot.say("You lose! {0} covers {1}".format(computer, player))
		    else:
			await self.bot.say("You win! {0} smashes {1}".format(player, computer))
		elif player == "paper":
		    if computer == "scissors":
			await self.bot.say("You lose! {0} cut {1}".format(computer, player))
		    else:
			await self.bot.say("You win! {0} covers {1}".format(player, computer))
		elif player == "scissors":
		    if computer == "rock":
			await self.bot.say("You lose! {0} smashes {1}".format(computer, player))
		    else:
			await self.bot.say("You win! {0} cut {1}".format(player, computer))
		else:
		    await self.bot.say("That's not a valid play. Check your spelling!")
