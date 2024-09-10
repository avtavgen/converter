from fastapi import APIRouter
from pydantic import ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND

from db.models import ResponseModel
from service.converter_service import converter

router = APIRouter()


@router.get("/convert", response_model=ResponseModel)
def convert(request: Request, convert_from: str, convert_to: str, amount: float):
    try:
        response = converter.convert(convert_from=convert_from, convert_to=convert_to, amount=amount)
    except (ValueError, ValidationError) as e:
        return JSONResponse(status_code=HTTP_404_NOT_FOUND, content={"message": str(e)})
    return response

