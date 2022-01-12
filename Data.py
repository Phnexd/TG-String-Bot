from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

Note 
1) Don't Block The Bot
2) Another Bites You Will Not Get Your String

You can use me to generate pyrogram and telethon string session. Use the below buttons to know more!
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Return Home", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton("✨ Maintaned By ✨", url="https://t.me/xGamer_s")],
        [
            InlineKeyboardButton("How To Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ WarZ Support ♥", url="https://t.me/WarZSupport")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - To Get About This Bot 🤖
/help - Check The Bot Commands 🔧
/start - Start The Bot
/generate - Generate Your String Now 😊
/cancel - Process Cancell 🥺
/restart - Restart And Start Generate String Session 😊
"""

    # About Message
    ABOUT = """
**About This Bot** 

A Telegram Bot To Generate Pyrogram And Telethon String Session...

Team WarZ : [Team WarZ](https://t.me/TeamWarZ)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @xGamer_s
    """
