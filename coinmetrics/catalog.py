"""
Coin Metrics API Catalog Module Definitions
"""
import logging
from .base import Base


class Catalog(Base):
    """
    Coin Metrics API Catalog Object
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
        self.catalog_base = "catalog-all"

    def assets(self, assets="", include="", exclude=""):
        """
        Returns a list of available assets along with information for them like metrics, markets,
        exchanges and time ranges of available data.

        :param assets: Comma separated list of assets. By default all assets are returned.
        :type assets: str, optional

        :param include: Comma separated list of fields to include in response. Supported values
                        are `metrics`, `markets`, `exchanges`.
        :type include: str, optional

        :param exclude: Comma separated list of fields to exclude from response. Supported values
                        are `metrics`, `markets`, `exchanges`.
        :type exclude: str, optional

        :return: Dictionary who's 'data' element is a list of dictionaries with the request
                 asset(s) information.
        :rtype: dict
        """
        self.logger.debug("Fetching assets.")
        self.logger.debug("Assets: '%s'", assets)
        self.logger.debug("Include: '%s'", include)
        self.logger.debug("Exclude: '%s'", exclude)
        endpoint = f"{self.catalog_base}/assets"
        options = {}
        _ = assets and (options.update({"assets": assets}))
        _ = include and (options.update({"include": include}))
        _ = exclude and (options.update({"exclude": exclude}))
        return self._api_query(endpoint, options)

    #: An alias for :py:func:`assets`
    get_assets = assets

    def metrics(self, metrics="", reviewable=""):
        """
        Returns a list of available metrics along with information for them like description,
        category and assets for which a metric is available.

        :param metrics: Comma separated list of metrics. By default all metrics are returned.
        :type metrics: str, optional

        :param reviewable: Limit to human-reviewable metrics. By default all metrics are returned.
        :type reviewable: str, optional

        :return: Dictionary who's 'data' element is a list of dictionaries with the request
                 metric(s) information.
        :rtype: dict
        """
        self.logger.debug("Fetching metrics.")
        self.logger.debug("Metrics: '%s'", metrics)
        self.logger.debug("Reviewable: '%s'", reviewable)
        endpoint = f"{self.catalog_base}/metrics"
        options = {}
        _ = metrics and (options.update({"metrics": metrics}))
        _ = reviewable and (options.update({"reviewable": reviewable}))
        return self._api_query(endpoint, options)

    #: An alias for :py:func:`metrics`
    get_metrics = metrics

    def exchanges(self, exchanges=""):
        """
        Returns a list of available exchanges along with available markets for them.

        :param exchanges: Comma separated list of exchanges. By default all exchanges are returned.
        :type exchanges: str, optional

        :return: Dictionary who's 'data' element is a list of dictionaries with the request
                 exchange(s) information.
        :rtype: dict
        """
        self.logger.debug("Fetching exchanges.")
        self.logger.debug("Exchanges: '%s'", exchanges)
        endpoint = f"{self.catalog_base}/exchanges"
        options = {}
        _ = exchanges and (options.update({"exchanges": exchanges}))
        return self._api_query(endpoint, options)

    #: An alias for :py:func:`exchanges`
    get_exchanges = exchanges

    def exchange_assets_pairs(self, exchange_assets=""):
        """
        Returns a list of available exchange-asset pairs along with information for them like
        metrics and time ranges of available data.

        :param exchange_assets: Comma separated list of exchange-assets. By default, all
                                exchange-assets pairs are returned.
        :type exchange_assets: str, optional

        :return: Dictionary who's 'data' element is a list of dictionaries with the request
                 exchange-asset(s) information.
        :rtype: dict
        """
        self.logger.debug("Fetching exchange asset pairs.")
        self.logger.debug("Exchange Assets: '%s'", exchange_assets)
        endpoint = f"{self.catalog_base}/exchange-assets"
        options = {}
        _ = exchange_assets and (options.update({"exchange_assets": exchange_assets}))
        return self._api_query(endpoint, options)

    #: An alias for :py:func:`exchange_assets_pairs`
    get_exchange_asset_pairs = exchange_assets_pairs

    def pairs(self, pairs=""):
        """
        Returns a list of all supported asset pairs along with information for them like metrics
        and time ranges of available data.

        :param pairs: Comma separated list of asset pairs. By default, all asset pairs are
                      returned.
        :type pairs: str, optional

        :return: Dictionary who's 'data' element is a list of dictionaries with the request
                 asset-pairs information.
        :rtype: dict
        """
        self.logger.debug("Fetching asset pairs.")
        self.logger.debug("Pairs: '%s'", pairs)
        endpoint = f"{self.catalog_base}/pairs"
        options = {}
        _ = pairs and (options.update({"pairs": pairs}))
        return self._api_query(endpoint, options)

    #: An alias for :py:func:`pairs`
    get_pairs, get_asset_pairs, asset_pairs = [pairs] * 3

    def institutions(self, institutions=""):
        """
        Returns a list of all support institutions along with information for them like metrics
        and time ranges of available data.

        :param institutions: Comma separated list of institutions. By default, all institutions
                             are returned.
        :type institutions: str, optional

        :return: Dictionary who's 'data' element is a list of dictionaries with the request
                 institution information.
        :rtype: dict
        """
        self.logger.debug("Fetching institutions.")
        self.logger.debug("Institutions: '%s'", institutions)
        endpoint = f"{self.catalog_base}/institutions"
        options = {}
        _ = institutions and (options.update({"institutions": institutions}))
        return self._api_query(endpoint, options)

    #: An alias for :py:func:`institutions`
    get_institutions = institutions

    # pylint: disable=R0913
    def markets(
        self,
        markets="",
        exchange="",
        market_type="",
        base="",
        quote="",
        asset="",
        symbol="",
        include="",
        exclude="",
        limit="",
    ):
        """
        Returns a list of all supported markets along with time ranges of available data.

        :param markets: Comma separated list of markets. By default all markets are returned.
        :type markets: str, optional

        :param exchange: Unique name of an exchange.
        :type exchange: str, optional

        :param market_type: Type of markets. Enum: "spot", "future", "option"
        :type market_type: str, optional

        :param base: Base asset of markets.
        :type base: str, optional

        :param quote: Quote asset of markets.
        :type quote: str, optional

        :param asset: Any asset of markets.
        :type asset: str, optional

        :param symbol: Symbol of derivative markets, full instrument name.
        :type symbol: str, optional

        :param include: Comma separated list of fields to include in response. Supported values
                        are `trades`, `orderbooks`, `quotes`, `candles`, `funding_rates`,
                        `openinterest`, `liquidations`. Included by default if omitted.
        :type include: str, optional

        :param exclude: Comma separated list of fields to exclude from response. Supported values
                        are `trades`, `orderbooks`, `quotes`, `candles`, `funding_rates`,
                        `openinterest`, `liquidations`. Included by default if omitted.
        :type exclude: str, optional

        :param limit: Limit of response items. none means no limit.
        :type limit: str, optional

        :return: Dictionary who's 'data' element is a list of dictionaries with the request markets
                 information.
        :rtype: dict
        """
        self.logger.debug("Fetching markets.")
        endpoint = f"{self.catalog_base}/markets"
        options = {}
        self.logger.debug("Markets: '%s'", markets)
        _ = markets and (options.update({"markets": markets}))
        self.logger.debug("Exchange: '%s'", exchange)
        _ = exchange and (options.update({"exchange": exchange}))
        self.logger.debug("Type: '%s'", market_type)
        _ = market_type and (options.update({"type": market_type}))
        self.logger.debug("Base: '%s'", base)
        _ = base and (options.update({"base": base}))
        self.logger.debug("Quote: '%s'", quote)
        _ = quote and (options.update({"quote": quote}))
        self.logger.debug("Asset: '%s'", asset)
        _ = asset and (options.update({"asset": asset}))
        self.logger.debug("Symbol: '%s'", symbol)
        _ = symbol and (options.update({"symbol": symbol}))
        self.logger.debug("Include: '%s'", include)
        _ = include and (options.update({"include": include}))
        self.logger.debug("Exclude: '%s'", exclude)
        _ = exclude and (options.update({"exclude": exclude}))
        self.logger.debug("Limit: '%s'", limit)
        _ = limit and (options.update({"limit": limit}))
        return self._api_query(endpoint, options)

    #: An alias for :py:func:`markets`
    get_markets = markets

    # pylint: disable=R0913
    def market_candles(
        self,
        markets="",
        exchange="",
        market_type="",
        base="",
        quote="",
        asset="",
        symbol="",
        limit="",
    ):
        """
        Returns a list of all markets with candles support along with time ranges of available
        data per candle duration.

        :param markets: Comma separated list of markets. By default all markets are returned.
        :type markets: str, optional

        :param exchange: Unique name of an exchange.
        :type exchange: str, optional

        :param market_type: Type of markets. Enum: "spot", "future", "option"
        :type market_type: str, optional

        :param base: Base asset of markets.
        :type base: str, optional

        :param quote: Quote asset of markets.
        :type quote: str, optional

        :param asset: Any asset of markets.
        :type asset: str, optional

        :param symbol: Symbol of derivative markets, full instrument name.
        :type symbol: str, optional

        :param limit: Limit of response items. none means no limit.
        :type limit: str, optional

        :return: Dictionary who's 'data' element is a list of dictionaries with the request market
                 candles information.
        :rtype: dict
        """
        self.logger.debug("Fetching market candles.")
        endpoint = f"{self.catalog_base}/market-candles"
        options = {}
        self.logger.debug("Markets: '%s'", markets)
        _ = markets and (options.update({"markets": markets}))
        self.logger.debug("Exchange: '%s'", exchange)
        _ = exchange and (options.update({"exchange": exchange}))
        self.logger.debug("Type: '%s'", market_type)
        _ = market_type and (options.update({"type": market_type}))
        self.logger.debug("Base: '%s'", base)
        _ = base and (options.update({"base": base}))
        self.logger.debug("Quote: '%s'", quote)
        _ = quote and (options.update({"quote": quote}))
        self.logger.debug("Asset: '%s'", asset)
        _ = asset and (options.update({"asset": asset}))
        self.logger.debug("Symbol: '%s'", symbol)
        _ = symbol and (options.update({"symbol": symbol}))
        self.logger.debug("Limit: '%s'", limit)
        _ = limit and (options.update({"limit": limit}))
        return self._api_query(endpoint, options)

    #: An alias for :py:func:`market_candles`
    get_market_candles = market_candles

    # pylint: disable=R0913
    def market_metrics(
        self,
        markets="",
        exchange="",
        market_type="",
        base="",
        quote="",
        asset="",
        symbol="",
        limit="",
    ):
        """
        Returns a list of all markets with market metrics support along with time ranges of
        available data per metric.

        :param markets: Comma separated list of markets. By default all markets are returned.
        :type markets: str, optional

        :param exchange: Unique name of an exchange.
        :type exchange: str, optional

        :param market_type: Type of markets. Enum: "spot", "future", "option"
        :type market_type: str, optional

        :param base: Base asset of markets.
        :type base: str, optional

        :param quote: Quote asset of markets.
        :type quote: str, optional

        :param asset: Any asset of markets.
        :type asset: str, optional

        :param symbol: Symbol of derivative markets, full instrument name.
        :type symbol: str, optional

        :param limit: Limit of response items. none means no limit.
        :type limit: str, optional

        :return: Dictionary who's 'data' element is a list of dictionaries with the request market
                 metric information.
        :rtype: dict
        """
        self.logger.debug("Fetching market metrics.")
        endpoint = f"{self.catalog_base}/market-metrics"
        options = {}
        self.logger.debug("Markets: '%s'", markets)
        _ = markets and (options.update({"markets": markets}))
        self.logger.debug("Exchange: '%s'", exchange)
        _ = exchange and (options.update({"exchange": exchange}))
        self.logger.debug("Type: '%s'", market_type)
        _ = market_type and (options.update({"type": market_type}))
        self.logger.debug("Base: '%s'", base)
        _ = base and (options.update({"base": base}))
        self.logger.debug("Quote: '%s'", quote)
        _ = quote and (options.update({"quote": quote}))
        self.logger.debug("Asset: '%s'", asset)
        _ = asset and (options.update({"asset": asset}))
        self.logger.debug("Symbol: '%s'", symbol)
        _ = symbol and (options.update({"symbol": symbol}))
        self.logger.debug("Limit: '%s'", limit)
        _ = limit and (options.update({"limit": limit}))
        return self._api_query(endpoint, options)

    #: An alias for :py:func:`market_metrics`
    get_market_metrics = market_metrics

    def indexes(self, indexes=""):
        """
        Returns a list of all supported indexes along with time ranges of available data.

        :param indexes: Comma separated list of indexes. By default all assets are returned.
        :type indexes: str, optional

        :return: Dictionary who's 'data' element is a list of dictionaries with the request
                 index information.
        :rtype: dict
        """
        self.logger.debug("Fetching indexes.")
        self.logger.debug("Indexes: '%s'", indexes)
        endpoint = f"{self.catalog_base}/indexes"
        options = {}
        _ = indexes and (options.update({"indexes": indexes}))
        return self._api_query(endpoint, options)

    #: An alias for :py:func:`indexes`
    get_indexes = indexes

    def asset_alerts(self, assets="", alerts=""):
        """
        Returns a list of all supported asset alerts along with their descriptions, thresholds
        and constituents.

        :param indexes: Comma separated list of assets. By default all assets are returned.
        :type indexes: str, optional

        :param alerts: Comma separated list of asset alert names. By default all asset alerts
                       are returned.
        :type alerts: str, optional

        :return: Dictionary who's 'data' element is a list of dictionaries with the request
                 index information.
        :rtype: dict
        """
        self.logger.debug("Fetching asset alerts.")
        self.logger.debug("Assets: '%s'", assets)
        self.logger.debug("Alerts: '%s'", alerts)
        endpoint = f"{self.catalog_base}/alerts"
        options = {}
        _ = assets and (options.update({"assets": assets}))
        _ = alerts and (options.update({"alerts": alerts}))
        return self._api_query(endpoint, options)

    #: An alias for :py:func:`indexes`
    get_asset_alerts = asset_alerts
