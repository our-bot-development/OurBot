import discord
from discord.ext import commands

class OnMemberCog (commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	



def setup(bot):
	bot.add_cog(OnMemberCog(bot))
PYTHONDONTWRITEBYTECODE=1