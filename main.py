import time;time_begin = time.time()
import sys;sys.dont_write_bytecode = True
import discord
from discord.ext import commands
from discord.ext import commands, tasks;
import sqlite3, os;
from random import choice
from dotenv import load_dotenv;
from rich.progress import track
load_dotenv()


intents = discord.Intents.all();global command_prefix
client = commands.Bot(command_prefix=commands.when_mentioned_or("?"), strip_after_prefix=True,  intents=intents, case_insensitive=True, owner_id=747864072879603743);
client.help_command = None;

########### database code #############
# c.execute("CREATE TABLE guild_prefixes (guild_id BIGINT, prefix STR DEFAULT \"?\")")

########## cogs code ################

initial_exten = [
	########### cogs.commands ##############
	# 'cogs.commands.ban',
	'cogs.commands.help',
	# 'cogs.commands.kick',
	# 'cogs.commands.create_role',
	'cogs.commands.avatar',
	# 'cogs.commands.setprefix',
	'cogs.commands.testcmd',

	########### cogs.voicecmds ###############
	'cogs.voicecmds.play',
	'cogs.voicecmds.leave',
	'cogs.voicecmds.pause',
	
	########## cogs.listeners #############
	'cogs.listeners.listeners',
	# 'cogs.listeners.onmember',
	# 'cogs.listeners.onguild',
	'cogs.listeners.on_guild_join',
	# 'cogs.listeners.onmessage',
	
	####### cogs.slashCommands ######
	'cogs.slashCommands.hi',
	'cogs.slashCommands.plays'
]

if __name__ == "__main__":
	from rich.table import Table
	print("\n\n")
	import time
	for i in track(range(2), description='Starting The Bot...'):
		time.sleep(0.3)
	table = Table(title='[green]Extensions[/green]\n-----------------')
	table.add_column('name')

	
	for extension in initial_exten:
		from rich import print
		
		
		
		client.load_extension(extension)
		ex_name = list(extension.split('.'))
		ex_name = ex_name[-1]
		table.add_row(f"[bold][red]{ex_name}[/red][/bold]" + "\n----------")
		
		# print(f'Extension: [red][bold]{ex_name}[/bold][/red] Loaded!')
	from rich import print
	print(table)


@client.command()
async def ping(ctx):
	embed = discord.Embed(title="Response!", description=f"It's {str(round(client.latency*1000))}ms!")
	print(client.latency * 1000)
	await ctx.reply(embed=embed)

@client.event
async def wait_until_ready(client: client):
	if await client.wait_until_ready():
			print("wait_until_ready() has been executed!")

stats = ["Hey There, My default Prefix is `?`", "My Owner is AnHalfGuy.py#6031", "Thanks For Choosing Me!, Appreciated", "Default Prefix Is `?`, You Can Change It By Command ?setprefix", "Do Any One Still Code With Java?", "I Don't Know Why Is My Owner Loves Python", "I Was Developed By A Python Lib Called py-cord | .gg/py-cord"]
@tasks.loop(seconds=20)
async def change_status():
	await client.change_presence(status=discord.Status.dnd, activity=discord.Game(choice(stats)))

@client.event
async def on_ready():
	# await client.change_presence(status=discord.Status., activity=discord.Game("?help"))
	await change_status.start()
	async for guildin in client.fetch_guilds():
		print(f"Server Name:{guildin.name}------------ID: {guildin.id}")
	#         # db = sqlite3.connect("./db/guildids.db	print("the bot is online")
	#  ")

time_end1 = time.time()
from rich import print
print(f"[bold][italic][cyan]Ready Time: {time_end1 - time_begin}[/cyan][/italic][/bold]")
token = os.getenv("TOKEN")
client.run(f"{token}")
time_end = time.time()

def print_that(text):
	print(str(text))
print(f"Execution Time: {time_end - time_begin}")