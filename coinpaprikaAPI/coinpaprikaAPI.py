from typing import List, Dict, Union

from .common.request import Request
from .common.const import API_PATH


class Coinpaprika(Request):  # pylint: disable=R0904
    def __init__(self, debug: bool=False,
                 headers: Dict[str, str]=None, proxy: Dict[str, str]=None,
                 *args, **kwargs):
        """Initialize a Coinpaprika instance.

        Args:
            debug: Output HTTP requests to stdout.
            headers: HTTP headers to with the HTTP request.
            proxy: Send HTTP requests through the supplied proxy.
        """
        super(Coinpaprika, self).__init__(debug, headers, proxy,
                                             *args, **kwargs)

    def global_market(self) -> Dict[str, Union[str, int]]:
        """Get market overview."""
        return self.get(API_PATH["global"])

    def coins(self) -> List[Dict[str, Union[str, int, bool]]]:
        """List all available coins.

            Args:
                coin_id
        """
        return self.get(API_PATH["coins_list"])

    def coin(self, coin_id: str) -> Dict[str, Union[str, int, bool, Dict]]:
        """Get coin data by ID.

            Args:
                coin_id
        """

        return self.get(API_PATH["coin_get_by_id"].format(coin_id=coin_id))

    def twitter(self, coin_id: str) -> List[Dict[str, Union[str, int, bool]]]:
        """Get twitter timeline for coin.

            Args:
                coin_id
        """
        return self.get(
                API_PATH["coin_get_twitter_timeline"].format(coin_id=coin_id))

    def events(self, coin_id: str) -> List[Dict[str, Union[str, bool]]]:
        """Get coin events by coin ID.

            Args:
                coin_id
        """
        return self.get(
                API_PATH["coin_get_exchanges_by_id"].format(coin_id=coin_id))

    def coin_exchanges(self, coin_id: str) -> List[Dict[str, Union[str, int, List[Dict]]]]:
        """Get exchanges by coin ID.

            Args:
                coin_id
        """
        return self.get(
                API_PATH["coin_get_exchanges_by_id"].format(coin_id=coin_id))

    def markets(self, coin_id: str) -> List[Dict[str, Union[str, bool, float, Dict[str, Dict[str, float]]]]]:
        """Get markets by coin ID.

            Args:
                coin_id
        """
        return self.get(API_PATH["coin_get_markets_by_id"].format(coin_id=coin_id))

    def ohlc(self, coin_id, quote="usd") -> List[Dict[str, Union[str, int]]]:
        """Get OHLC for last full day.

            Args:
                coin_id
                quote: Returned data quote.
        """
        return self.get(API_PATH["coin_get_ohlc_last_full_day_by_id"].format(
            coin_id=coin_id, quote=quote))

    def ohlcv(self, coin_id, *,
              start_date: str, end_date: str="",
              limit: int=1, quote: str="usd"):
        """Get historical OHLC.

            Args:
                coin_id
                start_date: Start point for historical data.
                end_date: End point for ohlcv (max 1 year).
                limit: Limit of result rows.
                quote: Returned data quote.
        """
        return self.get(API_PATH["coin_get_ohlc_historical_by_date"].format(
            coin_id=coin_id,
            start_date=start_date,
            end_date=end_date,
            limit=limit,
            quote=quote))

    def ohlcv_today(self, coin_id, quote="usd"):
        """Get today OHLC.

            Args:
                coin_id:
                quote: Returned data quote.
        """
        return self.get(API_PATH["coin_get_ohlc_today_by_id"].format(
            coin_id=coin_id,
            quote=quote))

    def people(self, person_id: str):
        """Get people by ID.

            Args:
                person_id
        """
        return self.get(API_PATH["people_get_by_id"].format(
            person_id=person_id))

    def tags(self, additional_fields=""):
        """List tags.

            Args:
                additional_fields: Comma separated list of additional fields to include in query result for each tag.
        """
        return self.get(API_PATH["tags_list"].format(
            additional_fields=additional_fields))

    def tag(self, tag_id: str, additional_fields=""):
        """Get tag by ID.

            Args:
                tag_id:
                additional_fields: Comma separated list of additional fields to include in query result for each tag.
        """
        return self.get(API_PATH["tag_get_by_id"].format(
            tag_id=tag_id,
            additional_fields=additional_fields))

    def tickers(self, quotes=""):
        """Get tickers for all coins.

            Args:
                quotes: Comma separated list of quotes to return.
        """
        return self.get(API_PATH["tickers_list"].format(quotes=quotes))

    def ticker(self, coin_id: str, quotes=""):
        """Get ticker information for specific coin.

            Args:
                coin_id:
                quotes: Comma separated list of quotes to return.
        """
        return self.get(API_PATH["ticker_get_information_by_id"].format(
            coin_id=coin_id,
            quotes=quotes))

    def historical_tickers(self, coin_id: str, *, start_date: str,
                           end_date: str="", limit: int=1000,
                           quote: str="usd", interval: str="5m"):
        """Get historical tickers for specific coin.

            Args:
                coin_id:
                start_date: Start point for historical data.
                end_date: End point for historical data.
                limit: Limit of result rows.
                quote: Returned data quote.
                interval: Returned points interval.
        """
        return self.get(API_PATH["ticker_get_historical_by_id"].format(
            coin_id=coin_id,
            start_date=start_date,
            end_date=end_date,
            limit=limit,
            quote=quote,
            interval=interval))

    def exchanges(self, quotes: str=""):
        """List exchanges.

            Args:
                quotes: Comma separated list of quotes to return.
        """
        return self.get(API_PATH["exchanges_list"].format(quotes=quotes))

    def exchange(self, exchange_id: str, quotes: str=""):
        """Get exchange by ID.

            Args:
                exchange_id:
                quotes: Comma separated list of quotes to return.
        """
        return self.get(API_PATH["exchange_get_by_id"].format(
            exchange_id=exchange_id,
            quotes=quotes))

    def exchange_markets(self, exchange_id: str, quotes: str=""):
        """Get markets by exchange ID.

            Args:
                exchange_id:
                quotes: Comma separated list of quotes to return.
        """
        self.get(API_PATH["exchange_get_markets_by_id"].format(
            exchange_id=exchange_id,
            quotes=quotes))

    def search(self, query: str, categories: str="",
               modifier: str="", limit: int=6):
        """Search the Coinpaprika API.

            Args:
                query: Phrase to search for.
                c: One or more categories (comma separated) to search.
                modifier: Set modifier for search results.
                limit: Limit of results per category.
        """
        return self.get(API_PATH["search"].format(
            query=query,
            categories=categories,
            modifier=modifier,
            limit=limit))

    def price_converter(self, base_currency_id: str,
                        quote_currency_id: str, amount: int=0):
        """Convert currencies.

            Args:
                base_currency_id
                quote_currency_id
                amount
        """
        return self.get(API_PATH["price_converter"].format(
            base_currency_id=base_currency_id,
            quote_currency_id=quote_currency_id,
            amount=amount))

#  vim: set ts=4 sw=4 tw=79 ft=python et :
