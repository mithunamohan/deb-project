from fastapi import APIRouter
import random

greetings_list = [
    'Hello,World',
    'Bonjour,Monde!',
    'Hallo,Welt!'
]



router = APIRouter()

@router.get("/")
async def hello_world():
    return {"message":"Hello,World!"}
@router.get("/greetings")
async def get_greetings():
    return greetings_list
@router.get("/visitors")
async def get_visitors():
    visitor_count = random.randint(0,1000)
    return {"Visitor Count : ":visitor_count}

