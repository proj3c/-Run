from kyt import *

#CRATE VMESS
@bot.on(events.CallbackQuery(data=b'create-vmess'))
async def create_vmess(event):
	async def create_vmess_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**Username:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**Quota:**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond("**Choose Expiry Day**",buttons=[
[Button.inline(" 3 Day ","3"),
Button.inline(" 7 Day ","7")],
[Button.inline(" 30 Day ","30"),
Button.inline(" 60 Day ","60")]])
			exp = exp.wait_event(events.CallbackQuery)
			exp = (await exp).data.decode("ascii")
		async with bot.conversation(chat) as limitiptele:
			await event.respond("**Choose Limit IP**",buttons=[
[Button.inline(" 1 IP ","1"),
Button.inline(" 2 IP ","2")],
[Button.inline(" 3 IP ","3"),
Button.inline(" 5 IP ","5")]])
			limitiptele = limitiptele.wait_event(events.CallbackQuery)
			limitiptele = (await limitiptele).data.decode("ascii")
		await event.edit("Processing.")
		await event.edit("Processing..")
		await event.edit("Processing...")
		await event.edit("Processing....")
		time.sleep(3)
		await event.edit("`Processing Crate Premium Account`")
		time.sleep(1)
		await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(2)
		await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(3)
		await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(2)
		await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 100%\n█████████████████████████ `")
		time.sleep(1)
		await event.edit("`Wait.. Setting up an Account`")
		cmd = f'printf "%s\n" "{user}" "{exp}" "{pw}" "{limitiptele}" | addws'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Already Exist**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			b = [x.group() for x in re.finditer("vmess://(.*)",a)]
#			c = [x.group() for x in re.finditer("Host XrayDNS(.*)",a)]
#			d = [x.group() for x in re.finditer("Pub Key(.*)",a)]
			print(b)
#			print(d)
#			print(c)
#			xx = re.search("Pub Key      :(.*)",d[0]).group(1)
#			xxx = re.search("Host XrayDNS :(.*)",d[0]).group(1)
			z = base64.b64decode(b[0].replace("vmess://","")).decode("ascii")
			z = json.loads(z)
			z1 = base64.b64decode(b[1].replace("vmess://","")).decode("ascii")
			z1 = json.loads(z1)
			msg = f"""
**━━━━━━━━━━━━━━━━━**
**⚡ Xray/Vmess Account ⚡**
**━━━━━━━━━━━━━━━━━**
**» Remarks      :** `{z["ps"]}`
**» Domain       :** `{z["add"]}`
**» XRAY DNS     :** `{HOST}`
**» User Quota   :** `{pw} GB`
**» User Quota   :** `{limitiptele} IP`
**» Port DNS     :** `443, 53`
**» port TLS     :** `222-1000`
**» Port NTLS    :** `80, 8080, 8081-9999`
**» Port GRPC    :** `443`
**» User ID      :** `{z["id"]}`
**» AlterId      :** `0`
**» Security     :** `auto`
**» NetWork      :** `(WS) or (gRPC)`
**» Path TLS     :** `(/multi path)/vmess`
**» Path NLS     :** `(/multi path)/vmess`
**» Path Dynamic :** `http://BUG.COM`
**» ServiceName  :** `vmess-grpc`
**» Pub Key      :** `{PUB}`
**━━━━━━━━━━━━━━━━━**
**» Link TLS     :** 
`{b[0].strip("'").replace(" ","")}`
**━━━━━━━━━━━━━━━━━**
**» Link NTLS    :** 
`{b[1].strip("'").replace(" ","")}`
**━━━━━━━━━━━━━━━━━**
**» Link GRPC    :** 
`{b[2].strip("'")}`
**━━━━━━━━━━━━━━━━━**
**» Format OpenClash :** https://{DOMAIN}:81/vmess-{user}.txt
**━━━━━━━━━━━━━━━━━**
**» Expired Until:** `{later}`
**» 🤖@sdctunneling_bot**
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

