from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api_routes import router
from db.db_instance import db_instance
import asyncio


listen_port = 8000
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174"],  # Allows all origins (*)
    allow_credentials=True,
    allow_methods=["GET","POST","PUT","DELETE"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.on_event("startup")
async def startup_db():
    await db_instance.connect()

@app.on_event("shutdown")
async def shutdown_db():
    await db_instance.disconnect()


app.include_router(router)

if __name__ == '__main__':
    import uvicorn
    print(f"Example app listen on port {listen_port}")
    uvicorn.run(app,host = "0.0.0.0",port = listen_port)