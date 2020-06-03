import discord
import asyncio
from discord.ext import commands
import logging
# import datetime as dt
# from dateutil.parser import parse
# import sched

logger = logging.getLogger('discord')
#logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

default_prefix = "."

TOKEN = ""

import traceback

try:
	with open("key.txt", encoding="utf-8") as f:
		TOKEN = f.read()
except:
	print("VALAMI NEM JÓ A key.txt FÁJLBAN:")
	traceback.print_exc()
	exit()


attachedMessages = {}

swearing = ["basz", "bassz", "bazd", "picsa", "picsá", "pina", "piná", "fasz", "geci", "kurva", "pénisz", "kúrt", "szop", "buzi", "szar", "dug"]
porn = ["https://www.pornhub.com", "https://www.xnxx.com"]
botChannels = [525701161768976394, 523962877053239296]


bot = commands.Bot(command_prefix=default_prefix)

bot.remove_command('help')
	
@bot.event
async def on_ready():
	# await bot.change_presence(activity=discord.Activity(name='Test',type=3))
	print("Everything's all ready to go~")
	
@bot.event
async def on_message(message):
	for swear in swearing:
		if swear in message.content.lower():
			await message.delete()
			await message.channel.send("{} Ne káromkodj! :rage:".format(message.author.mention), delete_after=3)
			return

	for link in porn:
		if link in message.content.lower():
			await message.delete()
			await message.channel.send("{} Azért pornót nyilvános chat-en ne ossz meg! :rage:".format(message.author.mention), delete_after=3)
			return

	if message.channel.id in botChannels: 
		await bot.process_commands(message)
		await asyncio.sleep(30)
		try:
			await message.delete()
		except:
			pass
	else:
		if message.content.startswith(".") or message.content.startswith("!"):
			await message.delete()
			await message.channel.send("Ebben a szobában nem használhatsz bot parancsokat, ezért az üzenetedet töröltem!", delete_after=3)

@bot.command()
@commands.guild_only()
async def help(ctx):
	await ctx.send("""```
Az alábbi parancsokkal tudod használni a botot:

.web - Kiírja a weboldalunk linkjét
.szabalyok - Meg tudod nézni a szabályokat
.steam - Kiírja a steam csoportunk linkjét
.ytchannel - Kiírja a csoportunk Youtube csatornáját
.ingyenjatek - Kiírja a Humble Bundle oldal linkjét
.css - Bizonyos CSS szerverek IP címét írja ki, melyeken néha aktívak vagyunk
```""")

@bot.command()
@commands.guild_only()
async def web(ctx):
	await ctx.send("**A Reversed weboldala:**\nhttps://reversed.webnode.hu/")

@bot.command()
@commands.guild_only()
async def szabalyok(ctx):
	await ctx.send("""**Szabályok:**

1. Spammelni, floodolni tilos
2. Káromkodni tilos
3. Szerver tagjait sértegetni tilos
4. Erősen kivételezni, és discriminálni tilos
5. Reklámozni tilos
6. Beleordítani és retardáltkodni a mikrofonba tilos
7. Gyorsan váltogatni a szobák közt tilos
8. Ha AFKolsz, akkor a szobában maradni tilos
9. Zaklatni és @ everyone -t és @ here-t használni tilos
10. Chaten csevegni csak a #chat szobában lehet, ha máshová írsz 1 órás+ muteot kapsz, ugyan ez érvényes a #bot  szobára, és feltétlenül olvassátok el a #notifications szobát is.

Reversed 2020""")

@bot.command()
@commands.guild_only()
async def steam(ctx):
	await ctx.send("**Reversed Steam csoportja:**\nhttp://steamcommunity.com/groups/reversedhungary")


@bot.command()
@commands.guild_only()
async def ytchannel(ctx):
	await ctx.send("**A Reversed Youtube csatornája:**\nhttps://www.youtube.com/channel/UC4uC5dWIXaOLqeLAkKSi2jg")

@bot.command()
@commands.guild_only()
async def ingyenjatek(ctx):
	await ctx.send("**Itt találhatsz ingyen játék kulcsokat:**\nhttps://www.humblebundle.com/best-of-2016-bundle")

@bot.command()
@commands.guild_only()
async def css(ctx):
	await ctx.send("""**Counter-Strike:Source szerver ip-k, amelyeken megtalálhatsz minket:**

**ANIMALS™ PUB/DM** - 87.229.77.227:27815
**ANIMALS™ FUN** - 87.229.77.227:27215
**ANIMALS™ ZOMBIE** - 87.229.77.227:27415
**MAFFIA!** - 87.229.77.40:27777
**[OldSchool]** - 37.17.172.36:27100
**|HOLLYWOOD|** - 87.229.77.40:27046
**]HeLL[ DM** - 178.32.53.216:27031""")


bot.run(TOKEN)