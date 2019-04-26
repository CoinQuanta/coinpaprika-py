from typing import List, Dict, Union

from .common.request import Request
from .common.const import API_PATH


class CoinpaprikaAPI(Request):  # pylint: disable=R0904
    def __init__(self, debug: bool=False,
                 headers: Dict[str, str]=None, proxy: Dict[str, str]=None,
                 *args, **kwargs):
        """Initialize a CoinpaprikaAPI instance.

        Args:
            debug: Output HTTP requests to stdout.
            headers: HTTP headers to with the HTTP request.
            proxy: Send HTTP requests through the supplied proxy.
        """
        super(CoinpaprikaAPI, self).__init__(debug, headers, proxy,
                                             *args, **kwargs)

    def global_market(self) -> Dict[str, Union[str, int]]:
        """Get market overview."""
        return self.get(API_PATH["global"])

    def coins(self) -> List[Dict[str, Union[str, int, bool]]]:
        """List all available coins."""
        return self.get(API_PATH["coins_list"])

    def coin(self, coin_id: str) -> Dict[str, Union[str, int, bool, Dict]]:
        """Get coin data by ID."""

        return self.get(API_PATH["coin_get_by_id"].format(coin_id=coin_id))

    def twitter(self, coin_id: str) -> List[Dict[str, Union[str, int, bool]]]:
        """Get twitter timeline for coin."""
        return self.get(
                API_PATH["coin_get_twitter_timeline"].format(coin_id=coin_id))

    def events(self, coin_id: str) -> List[Dict[str, Union[str, bool]]]:
        """Get coin events by coin ID."""
        return self.get(
                API_PATH["coin_get_exchanges_by_id"].format(coin_id=coin_id))

    def coin_exchanges(self, coin_id: str) -> List[Dict[str, Union[str, int, List[Dict]]]]:
        """Get exchanges by coin ID."""
        return self.get(
                API_PATH["coin_get_exchanges_by_id"].format(coin_id=coin_id))

    def markets(self, coin_id: str) -> List[Dict[str, Union[str, bool, float, Dict[str, Dict[str, float]]]]]:
        """Get markets by coin ID."""
        return self.get(API_PATH["coin_get_markets_by_id"].format(coin_id=coin_id))

    def ohlc(self, coin_id, quote="usd") -> List[Dict[str, Union[str, int]]]:
        """Get OHLC for last full day."""
        return self.get(API_PATH["coin_get_ohlc_last_full_day_by_id"].format(
            coin_id=coin_id, quote=quote))

    def ohlcv(self, coin_id, *,
              start_date: str, end_date: str="",
              limit: int=1, quote: str="usd"):
        """Get historical OHLC."""
        return self.get(API_PATH["coin_get_ohlc_historical_by_date"].format(
            coin_id=coin_id,
            start_date=start_date,
            end_date=end_date,
            limit=limit,
            quote=quote))

    def ohlcv_today(self, coin_id, quote="usd"):
        """Get today OHLC."""
        return self.get(API_PATH["coin_get_ohlc_today_by_id"].format(
            coin_id=coin_id,
            quote=quote))


#  vim: set ts=4 sw=4 tw=79 ft=python et :
