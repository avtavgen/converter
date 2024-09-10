from dotenv import load_dotenv
from fastapi import FastAPI
from routers.converter import router

load_dotenv('.env')

app = FastAPI()


app.include_router(router)


@app.get("/")
def read_root():
    return {"message": "Server is running."}
