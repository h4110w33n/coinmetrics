"""
Coin Metrics API Base Module Definitions
"""

from decimal import Decimal
import json
import logging
import urllib.parse
import requests
from dateutil import parser

class Base:
    """
    Coin Metrics API Base Object
    """
    def __init__(self, api_key=""):
        """
        Initialize API to use the Base API endpoints by default.
        An optional :samp:`api_key` can be supplied.

        :param api_key: API key to be used for the Pro API.
        :type api_key: str, optional
        """
        self.logger = logging.getLogger(__name__)
        if api_key:
            self.host_url = 'https://api.coinmetrics.io/v4/'
        else:
            self.host_url = 'https://community-api.coinmetrics.io/v4/'
        self.headers = {"api_key": api_key} if api_key != '' else {}

    def _api_query(self, endpoint, options=None):
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
        encoded_options = urllib.parse.urlencode(options if options is not None else {})
        request_url = self.host_url + endpoint + '?' + encoded_options
        self.logger.debug("Request URL: '%s'", str(request_url))
        response = requests.get(request_url, headers=self.headers).content.decode('utf-8')
        self.logger.debug("API query sent.")
        parsed_response = json.loads(response, parse_float=Decimal, parse_int=Decimal)
        return parsed_response
