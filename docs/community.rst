.. _community:

Community
---------
The :samp:`Community` class is an extension of the the :ref:`base` class and in inherits all of the :samp:`Base` class' functionality.

Primary Methods
"""""""""""""""

.. autoclass:: coinmetrics.community.Community
    :members: __init__, get_asset_info, get_exchange_info, get_metric_info, get_market_info, get_asset_metric_data

.. _conveniance_methods:

Conveniance Methods
"""""""""""""""""""

The methods are designed to provide a simple way to get a single metric, and essentially extend the :py:func:`coinmetrics.community.Community.get_asset_metric_data` method.

.. autoclass:: coinmetrics.community.Community
    :members: get_active_addresses, get_block_count, get_mean_block_size, get_mvrv_cur, get_real_cap, get_diff_mean, get_fee_mean, get_median_fee, get_fee_total, get_units_issued, get_units_issued_ann_pct, get_units_issued_usd, get_nvt_adj, get_nvt_adj_90, get_price_btc, get_price_usd, get_cur_sply, get_tx_count, get_txtfr_count, get_txtfr_val_adj, get_txtfr_val_adj_usd, get_txtfr_val_mean, get_txtfr_val_mean_usd, get_txtfr_val_med, get_txtfr_val_med_usd, get_txtfr_val, get_txtfr_val_usd, get_vty_ret_180d, get_vty_ret_30d, get_vty_ret_60d, get_available_data_types_for_asset, get_asset_data_for_time_range

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
