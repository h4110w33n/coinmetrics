#!/usr/bin/env python3
"""
Unit Tests for the Coin Metrics API
"""
import unittest
import logging
import coinmetrics

FORMAT = "%(message)s"
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
logging.getLogger("coinmetrics").setLevel(logging.INFO)
logging.getLogger("coinmetrics.api").setLevel(logging.INFO)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
LOG = logging.getLogger("test")

# Global Test Values
EXPECTED_ASSETS = ["btc", "eth", "ltc"]
EXPECTED_METRICS = ["FlowInExNtv", "NVTAdj", "PriceUSD"]
EXPECTED_EXCHANGES = ["binance", "bittrex", "coinbase"]
EXPECTED_EXCHANGE_ASSET_PAIRS = ["binance-btc", "coinbase-eth", "gemini-ltc"]
EXPECTED_ASSET_PAIRS = ["btc-usd", "eth-btc", "ltc-usdt"]
EXPECTED_INSTITUTIONS = ["grayscale"]
EXPECTED_MARKETS = [
    "binance-btc-usdt-spot",
    "coinbase-eth-usd-spot",
    "gemini-ltc-usd-spot",
]
EXPECTED_INDEXES = ["CMBI10", "RTREE"]
EXPECTED_ASSET_ALERTS = [
    "time_inter_block_hi",
    "block_count_by_unknown_miners_6b_equals_6",
]

# Initialize
CATALOG = coinmetrics.Catalog()


