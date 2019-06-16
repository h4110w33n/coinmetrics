.. _api_ref:

Community API
=============
The Coin Metrics API is provided for free and works without an API Key. See: https://coinmetrics.io/community-network-data/

The API implimentation has a few major sections:

1. The API has three official endpoints, which are grouped into the :ref:`core` section below. See: https://coinmetrics.io/api/
2. The `get_asset_data_for_time_range` endpoint has been extended into a number of more direct conveniance methods in the :ref:`extensions` section.
3. To accomidate a number of naming/formatting styles, aliases for each of the extended endpoints have been provided in the :ref:`aliases` section.
4. Basic sanity checkers that are internally used by this module are under the :ref:`helpers` section.
5. Errors due to invalid or misguided inputs are documented in the :ref:`exceptions` section.

.. _core:

Core
""""

A direct implimentation of the API provided by Coin Metrics.

.. autoclass:: coinmetrics.api.Community
    :members: get_supported_assets,get_available_data_types_for_asset,get_asset_data_for_time_range

.. _extensions:

Extensions
""""""""""

A number of conveniance functions that extend the :py:func:`get_asset_data_for_time_range` method into more memorable methods for each data type.

.. autoclass:: coinmetrics.api.Community
	:members: get_active_addresses, get_adjusted_tx_volume, get_average_difficulty, get_block_count, get_block_size, get_exchange_volume, get_fees, get_generated_coins, get_market_cap, get_median_fee, get_median_tx_value, get_payment_count, get_price, get_realized_cap, get_tx_count, get_tx_volume

.. _aliases:

Aliases
"""""""

All of the variations of the :ref:`extensions` listed above.

.. autoclass:: coinmetrics.api.Community
    :members: get_marketcap, getmarketcap, market_cap, marketcap, get_medianfee, getmedianfee, median_fee, medianfee, get_mediantxvalue, getmediantxvalue, median_tx_value, mediantxvalue, get_paymentcount, getpaymentcount, payment_count, paymentcount, getprice, price, get_realizedcap, getrealizedcap, realized_cap, realizedcap, get_txcount, gettxcount, tx_count, txcount, get_txvolume, gettxvolume, tx_volume, txcount

.. _helpers:

Helpers
"""""""

These are internally used functions to validate the arguments provided. The are resource intensive, as in they will fetch any necessary details through more basic functions to determine the validity. With this approach, we avoid sending a potentially large number of failed requests.

.. autoclass:: coinmetrics.api.Community
	:members: asset_checker, data_type_checker, timestamp_checker

.. _exceptions:

Exceptions
""""""""""

Not all plans go smoothly. Exceptions are here to handle those. These are raised within the :ref:`helpers` methods only.

.. automodule:: coinmetrics.api
    :members: Error, InvalidAssetError, InvalidDataTypeError, InvalidTimeRangeError
