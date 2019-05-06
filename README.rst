coinpaprikaAPI-py: The Python Coinpaprika API Wrapper
=====================================================
.. image:: https://readthedocs.org/projects/coinpaprikaapi-py/badge/?version=latest :target: https://coinpaprikaapi-py.readthedocs.io/en/latest/?badge=latest :alt: Documentation Status

coinpaprikaAPI-py is a python package that provides simple access to CoinPaprika's API. CoinpaprikaAPI-py aims to be easy to use and follows all of all of Coinpaprika's rules and limitations. With CoinpaprikaAPI-py there's no need to use `sleep` statements or implement rate limit decorators, the package does it all for you.

Installation
------------
CoinpaprikaAPI-py is supported on python3.4, 3.5, 3.6 and 3.7. The recommended and quickest way to install CoinpaprikaAPI-py is through `pip <https://pypi.python.org/pypi/pip>`_.

.. code-block:: bash

  pip install coinpaprikaAPI-py


Alternatively, you can clone the repository and run setup.py.

.. code-block:: bash

    git clone https://github.com/CoinQuanta/coinpaprikaAPI-py
    cd coinpaprikaAPI-py && python setup.py install


Quickstart
----------

You can instantiate an instance of CoinpaprikaAPI-py like so:

.. code-block:: python


    import coinpaprikaAPI
    coinpaprika = coinpaprikaAPI.Coinpaprika()


Using the `coinpaprika` instance, you can then interact with Coinpaprika's API:

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



Please see CoinpaprikaAPI-py's `documentation <https://coinpaprikaAPI-py.readthedocs.io/>`_ for more examples of what you can do with CoinpaprikaAPI-py.

Documentation
-------------

CoinpaprikaAPI-py's documentation is located at https://coinpaprikaAPI-py.readthedocs.io/.


License
-------
CoinpaprikaAPI-py's source is provided under the `MIT License <https://github.com/CoinQuanta/coinpaprikaAPI-py/blob/master/LICENSE>`_.


