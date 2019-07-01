"""
Coin Metrics API Error Module Definitions
"""

# We do not call these errors from this file, so we should ignore the lint error for it here.
# pylint: disable=W0611

class Error(Exception):
    """
    Base class for other exceptions.
    """

class InvalidAssetError(Error):
    """
    Raise an error when the given asset doesn't exist.
    """

class InvalidTimeRangeError(Error):
    """
    Raise and error when the given time range is not-sane (i.e. end before start).
    """

class InvalidMetricError(Error):
    """
    Raise and error when the given metric doesn't exist for the specified asset.
    """

class InvalidExchangeError(Error):
    """
    Raise and error when the given metric doesn't exist for the specified asset.
    """

class InvalidMarketError(Error):
    """
    Raise and error when the given metric doesn't exist for the specified asset.
    """

class InvalidDataTypeError(Error):
    """
    Raise and error when the given data_type doesn't exist for the specified asset.
    """
