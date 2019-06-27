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
		expected_result = ['ada', 'ae', 'aion', 'ant', 'bat', 'bch', 'bnb', 'bnb_mainnet', 'bsv', 'btc', 'btg', 'btm', 'cvc', 'dai', 'dash', 'dcr', 'dgb', 'doge', 'drgn', 'elf', 'eng', 'eos', 'etc', 'eth', 'ethos', 'fun', 'gas', 'gno', 'gnt', 'grin', 'gusd', 'icx', 'kcs', 'knc', 'loom', 'lrc', 'lsk', 'ltc', 'maid', 'mana', 'mkr', 'nas', 'neo', 'omg', 'pax', 'pay', 'pivx', 'poly', 'powr', 'ppt', 'qash', 'qtum', 'rep', 'snt', 'trx', 'tusd', 'usdc', 'usdt', 'usdt_eth', 'vet', 'vtc', 'waves', 'wtc', 'xem', 'xlm', 'xmr', 'xrp', 'xtz', 'xvg', 'zec', 'zil', 'zrx']
		self.assertEqual(CM.get_assets(), expected_result)

	def test_get_metrics(self):
		"""
		Determine if the supported metrics listing is what we expect.
		"""
		LOG.debug("\n\tFunction: get_metrics()")
		LOG.debug("\tArgument: None")
		expected_result = ['AdrActCnt', 'BlkCnt', 'BlkSizeByte', 'BlkSizeMeanByte', 'CapMVRVCur', 'CapMrktCurUSD', 'CapRealUSD', 'DiffMean', 'FeeMeanNtv', 'FeeMeanUSD', 'FeeMedNtv', 'FeeMedUSD', 'FeeTotNtv', 'FeeTotUSD', 'IssContNtv', 'IssContPctAnn', 'IssContUSD', 'IssTotNtv', 'IssTotUSD', 'NVTAdj', 'NVTAdj90', 'PriceBTC', 'PriceUSD', 'ROI1yr', 'ROI30d', 'SplyCur', 'TxCnt', 'TxTfr', 'TxTfrValAdjNtv', 'TxTfrValAdjUSD', 'TxTfrValMeanNtv', 'TxTfrValMeanUSD', 'TxTfrValMedNtv', 'TxTfrValMedUSD', 'TxTfrValNtv', 'TxTfrValUSD', 'VtyDayRet180d', 'VtyDayRet30d', 'VtyDayRet60d']
		self.assertEqual(CM.get_metrics(), expected_result)

	def test_get_exchanges(self):
		"""
		Determine if the supported exchanges listing is what we expect.
		"""
		LOG.debug("\n\tFunction: get_exchanges()")
		LOG.debug("\tArgument: None")
		expected_result = ['bitfinex', 'bitstamp', 'bittrex', 'coinbase', 'gemini', 'itbit', 'kraken', 'liquid']
		self.assertEqual(CM.get_exchanges(), expected_result)

	def test_get_markets(self):
		"""
		Determine if the supported markets listing is what we expect.
		"""
		LOG.debug("\n\tFunction: get_markets()")
		LOG.debug("\tArgument: None")
		expected_result = ['bitfinex-btc-usd-spot', 'bitfinex-eth-usd-spot', 'bitstamp-btc-usd-spot', 'bitstamp-eth-usd-spot', 'bittrex-btc-usd-spot', 'bittrex-eth-usd-spot', 'coinbase-btc-usd-spot', 'coinbase-eth-usd-spot', 'gemini-btc-usd-spot', 'gemini-eth-usd-spot', 'itbit-btc-usd-spot', 'itbit-eth-usd-spot', 'kraken-btc-usd-spot', 'kraken-eth-usd-spot', 'liquid-btc-usd-spot', 'liquid-eth-usd-spot']
		self.assertEqual(CM.get_markets(), expected_result)

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
		expected_exchanges = ['bitfinex', 'bitstamp', 'bittrex', 'coinbase', 'gemini', 'itbit', 'kraken', 'liquid']
		expected_markets = ['bitfinex-btc-usd-spot', 'bitstamp-btc-usd-spot', 'bittrex-btc-usd-spot', 'coinbase-btc-usd-spot', 'gemini-btc-usd-spot', 'itbit-btc-usd-spot', 'kraken-btc-usd-spot', 'liquid-btc-usd-spot']
		expected_metrics = ['AdrActCnt', 'BlkCnt', 'BlkSizeByte', 'BlkSizeMeanByte', 'CapMVRVCur', 'CapMrktCurUSD', 'CapRealUSD', 'DiffMean', 'FeeMeanNtv', 'FeeMeanUSD', 'FeeMedNtv', 'FeeMedUSD', 'FeeTotNtv', 'FeeTotUSD', 'IssContNtv', 'IssContPctAnn', 'IssContUSD', 'IssTotNtv', 'IssTotUSD', 'NVTAdj', 'NVTAdj90', 'PriceBTC', 'PriceUSD', 'ROI1yr', 'ROI30d', 'SplyCur', 'TxCnt', 'TxTfr', 'TxTfrValAdjNtv', 'TxTfrValAdjUSD', 'TxTfrValMeanNtv', 'TxTfrValMeanUSD', 'TxTfrValMedNtv', 'TxTfrValMedUSD', 'TxTfrValNtv', 'TxTfrValUSD', 'VtyDayRet180d', 'VtyDayRet30d', 'VtyDayRet60d']
		self.assertEqual(results[0]['exchanges'], expected_exchanges)
		self.assertEqual(results[0]['markets'], expected_markets)
		self.assertEqual(results[0]['metrics'], expected_metrics)

	def test_get_exchange_info(self):
		"""
		Test exchange asset information.
		"""
		LOG.debug("\n\tFunction: get_exchange_info()")
		LOG.debug("\tArgument: exchange = '%s'", EXCHANGE)
		expected_result = [{'id': 'coinbase', 'marketsInfo': [{'id': 'coinbase-btc-usd-spot', 'assetIdBase': 'btc', 'assetIdQuote': 'usd', 'minTime': None, 'maxTime': None}, {'id': 'coinbase-eth-usd-spot', 'assetIdBase': 'eth', 'assetIdQuote': 'usd', 'minTime': None, 'maxTime': None}]}]
		self.assertEqual(CM.get_exchange_info(EXCHANGE), expected_result)

	def test_get_metric_info(self):
		"""
		Test metric asset information.
		"""
		LOG.debug("\n\tFunction: get_metric_info()")
		LOG.debug("\tArgument: metric = '%s'", METRIC)
		expected_result = [{'id': 'PriceUSD', 'name': 'Price, USD', 'description': "The fixed closing price of the asset as of 00:00 UTC the following day (i.e., midnight UTC of the current day) denominated in USD. This price is generated by Coin Metrics' fixing/reference rate service. ", 'category': 'Market', 'subcategory': 'Price'}]
		self.assertEqual(CM.get_metric_info(METRIC), expected_result)

	def test_get_market_info(self):
		"""
		Test market asset information.
		"""
		LOG.debug("\n\tFunction: get_market_info()")
		LOG.debug("\tArgument: market = '%s'", MARKET)
		expected_result = [{'id': 'kraken-eth-usd-spot', 'assetIdBase': 'eth', 'assetIdQuote': 'usd', 'minTime': None, 'maxTime': None}]
		self.assertEqual(CM.get_market_info(MARKET), expected_result)

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
		expected_result = {'metrics': ['PriceUSD'], 'series': [{'time': '2019-01-01T00:00:00.000Z', 'values': ['3808.11783167738']}, {'time': '2019-01-02T00:00:00.000Z', 'values': ['3898.1974880187']}, {'time': '2019-01-03T00:00:00.000Z', 'values': ['3784.38863471654']}, {'time': '2019-01-04T00:00:00.000Z', 'values': ['3827.52459438925']}, {'time': '2019-01-05T00:00:00.000Z', 'values': ['3798.61395499708']}, {'time': '2019-01-06T00:00:00.000Z', 'values': ['4045.99377498539']}, {'time': '2019-01-07T00:00:00.000Z', 'values': ['4001.01827819988']}, {'time': '2019-01-08T00:00:00.000Z', 'values': ['3992.6227893045']}]}
		self.assertEqual(CM.get_asset_metric_data(ASSET, METRIC, BEGIN_TIMESTAMP, END_TIMESTAMP), expected_result)

if __name__ == '__main__':
	unittest.main(verbosity=2)













