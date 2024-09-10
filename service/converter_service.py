from currency_converter import CurrencyConverter

from db.models import ResponseModel


class Converter:
    _converter = CurrencyConverter()

    def is_valid(self, currency: str) -> bool:
        return currency in self._converter.currencies

    def convert(self, convert_from: str, convert_to: str, amount: float) -> ResponseModel:
        converted_amount = self._converter.convert(amount, convert_from, convert_to)
        response_model = ResponseModel(convert_from=convert_from,
                                       convert_to=convert_to,
                                       amount=amount,
                                       converted_amount=converted_amount)
        return response_model


converter = Converter()
