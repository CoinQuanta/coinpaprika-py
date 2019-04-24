"""HTTP request handling interface."""
import logging
from collections import namedtuple
from typing import Dict

import requests

from .ratelimit import rate_limited
from .const import API_BASE_ENDPOINT

class Request(requests.Session):

    CoinpaprikaResponse = namedtuple("CoinpaprikaResponse", [
        "content", "status_code", "headers", "url", "history",
        "encoding", "reason", "cookies", "elapsed", "request", "json"
    ])

    def __init__(self, debug: bool = False,
                 headers: Dict[str, str] = None, proxy: Dict[str, str] = None,
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
        url: str = API_BASE_ENDPOINT + path
        req: requests.models.Response = super(Request, self).request(method,
                                                                     url,
                                                                     *args,
                                                                     **kwargs)

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
