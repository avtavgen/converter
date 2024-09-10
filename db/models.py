from pydantic import BaseModel


class ResponseModel(BaseModel):
    convert_from: str
    convert_to: str
    amount: float
    converted_amount: float
