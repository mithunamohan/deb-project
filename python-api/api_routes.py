from fastapi import APIRouter
from db.db_instance import db_instance  # Import the DB instance
from db.greetings_model import Greetings
from db.visitors_model import Visitors


import random

# greetings_list = [
#     'Hello,World',
#     'Bonjour,Monde!',
#     'Hallo,Welt!'
# ]



router = APIRouter()

@router.get("/")
async def hello_world():
    return {"message":"Hello,World!"}

@router.get("/greetings")
async def get_greetings():
    greetings_cursor = db_instance.db["greetings"].find({})
    greetings = await greetings_cursor.to_list(length=100)
    
    # Extract only the greetings field
    greetings_list = [greeting["greetings"] for greeting in greetings]
    
    return greetings_list

@router.get("/visitors")
async def track_visitor():
    visitors_collection = db_instance.db["visitors"]

    visitor = await visitors_collection.find_one({"name": "latest"})  # Find document where name="latest"

    if visitor:
        # If document exists, increment visitor count
        new_count = visitor["visitorcount"] + 1
        await visitors_collection.update_one(
            {"_id": visitor["_id"]}, {"$set": {"visitorcount": new_count}}
        )
        print("Updated Visitor Count:", new_count)  # Debugging log

        return {"visitorcount": new_count}

    else:
        # If document does not exist, create a new one with visitorcount = 1
        new_visitor = {"name": "latest", "visitorcount": 1}
        await visitors_collection.insert_one(new_visitor)
        return {"visitorcount": 1}
