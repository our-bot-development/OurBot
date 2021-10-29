import sys;sys.dont_write_bytecode = True
import discord
from discord.ext import commands
import datetime
# from main import client
guild = discord.Guild

class ListenCog (commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_connect(self):
		print("i'm connected")
	
	@commands.Cog.listener()
	async def on_resumed(self):
		print("the client has resumed a session")
	# @commands.Cog.listener()
	# @commands.guild_only()
	# async def on_typing(self, channel_id, user, when: datetime.datetime):
	# 	embed = discord.Embed(title=f"Someone Typing in a channel", description=f"{user.mention} is typing in <#{channel_id.id}>", color=discord.Colour.from_rgb(125, 50, 90))
	# 	# await channel_id.guild.get_channel().send(embed=embed)
	# 	await client.get_channel(889105186797273119).send(embed=embed)



def setup(bot):
	bot.add_cog(ListenCog(bot))