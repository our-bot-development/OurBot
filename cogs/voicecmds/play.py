import discord, asyncio
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord.errors import ClientException
from discord.commands import SlashCommand, slash_command
import DiscordUtils
from discord.ui import View
from DiscordUtils import NotConnectedToVoice
music = DiscordUtils.Music()


# await something.send('Press the button!', view=view)

class PlayCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
# TODO: if voice client (the bot is to a voice channel) it wont join any other when the command is invoked
    @commands.command(name='play' , aliases=["p"])
    
    # @commands.before_invoke()
    async def play(self, ctx, *, song: str=None):


























        # if song != None:
        #     player = music.get_player(guild_id=ctx.message.guild.id)
        #     if (ctx.message.author.voice):
        #         try:
        #             voiceChannel =  ctx.message.author.voice.channel
        #             voice = await voiceChannel.connect()
        #         except AttributeError:
        #             await ctx.reply("You Are Not Connected To a Voice Channel")
        #         except:
        #             raise
        #     elif not ctx.message.author.voice:
        #         await ctx.reply("You Are Not Connected To a Voice Channel")
        #     if not player:
        #         try:
        #             player = music.create_player(ctx, ffmpeg_error_betterfix=True)
                
        #         except:
        #             raise
        #         # except DiscordUtils.Music.NotConnectedToVoice:
        #         #     await ctx.reply("TF-ing You Not Connected To Voice")
        #     if not ctx.voice_client.is_playing():
        #         try:
                    
        #             await player.queue(song, search=True)
        #             song = await player.play()
        #             await ctx.reply(f"I Have Started Playing `{song.name}`")
                
        #         except:
        #             raise
        #     else:
        #         song = await player.queue(song, search=True)
        #         await ctx.reply("Your Song Has Been Added To Queue") 
        # else:
        #     try:
        #         voiceChannel = ctx.author.voice.channel
        #         voice = await voiceChannel.connect()
        #         player = music.create_player(ctx, ffmpeg_error_betterfix=True)
        #         song = "rickroll"
        #         await player.queue(song, search=True)
        #         song = await player.play()
        #         await ctx.reply("In The Next Time, The Song Must Be a Song, Not Empty, OK?")
        #     except AttributeError:
        #         await ctx.reply("You Are Not Connected To A Voice Channel")
            
        #     except:
        #         raise
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if (song != None):
        #     player = music.get_player(guild_id=ctx.message.guild.id)
        #     try:
        #         voiceChannel =  ctx.message.author.voice.channel
        #         voice = await voiceChannel.connect()
        #     except AttributeError:
        #         await ctx.reply("you are not connected to any voice channel")
                
            
        #     except:
        #         raise
        if song == None:
            await ctx.reply("Please Specify Song")
        elif ctx.author.voice:
            voiceChannel = ctx.message.author.voice.channel
            voice = await voiceChannel.connect()
            # source = discord.FFmpegPCMAudio("rickroll.mp3", pipe=True)
            source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio())
            # source = discord.FFmpegPCMAudio("./songs/rickroll.mp3")
            voice.play(source)
            embed = discord.Embed(title="I Joined And Played Song!", description=f"Song Or Audio Played!\nVoice Channel: <#{ctx.author.voice.channel.id}>", color=4521907)
            await ctx.reply(embed=embed)
            print("audio is now playing")





def setup(bot):
    bot.add_cog(PlayCog(bot))