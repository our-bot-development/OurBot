import discord, sqlite3
from discord.ext import commands
import importlib, os, sys
sys.dont_write_bytecode = True
# c.execute("CREATE TABLE guild_prefixes (guild_id BIGINT, prefix STR DEFAULT \"?\")")
class OnGuildJoinCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        os.system("cd C:\\Users\\moon\\OneDrive\\Coding\\Python\\dis-bot\\db")
        conn = sqlite3.connect("guildPrefixes.db")
        c = conn.cursor()
        c.execute("CREATE TABLE guild_prefixes (guild_id BIGINT, prefix STR DEFAULT \"?\")")
        
        print(c.execute(f"INSERT INTO guild_prefixes (guild_id, prefix) VALUES ({int(guild.id)}, \"?\")"))
        print(c.execute(F"SELECT * FROM guild_prefixes WHERE guild_id={int(guild.id)}"))
        print(c.fetchall())
        conn.commit()
        conn.close()
        print("successed join guild ")



def setup(bot):
    bot.add_cog(OnGuildJoinCog(bot))