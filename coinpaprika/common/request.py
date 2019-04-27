"""HTTP request handling interface."""
import logging
from collections import namedtuple
from typing import Dict

import requests

from .ratelimit import rate_limited
from .const import API_BASE_ENDPOINT
from .exceptions import APIException, ClientException

class Request(requests.Session):

    CoinpaprikaResponse = namedtuple("CoinpaprikaResponse", [
        "content", "status_code", "headers", "url", "history",
        "encoding", "reason", "cookies", "elapsed", "request", "json"
    ])

    def __init__(self, debug: bool=False,
                 headers: Dict[str, str]=None, proxy: Dict[str, str]=None,
                 *args, **kwargs):
        super(Request, self).__init__(*args, **kwargs)

        if debug:
            logging.basicConfig(level=logging.DEBUG)
        if headers is not None:
            self.headers.update(headers)
        if proxy is not None:
            self.session.proxies.update(proxy)

    @rate_limited(10)
    def request(self, method, path, *args, **kwargs) -> CoinpaprikaResponse:
        """Send a HTTP request."""
        url = API_BASE_ENDPOINT + path
        req = super(Request, self).request(method, url, *args, **kwargs)

        # Response status code is less than 400.
        if req.status_code != requests.codes.ok:
            status_code = req.status_code
            error_message = req.json()["error"]

            # If status code response is 4XX.
            if 400 <= req.status_code < 500:
                raise ClientException(status_code, error_message)
            # If status code response is 5XX.
            elif 500 <= req.status_code < 600:
                raise APIException(status_code, error_message)

        return Request.CoinpaprikaResponse(
            content = req.content,
            status_code = req.status_code,
            headers = req.headers,
            url = req.url,
            history = req.history,
            encoding = req.encoding,
            reason = req.reason,
            cookies = req.cookies,
            elapsed = req.elapsed,
            request = req.request,
            json = req.json()
        )

#  vim: set ts=4 sw=4 tw=79 ft=python et :
