from fastapi import FastAPI, Depends
from routers.converter import router
from service.security_service import key_auth

app = FastAPI()


app.include_router(router)


@app.get("/", dependencies=[Depends(key_auth)])
def read_root():
    return {"message": "Server is running."}
