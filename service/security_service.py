import os

from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN

load_dotenv(".env")
API_KEY = os.getenv("API_KEY")


def key_sec(apikey_header=Depends(APIKeyHeader(name="X-API-Key", auto_error=False))):
    if not apikey_header or not API_KEY:
        return None
    return apikey_header == API_KEY


async def key_auth(api_key=Depends(key_sec)):
    if not api_key:
        raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Not authenticated")
