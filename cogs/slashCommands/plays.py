import discord
from discord.ext import commands
from discord.commands import Option, slash_command
from DiscordUtils import Music
music = Music()

class PlaysCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name='pla-it')
    async def _play(self, ctx, song: Option(str, "Enter Song's Name", required=True)):
        player = music.get_player(guild_id=ctx.message.guild.id)
        if (not ctx.voice_client) and (ctx.message.author.voice):
            voiceChannel =  ctx.message.author.voice.channel
            voice = await voiceChannel.connect()
        elif not ctx.message.author.voice:
            await ctx.reply("You Are Not Connected To a Voice Channel")
        if not player:
            player = music.create_player(ctx, ffmpeg_error_betterfix=True)
                # except DiscordUtils.Music.NotConnectedToVoice:
                #     await ctx.reply("TF-ing You Not Connected To Voice")
        if not ctx.voice_client.is_playing():
                
            await player.queue(song, search=True)
            song = await player.play()
            await ctx.reply(f"I Have Started Playing `{song.name}`")
        else:
            song = await player.queue(song, search=True)
            await ctx.reply("Your Song Has Been Added To Queue") 

def setup(bot):
    bot.add_cog(PlaysCog(bot))