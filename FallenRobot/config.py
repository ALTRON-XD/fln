class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 18776023
    API_HASH = "f453f409460b31898c28852faba1f5dd"

    CASH_API_KEY = "TVU5ZK9WTUIKJIKQ"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://xwufopfc:sfaUkM1By6c9t0UzbgcvGT9ugvTahysB@manny.db.elephantsql.com/xwufopfc"  # A sql database url from elephantsql.com

    EVENT_LOGS = ("-1001811125658")  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://alone:alone@cluster0.j4hrlec.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "a"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5886222029:AAFTpr178HDO9oL6LabGJZm_rvDcVuM81ao"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "x"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 1820525265  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
