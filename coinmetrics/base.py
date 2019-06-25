# -*- coding: utf-8 -*-

"""
Coin Metrics API Base Module Definitions
"""

from decimal import Decimal
import json
import logging
import requests
import urllib.parse
from dateutil import parser
from .errors import (
	Error,
	InvalidAssetError,
	InvalidTimeRangeError,
	InvalidMetricError,
	InvalidExchangeError,
	InvalidMarketError,
)

class Base:
	
	def __init__(self, api_key=""):
		"""
		Initialize API to use the Community API endpoints by default.
		An optional :samp:`api_key` can be supplied.
		
		:param api_key: API key to be used for the Pro API.
		:type api_key: str, optional
		"""
		self.logger = logging.getLogger(__name__)
		self.host_url = 'https://community-api.coinmetrics.io/v2/'
		self.headers = {"api_key": api_key} if api_key != '' else {}

	def _api_query(self, endpoint, options={}):
		"""
		Execute the raw API query and return the raw JSON output.

		:param endpoint: URL Path the query will be sent to. This includes any
						 URL based parameters.
		:type endpoint: string

		:param options: Query parameters, including asset(s), metric(s), 
						exchanges(s), and time range.
		:type options: dict, optional

		:return: Raw JSON response as dict.
		:rtype: dict
		"""
		self.logger.debug("Host URL: '%s'", self.host_url)
		self.logger.debug("Endpoint: '%s'", endpoint)
		self.logger.debug("Options: '%s'", str(options))
		self.logger.debug("Headers: '%s'", str(self.headers))
		encoded_options = urllib.parse.urlencode(options)
		request_url = self.host_url + endpoint + '?' + encoded_options
		self.logger.debug("Request URL: '%s'", str(request_url))
		response = requests.get(request_url, headers=self.headers).content.decode('utf-8')
		return json.loads(response, parse_float=Decimal, parse_int=Decimal)

	def get_assets(self):
		"""
		Fetch list of available assets.

		:return: List of supported assets.
		:rtype: list
		"""
		return self._api_query("assets")["assets"]

	#: An alias for :py:func:`get_assets`
	get_supported_assets, assets = [get_assets] * 2

	def asset_checker(self, asset):
		"""
		Helper function to determine if the requested asset(s) is(are) valid.

		:param asset: Unique ID corresponding to the asset's ticker.
		:type asset: str
		
		:raises: InvalidAssetError
		"""
		asset = asset.split(",")
		reference = self.get_assets()
		for a in asset:
			if a in reference:
				pass
			else:
				raise InvalidAssetError("Invalid asset: '{}'".format(a))

	def get_metrics(self):
		"""
		Fetch list of available metrics.

		:return: List of supported metrics.
		:rtype: list
		"""
		return self._api_query("metrics")['metrics']

	#: An alias for :py:func:`get_metrics`
	getmetrics, metrics = [get_metrics] * 2

	def metric_checker(self, metric):
		"""
		Helper function to determine if the requested metric(s) is(are) valid.

		:param metric: Unique ID corresponding to metric.
		:type metric: str

		:raises: InvalidMetricError
		"""
		metric = metric.split(",")
		reference = self.get_metrics()
		for m in metric:
			if m in reference:
				pass
			else:
				raise InvalidMetricError("Invalid metrics: '{}'".format(m))

	def get_exchanges(self):
		"""
		Fetch list of available exchanges.

		:return: List of supported exchanges.
		:rtype: list
		"""
		return self._api_query("exchanges")['exchanges']

	#: An alias for :py:func:`get_exchanges`
	getexchanges, exchange = [get_exchanges] * 2

	def exchange_checker(self, exchange):
		"""
		Helper function to determine if the requested exchange(s) is(are) valid.

		:param exchange: Unique ID corresponding to the exchange.
		:type exchange: str

		:raises: InvalidExchangeError
		"""
		exchange = exchange.split(",")
		reference = self.get_exchanges()
		for e in exchange:
			if e in reference:
				pass
			else:
				raise InvalidExchangeError("Invalid exchange: '{}'".format(e))

	def get_markets(self):
		"""
		Fetch list of available markets.

		:return: List of supported markets.
		:rtype: list
		"""
		return self._api_query("markets")['markets']

	#: An alias for :py:func:`get_markets`
	getmarkets, markets = [get_markets] * 2

	def market_checker(self, market):
		"""
		Helper function to determine if the requested market(s) is(are) valid.

		:param market: Unique ID corresponding to the market.
		:type market: str

		:raises: InvalidMarketError
		"""
		market = market.split(",")
		reference = self.get_markets()
		for m in market:
			if m in reference:
				pass
			else:
				raise InvalidMarketError("Invalid market: '{}'".format(m))

	def timestamp_checker(self, begin_timestamp, end_timestamp):
		"""
		Helper function to determine if the provided timerange is valid.

		:param begin_timestamp: Start of time inverval.
		:type begin_timestamp: str or datetime

		:param end_timestamp: End of time inverval.
		:type end_timestamp: str or datetime

		:raises: InvalidTimeRangeError
		"""
		# TODO: There is a beginning and end time in one of the info functions.
		self.logger.debug("Begin Timestamp: '%s'", begin_timestamp)
		self.logger.debug("End Timestamp: '%s'", end_timestamp)
		begin_timestamp = parser.parse(str(begin_timestamp))
		end_timestamp = parser.parse(str(end_timestamp))
		if begin_timestamp <= end_timestamp:
			pass
		else:
			raise InvalidTimeRangeError("Invalid time range starting: '{}', and ending: '{}'.".format(begin_timestamp, end_timestamp))
