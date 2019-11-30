#!/usr/bin/env python3
"""
Unit Tests for the Coin Metrics API
"""
import unittest
import logging
import pandas as pd
import coinmetrics
from coinmetrics.utils import (csv, cm_to_pandas, normalize)

FORMAT = "%(message)s"
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
logging.getLogger('coinmetrics').setLevel(logging.INFO)
logging.getLogger('coinmetrics.api').setLevel(logging.INFO)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
LOG = logging.getLogger('test')

# Global test defaults
ASSET = "btc"
MARKET = "kraken-eth-usd-spot"
EXCHANGE = "coinbase"
METRIC = "PriceUSD"
BEGIN_TIMESTAMP = "2019-01-01"
END_TIMESTAMP = "2019-01-08"

INVALID_ASSET = "invalid_asset"
INVALID_MARKET = "invalid_market"
INVALID_EXCHANGE = "invalid_exchange"
INVALID_METRIC = "invalid_metric"
INVALID_BEGIN_TIMESTAMP = "2019-02-01"
INVALID_END_TIMESTAMP = "2019-01-01"

SAMPLE_EXPECTED_EXCHANGES = ['bitfinex', 'bitstamp', 'coinbase', 'gemini', 'kraken']
SAMPLE_EXPECTED_MARKETS = ['bitfinex-btc-usd-spot', 'bitstamp-btc-usd-spot',
                           'coinbase-eth-btc-spot', 'gemini-btc-usd-spot', 'kraken-xrp-btc-spot']
SAMPLE_EXPECTED_METRICS = ['BlkCnt', 'CapMVRVCur', 'PriceUSD', 'ROI1yr', 'VtyDayRet30d']
SAMPLE_EXPECTED_ASSETS = ["btc", "eth", "ltc", "xrp", "usdt"]

CSV_OUT = "test.csv"

CM = coinmetrics.Community()


class BaseAPITests(unittest.TestCase):
    """
    Tests for the Coinmetrics Base API
    """
    def test_get_assets(self):
        """
        Determine if the supported assets are:
        1. Returned as a list.
        2. Returned as a list of multiple elements (i.e. isn't empty).
        3. Retruned containing a few expected results.
        """
        LOG.debug("\n\tFunction: get_assets()")
        LOG.debug("\tArgument(s): None")
        results = CM.get_assets()

        LOG.debug("\tTest 1: Return type == list")
        self.assertTrue(isinstance(results, list))
        LOG.debug("\tTest 1: PASS")

        LOG.debug("\tTest 2: List length != 0")
        self.assertTrue(len(results) != 0)
        LOG.debug("\tTest 2: List length != 0")

        LOG.debug("\tTest 3: Sample assets in results")
        for i, asset in enumerate(SAMPLE_EXPECTED_ASSETS):
            LOG.debug("\t\t3.%s - Searching for %s", i, asset)
            self.assertIn(asset, results)
        LOG.debug("\tTest 3: Pass")

    def test_get_metrics(self):
        """
        Determine if the supported metrics are:
        1. Returned as a list.
        2. Returned as a list of multiple elements (i.e. isn't empty).
        3. Retruned containing a few expected results.
        """
        LOG.debug("\n\tFunction: get_metrics()")
        LOG.debug("\tArgument(s): None")

        results = CM.get_metrics()

        LOG.debug("\tTest 1: Return type == list")
        self.assertTrue(isinstance(results, list))
        LOG.debug("\tTest 1: PASS")

        LOG.debug("\tTest 2: List length != 0")
        self.assertTrue(len(results) != 0)
        LOG.debug("\tTest 2: List length != 0")

        LOG.debug("\tTest 3: Sample assets in results")
        for i, metric in enumerate(SAMPLE_EXPECTED_METRICS):
            LOG.debug("\t\t3.%s - Searching for %s", i, metric)
            self.assertIn(metric, results)
        LOG.debug("\tTest 3: Pass")

    def test_get_exchanges(self):
        """
        Determine if the supported exchanges are:
        1. Returned as a list.
        2. Returned as a list of multiple elements (i.e. isn't empty).
        3. Retruned containing a few expected results.
        """
        LOG.debug("\n\tFunction: get_exchanges()")
        LOG.debug("\tArgument: None")

        results = CM.get_exchanges()

        LOG.debug("\tTest 1: Return type == list")
        self.assertTrue(isinstance(results, list))
        LOG.debug("\tTest 1: PASS")

        LOG.debug("\tTest 2: List length != 0")
        self.assertTrue(len(results) != 0)
        LOG.debug("\tTest 2: List length != 0")

        LOG.debug("\tTest 3: Sample assets in results")
        for i, exchange in enumerate(SAMPLE_EXPECTED_EXCHANGES):
            LOG.debug("\t\t3.%s - Searching for %s", i, exchange)
            self.assertIn(exchange, results)
        LOG.debug("\tTest 3: Pass")

    def test_get_markets(self):
        """
        Determine if the supported markets are:
        1. Returned as a list.
        2. Returned as a list of multiple elements (i.e. isn't empty).
        3. Retruned containing a few expected results.
        """
        LOG.debug("\n\tFunction: get_markets()")
        LOG.debug("\tArgument: None")

        results = CM.get_markets()

        LOG.debug("\tTest 1: Return type == list")
        self.assertTrue(isinstance(results, list))
        LOG.debug("\tTest 1: PASS")

        LOG.debug("\tTest 2: List length != 0")
        self.assertTrue(len(results) != 0)
        LOG.debug("\tTest 2: List length != 0")

        LOG.debug("\tTest 3: Sample assets in results")
        for i, market in enumerate(SAMPLE_EXPECTED_MARKETS):
            LOG.debug("\t\t3.%s - Searching for %s", i, market)
            self.assertIn(market, results)
        LOG.debug("\tTest 3: Pass")


