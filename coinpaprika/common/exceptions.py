"""Coinpaprika-py exception classes."""

class CoinpaprikaException(Exception):
    """Base class from which all other exception classes extend from."""

class APIException(CoinpaprikaException):
    """Indicate exception along responses from Coinpaprika's API."""
    def __init__(self, error_type: int, error_message: str):
        """Initialize an instance of APIException.

            Args:
                error_type: HTTP status code.
                error_message: Error message returned from Coinpaprika's API.
            """
        error_str = "{}: {}".format(error_type, error_message)

        super(APIException, self).__init__(error_str)
        self.error_type = error_type
        self.error_message = error_message


class ClientException(CoinpaprikaException):
    """Indicate exception that do not involve Coinpaprika's API."""

#  vim: set ts=4 sw=4 tw=79 ft=python et :
