import os

from telethon import Button, events

from R0R77 import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/2ad68bd0e391a69163d0a.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@N_B_1"
)

CAPTION = f"**سرعة البنك:** {ms}\n المالك:『{ALIVE}』"


@R0R77.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("السورس", "https://t.me/S8Y8S")]]
    await R0R77.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
