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

CM = coinmetrics.Community()

class BaseAPITests(unittest.TestCase):
	"""
	Tests for the Coinmetrics Base API
	"""
	def test_get_assets(self):
		"""
		Determine if the supported assets listing is what we expect.
		"""
		LOG.debug("\n\tFunction: get_assets()")
		LOG.debug("\tArgument: None")
		results = CM.get_assets()
		sample_expected_assets = ['bch', 'bnb', 'btc', 'dash', 'doge', 'eth', 'ltc', 'neo', 'xrp']
		for asset in sample_expected_assets:
			self.assertTrue(asset in results)

	def test_get_metrics(self):
		"""
		Determine if the supported metrics listing is what we expect.
		"""
		LOG.debug("\n\tFunction: get_metrics()")
		LOG.debug("\tArgument: None")
		sample_expected_metrics = ['AdrActCnt', 'BlkCnt', 'BlkSizeByte', 'BlkSizeMeanByte', 'CapMVRVCur', 'CapMrktCurUSD', 'CapRealUSD', 'DiffMean', 'FeeMeanNtv', 'FeeMeanUSD', 'FeeMedNtv', 'FeeMedUSD', 'FeeTotNtv', 'FeeTotUSD', 'IssContNtv', 'IssContPctAnn', 'IssContUSD', 'IssTotNtv', 'IssTotUSD', 'NVTAdj', 'NVTAdj90', 'PriceBTC', 'PriceUSD', 'ROI1yr', 'ROI30d', 'SplyCur', 'TxCnt', 'TxTfr', 'TxTfrValAdjNtv', 'TxTfrValAdjUSD', 'TxTfrValMeanNtv', 'TxTfrValMeanUSD', 'TxTfrValMedNtv', 'TxTfrValMedUSD', 'TxTfrValNtv', 'TxTfrValUSD', 'VtyDayRet180d', 'VtyDayRet30d', 'VtyDayRet60d']
		results = CM.get_metrics()
		for metric in sample_expected_metrics:
			self.assertTrue(metric in results)

	def test_get_exchanges(self):
		"""
		Determine if the supported exchanges listing is what we expect.
		"""
		LOG.debug("\n\tFunction: get_exchanges()")
		LOG.debug("\tArgument: None")
		sample_expected_exchanges = ['bitfinex', 'bitstamp', 'bittrex', 'coinbase', 'gemini', 'itbit', 'kraken', 'liquid']
		results = CM.get_exchanges()		
		for exchange in sample_expected_exchanges:
			self.assertTrue(exchange in results)		

	def test_get_markets(self):
		"""
		Determine if the supported markets listing is what we expect.
		"""
		LOG.debug("\n\tFunction: get_markets()")
		LOG.debug("\tArgument: None")
		sample_expected_markets = ['bitfinex-btc-usd-spot', 'bitfinex-eth-usd-spot', 'bitstamp-btc-usd-spot', 'bitstamp-eth-usd-spot', 'bittrex-btc-usd-spot', 'bittrex-eth-usd-spot', 'coinbase-btc-usd-spot', 'coinbase-eth-usd-spot', 'gemini-btc-usd-spot', 'gemini-eth-usd-spot', 'itbit-btc-usd-spot', 'itbit-eth-usd-spot', 'kraken-btc-usd-spot', 'kraken-eth-usd-spot', 'liquid-btc-usd-spot', 'liquid-eth-usd-spot']
		results = CM.get_markets()
		for market in sample_expected_markets:
			self.assertTrue(market in results)

	def test_asset_checker(self):
		"""
		Raise the correct error for an invalid asset.
		"""
		LOG.debug("\n\tFunction: asset_checker()")
		LOG.debug("\tArgument: asset = '%s'", INVALID_ASSET)
		with self.assertRaises(coinmetrics.errors.InvalidAssetError):
			CM.asset_checker(INVALID_ASSET)
		LOG.debug("\tError raised: Case PASS")

	def test_metric_checker(self):
		"""
		Raise the correct error for an invalid metric.
		"""
		LOG.debug("\n\tFunction: metric_checker()")
		LOG.debug("\tArgument: metric = '%s'", INVALID_METRIC)
		with self.assertRaises(coinmetrics.errors.InvalidMetricError):
			CM.metric_checker(INVALID_METRIC)
		LOG.debug("\tError raised: Case PASS")

	def test_market_checker(self):
		"""
		Raise the correct error for an invalid market.
		"""
		LOG.debug("\n\tFunction: market_checker()")
		LOG.debug("\tArgument: market = '%s'", INVALID_MARKET)
		with self.assertRaises(coinmetrics.errors.InvalidMetricError):
			CM.metric_checker(INVALID_MARKET)
		LOG.debug("\tError raised: Case PASS")

	def test_exchange_checker(self):
		"""
		Raise the correct error for an invalid exchange.
		"""
		LOG.debug("\n\tFunction: exchange_checker()")
		LOG.debug("\tArgument: exchange = '%s'", INVALID_EXCHANGE)
		with self.assertRaises(coinmetrics.errors.InvalidExchangeError):
			CM.exchange_checker(INVALID_EXCHANGE)
		LOG.debug("\tError raised: Case PASS")

	def test_timestamp_checker(self):
		"""
		Raise the correct error for an invalid time rance.
		"""
		LOG.debug("\n\tFunction: exchange_checker()")
		LOG.debug("\tArgument: begin = '%s', end = '%s'", INVALID_BEGIN_TIMESTAMP, INVALID_END_TIMESTAMP)
		with self.assertRaises(coinmetrics.errors.InvalidTimeRangeError):
			CM.timestamp_checker(INVALID_BEGIN_TIMESTAMP, INVALID_END_TIMESTAMP)
		LOG.debug("\tError raised: Case PASS")

