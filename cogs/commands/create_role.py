import discord
from discord.ext import commands
from discord.permissions import Permissions

class CreateRoleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def create_role(self, ctx, name="new role by bot", *, permissions):
        if permissions == None:
            await ctx.reply("That Is Not Allowed")


        elif permissions.lower() == "advanced":
            permissions = Permissions.advanced()
        
        elif permissions.lower() == "none":
            permissions = Permissions.none()
        

        elif permissions.lower() == "all":
            permissions = Permissions.all()
        

        elif permissions.lower() == "all_channel":
            permissions = Permissions.all_channel()
        

        elif permissions.lower() == "general":
            permissions = Permissions.general()


        elif permissions.lower() == "membership":
            permissions = Permissions.membership()
        

        elif permissions.lower() == "tnv":
            permissions = Permissions.text() and Permissions.voice()
        

        elif permissions.lower() == "stage":
            permissions = Permissions.stage()
        

        elif permissions.lower() == "stage_mod":
            permissions = Permissions.stage_moderator()

        # else:
        #     await ctx.reply("You Can't Man, choose one from these, [advanced(admin), ]")


        await ctx.guild.create_role(name=name, permissions=permissions)



def setup(bot):
    bot.add_cog(CreateRoleCog(bot))
