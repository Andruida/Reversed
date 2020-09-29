import discord
import asyncio
from discord.ext import commands
import logging
import datetime as dt
from dateutil.parser import parse
import sched, time

s = sched.scheduler(time.time, asyncio.sleep)

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

poll = {
	"started": False,
	"deadline": 0,
	"games": []
}

gamesDict = {
	"csgo": ":orange_circle: - Counter-Strike: Global Offensive",
	"ets" : ":purple_circle: - Euro Truck Simulator 2",
	"gta" :  ":green_circle: - Grand Theft Auto V",
	"r6"  :   ":blue_circle: - Rainbow Six: Siege",
	"hg"  :  ":brown_circle: - Heroes & Generals",
	"rl"  :  ":white_circle: - Rocket League",
	"rust":    ":red_circle: - Rust",
}

emojiNameDict = {
	"🟠": "csgo",
	"🟣": "ets",
	"🟢": "gta",
	"🔵": "r6",
	"🟤": "hg",
	"⚪": "rl",
	"🔴": "rust"
}

emojiDict = {
	"csgo": "🟠",
	"ets" : "🟣",
	"gta" : "🟢",
	"r6"  : "🔵",
	"hg"  : "🟤",
	"rl"  : "⚪",
	"rust": "🔴"
}

orderDict = {
	"csgo": 1,
	"ets" : 2,
	"gta" : 3,
	"r6"  : 4,
	"hg"  : 5,
	"rl"  : 6,
	"rust": 7
}

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
	elif message.channel.id == 716978612137623622:
		await bot.process_commands(message)
	else:
		if message.author.bot:
			await asyncio.sleep(5)
			try:
				await message.delete()
			except:
				pass
		if (message.content.startswith(".") or message.content.startswith("!")) and not message.content.startswith(".au"):
			try:
				await message.delete()
			except:
				pass
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
4. Erősen kivételezni, és diszkriminálni tilos
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


async def checkSchedule():
	# print(bot.is_closed())
	await bot.wait_until_ready()
	# print(bot.is_closed())
	while not bot.is_closed():
		try:
			s.run(False)
		except:
			traceback.print_exc()
		#print(scheduler.queue)
		await asyncio.sleep(5) #runs every 5 seconds

bot.loop.create_task(checkSchedule())

def genPoll():
	poll["games"].sort(key=lambda x: orderDict[x])
	description = "__**Lehetséges játékok**__\n"
	for game in poll["games"]:
		description += gamesDict.get(game) + "\n"

	embed = discord.Embed(	title="Szavazás", 
								description=description,
								color=0xFFFFFF)
	embed.add_field(name="Szavazás vége", value=dt.datetime.fromtimestamp(poll["deadline"]).strftime("%Y-%m-%d %H:%M"))
	return embed

@bot.command(name="poll")
@commands.guild_only()
@commands.has_role("Poll")
async def poll_command(ctx, *games):
	await asyncio.sleep(1)
	try:
		await ctx.message.delete()
	except:
		pass
	try:
		date = games[0]
		time = games[1]
		games = games[2:]
	except:
		traceback.print_exc()
		date = False
		time = False
		games = False
	if not (date and time and games):
		embed = discord.Embed(	title="Hiányzó paraméterek", 
								description="Legalább egy kötelező paraméter hiányzik.",
								color=0xFFFFFF)
		embed.add_field(name="Helyesen", value="`.poll <dátum> <időpont> <játék1> [játék2] ...`")
		embed.add_field(name="A parancsod:", value="`"+ctx.message.content+"`")
		await ctx.send(embed = embed, delete_after=30)
		return

	if poll["started"]:
		embed = discord.Embed(	title="Már megy egy szavazás", 
								description="Egy futó szavazást megszakíthatsz a .endpoll paranccsal, vagy módosíthatod a megjelenő játékokat .addgame és .delgame parancsokkal.",
								color=0xFFFFFF)
		embed.add_field(name="A szavazás véget ér", value=dt.datetime.fromtimestamp(poll["deadline"]).strftime("%Y-%m-%d %H:%M"))
		embed.add_field(name="A parancsod:", value="`"+ctx.message.content+"`")
		await ctx.send(embed = embed, delete_after=30)
		return
	try: 
		deadline = parse(date + " " + time)
	except:
		embed = discord.Embed(	title="Hibás dátum formátum", 
								description="A bot nem tudta értelmezni a megadott időpontot.",
								color=0xFFFFFF)
		embed.add_field(name="A parancsod:", value="`"+ctx.message.content+"`")
		await ctx.send(embed = embed, delete_after=30)
		return
	poll["started"] = True
	poll["deadline"] = deadline.timestamp()
	for game in games:
		if gamesDict.get(game):
			poll["games"].append(game)

	embed = genPoll()
	message = await ctx.send(embed=embed)
	poll["message"] = message
	for game in poll["games"]: 
		try:
			await message.add_reaction(emojiDict[game])
		except:
			pass
	s.enterabs(deadline.timestamp(), 1, lambda: bot.loop.create_task(endpoll_executor()))

