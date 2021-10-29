import discord
from discord.ext import commands

class OnGuildCog (commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	


def setup(bot):
	bot.add_cog(OnGuildCog(bot))
PYTHONDONTWRITEBYTECODE=1