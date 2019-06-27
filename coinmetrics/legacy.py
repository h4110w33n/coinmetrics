"""
Coin Metrics Legacy Community API Module Definitions
"""

from decimal import Decimal
import json
import logging
import requests
from .errors import InvalidAssetError, InvalidTimeRangeError, InvalidDataTypeError

class CommunityLegacy():
    """
    Community APIv1 Object
    """

    # Due to the conveniance methods, we trigger R0904: too-many-public-methods
    # even though this is desired.
    # pylint: disable=R0904
    def __init__(self):
        """
        The Community API object definition
        """
        self.logger = logging.getLogger(__name__)
        self.host_url = 'https://coinmetrics.io/api/v1/'
        self.methods = set(['get_supported_assets',
                            'get_available_data_types_for_asset',
                            'get_asset_data_for_time_range'])

    def _api_query(self, method, *options):
        """
        Execute the raw API query and return the raw JSON output.

        :param method: Query method for getting data.
        :type method: str

        :param options: Tuple containing all options, including: asset, data_type, and timestamps.
        :type options: tuple

        :return: Raw JSON response
        :rtype: dict
        """
        self.logger.debug("Method: '%s'", method)
        self.logger.debug("Options: '%s'", str(options))
        url_path = '' if not options else '/' + '/'.join(str(option) for option in options)
        request_url = ''
        if method in self.methods:
            request_url = self.host_url + method + url_path
        else:
            print("ERROR: Not a valid method.")
        response = requests.get(request_url).content.decode('utf-8')
        return json.loads(response, parse_float=Decimal, parse_int=Decimal)

    def get_supported_assets(self):
        """
        Returns list of assets that are supported by coinmetrics.io.

        :return: List of supported assets.
        :rtype: list
        """
        return self._api_query("get_supported_assets")

    def get_available_data_types_for_asset(self, asset):
        """
        Returns list of data types available for specified asset.

        :param asset: Unique ID corresponding to the asset's ticker: btc, ltc, gno
        :type asset: str

        :return: List of data types for the specified asset.
        :rtype: list
        """
        self.logger.debug("Asset: '%s'", asset)
        self.asset_checker(asset)
        return self._api_query("get_available_data_types_for_asset", asset.lower())['result']

    def get_asset_data_for_time_range(self, asset, data_type, begin_timestamp, end_timestamp):
        """
        Returns daily values of specified data type for specified asset on
        dates that belong to closed interval between begin_timestamp and end_timestamp.

        :param asset: Unique ID corresponding to the asset's ticker: btc, ltc, gno
        :type asset: str

        :param data_type: Unique ID corresponding to the metric.
        :type data_type: str

        :param begin_timestamp: Start of time inverval.
        :type begin_timestamp: str or int

        :param end_timestamp: End of time inverval.
        :type end_timestamp: str or int

        :return: List of lists, with unix timestamp and raw values.
        :rtype: list
        """
        self.logger.debug("Asset: '%s'", asset)
        self.logger.debug("Data Type: '%s'", data_type)
        self.logger.debug("Begin Timestamp: '%s'", begin_timestamp)
        self.logger.debug("End Timestamp: '%s'", end_timestamp)
        self.asset_checker(asset)
        self.data_type_checker(asset, data_type)
        self.timestamp_checker(begin_timestamp, end_timestamp)
        return self._api_query("get_asset_data_for_time_range", asset.lower(),
                               data_type, begin_timestamp, end_timestamp)['result']

    def get_active_addresses(self, asset, begin_timestamp, end_timestamp):
        """
        :param asset: Unique ID corresponding to the asset's ticker: btc, ltc, gno
        :type asset: str

        :param begin_timestamp: Start of time inverval.
        :type begin_timestamp: str or int

        :param end_timestamp: End of time inverval.
        :type end_timestamp: str or int

        :return: Simple count (int) of addresses.
        :rtype: list
        """
        self.logger.debug("Redirecting 'get_active_addresses' to 'get_asset_data_for_time_range'")
        return self.get_asset_data_for_time_range(asset, "activeaddresses",
                                                  begin_timestamp, end_timestamp)

    #: An alias for :py:func:`get_active_addresses`
    [get_activeaddresses, getactiveaddresses, active_addresses,
     activeaddresses] = [get_active_addresses] * 4

    def get_adjusted_tx_volume(self, asset, begin_timestamp, end_timestamp):
        """
        :param asset: Unique ID corresponding to the asset's ticker: btc, ltc, gno
        :type asset: str

        :param begin_timestamp: Start of time inverval.
        :type begin_timestamp: str or int

        :param end_timestamp: End of time inverval.
        :type end_timestamp: str or int

        :return: Volume (USD) of asset.
        :rtype: list
        """
        self.logger.debug("Redirecting 'get_adjusted_tx_volume' to 'get_asset_data_for_time_range'")
        return self.get_asset_data_for_time_range(asset,
                                                  "adjustedtxvolume",
                                                  begin_timestamp,
                                                  end_timestamp)

    #: An alias for :py:func:`get_adjusted_tx_volume`
    [get_adjustedtxvolume, getadjustedtxvolume, adjusted_tx_volume,
     adjustedtxvolume] = [get_adjusted_tx_volume] * 4

    def get_average_difficulty(self, asset, begin_timestamp, end_timestamp):
        """
        :param asset: Unique ID corresponding to the asset's ticker: btc, ltc, gno
        :type asset: str

        :param begin_timestamp: Start of time inverval.
        :type begin_timestamp: str or int

        :param end_timestamp: End of time inverval.
        :type end_timestamp: str or int

        :return: A large int representing difficulty.
        :rtype: list
        """
        self.logger.debug("Redirecting 'get_average_difficulty' to 'get_asset_data_for_time_range'")
        return self.get_asset_data_for_time_range(asset, "averagedifficulty",
                                                  begin_timestamp, end_timestamp)

    #: An alias for :py:func:`get_average_difficulty`
    [get_averagedifficulty, getaveragedifficulty, average_difficulty,
     averagedifficulty] = [get_average_difficulty] * 4

    def get_block_count(self, asset, begin_timestamp, end_timestamp):
        """
        :param asset: Unique ID corresponding to the asset's ticker: btc, ltc, gno
        :type asset: str

        :param begin_timestamp: Start of time inverval.
        :type begin_timestamp: str or int

        :param end_timestamp: End of time inverval.
        :type end_timestamp: str or int

        :return: Simple count (int) of blocks
        :rtype: list
        """
        self.logger.debug("Redirecting 'get_block_count' to 'get_asset_data_for_time_range'")
        return self.get_asset_data_for_time_range(asset, "blockcount",
                                                  begin_timestamp, end_timestamp)

    #: An alias for :py:func:`get_block_count`
    get_blockcount, getblockcount, block_count, blockcount = [get_block_count] * 4

    def get_block_size(self, asset, begin_timestamp, end_timestamp):
        """
        :param asset: Unique ID corresponding to the asset's ticker: btc, ltc, gno
        :type asset: str

        :param begin_timestamp: Start of time inverval.
        :type begin_timestamp: str or int

        :param end_timestamp: End of time inverval.
        :type end_timestamp: str or int

        :return: Size of blocks in MB.
        :rtype: list
        """
        self.logger.debug("Redirecting 'get_block_size' to 'get_asset_data_for_time_range'")
        return self.get_asset_data_for_time_range(asset, "blocksize",
                                                  begin_timestamp, end_timestamp)

    #: An alias for :py:func:`get_block_size`
    get_blocksize, getblocksize, block_size, blocksize = [get_block_size] * 4

    def get_exchange_volume(self, asset, begin_timestamp, end_timestamp):
        """
        :param asset: Unique ID corresponding to the asset's ticker: btc, ltc, gno
        :type asset: str

        :param begin_timestamp: Start of time inverval.
        :type begin_timestamp: str or int

        :param end_timestamp: End of time inverval.
        :type end_timestamp: str or int

        :return: Volume (int) of asset.
        :rtype: list
        """
        self.logger.debug("Redirecting 'get_exchange_volume' to 'get_asset_data_for_time_range'")
        return self.get_asset_data_for_time_range(asset, "exchangevolume",
                                                  begin_timestamp, end_timestamp)

    #: An alias for :py:func:`get_exchange_volume`
    [get_exchangevolume, getexchangevolume, exchange_volume,
     exchangevolume] = [get_exchange_volume] * 4

    def get_fees(self, asset, begin_timestamp, end_timestamp):
        """
        :param asset: Unique ID corresponding to the asset's ticker: btc, ltc, gno
        :type asset: str

        :param begin_timestamp: Start of time inverval.
        :type begin_timestamp: str or int

        :param end_timestamp: End of time inverval.
        :type end_timestamp: str or int

        :return: Amount (int) of asset.
        :rtype: list
        """
        self.logger.debug("Redirecting 'get_fees' to 'get_asset_data_for_time_range'")
        return self.get_asset_data_for_time_range(asset, "fees",
                                                  begin_timestamp, end_timestamp)

    #: An alias for :py:func:`get_fees`
    getfees, fees = [get_fees] * 2

    def get_generated_coins(self, asset, begin_timestamp, end_timestamp):
        """
        :param asset: Unique ID corresponding to the asset's ticker: btc, ltc, gno
        :type asset: str

        :param begin_timestamp: Start of time inverval.
        :type begin_timestamp: str or int

        :param end_timestamp: End of time inverval.
        :type end_timestamp: str or int

        :return: Amount (int) of asset.
        :rtype: list
        """
        self.logger.debug("Redirecting 'get_generated_coins' to 'get_asset_data_for_time_range'")
        return self.get_asset_data_for_time_range(asset, "generatedcoins",
                                                  begin_timestamp, end_timestamp)

    #: An alias for :py:func:`get_generated_coins`
    [get_generatedcoins, getgeneratedcoins, generated_coins,
     generatedcoins] = [get_generated_coins] * 4

    def get_market_cap(self, asset, begin_timestamp, end_timestamp):
        """
        :param asset: Unique ID corresponding to the asset's ticker: btc, ltc, gno
        :type asset: str

        :param begin_timestamp: Start of time inverval.
        :type begin_timestamp: str or int

        :param end_timestamp: End of time inverval.
        :type end_timestamp: str or int

        :return: Amount (USD) of asset.
        :rtype: list
        """
        self.logger.debug("Redirecting 'get_market_cap' to 'get_asset_data_for_time_range'")
        return self.get_asset_data_for_time_range(asset, "marketcap",
                                                  begin_timestamp, end_timestamp)

    #: An alias for :py:func:`get_market_cap`
    get_marketcap, getmarketcap, market_cap, marketcap = [get_market_cap] * 4

    def get_median_fee(self, asset, begin_timestamp, end_timestamp):
        """
        :param asset: Unique ID corresponding to the asset's ticker: btc, ltc, gno
        :type asset: str

        :param begin_timestamp: Start of time inverval.
        :type begin_timestamp: str or int

        :param end_timestamp: End of time inverval.
        :type end_timestamp: str or int

        :return: Amount (int) of asset.
        :rtype: list
        """
        self.logger.debug("Redirecting 'get_median_fee' to 'get_asset_data_for_time_range'")
        return self.get_asset_data_for_time_range(asset, "medianfee",
                                                  begin_timestamp, end_timestamp)

    #: An alias for :py:func:`get_median_fee`
    get_medianfee, getmedianfee, median_fee, medianfee = [get_median_fee] * 4

    def get_median_tx_value(self, asset, begin_timestamp, end_timestamp):
        """
        :param asset: Unique ID corresponding to the asset's ticker: btc, ltc, gno
        :type asset: str

        :param begin_timestamp: Start of time inverval.
        :type begin_timestamp: str or int

        :param end_timestamp: End of time inverval.
        :type end_timestamp: str or int

        :return: Amount (USD) of asset.
        :rtype: list
        """
        self.logger.debug("Redirecting 'get_median_tx_value' to 'get_asset_data_for_time_range'")
        return self.get_asset_data_for_time_range(asset, "mediantxvalue",
                                                  begin_timestamp, end_timestamp)

    #: An alias for :py:func:`get_median_tx_value`
    get_mediantxvalue, getmediantxvalue, median_tx_value, mediantxvalue = [get_median_tx_value] * 4

    def get_payment_count(self, asset, begin_timestamp, end_timestamp):
        """
        :param asset: Unique ID corresponding to the asset's ticker: btc, ltc, gno
        :type asset: str

        :param begin_timestamp: Start of time inverval.
        :type begin_timestamp: str or int

        :param end_timestamp: End of time inverval.
        :type end_timestamp: str or int

        :return: Amount (int) of asset.
        :rtype: list
        """
        self.logger.debug("Redirecting 'get_payment_count' to 'get_asset_data_for_time_range'")
        return self.get_asset_data_for_time_range(asset, "paymentcount",
                                                  begin_timestamp, end_timestamp)

    #: An alias for :py:func:`get_payment_count`
    get_paymentcount, getpaymentcount, payment_count, paymentcount = [get_payment_count] * 4

    def get_price(self, asset, begin_timestamp, end_timestamp):
        """
        :param asset: Unique ID corresponding to the asset's ticker: btc, ltc, gno
        :type asset: str

        :param begin_timestamp: Start of time inverval.
        :type begin_timestamp: str or int

        :param end_timestamp: End of time inverval.
        :type end_timestamp: str or int

        :return: Value (float) in USD.
        :rtype: list
        """
        self.logger.debug("Redirecting 'get_price' to 'get_asset_data_for_time_range'")
        return self.get_asset_data_for_time_range(asset, "price",
                                                  begin_timestamp, end_timestamp)

    #: An alias for :py:func:`get_price`
    getprice, price = [get_price] * 2

    def get_realized_cap(self, asset, begin_timestamp, end_timestamp):
        """
        :param asset: Unique ID corresponding to the asset's ticker: btc, ltc, gno
        :type asset: str

        :param begin_timestamp: Start of time inverval.
        :type begin_timestamp: str or int

        :param end_timestamp: End of time inverval.
        :type end_timestamp: str or int

        :return: Value (float) in USD
        :rtype: list
        """
        self.logger.debug("Redirecting 'get_realized_cap' to 'get_asset_data_for_time_range'")
        return self.get_asset_data_for_time_range(asset, "realizedcap",
                                                  begin_timestamp, end_timestamp)

    #: An alias for :py:func:`get_realized_cap`
    get_realizedcap, getrealizedcap, realized_cap, realizedcap = [get_realized_cap] * 4

    def get_tx_count(self, asset, begin_timestamp, end_timestamp):
        """
        :param asset: Unique ID corresponding to the asset's ticker: btc, ltc, gno
        :type asset: str

        :param begin_timestamp: Start of time inverval.
        :type begin_timestamp: str or int

        :param end_timestamp: End of time inverval.
        :type end_timestamp: str or int

        :return: Simple count (int).
        :rtype: list
        """
        self.logger.debug("Redirecting 'get_tx_count' to 'get_asset_data_for_time_range'")
        return self.get_asset_data_for_time_range(asset, "txcount",
                                                  begin_timestamp, end_timestamp)

    #: An alias for :py:func:`get_tx_count`
    get_txcount, gettxcount, tx_count, txcount = [get_tx_count] * 4

    def get_tx_volume(self, asset, begin_timestamp, end_timestamp):
        """
        :param asset: Unique ID corresponding to the asset's ticker: btc, ltc, gno
        :type asset: str

        :param begin_timestamp: Start of time inverval.
        :type begin_timestamp: str or int

        :param end_timestamp: End of time inverval.
        :type end_timestamp: str or int

        :return: Volume (int) of asset.
        :rtype: list
        """
        self.logger.debug("Redirecting 'get_tx_volume' to 'get_asset_data_for_time_range'")
        return self.get_asset_data_for_time_range(asset, "txcount",
                                                  begin_timestamp, end_timestamp)

    #: An alias for :py:func:`get_tx_volume`
    get_txvolume, gettxvolume, tx_volume, txcount = [get_tx_volume] * 4

    def asset_checker(self, asset):
        """
        Helper function to determine if the requested asset is valid or not.

        :param asset: Unique ID corresponding to the asset's ticker: btc, ltc, gno
        :type asset: str
        """
        if asset in self.get_supported_assets():
            pass
        else:
            self.logger.debug("Asset: '%s'", asset)
            raise InvalidAssetError

    def data_type_checker(self, asset, data_type):
        """
        Helper function to determine if the requested data type exists for a given asset

        :param asset: Unique ID corresponding to the asset's ticker: btc, ltc, gno
        :type asset: str

        :param data_type: Unique ID corresponding to the metric.
        :type data_type: str
        """
        if data_type in self.get_available_data_types_for_asset(asset):
            pass
        else:
            self.logger.debug("Asset: '%s'", asset)
            self.logger.debug("Data Type: '%s'", data_type)
            raise InvalidDataTypeError

    def timestamp_checker(self, begin_timestamp, end_timestamp):
        """
        Helper function to determine if the provided timerange is valid.

        :param begin_timestamp: Start of time inverval.
        :type begin_timestamp: str or int

        :param end_timestamp: End of time inverval.
        :type end_timestamp: str or int
        """
        if begin_timestamp <= end_timestamp:
            pass
        else:
            self.logger.debug("Begin Timestamp: '%s'", begin_timestamp)
            self.logger.debug("End Timestamp: '%s'", end_timestamp)
            raise InvalidTimeRangeError
