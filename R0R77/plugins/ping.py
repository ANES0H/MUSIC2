import os

from telethon import Button, events

from R0R77 import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/e81be48de729aa5229744.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@N_B_1"
)

CAPTION = f"**سرعة البنك:** {ms}\n المالك:『{ALIVE}』"


@R0R77.on(events.NewMessage(pattern="/بنك"))
async def _(event):
    UMM = [[Button.url("قناه السورس", "https://t.me/S8Y8S")]]
    await R0R77.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
