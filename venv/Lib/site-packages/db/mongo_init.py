from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

async def init_db():
    try:
        # Connect to MongoDB
        client = AsyncIOMotorClient("mongodb://localhost:27017/")  # Use "mongodb://mongodb:27017/" if using Docker
        db = client["deb"]  # Access the 'deb' database

        # Create 'greetings' collection and insert data
        greetings_collection = db["greetings"]
        greetings_data = [
            {"greetings": "Hello World!"},
            {"greetings": "Bonjour Monde!"},
            {"greetings": "Hallo Welt!"}
        ]

        # Check if collection already exists to avoid duplicates
        count = await greetings_collection.count_documents({})
        if count == 0:
            await greetings_collection.insert_many(greetings_data)
            print("✅ Greetings inserted into the database.")
        else:
            print("⚠️ Greetings collection already exists.")

        # Close the connection
        client.close()

    except Exception as e:
        print("❌ Error initializing the database:", str(e))

# Run the async function
if __name__ == "__main__":
    asyncio.run(init_db())
