import discord
from discord.commands import Option, SlashCommand
from discord.ext import commands

class hiCogS (commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # @slash_command(name="hi", description="Sends Hi Or Reply")
    @SlashCommand
    async def hi(
        self, 
        ctx,
        name: Option(str, "Enter Your Name", required=True),
        age: Option(int, "Enter Your Age", default=18, required=False),
        gender: Option(str, "Choose Your Gender", choices=["Male", "Female"], required=False)
    ):
        await ctx.respond(f"Hi {name} ")

def setup(bot):
    bot.add_cog(hiCogS(bot))