# TRIAL VMESS MASIH BELUM BERES
@bot.on(events.CallbackQuery(data=b'trial-vmess'))
async def trial_vmess(event):
	async def trial_vmess_(event):
		async with bot.conversation(chat) as exp:
			await event.respond("**Choose Expiry Minutes**",buttons=[
[Button.inline(" 10 Menit ","10"),
Button.inline(" 15 Menit ","15")],
[Button.inline(" 30 Menit ","30"),
Button.inline(" 60 Menit ","60")]])
			exp = exp.wait_event(events.CallbackQuery)
			exp = (await exp).data.decode("ascii")
		await event.edit("Processing.")
		await event.edit("Processing..")
		await event.edit("Processing...")
		await event.edit("Processing....")
		time.sleep(3)
		await event.edit("`Processing Crate Premium Account`")
		time.sleep(1)
		await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(2)
		await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(3)
		await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(2)
		await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 100%\n█████████████████████████ `")
		time.sleep(1)
		await event.edit("`Wait.. Setting up an Account`")
		cmd = f'printf "%s\n" "{exp}" | trialws'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Already Exist**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			b = [x.group() for x in re.finditer("vmess://(.*)",a)]
			print(b)
			z = base64.b64decode(b[0].replace("vmess://","")).decode("ascii")
			z = json.loads(z)
			z1 = base64.b64decode(b[1].replace("vmess://","")).decode("ascii")
			z1 = json.loads(z1)
			msg = f"""
**━━━━━━━━━━━━━━━━━**
**⚡ Xray/Vmess Account ⚡**
**━━━━━━━━━━━━━━━━━**
**» Remarks      :** `{z["ps"]}`
**» Domain       :** `{z["add"]}`
**» XRAY DNS     :** `{HOST}`
**» User Quota   :** `Unlimited`
**» Port DNS     :** `443, 53`
**» port TLS     :** `222-1000`
**» Port NTLS    :** `80, 8080, 8081-9999`
**» Port GRPC    :** `443`
**» User ID      :** `{z["id"]}`
**» AlterId      :** `0`
**» Security     :** `auto`
**» NetWork      :** `(WS) or (gRPC)`
**» Path TLS     :** `(/multi path)/vmess`
**» Path NLS     :** `(/multi path)/vmess`
**» Path Dynamic :** `http://BUG.COM`
**» ServiceName  :** `vmess-grpc`
**» Pub Key      :** `{PUB}`
**━━━━━━━━━━━━━━━━━**
**» Link TLS     :** 
`{b[0].strip("'").replace(" ","")}`
**━━━━━━━━━━━━━━━━━**
**» Link NTLS    :** 
`{b[1].strip("'").replace(" ","")}`
**━━━━━━━━━━━━━━━━━**
**» Link GRPC    :** 
`{b[2].strip("'")}`
**━━━━━━━━━━━━━━━━━**
**» Format OpenClash :** https://{DOMAIN}:81/vmess-{z["ps"]}.txt
**━━━━━━━━━━━━━━━━━**
**» Expired Until:** `{exp} Minutes`
**» 🤖@sdctunneling_bot**
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await trial_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

#CEK VMESS
@bot.on(events.CallbackQuery(data=b'cek-vmess'))
async def cek_vmess(event):
	async def cek_vmess_(event):
		cmd = 'bot-cek-ws'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.respond(f"""

{z}

**Shows Logged In Users Vmess**
**» 🤖@sdctunneling_bot**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await cek_vmess_(event)
	else:
		await event.answer("Access Denied",alert=True)

@bot.on(events.CallbackQuery(data=b'delete-vmess'))
async def delete_vmess(event):
	async def delete_vmess_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**Username:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		cmd = f'printf "%s\n" "{user}" | delws'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Not Found**")
		else:
			msg = f"""**Successfully Deleted**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await delete_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'vmess'))
