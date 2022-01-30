"""
Coin Metrics API Timeseries Module Definitions
"""
import logging
from .base import Base


class Timeseries(Base):
    """
    Coin Metrics API Timeseries Object
    """

    def __init__(self, api_key=""):
        """
        Initialize the Community API exactly the same way as the same way as
        :py:func:`coinmetrics.base.Base.__init__`. An optional :samp:`api_key` can be supplied.

        :param api_key: API key to be used for the Pro API.
        :type api_key: str, optional
        """
        super().__init__()
        self.logger = logging.getLogger(__name__)
        self.catalog_base = "timeseries"

    # def asset_metrics(self, assets="", include="", exclude=""):
    #     """
    #     Returns requested metrics for specified assets.

    #     Results for block by block metrics (1b frequency) are ordered by tuple (asset, height,
    #     block_hash), all other metrics are ordered by tuple (asset, time). You can change the
    #     sorting using sort query parameter.

    #     If multiple metrics are requested in the same time the strict policy for partially
    #     available metrics among requested ones is applied:

    #     - missing metric name in the JSON response means that the metric is "not a supported
    #       metric" for the asset and frequency while some other requested metrics are supported.
    #     - null value of the metric means "no data in the database" while some other requested
    #       metrics have data.

    #     :param assets: Comma separated list of assets.
    #     :type assets: str

    #     :param metrics: Comma separated metrics to request time series data for.
    #     :type metrics: str

    #     :param frequency: Frequency of the metrics. Supported values are 1b (block by block),
    #                       1s (one second), 1m (one minute), 1h (one hour), 1d (one day),
    #                       1d-ny-close (one day at New York close time).
    #     :type frequency: str, optional

    #     :param status: Which metric values do you want to see. Applicable only for "reviewable"
    #                    metrics. Enum: "all" "flash" "reviewed" "revised"
    #     :type status: str, optional

    #     :param start_time: Start of the time interval. If start_time is omitted, response will
    #                        include time series from the earliest time available. Inclusive by
    #                        default. Mutually exclusive with start_height and start_hash.
    #     :type start_time: str, optional

    #     :param end_time: End of the time interval. If end_time is omitted, response will include
    #                      time series up to the latest time available. Inclusive by default.
    #                      Mutually exclusive with start_height and start_hash.
    #     :type end_time: str, optional

    #     :param start_hash: The start hash indicates the beginning block height for the set of data
    #                        that are returned. Inclusive by default. Mutually exclusive with
    #                        start_time and start_height.
    #     :type start_hash: str, optional

    #     :param end_hash: The end hash indicates the ending block height for the set of data that
    #                      are returned. Inclusive by default. Mutually exclusive with end_time and
    #                      end_height.
    #     :type end_hash: str, optional

    #     :param start_inclusive: Inclusive or exclusive corresponding start_* parameters.
    #     :type start_inclusive: str, optional

    #     :param end_inclusive: Inclusive or exclusive corresponding end_* parameters.
    #     :type end_inclusive: str, optional

    #     :param min_confirmations: Specifies how many blocks behind the chain tip block by block
    #                               metrics (1b frequency) are based on. Default for btc is 2 and
    #                               99 for eth.
    #     :type min_confirmations: int, optional

    #     :param page_size: Number of items per single page of results. (Default: 100)
    #     :type page_size: int, optional

    #     :param paging_from: Where does the first page start, at the start of the interval or at the end.
    #                         Enum: "start" "end"
    #     :type paging_from: str, optional

    #     :return: Dictionary who's 'data' element is a list of dictionaries with the request
    #              asset(s) information.
    #     :rtype: dict
    #     """
    #     self.logger.debug("Fetching assets.")
    #     self.logger.debug("Assets: '%s'", assets)
    #     self.logger.debug("Include: '%s'", include)
    #     self.logger.debug("Exclude: '%s'", exclude)
    #     endpoint = f"{self.catalog_base}/assets"
    #     options = {}
    #     _ = assets and (options.update({"assets": assets}))
    #     _ = include and (options.update({"include": include}))
    #     _ = exclude and (options.update({"exclude": exclude}))
    #     return self._api_query(endpoint, options)

    # #: An alias for :py:func:`assets`
    # get_assets = assets