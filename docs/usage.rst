.. _usage:

Usage
=====

.. code-block:: python
  
  # API Setup #################################################################

  # Import the API
  import coinmetrics

  # Initialize a reference object, in this case `cm` for the Community API
  cm = coinmetrics.Community()

  # Usage Examples ############################################################

  # List the assets Coin Metrics has data for.
  supported_assets = cm.get_supported_assets()
  print("supported assets:", supported_assets)

  # List all available metrics for BTC.
  asset = "btc"
  available_data_types = cm.get_available_data_types_for_asset(asset)
  print("available data types:", available_data_types)

  # Fetch the `medianfee` data for BTC from timestamp 1514764800 to 1515283200.
  asset = "btc"
  data_type = "medianfee"
  begin_timestamp = 1514764800
  end_timestamp = 1515283200
  asset_data = cm.get_asset_data_for_time_range(asset, data_type, begin_timestamp, end_timestamp)
  print("data given timerange:", asset_data)

From here, the sky is the limit. Apply your logic and profit.