@bot.command()
@commands.guild_only()
@commands.has_role("Poll")
async def addgame(ctx, *games):
	await asyncio.sleep(1)
	try:
		await ctx.message.delete()
	except:
		pass
	if not ( games):
		embed = discord.Embed(	title="Hiányzó paraméterek", 
								description="Legalább egy kötelező paraméter hiányzik.",
								color=0xFFFFFF)
		embed.add_field(name="Helyesen", value="`.addgame <játék1> [játék2] ...`")
		embed.add_field(name="A parancsod:", value="`"+ctx.message.content+"`")
		await ctx.send(embed = embed, delete_after=30)
		return
	if not poll["started"]:
		embed = discord.Embed(	title="Még nem indítottál szavazást", 
								description="Nincs szavazás amit módosíthatnál",
								color=0xFFFFFF)
		embed.add_field(name="A parancsod:", value="`"+ctx.message.content+"`")
		await ctx.send(embed = embed, delete_after=30)
		return
	for game in games:
		if not game in poll["games"]:
			poll["games"].append(game) 

	try:
		await poll["message"].edit(embed=genPoll())
	except discord.NotFound:
		poll["games"] = []
		poll["started"] = False
		poll["deadline"] = 0
		del poll["message"]
	for game in poll["games"]: 
		try:
			await poll["message"].add_reaction(emojiDict[game])
		except:
			pass



@bot.command()
@commands.guild_only()
@commands.has_role("Poll")
async def delgame(ctx, *games):
	await asyncio.sleep(1)
	try:
		await ctx.message.delete()
	except:
		pass
	if not ( games):
		embed = discord.Embed(	title="Hiányzó paraméterek", 
								description="Legalább egy kötelező paraméter hiányzik.",
								color=0xFFFFFF)
		embed.add_field(name="Helyesen", value="`.delgame <játék1> [játék2] ...`")
		embed.add_field(name="A parancsod:", value="`"+ctx.message.content+"`")
		await ctx.send(embed = embed, delete_after=30)
	if not poll["started"]:
		embed = discord.Embed(	title="Még nem indítottál szavazást", 
								description="Nincs szavazás amit módosíthatnál",
								color=0xFFFFFF)
		embed.add_field(name="A parancsod:", value="`"+ctx.message.content+"`")
		await ctx.send(embed = embed, delete_after=30)
		return

	for game in games:
		if game in poll["games"]:
			poll["games"].remove(game) 
			await poll["message"].clear_reaction(emojiDict[game])

	try:
		await poll["message"].edit(embed=genPoll())
	except discord.NotFound:
		poll["games"] = []
		poll["started"] = False
		poll["deadline"] = 0
		del poll["message"]


	

async def endpoll_executor(cancel=False):
	if cancel:
		# print(s.queue)
		try:
			s.cancel(s.queue[0])
		except:
			pass

	results = {}
	message = await bot.get_channel(poll["message"].channel.id).fetch_message(poll["message"].id)
	for emoji in message.reactions:
		# print(emoji.emoji)
		if emojiNameDict.get(emoji.emoji):
			results[emojiNameDict.get(emoji.emoji)] = emoji.count

	# print(results)
	poll["games"].sort(key=lambda x: results[x])
	description = "__**Eredmények:**__\n"
	place = 0
	for game in poll["games"]:
		place += 1
		description += "{place}. - {game} ({votes} szavazat)\n".format(place=place, game=gamesDict[game], votes=results[game])

	embed = discord.Embed(	title="Szavazás eredmények:", 
								description=description,
								color=0xFFFFFF)

	await poll["message"].edit(embed=embed)
	poll["games"] = []
	poll["started"] = False
	poll["deadline"] = 0
	del poll["message"]


@bot.command()
@commands.guild_only()
@commands.has_role("Poll")
async def endpoll(ctx):
	await asyncio.sleep(1)
	try:
		await ctx.message.delete()
	except:
		pass
	if not poll["started"]:
		embed = discord.Embed(	title="Még nem indítottál szavazást", 
								description="Nincs szavazás amit módosíthatnál",
								color=0xFFFFFF)
		embed.add_field(name="A parancsod:", value="`"+ctx.message.content+"`")
		await ctx.send(embed = embed, delete_after=30)
		return
	await endpoll_executor(cancel=True)

bot.run(TOKEN)
