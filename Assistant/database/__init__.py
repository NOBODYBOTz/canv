from sys import exit
from motor.motor_asyncio import AsyncIOMotorClient
from Assistant import LOGGER
from config import DB_URI

try:
    # Create an instance of AsyncIOMotorClient
    mongo = AsyncIOMotorClient(DB_URI)
    # Access the database
    db = mongo["Assistant"]
    LOGGER.info("Connected to your Mongo Database.")
except Exception as e:
    LOGGER.error(f"Failed to connect to your Mongo Database. {e}")
    exit(1)
