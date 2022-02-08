import logging
import asyncio
from telethon import TelegramClient, events, Button
from decouple import config
from telethon.tl.functions.users import GetFullUserRequest

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)

# start the bot
print("Starting...")
try:
    apihash = config("API_HASH")
    apiid = config("APP_ID", cast=int)
    bottoken = config("BOT_TOKEN")
    frm = config("FROM_CHANNEL", cast=int)
    tochnl = config("TO_CHANNEL", cast=int)
    tochnl2 = config("TO_CHANNEL2", cast=int)
    tochnl3 = config("TO_CHANNEL3", cast=int)
    tochnl4 = config("TO_CHANNEL4", cast=int)
    tochnl5 = config("TO_CHANNEL5", cast=int)
    lasi = TelegramClient('bot', apiid, apihash).start(bot_token=bottoken)
except:
    print("Environment vars are missing! Kindly recheck.")
    print("Bot is quiting...")
    exit()


@lasi.on(events.NewMessage(pattern="/start"))
async def _(event):
    ok = await lasi(GetFullUserRequest(event.sender_id))
    await event.reply(f"ආයුබෝවන්`{ok.user.first_name}`!\n\n මම ඔබේ පරිශීලක සැගවුම් BOT වේ.\n කරුණාකර  /help  ලෙස ඒවා භාවිතය පිලිබදව දැනුවත් වන්න . \n[🤘](https://telegra.ph/file/1eca514b5e6202b1d92b3.jpg)", 
    buttons = [[Button.url("🤝Main Group🛰️", url="t.me/danuma01"), Button.url("📝Bot News🛸", url="https://t.me/danumabots")],[Button.url("✈️Developer✈️", url="https://lasiya.ml"),Button.url("🤙 Contact Dev 🛶", url="https://t.me/Danuma_admin_bot")]],link_preview=True)


@lasi.on(events.NewMessage(pattern="/help"))
async def helpp(event):
    await event.reply("**Help**\n\n මෙය ඔබගේ ප්‍රධාන ගිණුමට අමතර ආරක්ෂාවක් ලබාදීමට සකසූ බොට් කෙනෙකි \nමෙමගින් ඔබගේ ගිණුම රිපෝට් වීමකින් තොරව ඕනෑම සමුහයකට හෝ චැනලයකට පණිවුඩ යැවිය හැක.\n ඔබ අදාල චැනලයකට හෝ සමුහයකට මෙම BOT හරහා එක් කල පණිවුඩයක් රිපෝට් වීමකට ලක්වුවහොත් රිපෝටර් වන්නේ \n  මෙම BOT වන අතර ඔබගේ ගිණුම තාවකාලික හෝ පුර්ණ සිමවිමක් වන්නේ නැත\n මෙය පුර්ණ ලෙස anonymous ක්‍රියාකාරීත්වයක් පෙන්නුම් කරයි.   ")

@lasi.on(events.NewMessage(incoming=True, chats=frm)) 
async def _(event): 
    if not event.is_private:
        try:
            await event.client.send_message(tochnl, event.message)
            await event.client.send_message(tochnl2, event.message)
            await event.client.send_message(tochnl3, event.message)
            await event.client.send_message(tochnl4, event.message)
            await event.client.send_message(tochnl5, event.message)

        except:
            print("TO_CHANNEL ID is wrong or I can't send messages there (make me admin).")


print("Bot has started.")
print("Visit @Danuma01")
lasi.run_until_disconnected()
