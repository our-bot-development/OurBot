import discord
from discord.embeds import EmptyEmbed
from discord.ext import commands


class AvatarCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['a', 'pfp'])
    async def avatar(self, ctx, user: discord.User = None):
        if user == None:
            user = ctx.author
        av = user.avatar
        av = av.with_size(1024)
        embed = discord.Embed(title=f"{user}\'s Avatar", description=EmptyEmbed)
        embed.set_image(url=av)
        await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(AvatarCog(bot))
