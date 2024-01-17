import os
from urllib.parse import quote_plus

import motor.motor_asyncio
from dotenv import load_dotenv

load_dotenv()

MONGO_DRIVER = os.getenv("MONGO_DRIVER")
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = os.getenv("MONGO_PORT")
MONGO_USER = os.getenv("MONGO_USER")
password = os.getenv("MONGO_PASS")
MONGO_PASS = quote_plus(password)
MONGO_DB = os.getenv("MONGO_DB")

MONGO_URI = f"{MONGO_DRIVER}://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}/"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)

db = client[MONGO_DB]

sprites_collection = db.body

async def connect():
    return db.command("ping")

async def disconnect():
        await client.close()