class BaseErrorTests(unittest.TestCase):
    """
    Tests for the Coinmetrics Base API Errors
    """
    def test_asset_checker(self):
        """
        Raise the correct error for an invalid asset.
        """
        LOG.debug("\n\tFunction: asset_checker()")
        LOG.debug("\tArgument(s): asset = '%s'", INVALID_ASSET)
        LOG.debug("\tTest 1: Invalid asset throws correct error type")
        with self.assertRaises(coinmetrics.errors.InvalidAssetError):
            CM.asset_checker(INVALID_ASSET)
        LOG.debug("\tTest 1: PASS")

    def test_exchange_checker(self):
        """
        Raise the correct error for an invalid exchange.
        """
        LOG.debug("\n\tFunction: exchange_checker()")
        LOG.debug("\tArgument: exchange = '%s'", INVALID_EXCHANGE)
        LOG.debug("\tTest 1: Invalid exchange throws correct error type")
        with self.assertRaises(coinmetrics.errors.InvalidExchangeError):
            CM.exchange_checker(INVALID_EXCHANGE)
        LOG.debug("\tTest 1: PASS")

    def test_market_checker(self):
        """
        Raise the correct error for an invalid market.
        """
        LOG.debug("\n\tFunction: market_checker()")
        LOG.debug("\tArgument: market = '%s'", INVALID_MARKET)
        LOG.debug("\tTest 1: Invalid exchange throws correct error type")
        with self.assertRaises(coinmetrics.errors.InvalidMetricError):
            CM.metric_checker(INVALID_MARKET)
        LOG.debug("\tTest 1: PASS")

    def test_metric_checker(self):
        """
        Raise the correct error for an invalid metric.
        """
        LOG.debug("\n\tFunction: metric_checker()")
        LOG.debug("\tArgument: metric = '%s'", INVALID_METRIC)
        LOG.debug("\tTest 1: Invalid metric throws correct error type")
        with self.assertRaises(coinmetrics.errors.InvalidMetricError):
            CM.metric_checker(INVALID_METRIC)
        LOG.debug("\tTest 1: PASS")

    def test_timestamp_checker(self):
        """
        Raise the correct error for an invalid time rance.
        """
        LOG.debug("\n\tFunction: exchange_checker()")
        LOG.debug("\tArgument: begin = '%s', end = '%s'", INVALID_BEGIN_TIMESTAMP,
                  INVALID_END_TIMESTAMP)
        LOG.debug("\tTest 1: Invalid timestamp range throws correct error type")
        with self.assertRaises(coinmetrics.errors.InvalidTimeRangeError):
            CM.timestamp_checker(INVALID_BEGIN_TIMESTAMP, INVALID_END_TIMESTAMP)
        LOG.debug("\tTest 1: PASS")

    def test_asset_metric_checker(self):
        """
        Raise the correct for a metric that is not listed for an asset.
        """
        LOG.debug("\n\tFunction: asset_metric_checker()")
        LOG.debug("\tTest 1: Invalid metric for valid asset")
        LOG.debug("\tArgument: asset = %s, metric = %s", ASSET, INVALID_METRIC)
        with self.assertRaises(coinmetrics.errors.InvalidMetricError):
            CM.asset_metric_checker(ASSET, INVALID_METRIC)
        LOG.debug("\tTest 1: PASS")

        LOG.debug("\tTest 2: Valid metric for valid asset")
        LOG.debug("\tArgument: asset = %s, metric = %s", ASSET, METRIC)
        CM.asset_metric_checker(ASSET, METRIC)
        LOG.debug("\tTest 2: PASS")


