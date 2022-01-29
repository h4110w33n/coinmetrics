from .base import Base
import logging

class Catalog(Base):

    def __init__(self):
        """
        Initialize the Community API exactly the same way as the same way as
        :py:func:`coinmetrics.base.Base.__init__`. An optional :samp:`api_key` can be supplied.

        :param api_key: API key to be used for the Pro API.
        :type api_key: str, optional
        """
        super().__init__()
        self.logger = logging.getLogger(__name__)
        self.base_endpoint = "catalog"

    def assets(self, assets="", include="", exclude=""):
        """
        Returns a list of available assets along with information for them like metrics, markets, exchanges and time ranges of available data.

        :param assets: Comma separated list of assets. By default all assets are returned.
        :type assets: str, optional

        :param include: Comma separated list of fields to include in response. Supported values are `metrics`, `markets`, `exchanges`.
        :type include: str, optional

        :param exclude: Comma separated list of fields to exclude from response. Supported values are `metrics`, `markets`, `exchanges`.
        :type exclude: str, optional

        :return: Dictionary who's 'data' element is a list of dictionaries with the request asset(s) information.
        :rtype: dict
        """
        self.logger.debug("Fetching assets.")
        self.logger.debug("Assets: '%s'", assets)
        self.logger.debug("Include: '%s'", include)
        self.logger.debug("Exclude: '%s'", exclude)
        endpoint = f"{self.base_endpoint}/assets"
        options = {}
        assets and (options.update({"assets": assets}))
        include and (options.update({"include": include}))
        exclude and (options.update({"exclude": exclude}))
        return self._api_query(endpoint, options)

    #: An alias for :py:func:`assets`
    get_assets = assets

    def metrics(self, metrics="", reviewable=""):
        """
        Returns a list of available metrics along with information for them like description, category and assets for which a metric is available.

        :param metrics: Comma separated list of metrics. By default all metrics are returned.
        :type metrics: str, optional

        :param reviewable: Limit to human-reviewable metrics. By default all metrics are returned.
        :type reviewable: str, optional

        :return: Dictionary who's 'data' element is a list of dictionaries with the request metric(s) information.
        :rtype: dict
        """
        self.logger.debug("Fetching metrics.")
        self.logger.debug("Metrics: '%s'", metrics)
        self.logger.debug("Reviewable: '%s'", reviewable)
        endpoint = f"{self.base_endpoint}/metrics"
        options = {}
        metrics and (options.update({"metrics": metrics}))
        reviewable and (options.update({"reviewable": reviewable}))
        return self._api_query(endpoint, options)

    #: An alias for :py:func:`metrics`
    get_metrics = metrics

    def exchanges(self, exchanges=""):
        """
        Returns a list of available exchanges along with available markets for them.

        :param exchanges: Comma separated list of exchanges. By default all exchanges are returned.
        :type exchanges: str, optional

        :return: Dictionary who's 'data' element is a list of dictionaries with the request exchange(s) information.
        :rtype: dict
        """
        self.logger.debug("Fetching exchanges.")
        self.logger.debug("Exchanges: '%s'", exchanges)
        endpoint = f"{self.base_endpoint}/exchanges"
        options = {}
        exchanges and (options.update({"exchanges": exchanges}))
        return self._api_query(endpoint, options)

    #: An alias for :py:func:`metrics`
    get_exchanges = exchanges