async def vmess(event):
	async def vmess_(event):
		inline = [
[Button.inline(" TRIAL VMESS ","trial-vmess"),
Button.inline(" CREATE VMESS ","create-vmess")],
[Button.inline(" CHECK VMESS ","cek-vmess"),
Button.inline(" DELETE VMESS ","delete-vmess")],
[Button.inline(" RESTORE VMESS ","restore-vmess"),
Button.inline("‹ Main Menu ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		domain1 = f" cat /etc/xray/domain"
		domaintele = subprocess.check_output(domain1, shell=True).decode("ascii")
		msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━ 
**⚡ VMESS MANAGER ⚡**
━━━━━━━━━━━━━━━━━━━━━━━ 
✅ **» Service     :** `VMESS`
✅ **» Hostname/IP :** `{domaintele.strip()}`
✅ **» ISP         :** `{z["isp"]}`
✅ **» Country     :** `{z["country"]}`
🤖 **» @sdctunneling_bot**
━━━━━━━━━━━━━━━━━━━━━━━ 
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await vmess_(event)
	else:
		await event.answer("Access Denied",alert=True)

#Restore VMESS
@bot.on(events.CallbackQuery(data=b'restore-vmess'))
async def restore_vmess(event):
	async def restore_vmess_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**Username:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as uuid:
			await event.respond('**UUID:**')
			uuid = uuid.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			uuid = (await uuid).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**Quota:**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond("**Choose Expiry Day**",buttons=[
[Button.inline(" 3 Day ","3"),
Button.inline(" 7 Day ","7")],
[Button.inline(" 30 Day ","30"),
Button.inline(" 60 Day ","60")]])
			exp = exp.wait_event(events.CallbackQuery)
			exp = (await exp).data.decode("ascii")
		async with bot.conversation(chat) as limitiptele:
			await event.respond("**Choose Limit IP**",buttons=[
[Button.inline(" 1 IP ","1"),
Button.inline(" 2 IP ","2")],
[Button.inline(" 3 IP ","3"),
Button.inline(" 5 IP ","5")]])
			limitiptele = limitiptele.wait_event(events.CallbackQuery)
			limitiptele = (await limitiptele).data.decode("ascii")
		await event.edit("Processing.")
		await event.edit("Processing..")
		await event.edit("Processing...")
		await event.edit("Processing....")
		time.sleep(3)
		await event.edit("`Processing Crate Premium Account`")
		time.sleep(1)
		await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(2)
		await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(3)
		await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(2)
		await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 100%\n█████████████████████████ `")
		time.sleep(1)
		await event.edit("`Wait.. Setting up an Account`")
		cmd = f'printf "%s\n" "{user}" "{uuid}" "{exp}" "{pw}" "{limitiptele}" | restorevmess'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Already Exist**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			b = [x.group() for x in re.finditer("vmess://(.*)",a)]
#			c = [x.group() for x in re.finditer("Host XrayDNS(.*)",a)]
#			d = [x.group() for x in re.finditer("Pub Key(.*)",a)]
			print(b)
#			print(d)
#			print(c)
#			xx = re.search("Pub Key      :(.*)",d[0]).group(1)
#			xxx = re.search("Host XrayDNS :(.*)",d[0]).group(1)
			z = base64.b64decode(b[0].replace("vmess://","")).decode("ascii")
			z = json.loads(z)
			z1 = base64.b64decode(b[1].replace("vmess://","")).decode("ascii")
			z1 = json.loads(z1)
			msg = f"""
**━━━━━━━━━━━━━━━━━━━━━**
**⚡ Succes Restore Account Vmess ⚡**
**━━━━━━━━━━━━━━━━━━━━━**
**» Remarks      :** `{z["ps"]}`
**» Domain       :** `{z["add"]}`
**» User Quota   :** `{pw} GB`
**» Limit IP     :** `{limitiptele} IP`
**━━━━━━━━━━━━━━━━━**
**» Format OpenClash :** https://{DOMAIN}:81/vmess-{user}.txt
**━━━━━━━━━━━━━━━━━**
**» Expired Until:** `{later}`
**» 🤖@sdctunneling_bot**
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await restore_vmess_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
