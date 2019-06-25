# -*- coding: utf-8 -*-

"""
Coin Metrics API Pro Module Definitions
"""

import logging
from .base import Base
from .community import Community

class Pro(Community):
	"""
	TODO: Redoc this.
	Where pro-only APIs go, best effort for now.
	"""

	def __init__(self, api_key=''):
		self.logger = logging.getLogger(__name__)
		# self.host_url = "https://api.coinmetrics.io/v2/"
		self.host_url = 'https://community-api.coinmetrics.io/v2/'
		self.headers = {"api_key": api_key} if api_key != '' else {}

	def get_indexes(self):
		return self._api_query("indexes")

	def get_index_info(self, indexes):
		options = {"subset": indexes}
		return self._api_query("index_info", options)