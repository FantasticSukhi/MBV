from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True

    API_ID = int(getenv("API_ID", 6))
    API_HASH = getenv("API_HASH", None)
    ARQ_API_KEY = "PMPTTD-HOMLMF-SRBHNH-RZMWXL-ARQ"
    SPAMWATCH_API = None
    TOKEN = getenv("TOKEN", None)
    OWNER_ID = int(getenv("OWNER_ID", 7448520005))
    OWNER_USERNAME = getenv("OWNER_USERNAME", "GARUD_OWNER")
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "GARUD_NETWORK")
    LOGGER_ID = int(getenv("LOGGER_ID", "-1002124344872"))
    MONGO_URI = getenv(
        "MONGO_DB_URI",
        "mongodb+srv://Mamba:Mamba@cluster0.wnvgc6k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    )
    DB_NAME = getenv("DB_NAME", "ExonRobot")
    REDIS_URL = "redis://default:wK6ZCiclq4iQKYpgfY90v6kd6WdPfEwl@redis-10186.c263.us-east-1-2.ec2.cloud.redislabs.com:10186/default"
    DATABASE_URL = getenv("DATABASE_URL", None)

    # ɴᴏ ᴇᴅɪᴛ ᴢᴏɴᴇ
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
