# db/db_instance.py
from motor.motor_asyncio import AsyncIOMotorClient

class Database:
    def __init__(self):
        self.client = None
        self.db = None

    async def connect(self):
        try:
            self.client = AsyncIOMotorClient("mongodb://mongodb/deb")  # Same DB URL as in JS
            self.db = self.client["deb"]
            print("✅ Connected to database :)")
        except Exception as e:
            print("❌ Couldn't connect to database :(", str(e))

    async def disconnect(self):
        if self.client:
            self.client.close()
            print("🔌 Disconnected from database.")

# Create a single DB instance
db_instance = Database()
