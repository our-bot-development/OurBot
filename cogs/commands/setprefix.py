import sys;sys.dont_write_bytecode = True
import discord, sqlite3, os
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument

# conn = sqlite3.connect("./guildPrefixes.sqlite3")
# c = conn.cursor()
# c.execute("""CREATE TABLE GUILDS_PREFIXES (guild_id int, prefix str)""")


class SetprefixCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["pre", "sp"])
    @commands.has_guild_permissions(manage_guild=True)
    @commands.guild_only()
    async def setprefix(self, ctx, new_prefix: str):
        if (new_prefix != None) and (len(new_prefix) > 0 and len(new_prefix) < 3):
            try:
                os.system("cd C:\\Users\\moon\\OneDrive\\Coding\\Python\\dis-bot\\db")
                conn = sqlite3.connect("guildPrefixes.db")
                c = conn.cursor()
                # c.execute("CREATE TABLE guilds_prefixes (guild_id BIGINT, new_prefix STR)")
                # c.execute(f"INSERT INTO guild_prefixes VALUES (?, ?)", (ctx.guild.id, str(new_prefix)))
                c.execute(f"UPDATE guild_prefixes SET prefix=\"{str(new_prefix)}\" WHERE guild_id={int(ctx.guild.id)}")
                conn.commit()
                conn.close()
                print(f"successed set prefix to {new_prefix}")
                await ctx.reply(f"Successed Set To `{new_prefix}` For The Server {{{ctx.guild}}}")
            except:
                raise
        
        else:
            await ctx.reply("An Error Occurred, Please Follow The Rules")
        # except MissingRequiredArgument:
        #         await ctx.reply(f"You Have Missing Required Argument Which Is new_prefix")
            
            

def setup(bot):
    bot.add_cog(SetprefixCog(bot))
