import discord
from discord.app.commands import command
from discord.ext import commands


class ClearCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['c', 'clean'])
    @commands.has_guild_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        if amount == None:
            await ctx.reply("** **")
            await ctx.channel.purge(limit=amount)


def sCogetup(bot):
    bot.add_cog(ClearCog(bot))
