print("amir bot runes")
from rubika.client import Bot
from rubika.tools import Tools
from rubika.encryption import encryption
import random
from random import choice

#شناسه اکانت
bot = Bot("AppName", auth= "hulrjsgdvfaahddrywwduiggnoyqsdzv")
#......
#شناسه گروه
target = "g0BkdiW06f93fc0f9ef5de10eab8f725"
#gqlocjpxxxkygxcqbmgvdokbkydtfadz
answered,retries = [],{}


while True:
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		min_id = bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]
		while True:
			try:
				messages = bot.getMessages(target,min_id)
				break
			except:
				continue

		for msg in messages:
			try:
				if msg["type"]=="Text" and not msg.get("message_id") in answered:
					if msg.get("text").startswith("سین زن روشن"):
							try:
								bot.sendMessage(target, "🤖در پیام بعدی لینک گروه مورد نظر را ثبت نمائید🤖\nمثال:\n\nجوین گپ\nhttps://rubika.ir/joinc/BEDJEHGJ0LXSIPACCXGCQCBIJBZESKWA")
							except:
								print("error ersal start1")


					elif msg.get("text").startswith("جوین گپ"):
							try:
								matnsingzf = open("banerlinkdoneSINZAN.txt","w",encoding='utf-8').write(str(msg.get("text").strip("جوین گروه")))
								matnsingz = open("banerlinkdoneSINZAN.txt").read().split("\n")
								bot.sendMessage(target,  "✅ با موفقیت لینک گروه مورد نظر ثبت شد")
								bot.sendMessage(target,  "\n🤖بنر خود را برای سین زنی در پیام بعدی ثبت نمائید🤖\n\nمثال رو پیامی که می خواهید سین زده شود ریپ بزنید و بگویید [سین بزن]\n")
							except:
								print("error sabt_link-sinzan")

					elif msg.get("text").startswith("سین بزن"):
						while True:
							matntabb = list(matnsingz)
							randomli = choice(matntabb)
							writelin = open("TARGET_SINZAN.txt","w",encoding='utf-8').write(str(randomli))
							tabgligh = open("TARGET_SINZAN.txt","r",encoding='utf-8').read()
							tabeligh = bot.joinGroup(tabgligh)
							tabrligh = tabeligh['data']['group']['group_guid']
							bot.forwardMessages(target,[msg.get("reply_to_message_id")],tabrligh)
							bot.leaveGroup(tabrligh)

			except:
				continue
			answered.append(msg.get("message_id"))
			

	except KeyboardInterrupt:
		exit()

	except Exception as e:
		if type(e) in list(retries.keys()):
			if retries[type(e)] < 3:
				retries[type(e)] += 1
				continue
			else:
				retries.pop(type(e))
		else:
			retries[type(e)] = 1
			continue
