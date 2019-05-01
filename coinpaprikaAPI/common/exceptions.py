"""Coinpaprika-py exception classes."""

class CoinpaprikaException(Exception):
    """Base class from which all other exception classes extend from."""
    def __init__(self, error_type: int, error_message: str):
        error_str = "{}: {}".format(error_type, error_message)

        super(CoinpaprikaException, self).__init__(error_str)
        self.error_type = error_type
        self.error_message = error_message


class APIException(CoinpaprikaException):
    """Indicate exception along responses from Coinpaprika's API."""


class ClientException(CoinpaprikaException):
    """Indicate exception that do not involve Coinpaprika's API."""

#  vim: set ts=4 sw=4 tw=79 ft=python et :
