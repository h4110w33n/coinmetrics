#!/usr/bin/env python3
"""
Unit Tests for the Coin Metrics API
"""
import random
import time
import unittest
import logging
import coinmetrics

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
EXCHANGE = "bitfinex"
METRIC = "PriceUSD"
BEGIN_TIMESTAMP = "2019-01-01"
END_TIMESTAMP = "2019-02-01"

INVALID_ASSET = "invalid_asset"
INVALID_MARKET = "invalid_market"
INVALID_EXCHANGE = "invalid_exchange"
INVALID_METRIC = "invalid_metric"
INVALID_BEGIN_TIMESTAMP = "2019-02-01"
INVALID_END_TIMESTAMP = "2019-01-01"

# Tunables
API_WAIT_TIME = 5
RANDOM_TEST_ITERATIONS = 5

CM = coinmetrics.Community()

class CommunityAPITests(unittest.TestCase):
	"""
	Tests for the Coinmetrics Community API
	"""

	# def test_get_assets(self):
	# 	"""
	# 	Determine if the supported assets listing is what we expect.
	# 	"""
	# 	LOG.debug("\n\tFunction: get_assets()")
	# 	LOG.debug("\tArgument: None")
	# 	expected_result = ['ada', 'ae', 'aion', 'ant', 'bat', 'bch', 'bnb', 'bnb_mainnet', 'bsv', 'btc', 'btg', 'btm', 'cvc', 'dai', 'dash', 'dcr', 'dgb', 'doge', 'drgn', 'elf', 'eng', 'eos', 'etc', 'eth', 'ethos', 'fun', 'gas', 'gno', 'gnt', 'grin', 'gusd', 'icx', 'kcs', 'knc', 'loom', 'lrc', 'lsk', 'ltc', 'maid', 'mana', 'mkr', 'nas', 'neo', 'omg', 'pax', 'pay', 'pivx', 'poly', 'powr', 'ppt', 'qash', 'qtum', 'rep', 'snt', 'trx', 'tusd', 'usdc', 'usdt', 'usdt_eth', 'vet', 'vtc', 'waves', 'wtc', 'xem', 'xlm', 'xmr', 'xrp', 'xtz', 'xvg', 'zec', 'zil', 'zrx']
	# 	self.assertEqual(CM.get_assets(), expected_result)

	# def test_get_metrics(self):
	# 	"""
	# 	Determine if the supported assets listing is what we expect.
	# 	"""
	# 	LOG.debug("\n\tFunction: get_metrics()")
	# 	LOG.debug("\tArgument: None")
	# 	expected_result = ['AdrActCnt', 'BlkCnt', 'BlkSizeByte', 'BlkSizeMeanByte', 'CapMVRVCur', 'CapMrktCurUSD', 'CapRealUSD', 'DiffMean', 'FeeMeanNtv', 'FeeMeanUSD', 'FeeMedUSD', 'FeeTotUSD', 'IssContNtv', 'IssContPctAnn', 'IssContUSD', 'IssTotUSD', 'NVTAdj', 'NVTAdj90', 'PriceBTC', 'PriceUSD', 'ROI1yr', 'ROI30d', 'SplyCur', 'TxCnt', 'TxTfr', 'TxTfrValAdjNtv', 'TxTfrValAdjUSD', 'TxTfrValMeanNtv', 'TxTfrValMeanUSD', 'TxTfrValMedNtv', 'TxTfrValMedUSD', 'TxTfrValNtv', 'TxTfrValUSD', 'VtyDayRet180d', 'VtyDayRet30d', 'VtyDayRet60d']
	# 	self.assertEqual(CM.get_metrics(), expected_result)

	# def test_get_exchanges(self):
	# 	"""
	# 	Determine if the supported assets listing is what we expect.
	# 	"""
	# 	LOG.debug("\n\tFunction: get_exchanges()")
	# 	LOG.debug("\tArgument: None")
	# 	expected_result = ['bitfinex', 'bitstamp', 'bittrex', 'coinbase', 'gemini', 'itbit', 'kraken', 'liquid']
	# 	self.assertEqual(CM.get_exchanges(), expected_result)

	# def test_get_markets(self):
	# 	"""
	# 	Determine if the supported assets listing is what we expect.
	# 	"""
	# 	LOG.debug("\n\tFunction: get_markets()")
	# 	LOG.debug("\tArgument: None")
	# 	expected_result = ['bitfinex-btc-usd-spot', 'bitfinex-eth-usd-spot', 'bitstamp-btc-usd-spot', 'bitstamp-eth-usd-spot', 'bittrex-btc-usd-spot', 'bittrex-eth-usd-spot', 'coinbase-btc-usd-spot', 'coinbase-eth-usd-spot', 'gemini-btc-usd-spot', 'gemini-eth-usd-spot', 'itbit-btc-usd-spot', 'itbit-eth-usd-spot', 'kraken-btc-usd-spot', 'kraken-eth-usd-spot', 'liquid-btc-usd-spot', 'liquid-eth-usd-spot']
	# 	self.assertEqual(CM.get_markets(), expected_result)

	# def test_asset_checker(self):
	# 	LOG.debug("\n\tFunction: asset_checker()")
	# 	LOG.debug("\tArgument: asset = '%s'", INVALID_ASSET)
	# 	with self.assertRaises(coinmetrics.errors.InvalidAssetError):
	# 		CM.asset_checker(INVALID_ASSET)
	# 	LOG.debug("\tError raised: Case PASS")

	# def test_metric_checker(self):
	# 	LOG.debug("\n\tFunction: metric_checker()")
	# 	LOG.debug("\tArgument: metric = '%s'", INVALID_METRIC)
	# 	with self.assertRaises(coinmetrics.errors.InvalidMetricError):
	# 		CM.metric_checker(INVALID_METRIC)
	# 	LOG.debug("\tError raised: Case PASS")

	# def test_exchange_checker(self):
	# 	LOG.debug("\n\tFunction: exchange_checker()")
	# 	LOG.debug("\tArgument: exchange = '%s'", INVALID_EXCHANGE)
	# 	with self.assertRaises(coinmetrics.errors.InvalidExchangeError):
	# 		CM.exchange_checker(INVALID_EXCHANGE)
	# 	LOG.debug("\tError raised: Case PASS")

	# def test_timestamp_checker(self):
	# 	LOG.debug("\n\tFunction: exchange_checker()")
	# 	LOG.debug("\tArgument: begin = '%s', end = '%s'", INVALID_BEGIN_TIMESTAMP, INVALID_END_TIMESTAMP)
	# 	with self.assertRaises(coinmetrics.errors.InvalidTimeRangeError):
	# 		CM.timestamp_checker(INVALID_BEGIN_TIMESTAMP, INVALID_END_TIMESTAMP)
	# 	LOG.debug("\tError raised: Case PASS")

if __name__ == '__main__':
	unittest.main(verbosity=2)













