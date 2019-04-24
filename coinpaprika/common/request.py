"""HTTP request handling interface."""
import logging
from typing import Dict

import requests

from .ratelimit import rate_limited
from .const import API_BASE_ENDPOINT

class Request(requests.Session):
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
    def request(self, method, path, *args, **kwargs) -> requests.models.Response:
        """Send a HTTP request."""
        url: str = API_BASE_ENDPOINT + path
        return super(Request, self).request(method, url, *args, **kwargs)

#  vim: set ts=4 sw=4 tw=79 ft=python et :
