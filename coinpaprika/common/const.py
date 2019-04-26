"""coinpaprika-py constants."""

__version__ = "1.0-a1"

API_BASE_ENDPOINT = "https://api.coinpaprika.com/v1/"
API_PATH = {
        "global": "global",
        "coins_list": "coins",
        "coin_get_by_id": "coins/{coin_id}",
        "coin_get_twitter_timeline": "coins/{coin_id}/twitter",
        "coin_get_events_by_id": "coins/{coin_id}/events",
        "coin_get_exchanges_by_id": "coins/{coin_id}/exchanges",
        "coin_get_markets_by_id": "coins/{coin_id}/markets",
        "coin_get_ohlc_last_full_day_by_id": "coins/{coin_id}/ohlcv/latest?quote={quote}",
        "coin_get_ohlc_historical_by_date": ("coins/{coin_id}/ohlcv/" \
                                             "historical?start={start_date}" \
                                             "&end={end_date}" \
                                             "&limit={limit}" \
                                             "&quote={quote}"),
        "coin_get_ohlc_today_by_id": "coins/{coin_id}/ohlcv/today?quote={quote}",
        "people_get_by_id": "people/{person_id}",
        "tags_list": "tags?additional_fields={additional_fields}",
        "tag_get_by_id": "tags/{tag_id}?additional_fields={additional_fields}",
        "tickers_list": "tickers?quotes={quotes}",
        "ticker_get_information_by_id": "tickers/{coin_id}?quotes={quotes}",
        "ticker_get_historical_by_id": ("tickers/{coin_id}/" \
                                        "historical?start={start_date}" \
                                        "&end={end_date}" \
                                        "&limit={limit}" \
                                        "&quote={quote}" \
                                        "&interval={interval}"),
        "exchanges_list": "exchanges?quotes={quotes}",
        "exchange_get_by_id": "exchanges/{exchange_id}?quotes={quotes}",
        "exchange_get_markets_by_id": "exchanges/{exchange_id}/markets?quotes={quotes}",
        "search": "search?q={query}&c={categories}&modifier={modifier}&limit={limit}",
        "price_converter": ("price-converter?base_currency_id={base_currency_id}" \
                            "&quote_currency_id={quote_currency_id}" \
                            "&amount={amount}"),
}

USER_AGENT_FORMAT = "{{}} coinpaprika-py/{}".format(__version__)

#  vim: set ts=4 sw=4 tw=79 ft=python et :
