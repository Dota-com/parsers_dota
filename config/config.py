import os
import logging
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

DOTA_API = os.environ.get("DOTA_API")

MONGO_USER = os.environ.get("MONGO_USERNAME")
MONGO_PASS = os.environ.get("MONGO_PASSWORD")

DB_SQLITE_NAME = os.environ.get("DB_SQLITE_NAME")

DB_NAME = os.environ.get("DB_NAME")
DB_PORT = os.environ.get("DB_PORT")
DB_PASS = os.environ.get("DB_PASS")
DB_USER = os.environ.get("DB_USER")
DB_HOST = os.environ.get("DB_HOST")

CONNECT = f"mongodb://{MONGO_USER}:{MONGO_PASS}@mongo:27017/"

client = MongoClient(CONNECT)

logging.basicConfig(level=logging.DEBUG)
#
# from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
# from typing import AsyncGenerator
#
# engine = create_async_engine(f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
#
# async_session_maker = async_sessionmaker(engine, expire_on_commit=False)
#
#
# async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session:
#         yield session
