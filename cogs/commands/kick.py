import discord
from discord import errors
from discord.ext import commands


class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(aliases=['k', 'طرد'])
    @commands.has_permissions(administrator=True)
    @commands.guild_only()
    async def kick(self, ctx, user: discord.User, *, reason=None):
        try:
            await user.kick(reason=reason)
            embed1 = discord.Embed(title="Kick Command", description=f"User ({user.mention}) Has Been Kicked!", color=discord.Colour.from_rgb(55,115,67))
            await ctx.channel.send(embed=embed1)
            dm_embed = discord.Embed(title="You Got kicked!", description=f"You Got Kicked By <@{ctx.author.id}> In Server {ctx.guild.name}")
            await user.send(embed=dm_embed)
        
        except discord.Forbidden:
            await ctx.channel.send("Gimme perms")
        except discord.ext.commands.errors.MissingPermissions:
            await ctx.channel.send("u dont have perms")
        
        
        
        
        
        
        
        
        # except discord.Forbidden.with_traceback():
        #     print("i can't")
        #     await ctx.reply(f"😕 Couldn't Kick That Guy ({user.mention})")
        # except discord.ext.command.MissingPermissions:
        #     print("the guy have missing perms")
        #     await ctx.channel.send("You Are Missing Some Permissions")




def setup(bot):
    bot.add_cog(Kick(bot))
PYTHONDONTWRITEBYTECODE=1