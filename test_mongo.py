import motor.motor_asyncio
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

async def test_connection():
    uri = os.getenv('DATABASE_URL')
    print(f"Attempting to connect to MongoDB with URI: {uri}")
    try:
        client = motor.motor_asyncio.AsyncIOMotorClient(uri, serverSelectionTimeoutMS=5000)
        await client.server_info()
        print("MongoDB connection successful!")
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")

if __name__ == "__main__":
    asyncio.run(test_connection())