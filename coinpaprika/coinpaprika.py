from common.request import Request
from typing import Dict

class CoinpaprikaAPI(Request):
    def __init__(self, debug: bool = False,
                 headers: Dict[str, str] = None, proxy: Dict[str, str] = None,
                 *args, **kwargs):
        """Initialize a CoinpaprikaAPI instance.

        Args:
            debug: Output HTTP requests to stdout.
            headers: HTTP headers to with the HTTP request.
            proxy: Send HTTP requests through the supplied proxy.
        """
        super(CoinpaprikaAPI, self).__init__(debug, headers, proxy,
                                             *args, **kwargs)


#  vim: set ts=4 sw=4 tw=79 ft=python et :
