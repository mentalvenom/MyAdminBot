import discord
from discord.ext import commands
import random

def setup(bot):
    bot.add_cog(RPS(bot))

class RPS(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

@commands.command()
async def rps(self, ctx, *, player_input):
	choices = ['Rock', 'Paper', 'Scissors']
	bot_input = random.choice(choices)

	if player_input.lower() == bot_input.lower():
	    embed = discord.Embed(title = "Rock, Paper, Scissors", description = " ")
	    embed.add_field(name = "User's Choice", value = f"{player_input}", inline = True)
	    embed.add_field(name = "Bot's Choice", value = f"{bot_input}", inline = True)
	    embed.add_field(name = "Result", value = "Tie!") 
	    await ctx.send(embed = embed)
	elif player_input.lower() == "rock" and bot_input.lower() == "scissors":
	    embed = discord.Embed(title = "Rock, Paper, Scissors", description = " ")
	    embed.add_field(name = "User's Choice", value = f"{player_input}")
	    embed.add_field(name = "Bot's Choice", value = f"{bot_input}")
	    embed.add_field(name = "Result", value = "You win! :)")
	    await ctx.send(embed = embed)
	elif player_input.lower() == "scissors" and bot_input.lower() == "rock":
	    embed = discord.Embed(title = "Rock, Paper, Scissors", description = " ")
	    embed.add_field(name = "User's Choice", value = f"{player_input}", inline = True)
	    embed.add_field(name = "Bot's Choice", value = f"{bot_input}", inline = True)
	    embed.add_field(name = "Result", value = "You lose.")
	    await ctx.send(embed = embed)
	elif player_input.lower() == "paper" and bot_input.lower() == "rock":
	    embed = discord.Embed(title = "Rock, Paper, Scissors", description = " ")
	    embed.add_field(name = "User's Choice", value = f"{player_input}", inline = True)
	    embed.add_field(name = "Bot's Choice", value = f"{bot_input}", inline = True)
	    embed.add_field(name = "Result", value = "You win! :)")
	    await ctx.send(embed = embed)
	elif player_input.lower() == "rock" and bot_input.lower() == "paper":
	    embed = discord.Embed(title = "Rock, Paper, Scissors", description = " ")
	    embed.add_field(name = "User's Choice", value = f"{player_input}", inline = True)
	    embed.add_field(name = "Bot's Choice", value = f"{bot_input}", inline = True)
	    embed.add_field(name = "Result", value = "You lose.")
	    await ctx.send(embed = embed)
	elif player_input.lower() == "scissors" and bot_input.lower() == "paper":
	    embed = discord.Embed(title = "Rock, Paper, Scissors", description = " ")
	    embed.add_field(name = "User's Choice", value = f"{player_input}", inline = True)
	    embed.add_field(name = "Bot's Choice", value = f"{bot_input}", inline = True)
	    embed.add_field(name = "Result", value = "You win! :)")
	    await ctx.send(embed = embed)
	elif player_input.lower() == "paper" and bot_input.lower() == "scissors":
	    embed = discord.Embed(title = "Rock, Paper, Scissors", description = " ")
	    embed.add_field(name = "User's Choice", value = f"{player_input}", inline = True)
	    embed.add_field(name = "Bot's Choice", value = f"{bot_input}", inline = True)
	    embed.add_field(name = "Result", value = "You lose.")
	    await ctx.send(embed = embed)
	else:
	    await ctx.send(f"{ctx.author.mention} Be sure to choose an option. Rock, Paper, or Scissors?")

	@rps.error
	async def rps_error(self, ctx, error):
	if isinstance(error, (commands.MissingRequiredArgument)):
	    await ctx.send(f"{ctx.author.mention} Be sure to choose an option. Rock, Paper, or Scissors? Try: `;rps <option>`.")
