# -*- coding: utf-8 -*-

"""
Coin Metrics API Pro Module Definitions
"""

import logging
from .base import Base
from .community import Community

class Pro(Community):

	# Due to the conveniance methods, we trigger R0904: too-many-public-methods even though this is desired.
	# pylint: disable=R0904

	def __init__(self, api_key=''):
		"""
		Initialize the Pro API in much the same way as the same way as
		:py:func:`coinmetrics.base.Community.__init__`, except the
		:samp:`api_key` is now required for functionality.

		:param api_key: API key to be used for the Pro API.
		:type api_key: str, optional
		"""
		self.logger = logging.getLogger(__name__)
		self.host_url = "https://api.coinmetrics.io/v2/"
		self.headers = {"api_key": api_key} if api_key != '' else {}

	def get_indexes(self):
		"""
		Fetch list of available assets.

		:return: List of supported indices.
		:rtype: list
		"""
		return self._api_query("indexes")['indexes']

	#: An alias for :py:func:`get_indexes`
	getindexes, indexes = [get_indexes] * 2

	def index_checker(self, indexes):
		"""
		Helper function to determine if the requested index(es) is(are) valid.

		:param metric: Unique ID corresponding to index.
		:type metric: str

		:raises: InvalidMetricError
		"""
		index = index.split(",")
		reference = self.get_indexes()
		for i in index:
			if i in reference:
				pass
			else:
				raise InvalidMetricError("Invalid metrics: '{}'".format(i))

	def get_index_info(self, indexes):
		"""
		Fetch index(es) information. Including applicable assets, firendly
		name and most recent and oldest data timestamps. No specified
		asset will return all available asset info.

		:param assets: Unique ID corresponding to the index's name.
		:type assets: str, optional

		:return: Index(es) information.
		:rtype: list of dict
		"""
		options = {"subset": indexes}
		return self._api_query("index_info", options)['indexesInfo']
	