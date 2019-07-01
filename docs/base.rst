.. _base:

Base
----
This is the core definition for all v2+ Coinmetrics APIs, both Community
and Pro. This object includes the primary query device, all `*_checker`
functions and the necessary discovery methods to enable the them.

Primary Methods
"""""""""""""""

.. autoclass:: coinmetrics.base.Base
    :members: __init__, _api_query, get_assets, get_metrics, get_exchanges, get_markets, asset_checker, metric_checker, exchange_checker, market_checker, timestamp_checker

Alias Methods
"""""""""""""

A group of alternative methods that function identically to the references functions above. This is to support any legacy API method names.

.. autoclass:: coinmetrics.base.Base
	:members: get_supported_assets, assets, getmetrics, metrics, getexchanges, exchange, getmarkets, markets