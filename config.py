#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler




TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6551603754:AAHx2ZtBfnx24X4tlXoxr7-02k0BreOns9g")
APP_ID = int(os.environ.get("APP_ID", "24314601"))
API_HASH = os.environ.get("API_HASH", "ede341e2d490a0fad5469866dedf8a95")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002171020418"))
OWNER_ID = int(os.environ.get("OWNER_ID", "640617767"))
PORT = os.environ.get("PORT", "8080")
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://13duddududdu:13duddududdu@cluster0.dvpxim9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "files")
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002215944038"))
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#SHORTLINK
SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "easysky.in")
SHORTLINK_API = os.environ.get('SHORTLINK_API', "a3f19acc6e58669565e8a3eb4cd5f7b040db4989")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001907363638"))


#start message
START_MSG = os.environ.get("START_MESSAGE", "🔆 First join My All Channel 🔆")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "640617767").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(640617767)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
