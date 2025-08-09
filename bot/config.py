import os


class Config:

    API_ID = int(os.environ.get("API_ID", "27705761"))
    API_HASH = os.environ.get("API_HASH", "822cb334ca4527a134aae97f9fe44fd6")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7626180904:AAHrynubTAgAw7mW7lSUJ76_Nz1AQIehQCU")
    SESSION_NAME = os.environ.get("SESSION_NAME", ":memory:")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002616161685"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://username:password@cluster0.pv6yd2f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    AUTH_USERS = [int(i) for i in os.environ.get("AUTH_USERS", "8110231942").split() if i.strip()]
    MAX_PROCESSES_PER_USER = int(os.environ.get("MAX_PROCESSES_PER_USER", 2))
    MAX_TRIM_DURATION = int(os.environ.get("MAX_TRIM_DURATION", 600))
    TRACK_CHANNEL = int(os.environ.get("TRACK_CHANNEL", 0)) if os.environ.get("TRACK_CHANNEL") else None
    SLOW_SPEED_DELAY = int(os.environ.get("SLOW_SPEED_DELAY", 5))
    HOST = os.environ.get("HOST", "")
    TIMEOUT = int(os.environ.get("TIMEOUT", 60 * 30))
    DEBUG = os.environ.get("DEBUG", "False").lower() in ("true", "1", "yes")
    WORKER_COUNT = int(os.environ.get("WORKER_COUNT", 20))
    IAM_HEADER = os.environ.get("IAM_HEADER", "")
    
    COLORS = [
        "white",
        "black",
        "red",
        "blue",
        "green",
        "yellow",
        "orange",
        "purple",
        "brown",
        "gold",
        "silver",
        "pink",
    ]
    FONT_SIZES_NAME = ["Small", "Medium", "Large"]
    FONT_SIZES = [30, 40, 50]
    POSITIONS = [
        "Top Left",
        "Top Center",
        "Top Right",
        "Center Left",
        "Centered",
        "Center Right",
        "Bottom Left",
        "Bottom Center",
        "Bottom Right",
    ]
