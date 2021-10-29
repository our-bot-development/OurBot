import discord
from discord.ext import commands
import DiscordUtils
music = DiscordUtils.Music()

class PauseCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pause(self, ctx):
        try:
            player = music.get_player(guild_id=ctx.message.guild.id)
            song = await player.pause()
            await ctx.reply(f"Paused\nBy: {ctx.author.mention}")            
        except DiscordUtils.NotConnectedToVoice:
            await ctx.reply("I'm Not Even In a Voice Channel Right Now")
        
        except DiscordUtils.NotPlaying:
            await ctx.reply("I'm Not Playing Music Right Now")
        
        except:
            raise

        # await ctx.send('`,`'.join([song.name for song in player.current_queue()]))
    

def setup(bot):
    bot.add_cog(PauseCog(bot))