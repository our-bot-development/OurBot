import discord
from discord.ext import commands


class OnCommandErr(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(ctx, error):
        if error == TypeError:
            print("jdfa")
        else:
            raise error
    

def setup(bot):
    bot.add_cog(OnCommandErr(bot))
PYTHONDONTWRITEBYTECODE=1
