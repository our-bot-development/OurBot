import discord
from discord.ext import commands
import sqlite3

class SetupbotCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    @commands.guild_only()
    async def setup(self, ctx):
        guild = ctx.guild
        default_prefix = "?"
        guild_id = guild.id
        try:
            our_category = await ctx.message.guild.create_category("Music🎵")
            our_category_name = str(our_category)
            our_category_id = our_category.id
            await our_category.create_text_channel('for-music', reason="because an admin run the command `?setup`", category=our_category_name)
        except discord.Forbidden:
            await ctx.reply("**I Don't Have The `Manage Channels` Permission**\n**Give It To Me To Run That Command**")
        
        co = sqlite3.connect(".../db/setup.db")
        c = co.cursor()
        c.execute(f"INSERT INTO setups (guild_id, prefix, music_channel_id) VALUES ({guild_id}, {default_prefix}, {our_category_id})")
        
        await ctx.reply("Setup For This Server Created")
















def setup(bot):
    bot.add_cog(SetupbotCog(bot))
