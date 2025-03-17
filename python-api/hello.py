from fastapi import FastAPI
from api_routes import router



listen_port = 8000
app = FastAPI()

app.include_router(router)

if __name__ == '__main__':
    import uvicorn
    print(f"Example app listen on port {listen_port}")
    uvicorn.run(app,host = "0.0.0.0",port = listen_port)