class CommunityAPITests(unittest.TestCase):
    """
    Tests for the Coinmetrics Base API
    """
    def test_get_asset_info(self):
        """
        Verify that asset information:
        1. Returns type list
        2. Returned list has elements (i.e. not empty)
        3. Each element is a dict with specific keys
        4. Exchanges listed in the dict contain expected values.
        5. Markets "
        6. Metrics "
        7. The correct error is raised when given an invalid asset
        """
        LOG.debug("\n\tFunction: get_asset_info()")

        LOG.debug("\tTest 0: Executes without arguments/defaults")
        LOG.debug("\tArgument: asset = None")
        results = CM.get_asset_info()
        self.assertTrue(isinstance(results, list))
        LOG.debug("\tTest 0: PASS")

        LOG.debug("\tArgument: asset = '%s'", ASSET)
        results = CM.get_asset_info(ASSET)

        LOG.debug("\tTest 1: Return type == list")
        self.assertTrue(isinstance(results, list))
        LOG.debug("\tTest 1: PASS")

        LOG.debug("\tTest 2: List length != 0")
        self.assertTrue(len(results) != 0)
        LOG.debug("\tTest 2: List length != 0")

        LOG.debug("\tNOTE: Examining first element only")
        result = results[0]

        LOG.debug("\tTest 3: Verify expected keys exist")
        expected_shape = {"id": str, "name": str, "metrics": list, "exchanges": list,
                          "markets": list, "hasReferenceRate": bool, "minTime": str,
                          "maxTime": str}
        for i, [key, value] in enumerate(expected_shape.items()):
            LOG.debug("\t\t3.%s - Searching for %s", i, key)
            self.assertIn(key, result)
            LOG.debug("\t\t3.%s - Type check on %s", i, key)
            self.assertTrue(isinstance(result[key], value))
        LOG.debug("\tTest 3: PASS")

        LOG.debug("\tTest 4: Sample exchanges in results")
        for i, exchange in enumerate(SAMPLE_EXPECTED_EXCHANGES):
            LOG.debug("\t\t4.%s - Searching for %s", i, exchange)
            self.assertIn(exchange, result['exchanges'])
        LOG.debug("\tTest 4: PASS")

        LOG.debug("\tTest 5: Sample markets in results")
        for i, market in enumerate(SAMPLE_EXPECTED_MARKETS):
            LOG.debug("\t\t5.%s - Searching for %s", i, market)
            self.assertIn(market, result['markets'])
        LOG.debug("\tTest 5: PASS")

        LOG.debug("\tTest 6: Sample metrics in results")
        for i, metric in enumerate(SAMPLE_EXPECTED_METRICS):
            LOG.debug("\t\t6.%s - Searching for %s", i, metric)
            self.assertIn(metric, result['metrics'])
        LOG.debug("\tTest 6: PASS")

        LOG.debug("\tTest 7: Raise correct error for invalid asset")
        with self.assertRaises(coinmetrics.errors.InvalidAssetError):
            CM.get_asset_info(INVALID_ASSET)
        LOG.debug("\tTest 7: PASS")

    def test_get_exchange_info(self):
        """
        Test exchange exchange information.
        1. Returns type list
        2. Returned list has elements (i.e. not empty)
        3. Each element is a dict with specific keys
        4. Verify expected keys exist, and are correct type.
        5. The correct error is raised when given an invalid exchange
        """
        LOG.debug("\n\tFunction: get_exchange_info()")

        LOG.debug("\tArgument: exchange = '%s'", EXCHANGE)
        results = CM.get_exchange_info(EXCHANGE)

        LOG.debug("\tTest 1: Return type == list")
        self.assertTrue(isinstance(results, list))
        LOG.debug("\tTest 1: PASS")

        LOG.debug("\tTest 2: List length != 0")
        self.assertTrue(len(results) != 0)
        LOG.debug("\tTest 2: PASS")

        LOG.debug("\tNOTE: Examining first element from exchangeInfo")
        result = results[0]

        LOG.debug("\tTest 3: Verify expected keys exist")
        expected_shape = {"id": str, "marketsInfo": list}
        for i, [key, value] in enumerate(expected_shape.items()):
            LOG.debug("\t\t3.%s - Searching for %s", i, key)
            self.assertIn(key, result)
            LOG.debug("\t\t3.%s - Type check on %s", i, key)
            self.assertTrue(isinstance(result[key], value))
        LOG.debug("\tTest 3: PASS")

        LOG.debug("\tNOTE: Examining first element from marketsInfo")
        result = result["marketsInfo"][0]

        LOG.debug("\tTest 4: Verify expected keys exist")
        expected_shape = {"id": [str], "assetIdBase": [str], "assetIdQuote": [str],
                          "minTime": [str, type(None)], "maxTime": [str, type(None)]}
        for i, [key, value] in enumerate(expected_shape.items()):
            LOG.debug("\t\t4.%s - Searching for %s", i, key)
            self.assertIn(key, result)
            LOG.debug("\t\t4.%s - Type check on %s", i, key)
            self.assertIn(type(result[key]), value)
        LOG.debug("\tTest 4: PASS")

        LOG.debug("\tTest 5: Raise correct error for invalid exchange")
        LOG.debug("\tArgument: exchange = '%s'", INVALID_EXCHANGE)
        with self.assertRaises(coinmetrics.errors.InvalidExchangeError):
            CM.get_exchange_info(INVALID_EXCHANGE)
        LOG.debug("\tTest 5: PASS")

    def test_get_metric_info(self):
        """
        Test metric asset information.
        1. Returns type list
        2. Returned list has elements (i.e. not empty)
        3. Each element is a dict with specific keys
        4. The correct error is raised when given an invalid exchange
        """
        LOG.debug("\n\tFunction: get_metric_info()")

        LOG.debug("\tTest 0: Executes without arguments/defaults")
        LOG.debug("\tArgument: asset = None")
        results = CM.get_metric_info()
        self.assertTrue(isinstance(results, list))
        LOG.debug("\tTest 0: PASS")

        LOG.debug("\tArgument: metric = '%s'", METRIC)
        results = CM.get_metric_info(METRIC)

        LOG.debug("\tTest 1: Return type == list")
        self.assertTrue(isinstance(results, list))
        LOG.debug("\tTest 1: PASS")

        LOG.debug("\tTest 2: List length != 0")
        self.assertTrue(len(results) != 0)
        LOG.debug("\tTest 2: PASS")

        LOG.debug("\tNOTE: Examining first element from results")
        result = results[0]

        LOG.debug("\tTest 3: Verify expected keys exist")
        expected_shape = {"category": str, "description": str, "id": str, "name": str,
                          "subcategory": str}
        for i, [key, value] in enumerate(expected_shape.items()):
            LOG.debug("\t\t3.%s - Searching for %s", i, key)
            self.assertIn(key, result)
            LOG.debug("\t\t3.%s - Type check on %s", i, key)
            self.assertTrue(isinstance(result[key], value))
        LOG.debug("\tTest 3: PASS")

        LOG.debug("\tTest 4: Raise correct error for invalid metric")
        LOG.debug("\tArgument: metric = '%s'", INVALID_METRIC)
        with self.assertRaises(coinmetrics.errors.InvalidMetricError):
            CM.get_metric_info(INVALID_METRIC)
        LOG.debug("\tTest 4: PASS")

    def test_get_market_info(self):
        """
        Test market asset information.
        1. Returns type list
        2. Returned list has elements (i.e. not empty)
        3. Each element is a dict with specific keys
        4. The correct error is raised when given an invalid exchange
        """
        LOG.debug("\n\tFunction: get_market_info()")

        LOG.debug("\tArgument: market = '%s'", MARKET)
        results = CM.get_market_info(MARKET)

        LOG.debug("\tTest 1: Return type == list")
        self.assertTrue(isinstance(results, list))
        LOG.debug("\tTest 1: PASS")

        LOG.debug("\tTest 2: List length != 0")
        self.assertTrue(len(results) != 0)
        LOG.debug("\tTest 2: PASS")

        LOG.debug("\tNOTE: Examining first element from results")
        result = results[0]

        LOG.debug("\tTest 3: Verify expected keys exist")
        expected_shape = {"assetIdBase": [str], "assetIdQuote": [str], "id": [str],
                          "maxTime": [str, type(None)], "minTime": [str, type(None)]}
        for i, [key, value] in enumerate(expected_shape.items()):
            LOG.debug("\t\t3.%s - Searching for %s", i, key)
            self.assertIn(key, result)
            LOG.debug("\t\t3.%s - Type check on %s", i, key)
            self.assertIn(type(result[key]), value)
        LOG.debug("\tTest 3: PASS")

        LOG.debug("\tTest 4: Raise correct error for invalid market")
        LOG.debug("\tArgument: market = '%s'", INVALID_MARKET)
        with self.assertRaises(coinmetrics.errors.InvalidMarketError):
            CM.get_market_info(INVALID_MARKET)
        LOG.debug("\tTest 4: PASS")

    def test_get_asset_metrics(self):
        """
        Test market asset to metric information.
        1. Returns type list
        2. Returned list has elements (i.e. not empty)
        3. Each element is a dict with specific keys
        4. The correct error is raised when given an invalid exchange
        """
        LOG.debug("\n\tFunction: get_asset_metrics()")
        LOG.debug("\tArgument: asset = '%s'", ASSET)
        result = CM.get_asset_metrics(ASSET)

        LOG.debug("\tTest 1: Return type == list")
        self.assertTrue(isinstance(result, list))
        LOG.debug("\tTest 1: PASS")

        LOG.debug("\tTest 2: List length != 0")
        self.assertTrue(len(result) != 0)
        LOG.debug("\tTest 2: PASS")

        LOG.debug("\tTest 3: Sample metrics in results")
        for i, market in enumerate(SAMPLE_EXPECTED_METRICS):
            LOG.debug("\t\t3.%s - Searching for %s", i, market)
            self.assertIn(market, result)
        LOG.debug("\tTest 3: PASS")

        LOG.debug("\tTest 4: Raise correct error for invalid asset")
        LOG.debug("\tArgument: asset = '%s'", INVALID_ASSET)
        with self.assertRaises(coinmetrics.errors.InvalidAssetError):
            CM.get_asset_metrics(INVALID_ASSET)
        LOG.debug("\tTest 4: PASS")

        multiple_assets = "btc,eth"
        LOG.debug("\tTest 5: Raise correct error for multiple assets")
        LOG.debug("\tArgument: asset = '%s'", multiple_assets)
        with self.assertRaises(coinmetrics.errors.InvalidAssetError):
            CM.get_asset_metrics(multiple_assets)
        LOG.debug("\tTest 5: PASS")

    def test_get_asset_metric_data(self):
        """
        Test fetching metric data.
        """
        # pylint: disable-msg=too-many-statements
        LOG.debug("\n\tFunction: get_asset_metric_data()")
        LOG.debug("\tArgument: asset = '%s'", ASSET)
        LOG.debug("\tArgument: start = '%s'", BEGIN_TIMESTAMP)
        LOG.debug("\tArgument: end = '%s'", END_TIMESTAMP)

        metric = "all"
        LOG.debug("\tTest 0: Default arguments")
        LOG.debug("\tArgument: metric = '%s'", metric)
        _ = CM.get_asset_metric_data(ASSET, metric, BEGIN_TIMESTAMP, END_TIMESTAMP)
        LOG.debug("\tTest 0: PASS")

        results = CM.get_asset_metric_data(ASSET, METRIC, BEGIN_TIMESTAMP, END_TIMESTAMP)
        LOG.debug("\tArgument: metric = '%s'", METRIC)
        LOG.debug("\tTest 1: Return type == dict")
        self.assertTrue(isinstance(results, dict))
        LOG.debug("\tTest 1: PASS")

        LOG.debug("\tTest 2: Verify expected keys exist")
        expected_shape = {"metrics": list, "series": list}
        for i, [key, value] in enumerate(expected_shape.items()):
            LOG.debug("\t\t2.%s - Searching for %s", i, key)
            self.assertIn(key, results)
            LOG.debug("\t\t2.%s - Type check on %s", i, key)
            self.assertTrue(isinstance(results[key], value))
        LOG.debug("\tTest 2: PASS")

        LOG.debug("\tNOTE: Examining metrics")
        metrics = results["metrics"]

        LOG.debug("\tTest 3: metrics list length != 0")
        self.assertTrue(len(metrics) != 0)
        LOG.debug("\tTest 3: PASS")

        LOG.debug("\tTest 4: metrics elements type == str")
        self.assertTrue(isinstance(metrics[0], str))
        LOG.debug("\tTest 4: PASS")

        LOG.debug("\tNOTE: Examining series")
        series = results["series"]

        LOG.debug("\tTest 5: series list length != 0")
        self.assertTrue(len(series) != 0)
        LOG.debug("\tTest 5: PASS")

        LOG.debug("\tNOTE: Examining first element in series")
        result = results["series"][0]

        LOG.debug("\tTest 6: Verify expected keys exist")
        expected_shape = {"time": str, "values": list}
        for i, [key, value] in enumerate(expected_shape.items()):
            LOG.debug("\t\t6.%s - Searching for %s", i, key)
            self.assertIn(key, result)
            LOG.debug("\t\t6.%s - Type check on %s", i, key)
            self.assertTrue(isinstance(result[key], value))
        LOG.debug("\tTest 6: PASS")

        LOG.debug("\tTest 7: Raise correct error for invalid asset")
        LOG.debug("\tArgument: asset = '%s'", INVALID_ASSET)
        with self.assertRaises(coinmetrics.errors.InvalidAssetError):
            CM.get_asset_metrics(INVALID_ASSET)
        LOG.debug("\tTest 7: PASS")

        LOG.debug("\tTest 8: Raise correct error for invalid metric")
        LOG.debug("\tArgument: metric = '%s'", INVALID_METRIC)
        with self.assertRaises(coinmetrics.errors.InvalidMetricError):
            CM.get_metric_info(INVALID_METRIC)
        LOG.debug("\tTest 8: PASS")


