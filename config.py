import os
from typing import List

API_ID = os.environ.get("API_ID", "29841034")
API_HASH = os.environ.get("API_HASH", "fc533d811f28228e121bbe3901d8f565")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "6317211079"))
PICS = (os.environ.get("PICS", "https://telegra.ph/file/e97e5fbbfed495dec3132-f7930d53ef0027b5a8.jpg")).split()

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002421781174"))

DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "Cluster0")

IS_FSUB = os.environ.get("IS_FSUB", "True").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1002553442366").split())) # Add Multiple channel ids

EMOJIS = [
    "👍", "❤️", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "😢",
    "🎉", "🤩", "🙏", "👌", "🕊", "🤡", "🥱", "🥴", "😍", "🤷‍♂️",
    "❤️‍🔥", "🌚", "💯", "🤣", "⚡", "🏆", "🗿", "😐", "🤨", "🍾",
    "💋", "😈", "😴", "😭", "🤓", "👻", "👨‍💻", "👀", "🙈", "🤷‍♀️",
    "😇", "🤝", "✍️", "🤗", "🫡", "😨", "🧑‍🎄", "🎄", "⛄", "🤪",
    "🆒", "💘", "🙊", "🦄", "😘", "🙉", "💊", "😎", "👾", "🤷"
]