class CatalogAPITests(unittest.TestCase):
    """
    Coinmetrics catalog API validation tests
    """

    def test_get_assets(self):
        """
        Determine if `get_assets()`:
        0. works without error,
        1. returns the "data" key,
        2. has a list type for the value of "data",
        3. has a list that is non-zero length,
        4. contains a few expected assets, and
        5. endpoint functions with `exclude` param.
        """
        LOG.debug("\n\tTest 0: Determine if function executes without error")
        LOG.debug("\t\tFunction: get_assets()")
        assets = ",".join(EXPECTED_ASSETS)
        LOG.debug("\t\tArgument: assets = %s", assets)
        include = "metrics"
        LOG.debug("\t\tArgument: include = %s", include)
        results = CATALOG.get_assets(assets=assets, include=include)
        LOG.debug("\tTest 0: Pass")

        LOG.debug("\tTest 1: 'data' element in results")
        self.assertTrue("data" in results)
        LOG.debug("\tTest 1: Pass")

        LOG.debug("\tTest 2: Return type == list")
        self.assertIsInstance(results["data"], list)
        LOG.debug("\tTest 2: Pass")

        LOG.debug("\tTest 3: 'data' element has data/not-empty")
        self.assertTrue(results["data"])
        LOG.debug("\tTest 3: Pass")

        results = results["data"]

        LOG.debug("\tTest 4: Check for some expected assets")
        for i, asset in enumerate(EXPECTED_ASSETS):
            LOG.debug("\t\t4.%s - Searching for %s", i, asset)
            found = [item for item in results if item["asset"] == asset]
            self.assertTrue(found)
        LOG.debug("\tTest 4: Pass")

        LOG.debug("\tTest 5: Verify execution with different parameters")
        LOG.debug("\t\tFunction: get_assets()")
        LOG.debug("\t\tArgument: assets = %s", assets)
        exclude = "metrics"
        LOG.debug("\t\tArgument: exclude = %s", exclude)
        results = CATALOG.get_assets(assets=assets, exclude=exclude)
        LOG.debug("\tTest 5: Pass")

    def test_get_metrics(self):
        """
        Determine if `get_metrics()`:
        0. works without error,
        1. returns the "data" key,
        2. has a list type for the value of "data",
        3. has a list that is non-zero length,
        4. contains a few expected metrics, and
        5. endpoint functions with `reviewable` param.
        """
        LOG.debug("\n\tTest 0: Determine if function executes without error")
        LOG.debug("\t\tFunction: get_metrics()")
        metrics = ",".join(EXPECTED_METRICS)
        LOG.debug("\t\tArgument: metrics = %s", metrics)
        results = CATALOG.get_metrics(metrics=metrics)
        LOG.debug("\tTest 0: Pass")

        LOG.debug("\tTest 1: 'data' element in results")
        self.assertTrue("data" in results)
        LOG.debug("\tTest 1: Pass")

        LOG.debug("\tTest 2: Return type == list")
        self.assertIsInstance(results["data"], list)
        LOG.debug("\tTest 2: Pass")

        LOG.debug("\tTest 3: Dict length != 0")
        self.assertTrue(results["data"])
        LOG.debug("\tTest 3: Pass")

        results = results["data"]

        LOG.debug("\tTest 4: Check for some expected metrics")
        for i, metric in enumerate(EXPECTED_METRICS):
            LOG.debug("\t\t4.%s - Searching for %s", i, metric)
            found = [item for item in results if item["metric"] == metric]
            self.assertTrue(found)
        LOG.debug("\tTest 4: Pass")

        LOG.debug("\tTest 5: Verify execution with different parameters")
        LOG.debug("\t\tFunction: get_metrics()")
        LOG.debug("\t\tArgument: metrics = %s", metrics)
        reviewable = True
        LOG.debug("\t\tArgument: reviewable = %s", reviewable)
        results = CATALOG.get_metrics(metrics=metrics, reviewable=reviewable)
        LOG.debug("\tTest 5: Pass")

    def test_get_exchanges(self):
        """
        Determine if `get_exchanges()`:
        0. works without error,
        1. returns the "data" key,
        2. has a list type for the value of "data",
        3. has a list that is non-zero length,
        4. contains a few expected exchanges, and
        5. endpoint functions with no params.
        """
        LOG.debug("\n\tTest 0: Determine if function executes without error")
        LOG.debug("\t\tFunction: get_exchanges()")
        exchanges = ",".join(EXPECTED_EXCHANGES)
        LOG.debug("\t\tArgument: exchanges = %s", exchanges)
        results = CATALOG.get_exchanges(exchanges=exchanges)
        LOG.debug("\tTest 0: Pass")

        LOG.debug("\tTest 1: 'data' element in results")
        self.assertTrue("data" in results)
        LOG.debug("\tTest 1: Pass")

        LOG.debug("\tTest 2: Return type == list")
        self.assertIsInstance(results["data"], list)
        LOG.debug("\tTest 2: Pass")

        LOG.debug("\tTest 3: Dict length != 0")
        self.assertTrue(results["data"])
        LOG.debug("\tTest 3: Pass")

        results = results["data"]

        LOG.debug("\tTest 4: Check for some expected exchanges")
        for i, exchange in enumerate(EXPECTED_EXCHANGES):
            LOG.debug("\t\t4.%s - Searching for %s", i, exchange)
            found = [item for item in results if item["exchange"] == exchange]
            self.assertTrue(found)
        LOG.debug("\tTest 4: Pass")

        LOG.debug("\tTest 5: Verify execution without any arguments")
        LOG.debug("\t\tFunction: get_exchanges()")
        LOG.debug("\t\tArgument: None")
        results = CATALOG.get_exchanges()
        LOG.debug("\tTest 5: Pass")

    def test_get_exchange_assets(self):
        """
        Determine if `get_exchange_assets()`:
        0. works without error,
        1. returns the "data" key,
        2. has a list type for the value of "data",
        3. has a list that is non-zero length,
        4. contains a few expected exchange assets, and
        5. endpoint functions with no params.
        """
        LOG.debug("\n\tTest 0: Determine if function executes without error")
        LOG.debug("\t\tFunction: get_exchanges()")
        exchange_assets = ",".join(EXPECTED_EXCHANGE_ASSET_PAIRS)
        LOG.debug("\t\tArgument: exchange_assets = %s", exchange_assets)
        results = CATALOG.get_exchange_asset_pairs(exchange_assets=exchange_assets)
        LOG.debug("\tTest 0: Pass")

        LOG.debug("\tTest 1: 'data' element in results")
        self.assertTrue("data" in results)
        LOG.debug("\tTest 1: Pass")

        LOG.debug("\tTest 2: Return type == list")
        self.assertIsInstance(results["data"], list)
        LOG.debug("\tTest 2: Pass")

        LOG.debug("\tTest 3: Dict length != 0")
        self.assertTrue(results["data"])
        LOG.debug("\tTest 3: Pass")

        results = results["data"]

        LOG.debug("\tTest 4: Check for some expected exchange assets")
        for i, exchange_asset in enumerate(EXPECTED_EXCHANGE_ASSET_PAIRS):
            LOG.debug("\t\t4.%s - Searching for %s", i, exchange_asset)
            found = [
                item for item in results if item["exchange_asset"] == exchange_asset
            ]
            self.assertTrue(found)
        LOG.debug("\tTest 4: Pass")

        LOG.debug("\tTest 5: Verify execution without any arguments")
        LOG.debug("\t\tFunction: get_exchange_assets()")
        LOG.debug("\t\tArgument: None")
        results = CATALOG.get_exchange_asset_pairs()
        LOG.debug("\tTest 5: Pass")

    def test_get_pairs(self):
        """
        Determine if `get_pairs()`:
        0. works without error,
        1. returns the "data" key,
        2. has a list type for the value of "data",
        3. has a list that is non-zero length,
        4. contains a few expected asset pairs, and
        5. endpoint functions with no params.
        """
        LOG.debug("\n\tTest 0: Determine if function executes without error")
        LOG.debug("\t\tFunction: get_pairs()")
        pairs = ",".join(EXPECTED_ASSET_PAIRS)
        LOG.debug("\t\tArgument: pairs = %s", pairs)
        results = CATALOG.get_pairs(pairs=pairs)
        LOG.debug("\tTest 0: Pass")

        LOG.debug("\tTest 1: 'data' element in results")
        self.assertTrue("data" in results)
        LOG.debug("\tTest 1: Pass")

        LOG.debug("\tTest 2: Return type == list")
        self.assertIsInstance(results["data"], list)
        LOG.debug("\tTest 2: Pass")

        LOG.debug("\tTest 3: Dict length != 0")
        self.assertTrue(results["data"])
        LOG.debug("\tTest 3: Pass")

        results = results["data"]

        LOG.debug("\tTest 4: Check for some expected asset pairs")
        for i, pair in enumerate(EXPECTED_ASSET_PAIRS):
            LOG.debug("\t\t4.%s - Searching for %s", i, pair)
            found = [item for item in results if item["pair"] == pair]
            self.assertTrue(found)
        LOG.debug("\tTest 4: Pass")

        LOG.debug("\tTest 5: Verify execution without any arguments")
        LOG.debug("\t\tFunction: get_pairs()")
        LOG.debug("\t\tArgument: None")
        results = CATALOG.get_pairs()
        LOG.debug("\tTest 5: Pass")

    def test_get_institutions(self):
        """
        Determine if `get_institutions()`:
        0. works without error,
        1. returns the "data" key,
        2. has a list type for the value of "data",
        3. has a list that is non-zero length,
        4. contains a few expected institutions, and
        5. endpoint functions with no params.
        """
        LOG.debug("\n\tTest 0: Determine if function executes without error")
        LOG.debug("\t\tFunction: get_institutions()")
        institutions = ",".join(EXPECTED_INSTITUTIONS)
        LOG.debug("\t\tArgument: institutions = %s", institutions)
        results = CATALOG.get_institutions(institutions=institutions)
        LOG.debug("\tTest 0: Pass")

        LOG.debug("\tTest 1: 'data' element in results")
        self.assertTrue("data" in results)
        LOG.debug("\tTest 1: Pass")

        LOG.debug("\tTest 2: Return type == list")
        self.assertIsInstance(results["data"], list)
        LOG.debug("\tTest 2: Pass")

        LOG.debug("\tTest 3: Dict length != 0")
        self.assertTrue(results["data"])
        LOG.debug("\tTest 3: Pass")

        results = results["data"]

        LOG.debug("\tTest 4: Check for some expected institutions")
        for i, institution in enumerate(EXPECTED_INSTITUTIONS):
            LOG.debug("\t\t4.%s - Searching for %s", i, institution)
            found = [item for item in results if item["institution"] == institution]
            self.assertTrue(found)
        LOG.debug("\tTest 4: Pass")

        LOG.debug("\tTest 5: Verify execution without any arguments")
        LOG.debug("\t\tFunction: get_pairs()")
        LOG.debug("\t\tArgument: None")
        results = CATALOG.get_institutions()
        LOG.debug("\tTest 5: Pass")

    def test_get_markets(self):
        """
        Determine if `get_markets()`:
        0. works without error,
        1. returns the "data" key,
        2. has a list type for the value of "data",
        3. has a list that is non-zero length,
        4. contains a few expected markets, and
        5. endpoint functions with no params.
        """
        LOG.debug("\n\tTest 0: Determine if function executes without error")
        LOG.debug("\t\tFunction: get_markets()")
        markets = ",".join(EXPECTED_MARKETS)
        LOG.debug("\t\tArgument: markets = %s", markets)
        results = CATALOG.get_markets(markets=markets)
        LOG.debug("\tTest 0: Pass")

        LOG.debug("\tTest 1: 'data' element in results")
        self.assertTrue("data" in results)
        LOG.debug("\tTest 1: Pass")

        LOG.debug("\tTest 2: Return type == list")
        self.assertIsInstance(results["data"], list)
        LOG.debug("\tTest 2: Pass")

        LOG.debug("\tTest 3: Dict length != 0")
        self.assertTrue(results["data"])
        LOG.debug("\tTest 3: Pass")

        results = results["data"]

        LOG.debug("\tTest 4: Check for some expected markets")
        for i, market in enumerate(EXPECTED_MARKETS):
            LOG.debug("\t\t4.%s - Searching for %s", i, market)
            found = [item for item in results if item["market"] == market]
            self.assertTrue(found)
        LOG.debug("\tTest 4: Pass")

        LOG.debug("\tTest 5: Verify execution without any arguments")
        LOG.debug("\t\tFunction: get_pairs()")
        LOG.debug("\t\tArgument: None")
        results = CATALOG.get_markets()
        LOG.debug("\tTest 5: Pass")

    def test_get_market_candles(self):
        """
        Determine if `get_market_candles()`:
        0. works without error,
        1. returns the "data" key,
        2. has a list type for the value of "data",
        3. has a list that is non-zero length,
        4. contains a few expected market candles, and
        5. endpoint functions with no params.
        """
        LOG.debug("\n\tTest 0: Determine if function executes without error")
        LOG.debug("\t\tFunction: get_market_candles()")
        markets = ",".join(EXPECTED_MARKETS)
        LOG.debug("\t\tArgument: markets = %s", markets)
        results = CATALOG.get_market_candles(markets=markets)
        LOG.debug("\tTest 0: Pass")

        LOG.debug("\tTest 1: 'data' element in results")
        self.assertTrue("data" in results)
        LOG.debug("\tTest 1: Pass")

        LOG.debug("\tTest 2: Return type == list")
        self.assertIsInstance(results["data"], list)
        LOG.debug("\tTest 2: Pass")

        LOG.debug("\tTest 3: Dict length != 0")
        self.assertTrue(results["data"])
        LOG.debug("\tTest 3: Pass")

        results = results["data"]

        LOG.debug("\tTest 4: Check for some expected markets")
        for i, market in enumerate(EXPECTED_MARKETS):
            LOG.debug("\t\t4.%s - Searching for %s", i, market)
            found = [item for item in results if item["market"] == market]
            self.assertTrue(found)
        LOG.debug("\tTest 4: Pass")

        LOG.debug("\tTest 5: Verify execution without any arguments")
        LOG.debug("\t\tFunction: get_pairs()")
        LOG.debug("\t\tArgument: None")
        results = CATALOG.get_markets()
        LOG.debug("\tTest 5: Pass")

    def test_get_market_metrics(self):
        """
        Determine if `get_market_metrics()`:
        0. works without error,
        1. returns the "data" key,
        2. has a list type for the value of "data",
        3. has a list that is non-zero length,
        4. contains a few expected market candles, and
        5. endpoint functions with no params.
        """
        LOG.debug("\n\tTest 0: Determine if function executes without error")
        LOG.debug("\t\tFunction: get_market_metrics()")
        markets = ",".join(EXPECTED_MARKETS)
        LOG.debug("\t\tArgument: markets = %s", markets)
        results = CATALOG.get_market_candles(markets=markets)
        LOG.debug("\tTest 0: Pass")

        LOG.debug("\tTest 1: 'data' element in results")
        self.assertTrue("data" in results)
        LOG.debug("\tTest 1: Pass")

        LOG.debug("\tTest 2: Return type == list")
        self.assertIsInstance(results["data"], list)
        LOG.debug("\tTest 2: Pass")

        LOG.debug("\tTest 3: Dict length != 0")
        self.assertTrue(results["data"])
        LOG.debug("\tTest 3: Pass")

        results = results["data"]

        LOG.debug("\tTest 4: Check for some expected markets")
        for i, market in enumerate(EXPECTED_MARKETS):
            LOG.debug("\t\t4.%s - Searching for %s", i, market)
            found = [item for item in results if item["market"] == market]
            self.assertTrue(found)
        LOG.debug("\tTest 4: Pass")

        LOG.debug("\tTest 5: Verify execution without any arguments")
        LOG.debug("\t\tFunction: get_pairs()")
        LOG.debug("\t\tArgument: None")
        results = CATALOG.get_market_metrics()
        LOG.debug("\tTest 5: Pass")

    def test_get_indexes(self):
        """
        Determine if `get_indexes()`:
        0. works without error,
        1. returns the "data" key,
        2. has a list type for the value of "data",
        3. has a list that is non-zero length,
        4. contains a few expected indexes, and
        5. endpoint functions with no params.
        """
        LOG.debug("\n\tTest 0: Determine if function executes without error")
        LOG.debug("\t\tFunction: get_indexes()")
        indexes = ",".join(EXPECTED_INDEXES)
        LOG.debug("\t\tArgument: indexes = %s", indexes)
        results = CATALOG.get_indexes(indexes=indexes)
        LOG.debug("\tTest 0: Pass")

        LOG.debug("\tTest 1: 'data' element in results")
        self.assertTrue("data" in results)
        LOG.debug("\tTest 1: Pass")

        LOG.debug("\tTest 2: Return type == list")
        self.assertIsInstance(results["data"], list)
        LOG.debug("\tTest 2: Pass")

        LOG.debug("\tTest 3: Dict length != 0")
        self.assertTrue(results["data"])
        LOG.debug("\tTest 3: Pass")

        results = results["data"]

        LOG.debug("\tTest 4: Check for some expected indexes")
        for i, index in enumerate(EXPECTED_INDEXES):
            LOG.debug("\t\t4.%s - Searching for %s", i, index)
            found = [item for item in results if item["index"] == index]
            self.assertTrue(found)
        LOG.debug("\tTest 4: Pass")

        LOG.debug("\tTest 5: Verify execution without any arguments")
        LOG.debug("\t\tFunction: get_pairs()")
        LOG.debug("\t\tArgument: None")
        results = CATALOG.get_indexes()
        LOG.debug("\tTest 5: Pass")

    def test_get_asset_alerts(self):
        """
        Determine if `get_market_candles()`:
        0. works without error,
        1. returns the "data" key,
        2. has a list type for the value of "data",
        3. has a list that is non-zero length,
        4. contains a few expected asset alerts, and
        5. endpoint functions with no params.
        """
        LOG.debug("\n\tTest 0: Determine if function executes without error")
        LOG.debug("\t\tFunction: get_asset_alerts()")
        alerts = ",".join(EXPECTED_ASSET_ALERTS)
        LOG.debug("\t\tArgument: alerts = %s", alerts)
        results = CATALOG.get_asset_alerts(alerts=alerts)
        LOG.debug("\tTest 0: Pass")

        LOG.debug("\tTest 1: 'data' element in results")
        self.assertTrue("data" in results)
        LOG.debug("\tTest 1: Pass")

        LOG.debug("\tTest 2: Return type == list")
        self.assertIsInstance(results["data"], list)
        LOG.debug("\tTest 2: Pass")

        LOG.debug("\tTest 3: Dict length != 0")
        self.assertTrue(results["data"])
        LOG.debug("\tTest 3: Pass")

        results = results["data"]

        LOG.debug("\tTest 4: Check for some expected asset alerts")
        for i, alert in enumerate(EXPECTED_ASSET_ALERTS):
            LOG.debug("\t\t4.%s - Searching for %s", i, alert)
            found = [item for item in results if item["name"] == alert]
            self.assertTrue(found)
        LOG.debug("\tTest 4: Pass")

        LOG.debug("\tTest 5: Verify execution without any arguments")
        LOG.debug("\t\tFunction: get_pairs()")
        LOG.debug("\t\tArgument: None")
        results = CATALOG.get_asset_alerts()
        LOG.debug("\tTest 5: Pass")


if __name__ == "__main__":
    unittest.main(verbosity=2)