class UtilsTests(unittest.TestCase):
    """
    Coinmetrics Utils testing.
    """
    def test_cm_to_pandas(self):
        """
        Test the utility function that converts the raw Coinmetrics object to
        a standard Pandas DataFrame.
        """
        LOG.debug("\n\tFunction: normalize()")
        LOG.debug("\tData: Gathering from test_get_asset_metric_data()")
        LOG.debug("\tArgument: asset = '%s'", ASSET)
        LOG.debug("\tArgument: start = '%s'", BEGIN_TIMESTAMP)
        LOG.debug("\tArgument: end = '%s'", END_TIMESTAMP)
        LOG.debug("\tArgument: metric = '%s'", METRIC)

        data = CM.get_asset_metric_data(ASSET, METRIC, BEGIN_TIMESTAMP, END_TIMESTAMP)

        LOG.debug("\tTest 1: Conversion of test data executes")
        results = cm_to_pandas(data)
        LOG.debug("\tTest 1: PASS")

        LOG.debug("\tTest 2: results length != 0")
        self.assertTrue(len(results) != 0)
        LOG.debug("\tTest 2: PASS")

        LOG.debug("\tTest 3: results type == pd.DataFrame")
        self.assertTrue(isinstance(results, pd.DataFrame))
        LOG.debug("\tTest 3: PASS")

        LOG.debug("\tTest 4: Pass on conversion if already pd.DataFrame")
        results = cm_to_pandas(results)
        LOG.debug("\tTest 4: PASS")

    def test_normalize(self):
        """
        Test the utility function that converts the raw Coinmetrics object to
        a list of dictionaires.
        """
        LOG.debug("\n\tFunction: normalize()")
        LOG.debug("\tData: Gathering from test_get_asset_metric_data()")
        LOG.debug("\tArgument: asset = '%s'", ASSET)
        LOG.debug("\tArgument: start = '%s'", BEGIN_TIMESTAMP)
        LOG.debug("\tArgument: end = '%s'", END_TIMESTAMP)
        LOG.debug("\tArgument: metric = '%s'", METRIC)

        data = CM.get_asset_metric_data(ASSET, METRIC, BEGIN_TIMESTAMP, END_TIMESTAMP)

        LOG.debug("\tTest 1: Conversion of test data executes")
        results = normalize(data)
        LOG.debug("\tTest 1: PASS")

        LOG.debug("\tTest 2: results length != 0")
        self.assertTrue(len(results) != 0)
        LOG.debug("\tTest 2: PASS")

        LOG.debug("\tTest 3: results type == list")
        self.assertTrue(isinstance(results, list))
        LOG.debug("\tTest 3: PASS")

        LOG.debug("\tNOTE: Examining first element only")
        result = results[0]

        LOG.debug("\tTest 4: results type == dict")
        self.assertTrue(isinstance(result, dict))
        LOG.debug("\tTest 4: PASS")

        LOG.debug("\tTest 5: Verify expected keys exist")
        expected_shape = {"time": str, "PriceUSD": str}
        for i, [key, value] in enumerate(expected_shape.items()):
            LOG.debug("\t\t5.%s - Searching for %s", i, key)
            self.assertIn(key, result)
            LOG.debug("\t\t5.%s - Type check on %s", i, key)
            self.assertTrue(isinstance(result[key], value))
        LOG.debug("\tTest 5: PASS")

    def test_csv(self):
        """
        Test the utility function that exports the raw Coinmetrics object as a
        CSV to a file.
        """
        LOG.debug("\n\tFunction: csv()")
        LOG.debug("\tData: Gathering from test_get_asset_metric_data()")
        LOG.debug("\tArgument: asset = '%s'", ASSET)
        LOG.debug("\tArgument: start = '%s'", BEGIN_TIMESTAMP)
        LOG.debug("\tArgument: end = '%s'", END_TIMESTAMP)
        LOG.debug("\tArgument: metric = '%s'", METRIC)

        results = CM.get_asset_metric_data(ASSET, METRIC, BEGIN_TIMESTAMP, END_TIMESTAMP)

        LOG.debug("\tTest 0: results length != 0")
        self.assertTrue(len(results) != 0)
        LOG.debug("\tTest 0: PASS")

        LOG.debug("\tTest 1: Conversion of results data executes")
        LOG.debug("\tArgument: file = '%s'", CSV_OUT)
        csv(results, CSV_OUT)
        LOG.debug("\tTest 1: PASS")


if __name__ == '__main__':
    unittest.main(verbosity=2)