class CommunityAPITests(unittest.TestCase):
	"""
	Tests for the Coinmetrics Base API
	"""
	def test_get_asset_info(self):
		"""
		Test fetching asset information.
		"""
		LOG.debug("\n\tFunction: get_asset_info()")
		LOG.debug("\tArgument: asset = '%s'", ASSET)
		results = CM.get_asset_info(ASSET)
		self.assertTrue('exchanges' in results[0])
		self.assertTrue('markets' in results[0])
		self.assertTrue('metrics' in results[0])
		sample_expected_exchanges = ['bitfinex', 'coinbase', 'bittrex']
		for exchange in sample_expected_exchanges:
			self.assertTrue(exchange in results[0]['exchanges'])
		sample_expected_markets = ['binance-eth-btc-spot', 'bittrex-ltc-btc-spot', 'poloniex-xrp-btc-spot']
		for market in sample_expected_markets:
			self.assertTrue(market in results[0]['markets'])
		sample_expected_metrics = ['BlkCnt', 'NVTAdj', 'PriceUSD']
		for metric in sample_expected_metrics:
			self.assertTrue(metric in results[0]['metrics'])

	def test_get_exchange_info(self):
		"""
		Test exchange asset information.
		"""
		LOG.debug("\n\tFunction: get_exchange_info()")
		LOG.debug("\tArgument: exchange = '%s'", EXCHANGE)
		results = CM.get_exchange_info(EXCHANGE)
		self.assertTrue('marketsInfo' in results[0])
		sample_expected_metric_info = {'assetIdBase': 'btc', 'assetIdQuote': 'usd', 'id': 'coinbase-btc-usd-spot', 'maxTime': None, 'minTime': None}
		self.assertTrue(sample_expected_metric_info in results[0]['marketsInfo'])

	def test_get_metric_info(self):
		"""
		Test metric asset information.
		"""
		LOG.debug("\n\tFunction: get_metric_info()")
		LOG.debug("\tArgument: metric = '%s'", METRIC)
		results = CM.get_metric_info(METRIC)
		self.assertTrue('id' in results[0])
		self.assertTrue('category' in results[0])
		self.assertTrue('subcategory' in results[0])
		self.assertTrue('PriceUSD' in results[0]['id'])
		self.assertTrue('Market' in results[0]['category'])
		self.assertTrue('Price' in results[0]['subcategory'])

	def test_get_market_info(self):
		"""
		Test market asset information.
		"""
		LOG.debug("\n\tFunction: get_market_info()")
		LOG.debug("\tArgument: market = '%s'", MARKET)
		results = CM.get_market_info(MARKET)
		self.assertTrue('assetIdBase' in results[0])
		self.assertTrue('assetIdQuote' in results[0])
		self.assertTrue('id' in results[0])
		self.assertTrue('eth' in results[0]['assetIdBase'])
		self.assertTrue('usd' in results[0]['assetIdQuote'])
		self.assertTrue('kraken-eth-usd-spot' in results[0]['id'])

	def test_get_asset_metrics(self):
		"""
		Test market asset to metric information.
		"""
		LOG.debug("\n\tFunction: get_asset_metrics()")
		LOG.debug("\tArgument: asset = '%s'", ASSET)
		expected_result = ['AdrActCnt', 'BlkCnt', 'BlkSizeByte', 'BlkSizeMeanByte', 'CapMVRVCur', 'CapMrktCurUSD', 'CapRealUSD', 'DiffMean', 'FeeMeanNtv', 'FeeMeanUSD', 'FeeMedNtv', 'FeeMedUSD', 'FeeTotNtv', 'FeeTotUSD', 'IssContNtv', 'IssContPctAnn', 'IssContUSD', 'IssTotNtv', 'IssTotUSD', 'NVTAdj', 'NVTAdj90', 'PriceBTC', 'PriceUSD', 'ROI1yr', 'ROI30d', 'SplyCur', 'TxCnt', 'TxTfr', 'TxTfrValAdjNtv', 'TxTfrValAdjUSD', 'TxTfrValMeanNtv', 'TxTfrValMeanUSD', 'TxTfrValMedNtv', 'TxTfrValMedUSD', 'TxTfrValNtv', 'TxTfrValUSD', 'VtyDayRet180d', 'VtyDayRet30d', 'VtyDayRet60d']
		self.assertEqual(CM.get_asset_metrics(ASSET), expected_result)

	def test_asset_metric_checker(self):
		"""
		Test if the metric(s) exist for a asset.
		"""
		LOG.debug("\n\tFunction: asset_metric_checker()")
		LOG.debug("\tArgument: asset = '%s'", ASSET)
		LOG.debug("\tArgument: metric = '%s'", METRIC)
		with self.assertRaises(coinmetrics.errors.InvalidMetricError):
			CM.asset_metric_checker(ASSET, INVALID_METRIC)
		LOG.debug("\tError raised: Case PASS")

	def test_get_asset_metric_data(self):
		"""
		Test fetching metric data.
		"""
		LOG.debug("\n\tFunction: get_asset_metric_data()")
		LOG.debug("\tArgument: asset = '%s'", ASSET)
		LOG.debug("\tArgument: metric = '%s'", METRIC)
		LOG.debug("\tArgument: start = '%s'", BEGIN_TIMESTAMP)
		LOG.debug("\tArgument: end = '%s'", END_TIMESTAMP)
		results = CM.get_asset_metric_data(ASSET, METRIC, BEGIN_TIMESTAMP, END_TIMESTAMP)
		self.assertTrue('metrics' in results)
		self.assertTrue('series' in results)
		self.assertTrue('PriceUSD' in results['metrics'])
		sample_expected_series = {'time': '2019-01-01T00:00:00.000Z', 'values': ['3873.6838767067']}
		self.assertTrue(sample_expected_series in results['series'])

if __name__ == '__main__':
	unittest.main(verbosity=2)
