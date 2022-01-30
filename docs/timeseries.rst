.. _timeseries:

Timeseries
---------
The :samp:`Timeseries` class is an extension of the the :ref:`base` class and in inherits all of the :samp:`Base` class' functionality.

Primary Methods
"""""""""""""""

.. autoclass:: coinmetrics.community.Timeseries
    :members: get_asset_info, get_exchange_info, get_metric_info, get_market_info, get_asset_metric_data

.. _conveniance_methods:

Conveniance Methods
"""""""""""""""""""

The methods are designed to provide a simple way to get a single metric, and essentially extend the :py:func:`coinmetrics.community.Timeseries.get_asset_metric_data` method.

.. autoclass:: coinmetrics.community.Timeseries
    :members: assets, metrics, exchanges, exchange_assets_pairs, pairs, institutions, markets, market_candles, market_metrics, indexes, asset_alerts

.. note:: The conveniance methods are not explicitly included in the coverage testing at this time.

Alias Methods
"""""""""""""

There are a very large number of aliases for the :ref:`conveniance_methods` above, that can be found in the code under each method definition. Below is an example of the aliases for :py:func:`get_active_addresses`.

.. code-block:: python

  # Method definition:
  def get_active_addresses(self, assets, start, end):
      return self.get_asset_metric_data(assets, "AdrActCnt", start, end)

  # Alias definition:
  active_addresses, activeaddresses, AdrActCnt = [get_active_addresses] * 3

The complete list of available aliases can be found using the following lines of code.

.. code-block:: python

  # Import the library
  import coinmetrics
  
  # Write out the complete method/atribute listing for the library
  print(dir(coinmetrics))
