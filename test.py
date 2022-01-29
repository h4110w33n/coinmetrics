#!/usr/bin/env python3
"""
Unit Tests for the Coin Metrics API
"""
import unittest
import logging
import pandas as pd
import coinmetrics

FORMAT = "%(message)s"
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
logging.getLogger('coinmetrics').setLevel(logging.INFO)
logging.getLogger('coinmetrics.api').setLevel(logging.INFO)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
LOG = logging.getLogger('test')

# Global Test Values

EXPECTED_ASSETS = ["btc", "eth", "ltc"]
EXPECTED_METRICS = ["FlowInExNtv", "NVTAdj", "PriceUSD"]
EXPECTED_EXCHANGES = ["binance", "bittrex", "coinbase"]

# Initialize
CM = coinmetrics.Catalog()

class CatalogAPITests(unittest.TestCase):

    # def test_get_assets(self):
    #     """
    #     Determine if `get_assets()`:
    #     0. works without error,
    #     1. returns the "data" key,
    #     2. has a list type for the value of "data",
    #     3. has a list that is non-zero length,
    #     4. contains a few expected assets, and
    #     5. endpoint functions with `exclude` param.
    #     """
    #     LOG.debug("\tTest 0: Determine if function executes without error")
    #     LOG.debug("\t\tFunction: get_assets()")
    #     assets = ",".join(EXPECTED_ASSETS)
    #     LOG.debug("\t\tArgument: assets = %s", assets)
    #     include = "metrics"
    #     LOG.debug("\t\tArgument: include = %s", include)
    #     results = CM.get_assets(assets=assets, include=include)
    #     LOG.debug("\tTest 0: Pass")

    #     LOG.debug("\tTest 1: 'data' element in results")
    #     self.assertTrue('data' in results)
    #     LOG.debug("\tTest 1: Pass")

    #     LOG.debug("\tTest 2: Return type == list")
    #     self.assertIsInstance(results['data'], list)
    #     LOG.debug("\tTest 2: Pass")

    #     LOG.debug("\tTest 3: 'data' element has data/not-empty")
    #     self.assertTrue(results['data'])
    #     LOG.debug("\tTest 3: Pass")

    #     results = results["data"]

    #     LOG.debug("\tTest 4: Check for some expected assets")
    #     for i, asset in enumerate(EXPECTED_ASSETS):
    #         LOG.debug("\t\t4.%s - Searching for %s", i, asset)
    #         found = [ item for item in results if item["asset"] == asset]
    #         self.assertTrue(found)
    #     LOG.debug("\tTest 4: Pass")

    #     LOG.debug("\tTest 5: Verify execution with different parameters")
    #     LOG.debug("\t\tFunction: get_assets()")
    #     LOG.debug("\t\tArgument: assets = %s", assets)
    #     exclude = "metrics"
    #     LOG.debug("\t\tArgument: exclude = %s", exclude)
    #     results = CM.get_assets(assets=assets, exclude=exclude)
    #     LOG.debug("\tTest 5: Pass")

    # def test_get_metrics(self):
    #     """
    #     Determine if `get_assets()`:
    #     0. works without error,
    #     1. returns the "data" key,
    #     2. has a list type for the value of "data",
    #     3. has a list that is non-zero length,
    #     4. contains a few expected metrics, and
    #     5. endpoint functions with `reviewable` param.
    #     """
    #     LOG.debug("\tTest 0: Determine if function executes without error")
    #     LOG.debug("\t\tFunction: get_metrics()")
    #     metrics = ",".join(EXPECTED_METRICS)
    #     LOG.debug("\t\tArgument: metrics = %s", metrics)
    #     results = CM.get_metrics(metrics=metrics)
    #     LOG.debug("\tTest 0: Pass")

    #     LOG.debug("\tTest 1: 'data' element in results")
    #     self.assertTrue('data' in results)
    #     LOG.debug("\tTest 1: Pass")

    #     LOG.debug("\tTest 2: Return type == list")
    #     self.assertIsInstance(results['data'], list)
    #     LOG.debug("\tTest 2: Pass")

    #     LOG.debug("\tTest 3: Dict length != 0")
    #     self.assertTrue(results['data'])
    #     LOG.debug("\tTest 3: Pass")

    #     results = results["data"]

    #     LOG.debug("\tTest 4: Check for some expected assets")
    #     for i, metric in enumerate(EXPECTED_METRICS):
    #         LOG.debug("\t\t4.%s - Searching for %s", i, metric)
    #         found = [ item for item in results if item["metric"] == metric]
    #         self.assertTrue(found)
    #     LOG.debug("\tTest 4: Pass")

    #     LOG.debug("\tTest 5: Verify execution with different parameters")
    #     LOG.debug("\t\tFunction: get_metrics()")
    #     LOG.debug("\t\tArgument: metrics = %s", metrics)
    #     reviewable = True
    #     LOG.debug("\t\tArgument: reviewable = %s", reviewable)
    #     results = CM.get_metrics(metrics=metrics, reviewable=reviewable)
    #     LOG.debug("\tTest 5: Pass")

    def test_get_exchanges(self):
        """
        Determine if `get_assets()`:
        0. works without error,
        1. returns the "data" key,
        2. has a list type for the value of "data",
        3. has a list that is non-zero length,
        4. contains a few expected exchanges, and
        5. endpoint functions with no params.
        """
        LOG.debug("\tTest 0: Determine if function executes without error")
        LOG.debug("\t\tFunction: get_exchanges()")
        exchanges = ",".join(EXPECTED_EXCHANGES)
        LOG.debug("\t\tArgument: exchanges = %s", exchanges)
        results = CM.get_exchanges(exchanges=exchanges)
        LOG.debug("\tTest 0: Pass")

        LOG.debug("\tTest 1: 'data' element in results")
        self.assertTrue('data' in results)
        LOG.debug("\tTest 1: Pass")

        LOG.debug("\tTest 2: Return type == list")
        self.assertIsInstance(results['data'], list)
        LOG.debug("\tTest 2: Pass")

        LOG.debug("\tTest 3: Dict length != 0")
        self.assertTrue(results['data'])
        LOG.debug("\tTest 3: Pass")

        results = results["data"]

        LOG.debug("\tTest 4: Check for some expected assets")
        for i, exchange in enumerate(EXPECTED_EXCHANGES):
            LOG.debug("\t\t4.%s - Searching for %s", i, exchange)
            found = [ item for item in results if item["exchange"] == exchange]
            self.assertTrue(found)
        LOG.debug("\tTest 4: Pass")

        LOG.debug("\tTest 5: Check for some expected assets")
        LOG.debug("\t\tFunction: get_exchanges()")
        LOG.debug("\t\tArgument: None")
        results = CM.get_exchanges()
        LOG.debug("\tTest 5: Pass")



# class BaseAPITests(unittest.TestCase):
#     """
#     Tests for the Coinmetrics Base API
#     """
#     def test_get_assets(self):
        # """
        # Determine if the supported assets are:
        # 1. Returned as a list.
        # 2. Returned as a list of multiple elements (i.e. isn't empty).
        # 3. Retruned containing a few expected results.
        # """
#         LOG.debug("\n\tFunction: get_assets()")
#         LOG.debug("\tArgument(s): None")
#         results = CM.get_assets()

#         LOG.debug("\tTest 1: Return type == list")
#         self.assertTrue(isinstance(results, list))
#         LOG.debug("\tTest 1: Pass")

#         LOG.debug("\tTest 2: Dict length != 0")
#         self.assertTrue(len(results) != 0)
#         LOG.debug("\tTest 2: Pass")

#         LOG.debug("\tTest 3: Sample assets in results")
#         for i, asset in enumerate(SAMPLE_EXPECTED_ASSETS):
#             LOG.debug("\t\t3.%s - Searching for %s", i, asset)
#             found = [ item for item in results if item["asset"] == asset]
#             self.assertTrue(found)
#         LOG.debug("\tTest 3: Pass")


if __name__ == '__main__':
    unittest.main(verbosity=2)
