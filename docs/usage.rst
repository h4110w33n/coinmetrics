.. _usage:

Usage
=====

Fetching Data
"""""""""""""

.. code-block:: python
  
  # API Setup #################################################################

  # Import the API
  import coinmetrics

  # Initialize a reference object, in this case `cm` for the Community API
  cm = coinmetrics.Community()

  # Usage Examples ############################################################

  # List the assets Coin Metrics has data for.
  supported_assets = cm.get_supported_assets()
  print("supported assets:\n", supported_assets)

  # List all available metrics for BTC.
  asset = "btc"
  available_data_types = cm.get_available_data_types_for_asset(asset)
  print("available data types:\n", available_data_types)

  # Fetch the `PriceUSD` and `ROI30d` data for BTC from 2019-01-01 to 2019-01-08.
  asset = "btc"
  metric = "PriceUSD,ROI30d"
  begin_timestamp = "2019-01-01"  # The `datetime` type is also accepted
  end_timestamp = "2019-01-08"  # The `datetime` type is also accepted
  asset_data = cm.get_asset_data_for_time_range(asset, metric, begin_timestamp, end_timestamp)
  print("data given timerange:\n", asset_data)

Transforming Data
"""""""""""""""""

.. code-block:: python

  # Convert the data object we recieved to a Pandas DataFrame for further processing.
  # We are reusing the `asset_data` from the previous step.
  pandas_data_frame = coinmetrics.cm_to_pandas(asset_data)
  print("pandas data frame:\n", pandas_data_frame)

  # Save the Pandas DataFrame OR raw Coimetrics object into a CSV.
  # We are resuing the `pandas_data_frame` from the previous step, but the `asset_data`
  # from the step before that is also a valid input.
  path_or_filename = "output.csv"
  coinmetrics.csv(pandas_data_frame, path_or_filename)
  print("CSV written:", path_or_filename)

From here, the sky is the limit. Apply your logic and profit.