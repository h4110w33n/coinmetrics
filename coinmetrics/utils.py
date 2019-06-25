# -*- coding: utf-8 -*-

"""
Coin Metrics API Conversion Utilities
"""

class Utils:
	"""
	A few utilities to convert the data gathered from the APIs into more
	useful forms for processing.
	"""

	def pandas(self, object):
		"""
		# TODO: STUB
		Convert an object output from :py:func:`Community.get_metric_data`
		to a Pandas object for further processing.

		:param object: Raw data object to convert to Pandas datagram.
		:type object: dict

		:return: Pandas datagram form of original object.
		:rtype: pandas datagram
		"""

	def normalize(self, object):
		"""
		# TODO: STUB
		Convert an object output from :py:func:`Community.get_metric_data`
		to a standard list of dictionaries for further processing.

		:param object: Raw data object to convert to list of dict.
		:type object: dict

		:return: A normalized list of dictionaries
		:rtype: list
		"""

	def csv(self, object, path):
		"""
		# TODO: STUB
		Convert an object output from :py:func:`Community.get_metric_data`
		to a standard list of dictionaries for further processing.

		:param object: Raw data object to convert to Pandas datagram.
		:type object: dict

		:param path: Location to save the CSV file to.
		:type path: str, optional
		"""