import discord
from discord.ext import commands
# from .play import player
from DiscordUtils import Music
music = Music()


class LeaveCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["l"])
    async def leave(self, ctx):
        # our_player = music.get_player(guild_id=ctx.message.guild.id)
        voicetrue = ctx.author.voice
        mevoicetrue = ctx.guild.me.voice
        if (ctx.voice_client):
            player = music.get_player(guild_id=ctx.voice_client.guild.id)
            music.queue = {}
            
            embed = discord.Embed(title="I left.", description=f"I left The Voice Channel\nVoice Channel: <#{ctx.voice_client.channel.id}>", color=4521907)
            voiceChannel = ctx.guild.voice_client
            await voiceChannel.disconnect()
            await ctx.reply(embed=embed)
            

def setup(bot):
    bot.add_cog(LeaveCog(bot))
