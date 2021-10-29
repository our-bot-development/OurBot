from os import name
import discord
from discord.ext import commands
from main import command_prefix as cmdpre

class Helpm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_guild_permissions(send_messages=True)
    @commands.guild_only()
    async def helpm(self, ctx, command=None):
        if command == None:
            embed = discord.Embed(title="Please Specify A Command", description="I Need An Argument")
            await ctx.reply(embed=embed);
        elif command == ("ban" or "b").lower():
            embed = discord.Embed(title="HelpM Ban Command!", description="Ban The User Specified With Reason (Reason Appear In Audit Log)", color="#43fh34")
            embed.add_field(name="Shortcuts", value=f"{cmdpre}ban\n{cmdpre}b", inline=False)
            embed.add_field(name="How To Use Ban Command", value=f"b <@{ctx.author.mention}> swear words man\nb {ctx.author.id} asking for admin") 
            embed.set_thumbnail(url="fd")


#ban[b](ban the user) 
def setup(bot):
    bot.add_cog(Helpm(bot))
