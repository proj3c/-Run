from kyt import *

@bot.on(events.NewMessage(pattern=r"(?:.menu|/menu)$"))
@bot.on(events.CallbackQuery(data=b'menu'))
async def menu(event):
	inline = [
[Button.inline(" SSH OVPN MANAGER ","ssh")],
[Button.inline(" VMESS MANAGER ","vmess"),
Button.inline(" VLESS MANAGER ","vless")],
[Button.inline(" TROJAN MANAGER ","trojan"),
Button.inline(" SHDWSK MANAGER ","shadowsocks")],
[Button.inline(" CHECK VPS INFO ","info"),
Button.inline(" OTHER SETTING ","setting")],
[Button.inline(" ‹ Back Menu › ","start")]]
	sender = await event.get_sender()
	val = valid(str(sender.id))
	if val == "false":
		try:
			await event.answer("Akses Ditolak", alert=True)
		except:
			await event.reply("Akses Ditolak")
	elif val == "true":
		import subprocess

		sh = f"awk -F: '$3 >= 1000 && $1 != \"nobody\" {{print $1}}' /etc/passwd | wc -l"
		ssh = subprocess.check_output(sh, shell=True, stderr=subprocess.STDOUT).decode("ascii")
		vm = f'grep -E "^### " "/etc/xray/config.json" | cut -d " " -f 2-3 | column -t | sort | uniq | wc -l'

		try:
			# Menjalankan perintah dan mendapatkan output
			output = subprocess.check_output(vm, shell=True, stderr=subprocess.STDOUT).decode("ascii")

		except subprocess.CalledProcessError as e:
			print("Error:", e.output.decode("utf-8"))
		vl = f' cat /etc/vless/.vless.db | grep "###" | wc -l'
		vls = subprocess.check_output(vl, shell=True).decode("ascii")
		tr = f' cat /etc/trojan/.trojan.db | grep "###" | wc -l'
		trj = subprocess.check_output(tr, shell=True).decode("ascii")
		sdss = f" cat /etc/os-release | grep -w PRETTY_NAME | head -n1 | sed 's/=//g' | sed 's/PRETTY_NAME//g'"
		namaos = subprocess.check_output(sdss, shell=True).decode("ascii")
		ipvps = f" curl -s ipv4.icanhazip.com"
		ipsaya = subprocess.check_output(ipvps, shell=True).decode("ascii")
		citsy = f" cat /etc/xray/city"
		city = subprocess.check_output(citsy, shell=True).decode("ascii")
		domain1 = f" cat /etc/xray/domain"
		domaintele = subprocess.check_output(domain1, shell=True).decode("ascii")

		msg = f"""
━━━━━━━━━━━━━━━━━━━━━ 
**✅ ADMIN PANEL MENU ✅**
━━━━━━━━━━━━━━━━━━━━━ 
**» OS     :** `{namaos.strip().replace('"','')}`
**» CITY   :** `{city.strip()}`
**» HOST   :** `{domaintele.strip()}`
**» IP VPS :** `{ipsaya.strip()}`
**» Total Account Created:** 

**» 🚀SSH OVPN    :** `{ssh.strip()}` __account__
**» 🎭XRAY VMESS  :** `{output.strip()}` __account__
**» 🗼XRAY VLESS  :** `{vls.strip()}` __account__
**» 🎯XRAY TROJAN :** `{trj.strip()}` __account__
━━━━━━━━━━━━━━━━━━━━━━━ 
"""
		x = await event.edit(msg,buttons=inline)
		if not x:
			await event.reply(msg,buttons=inline)


