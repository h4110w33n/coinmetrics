"""
Coin Metrics API Pro Module Definitions
"""

from .community import Community

class Pro(Community):
    """
    Coin Metrics API Community Object
    """

    def __init__(self, api_key=""):
        """
        Initialize the Community API exactly the same way as the same way as :py:func:`coinmetrics.base.Base.__init__`. However the api_key variable is required.
        """
        super().__init__()
        self.host_url = 'https://api.coinmetrics.io/v2/'
        self.headers = {"Authorization": api_key} if api_key != '' else {}

    def get_index_info(self, index_id):
        """
        Methods for fetching index values data.

        :param index_id: Unique ID corresponding to the index.
        :type index_id: str

        :return: Index information.
        :rtype: list of dict
        """
        self.logger.debug("Index: '%s'", index_id)
        endpoint = "indexes/%s/values" % index_id
        return self._api_query(endpoint)
