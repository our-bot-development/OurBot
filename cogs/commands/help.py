import discord
from discord.colour import Color
from discord.ext import commands


class HelpCog (commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['h', 'مساعدة'])
    async def help(self, ctx, command=None):
        if command == None:
            embed = discord.Embed(title="Help Command", description=f"the help has reached you!", color=discord.Colour.from_rgb(90,156,159))
            embed.set_author(name="Help Reached!", icon_url="https://probot.media/3OwOpxw4q8.png")
            embed.add_field(name="Admin's Commands", value="ban[b]\nkick[k]\n")# `--------` Usage: <user_mention> <reason>  Ban The User From This Server\n")
            await ctx.message.add_reaction("✅")
            #embed.set_footer(text=discord.utils.utcnow())
            await ctx.author.send(embed=embed)
        elif command == ("b" or "ban"):
            embed = discord.Embed(title="Ban command!", description="b/ban `--------` Usage: <user mention> <reason>")
            await ctx.author.send(embed=embed)
def setup(bot):
    bot.add_cog(HelpCog(bot))