import datetime
import discord
from discord.ext import commands
import datetime, calendar



class OnMsgCog (commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message_delete(self, message):
        embed = discord.Embed(title="Message(s) Deleted", description=f"message deleted in <#{message.channel.id}>", color=discord.Colour.from_rgb(166,109,149), timestamp=datetime.datetime.now())
        embed.add_field(name="🔽 Content 🔽", value=f"Message Author: {message.author.mention}\nChannel: <#{message.channel.id}>\nContent:```msg\n{message.content}```", inline=False)
        embed.set_footer(icon_url=message.author.avatar.url)
        await message.channel.guild.get_channel(889105186797273119).send(embed=embed)
    
    @commands.Cog.listener()
    @commands.guild_only()
    async def on_message_edit(self, before, after):
        embed = discord.Embed(title=f"Message Edited", description=f"Message Edited In <#{before.channel.id}>\nContent(before):```msg\n{before.content}```\nContent(after)```msg\n{after.content}```", color=discord.Colour.from_rgb(60,231,167), timestamp=datetime.datetime.now())
        embed.set_author(name=f"{before.author.name}", icon_url="https://probot.media/3OwOpxw4q8.png")
        await before.guild.get_channel(889105186797273119).send(embed=embed)
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author.bot:
            return
        elif msg.content == "foo":
            await msg.channel.send("Tic Tac Toe: X goes first")


    # @commands.Cog.listener()
    # async def on_message(self, msg):
    #     # if (msg == True) and (msg.author != msg.author.bot):
    #     if msg:
    #         dee = datetime.datetime.utcnow()
    #         unixtime = calendar.timegm(dee.utctimetuple())
    #         # print(f"{unixtime}")
    #         # await msg.channel.send(f"hmmm\n {unixtime} ")
    #         embed = discord.Embed(title="hmmmmm, a new message", description="bro what", timestamp=datetime.datetime.now())
            # await msg.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(OnMsgCog(bot))