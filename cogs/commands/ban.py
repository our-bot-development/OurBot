import discord
from discord.ext import commands
import datetime

class ModCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=["باند", "b"])
	#@commands.has_permissions((administrator=True) or (ban_members=True))
	@commands.guild_only()
	async def ban(self, ctx, member:discord.Member, *, reason=None):
		try:
			await member.ban(reason=reason)
			current_time = datetime.datetime.now()
			user = member
			embed = discord.Embed(title="User Banned!", description=f"User {user.mention} has been Banned!\nBy {ctx.author.mention}", color=discord.Colour.from_rgb(10, 70, 200))
			await ctx.channel.send(embed=embed)
			await ctx.guild.get_channel(889105186797273119).send(embed=embed)
			
		except discord.Forbidden:
			print("i can't ban")
			await ctx.reply(f"😕 Couldn't Ban That Guy ({member.mention})")

# embed.set_footer(text=current_time, icon_url=ctx.author.avatar.url)
def setup(bot):
    bot.add_cog(ModCog(bot))
PYTHONDONTWRITEBYTECODE=1