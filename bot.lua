local discordia = require('discordia')
local client = discordia.Client()
local timer = require("timer")

client:on('ready', function()
	-- client.user is the path for your bot
	print('Logged in as '.. client.user.username)
	
end)

prefix = "."

commands = {"help", "web","szabalyok", "steam", "ytchannel", "css", "ingyenjatek", "joinduo" --[["facebook"]]}
texts = {
	{content = "Az alábbi parancsokkal tudod használni a botot:\n\n.web - Kiírja a weboldalunk linkjét\n.szabalyok - Meg tudod nézni a szabályokat\n.steam - Kiírja a steam csoportunk linkjét\n.ytchannel - Kiírja a csoportunk Youtube csatornáját\n.ingyenjatek - Kiírja a Humble Bundle oldal linkjét\n.css - Bizonyos CSS szerverek IP címét írja ki, melyeken néha aktívak vagyunk", code = true}, 
	"**A Reversed weboldala:**\nhttps://reversed.webnode.hu/",
	"**Szabályok:**\n\n1. Spammelni, floodolni tilos\n2. Káromkodni tilos\n3. Szerver tagjait sértegetni tilos\n4. Erősen kivételezni, és discriminálni tilos\n5. Reklámozni tilos\n6. Beleordítani és retardáltkodni a mikrofonba tilos\n7. Gyorsan váltogatni a szobák közt tilos\n8. Ha AFKolsz, akkor a szobában maradni tilos\n9. Zaklatni és @ everyone -t és @ here-t használni tilos\n10. Chaten csevegni csak a #chat szobában lehet, ha máshová írsz 1 órás+ muteot kapsz, ugyan ez érvényes a #bot  szobára, és feltétlenül olvassátok el a #notifications szobát is.\n\nReversed 2017",
	"**Reversed Steam csoportja:**\nhttp://steamcommunity.com/groups/reversedhungary",
	"**A Reversed Youtube csatornája:**\nhttps://www.youtube.com/channel/UC4uC5dWIXaOLqeLAkKSi2jg",
	"**Counter-Strike:Source szerver ip-k, amelyeken megtalálhatsz minket:**\n\n**ANIMALS™ PUB/DM** - 87.229.77.227:27815\n**ANIMALS™ FUN** - 87.229.77.227:27215\n**ANIMALS™ ZOMBIE** - 87.229.77.227:27415\n**MAFFIA!** - 87.229.77.40:27777\n**[OldSchool]** - 37.17.172.36:27100\n**|HOLLYWOOD|** - 87.229.77.40:27046\n**]HeLL[ DM** - 178.32.53.216:27031",
	"**Itt találhatsz ingyen játék kulcsokat:**\nhttps://www.humblebundle.com/best-of-2016-bundle",
	false,
	--"**Facebook csoportunk:**\nhttps://www.facebook.com/groups/261147987690497/?ref=bookmarks"
}

functions = {}

szobak = {
	duo = {}
}

functions[8] = function(message) 
end

--messagesWaiting = {}

moderate = { "basz", "bassz", "bazd", "picsa", "picsá", "pina", "piná", "fasz", "geci", "kurva", "pénisz", "kúrt", "szop", "buzi", "szar", "dug"}

moderateLinks = {"https://www.pornhub.com", "https://www.xnxx.com/"}

client:on('messageCreate', function(message)
	--tableTree(message)
	--table.insert(messagesWaiting, message)
	print("["..message.channel.name.." : "..message.author.username.."] : "..message.content)
	if message.content == prefix.."channelID" then
			message.channel:send("A channelID: \n"..tostring(message.channel.id))
			--message:reply("**Bot karbantartás folyamatban... (Windows 10 update)**\nÚjra működni fog reggel 8 órától")
		end
	if message.channel.id == "523962877053239296" or message.channel.id == "525701161768976394" then
		timer.setTimeout(30000, function(message)
			coroutine.resume(coroutine.create(function()
				message:delete()
				--print("deleted: "..message.content)
			end))
		end, message)
	
		--[[if message.content == prefix..'help' then
			message.channel:send{content = "Az alábbi parancsokkal tudod használni a botot:\n\n.web - Kiírja a weboldalunk linkjét\n.szabalyok - Meg tudod nézni a szabályokat\n.steam - Kiírja a steam csoportunk linkjét\n.ytchannel - Kiírja a csoportunk Youtube csatornáját\n.facebook - Kiírja a Facebook csoportunk oldalát\n.ingyenjatek - Kiírja a Humble Bundle oldal linkjét\n.css - Bizonyos CSS szerverek IP címét írja ki, melyeken néha aktívak vagyunk", code = true}
		end]]
		local bool, id = isCommand(message.content)
		if bool and texts[id] then 
			message:reply(texts[id])
		elseif functions[id] then
			functions[id](message)
		end
	elseif message.channel.id == "523962965179760674" then
		timer.setTimeout( 2* 60 * 60 * 1000, function(message)
			coroutine.resume(coroutine.create(function()
				message:delete()
				--print("deleted: "..message.content)
			end))
		end, message)
	elseif isCommand(message.content) then
		timer.setTimeout(1000, function(message)
			coroutine.resume(coroutine.create(function()
				message:delete()
				message:reply({content = "Ebben a channel-ben nem használhatsz bot parancsokat, ezért az üzenetedet töröltem! ", mention = message.author})
				--print("deleted: "..message.content)
			end))
		end, message)
	elseif message.author.id == client.user.id then
		timer.setTimeout(5000, function(message)
			coroutine.resume(coroutine.create(function()
				message:delete()
				--print("deleted: "..message.content)
			end))
		end, message)
	end
	local karomkodas = false
	for k,v in pairs(moderate) do
		if message.content:lower():find(v) then
			karomkodas = true
		end
	end
	if karomkodas == true then
		timer.setTimeout(1000, function(message)
			coroutine.resume(coroutine.create(function()
				message:delete()
				message:reply({content = "Ne káromkodj! :rage: ", mention = message.author})
				--print("deleted: "..message.content)
			end))
		end, message)
	end
	for k,v in pairs(moderateLinks) do
		if message.content:lower():find(v) then
			timer.setTimeout(1000, function(message)
				coroutine.resume(coroutine.create(function()
					message:delete()
					message:reply({content = "Azért pornót nyilvános chat-en ne ossz meg! :rage: ", mention = message.author})
					--print("deleted: "..message.content)
				end))
			end, message)
		end
	end
end)

function isCommand(str)
	for k, v in pairs(commands) do
		if prefix..v == str then
			return true, k
		end
	end
	return false
end

function tableTree(result)
	for k, v in pairs(result) do
		print(k.." = "..tostring(v))
		if tostring(v):find("table:") then
			for kk, vv in pairs(v) do
				print("     "..kk.." = "..tostring(vv))
				if tostring(vv):find("table:") then
					for kkk, vvv in pairs(vv) do
						print("          "..kkk.." = "..tostring(vvv))
						if tostring(vvv):find("table:") then
							for kkkk, vvvv in pairs(vvv) do
								print("               "..kkkk.." = "..tostring(vvvv))
							end
						end
					end
				end
			end
		end
	end
end

io.input("key.txt")
client:run('Bot '..io.read())
io.close()
