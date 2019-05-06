Quick Start
===========

You can instantiate an instance of CoinpaprikaAPI-py like so:

.. code-block:: python


    import coinpaprikaAPI
    coinpaprika = coinpaprikaAPI.Coinpaprika()


Using the `coinpaprikaAPI` instance, you can then interact with Coinpaprika's API:

.. code-block:: python

    # Get all coins
    all_coins = coinpaprika.coins()

    # Get coin by ID
    bitcoin_data = coinpaprika.coin("btc-bitcoin")

    # Get tickers for all coins
    all_coin_tickers = coinpaprika.tickers(quotes="USD,BTC")

    # Get ticker by ID
    bitcoin_ticker_data = coinpaprika.ticker("btc-bitcoin")

    # Get all exchanges
    all_exchanges = coinpaprika.exchanges()

    # Get exchange by ID
    binance_exchange_data = coinpaprika.exchange("binance")

