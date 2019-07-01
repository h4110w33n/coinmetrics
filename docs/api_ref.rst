.. _api_ref:

API Reference
=============
The Coin Metrics API provides discovery mechanisms, network, exchange, and asset data via a direct JSON REST API. This module acts as a client interface.

The :ref:`base` and :ref:`community` APIs are available to all users without an API key. The :ref:`pro` API does require an API key that is only obtainable though `CM Network Data Pro`_.

.. _CM Network Data Pro: https://coinmetrics.io/cm-network-data-pro/

.. note:: The following arguments can consist of a single element or a comma delimited list within a string. A Python :samp:`list` is not valid at this time.

	- Asset: :samp:`btc` or :samp:`btc,ltc,eth`
	- Metric: :samp:`PriceUSD` or :samp:`NVTAdj,NVTAdj90,PriceUSD`
	- Exchange: :samp:`coinbase` or :samp:`bitfinex,coinbase,kraken`
	- Market: :samp:`bitfinex-btc-usd-spot` or  :samp:`bitfinex-btc-usd-spot, bitfinex-eth-usd-spot,kraken-btc-usd-spot`

.. toctree::
   :maxdepth: 2
   :caption: Class and Method Definitions:

   base
   community
   pro
   utils

