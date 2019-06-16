#!/usr/bin/env python3
"""
Unit Tests for the Coin Metrics API
"""
import random
import time
import unittest
from decimal import Decimal
import logging
import coinmetrics

FORMAT = "%(message)s"
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
logging.getLogger('coinmetrics').setLevel(logging.INFO)
logging.getLogger('coinmetrics.api').setLevel(logging.INFO)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
LOG = logging.getLogger('test')

CM = coinmetrics.Community()

# Global test defaults
ASSET = "btc"
DATA_TYPE = "medianfee"
BEGIN_TIMESTAMP = 1514764800
END_TIMESTAMP = 1515283200
INVALID_ASSET = "asdf"
INVALID_DATA_TYPE = "asdf"
INVALID_BEGIN_TIMESTAMP = 1515283200
INVALID_END_TIMESTAMP = 1514764800

# Tunables
API_WAIT_TIME = 5
RANDOM_TEST_ITERATIONS = 5

class CommunityAPITests(unittest.TestCase):
	"""
	Tests for the Coinmetrics Community API
	"""

	def test_supported_assets(self):
		"""
		Determine if the supported assets listing is what we expect.
		"""
		LOG.debug("\n\tFunction: get_supported_assets()")
		LOG.debug("\tArgument: None")
		expected_result = ['ada', 'ae', 'aion', 'ant', 'bat', 'bch', 'bnb', 'bsv', 'btc', 'btcp', 'btg', 'btm', 'cennz', 'ctxc', 'cvc', 'dai', 'dash', 'dcr', 'dgb', 'doge', 'drgn', 'elf', 'eng', 'eos', 'etc', 'eth', 'ethos', 'fun', 'gas', 'gno', 'gnt', 'gusd', 'icn', 'icx', 'kcs', 'knc', 'loom', 'lrc', 'lsk', 'ltc', 'maid', 'mana', 'mtl', 'nas', 'neo', 'omg', 'pax', 'pay', 'pivx', 'poly', 'powr', 'ppt', 'qash', 'rep', 'rhoc', 'salt', 'snt', 'srn', 'trx', 'tusd', 'usdc', 'usdt', 'ven', 'veri', 'vtc', 'waves', 'wtc', 'xem', 'xlm', 'xmr', 'xrp', 'xvg', 'zec', 'zil', 'zrx']
		self.assertEqual(CM.get_supported_assets(), expected_result)

	def test_get_available_data_types_for_asset(self):
		"""
		Determine if the data types for an assest are what we expect.
		"""
		LOG.debug("\n\tFunction: get_available_data_types_for_asset(ASSET)")
		LOG.debug("\tArgument: ASSET = '%s'", ASSET)
		expected_result = ['activeaddresses', 'adjustedtxvolume(usd)', 'averagedifficulty', 'blockcount', 'blocksize', 'exchangevolume(usd)', 'fees', 'generatedcoins', 'marketcap(usd)', 'medianfee', 'mediantxvalue(usd)', 'paymentcount', 'price(usd)', 'realizedcap(usd)', 'txcount', 'txvolume(usd)']
		self.assertEqual(CM.get_available_data_types_for_asset(ASSET), expected_result)

	def test_get_asset_data_for_time_range(self):
		"""
		Determine if the data retrieved for an asset over a given time range is what we expect.
		"""
		LOG.debug("\n\tFunction: get_asset_data_for_time_range(ASSET, DATA_TYPE, BEGIN_TIMESTAMP, END_TIMESTAMP)")
		LOG.debug("\tArgument: ASSET = '%s'", ASSET)
		LOG.debug("\tArgument: DATA_TYPE = '%s'", DATA_TYPE)
		LOG.debug("\tArgument: BEGIN_TIMESTAMP = '%s'", str(BEGIN_TIMESTAMP))
		LOG.debug("\tArgument: END_TIMESTAMP = '%s'", str(END_TIMESTAMP))
		expected_result = [[Decimal('1514764800'), Decimal('0.0010815')], [Decimal('1514851200'), Decimal('0.0009030700000000001')], [Decimal('1514937600'), Decimal('0.00103344')], [Decimal('1515024000'), Decimal('0.0010427400000000001')], [Decimal('1515110400'), Decimal('0.0010892')], [Decimal('1515196800'), Decimal('0.00104361')], [Decimal('1515283200'), Decimal('0.00114465')]]
		self.assertEqual(CM.get_asset_data_for_time_range(ASSET, DATA_TYPE, BEGIN_TIMESTAMP, END_TIMESTAMP), expected_result)

	def test_random(self):
		"""
		This test simulates plausable use cases for the API, chosen at random. 
		No data validation is performed. Not faulting is the PASS criteria.
		"""
		LOG.debug("\n\tSimulation Testing:")
		for i in range(0, RANDOM_TEST_ITERATIONS):
			LOG.debug("\n\t[%s] Function: get_supported_assets()", i)
			LOG.debug("\t[%s] Argument: None", i)
			supported_assets = CM.get_supported_assets()
			asset = random.choice(supported_assets)
			LOG.debug("\t[%s] Function: get_available_data_types_for_asset(asset)", i)
			LOG.debug("\t[%s] Argument: asset = '%s'", i, asset)
			supported_data_types = CM.get_available_data_types_for_asset(asset)
			data_type = random.choice(supported_data_types)
			LOG.debug("\t[%s] Function: get_asset_data_for_time_range(asset, data_type, BEGIN_TIMESTAMP, END_TIMESTAMP)", i)
			LOG.debug("\t[%s] Argument: asset = '%s'", i, asset)
			LOG.debug("\t[%s] Argument: data_type = '%s'", i, data_type)
			LOG.debug("\t[%s] Argument: BEGIN_TIMESTAMP = '%s'", i, str(BEGIN_TIMESTAMP))
			LOG.debug("\t[%s] Argument: END_TIMESTAMP = '%s'", i, str(END_TIMESTAMP))
			data = CM.get_asset_data_for_time_range(asset, data_type, BEGIN_TIMESTAMP, END_TIMESTAMP)
			self.assertNotEqual(data, None)
			LOG.info("\t[%s] Data retrieved: Case %s PASS", i, i)
			time.sleep(API_WAIT_TIME)

	def test_invalid_asset_error(self):
		"""
		Determine if the InvalidAssetError is correctly raised when we call for a non-existant asset.
		"""
		LOG.debug("\n\tExpecting: 'coinmetrics.api.InvalidAssetError'")
		LOG.debug("\n\t[1]Function: get_available_data_types_for_asset(INVALID_ASSET)")
		LOG.debug("\t[1]Argument: INVALID_ASSET = '%s'", INVALID_ASSET)
		with self.assertRaises(coinmetrics.api.InvalidAssetError):
			CM.get_available_data_types_for_asset(INVALID_ASSET)
		LOG.debug("\t[1]Error raised: Case 1 PASS")

		LOG.debug("\n\t[2]Function: get_asset_data_for_time_range(INVALID_ASSET, DATA_TYPE, BEGIN_TIMESTAMP, END_TIMESTAMP)")
		LOG.debug("\t[2]Argument: INVALID_ASSET = '%s'", INVALID_ASSET)
		LOG.debug("\t[2]Argument: DATA_TYPE = '%s'", DATA_TYPE)
		LOG.debug("\t[2]Argument: BEGIN_TIMESTAMP = '%s'", str(BEGIN_TIMESTAMP))
		LOG.debug("\t[2]Argument: END_TIMESTAMP = '%s'", str(END_TIMESTAMP))
		with self.assertRaises(coinmetrics.api.InvalidAssetError):
			CM.get_asset_data_for_time_range(INVALID_ASSET, DATA_TYPE, BEGIN_TIMESTAMP, END_TIMESTAMP)
		LOG.debug("\t[2]Error raised: Case 2 PASS")

	def test_invalid_data_type_error(self):
		"""
		Determine if the InvalidDataTypeError is correctly raised when we call for a non-existant data_type.
		"""
		LOG.debug("\n\tFunction: get_asset_data_for_time_range(ASSET, INVALID_DATA_TYPE, BEGIN_TIMESTAMP, END_TIMESTAMP)")
		LOG.debug("\tArgument: ASSET = '%s'", ASSET)
		LOG.debug("\tArgument: INVALID_DATA_TYPE = '%s'", INVALID_DATA_TYPE)
		LOG.debug("\tArgument: BEGIN_TIMESTAMP = '%s'", str(BEGIN_TIMESTAMP))
		LOG.debug("\tArgument: END_TIMESTAMP = '%s'", str(END_TIMESTAMP))
		with self.assertRaises(coinmetrics.api.InvalidDataTypeError):
			CM.get_asset_data_for_time_range(ASSET, INVALID_DATA_TYPE, BEGIN_TIMESTAMP, END_TIMESTAMP)
		LOG.debug("\tError raised: PASS")

	def test_invalid_time_range_error(self):
		"""
		Determine if the InvalidTimeRangeError is correctly raised when we call for a non-existant data_type.
		"""
		LOG.debug("\n\tFunction: get_asset_data_for_time_range(ASSET, DATA_TYPE, INVALID_BEGIN_TIMESTAMP, INVALID_END_TIMESTAMP)")
		LOG.debug("\tArgument: ASSET = '%s'", ASSET)
		LOG.debug("\tArgument: DATA_TYPE = '%s'", DATA_TYPE)
		LOG.debug("\tArgument: INVALID_BEGIN_TIMESTAMP = '%s'", str(INVALID_BEGIN_TIMESTAMP))
		LOG.debug("\tArgument: INVALID_END_TIMESTAMP = '%s'", str(INVALID_END_TIMESTAMP))
		with self.assertRaises(coinmetrics.api.InvalidTimeRangeError):
			CM.get_asset_data_for_time_range(ASSET, DATA_TYPE, INVALID_BEGIN_TIMESTAMP, INVALID_END_TIMESTAMP)
		LOG.debug("\tError raised: PASS")

if __name__ == '__main__':
	unittest.main(verbosity=2)
