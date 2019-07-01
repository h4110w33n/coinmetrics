"""
Coin Metrics API Community Module Definitions
"""

import logging
from .base import Base
from .errors import InvalidAssetError, InvalidMetricError

class Community(Base):
    """
    Coin Metrics API Community Object
    """

    # Due to the conveniance methods, we trigger R0904: too-many-public-methods
    # even though this is desired.
    # pylint: disable=R0904

    def __init__(self, api_key=""):
        """
        Initialize the Community API exactly the same way as the same way as
        :py:func:`coinmetrics.base.Base.__init__`. An optional :samp:`api_key` can be supplied.

        :param api_key: API key to be used for the Pro API.
        :type api_key: str, optional
        """
        super().__init__()
        self.logger = logging.getLogger(__name__)

    def get_asset_info(self, assets=""):
        """
        Fetch asset(s) information. Including exchanges the asset is in,
        friendly name, markets, metrics, and most recent and oldest data
        timestamps. No specified asset will return all available asset info.

        :param assets: Unique ID corresponding to the asset's ticker.
        :type assets: str, optional

        :return: Asset information.
        :rtype: list of dict
        """
        self.logger.debug("Assets: '%s'", assets)
        if assets != "":
            options = {"subset": assets}
            self.asset_checker(assets)
        else:
            options = {}
        return self._api_query("asset_info", options)['assetsInfo']

    def get_exchange_info(self, exchanges=""):
        """
        Fetch exchange(s) information. Including assets, quotes, markets,
        and most recent and oldest data timestamps for each. No specified
        exchange will return all available exchange info.

        :param exchanges: Unique ID corresponding to the exchange.
        :type exchanges: str, optional

        :return: Exchange information.
        :rtype: list of dict
        """
        self.logger.debug("Exchanges: '%s'", exchanges)
        if exchanges != "":
            options = {"subset": exchanges}
            self.exchange_checker(exchanges)
        else:
            options = {}
        return self._api_query("exchange_info", options)['exchangesInfo']

    def get_metric_info(self, metrics=""):
        """
        Fetch metric(s) information. Including friendly name, dscription,
        category.

        :param metrics: Unique ID corresponding to the metrics.
        :type metrics: str, optional

        :return: Metric information.
        :rtype: list of dict
        """
        self.logger.debug("Metrics: '%s'", metrics)
        if metrics != "":
            self.metric_checker(metrics)
            options = {"subset": metrics}
        else:
            options = {}
        return self._api_query("metric_info", options)['metricsInfo']

    def get_market_info(self, markets=""):
        """
        Fetch market(s) information. Includes assets, quotes,
        and most recent and oldest data timestamps for each.

        :param markets: Unique ID corresponding to the market.
        :type markets: str, optional

        :return: Market information.
        :rtype: list of dict
        """
        self.logger.debug("Markets: '%s'", markets)
        if markets != "":
            self.market_checker(markets)
            options = {"subset": markets}
        else:
            options = {}
        return self._api_query("market_info", options)['marketsInfo']

    def get_asset_metrics(self, asset):
        """
        Fetch list of available metrics for a given asset. This will only
        fetch metrics corresponding to one asset at a time.

        :param asset: Unique ID corresponding to the asset's ticker.
        :type asset: str

        :return: List of supported metrics for the asset.
        :rtype: list
        """
        self.logger.debug("Asset: '%s'", asset)
        if "," in asset:
            raise InvalidAssetError("""Can only fetch compatible metrics from
                                       a single asset at a time.""")
        return self.get_asset_info(asset)[0]['metrics']

    #: An alias for :py:func:`get_asset_metrics` (backwards compatibility)
    get_available_data_types_for_asset = get_asset_metrics

    def asset_metric_checker(self, asset, metrics):
        """
        Helper function to determine if the requested metric(s) is(are) valid
        for an asset. This will only validate metrics corresponding to one
        asset at a time.

        :param asset: Unique ID corresponding to the asset's ticker.
        :type asset: str

        :param metric: Unique ID corresponding to metric.
        :type metric: str
        """
        self.logger.debug("Asset: '%s'", asset)
        self.logger.debug("Metrics: '%s'", metrics)
        metrics = metrics.split(",")
        reference = self.get_asset_metrics(asset)
        for metric in metrics:
            if metric in reference:
                pass
            else:
                raise InvalidMetricError("""Invalid metric '{}' for the given
                                            asset '{}'.""".format(metric, asset))

    def get_asset_metric_data(self, asset, metrics, start, end, time_agg="day"):
        """
        Fetch metric(s) data given a specified asset, and timeframe.
        See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :param asset: Unique ID corresponding to the asset's ticker.
        :type asset: str

        :param metrics: Unique ID corresponding to the metrics.
        :type metrics: str

        :param begin_timestamp: Start of time inverval.
        :type begin_timestamp: str or datetime

        :param end_timestamp: End of time inverval.
        :type end_timestamp: str or datetime

        :param time_agg: Interval the time is descritized into: day, hour.
        :type time_agg: str

        :return: Coin Metrics API data object. See the `API reference`_ for details
        :rtype: dict

        .. _`API reference`: https://docs.coinmetrics.io/api/v2/#operation/getAssetMetricsData
        """
        #pylint: disable=R0913
        if metrics == "all" or None:
            metrics = ','.join(self.get_asset_metrics(asset))
        self.logger.debug("asset: '%s'", asset)
        self.logger.debug("Metrics: '%s'", metrics)
        self.logger.debug("Start Timestamp: '%s'", start)
        self.logger.debug("End Timestamp: '%s'", end)
        self.asset_checker(asset)
        self.metric_checker(metrics)
        self.timestamp_checker(start, end)
        endpoint = "assets/%s/metricdata" % asset
        options = {"metrics": metrics, "start": start, "end": end, "time_agg": time_agg}
        return self._api_query(endpoint, options)['metricData']

    #: An alias for :py:func:`get_asset_metric_data` (backwards compatibility)
    get_asset_data_for_time_range = get_asset_metric_data

    def get_active_addresses(self, assets, start, end):
        """
        The sum count of unique addresses that were active in the network
        (either as a recipient or originator of a ledger change) that day.
        All parties in a ledger change action (recipients and originators)
        are counted. Individual addresses are not double-counted if
        previously active. See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "AdrActCnt", start, end)

    #: An alias for :py:func:`get_active_addresses`
    active_addresses, activeaddresses, AdrActCnt = [get_active_addresses] * 3

    def get_block_count(self, assets, start, end):
        """
        The sum count of unique addresses that were active in the network
        (either as a recipient or originator of a ledger change) that day.
        All parties in a ledger change action (recipients and originators)
        are counted. Individual addresses are not double-counted if
        previously active. See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "BlkCnt", start, end)

    #: An alias for :py:func:`get_block_count`
    block_count, blockcount, BlkCnt = [get_block_count] * 3

    def get_mean_block_size(self, assets, start, end):
        """
        The mean size (in bytes) of all blocks created that day.
        See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "BlkSizeMeanByte", start, end)

    #: An alias for :py:func:`get_mean_block_size`
    get_meanblocksize, meanblocksize, BlkSizeMeanByte = [get_mean_block_size] * 3

    def get_mvrv_cur(self, assets, start, end):
        """
        The ratio of the sum USD value of the current supply to the sum
        "realized" USD value of the current supply. See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "CapMVRVCur", start, end)

    #: An alias for :py:func:`get_mvrv_cur`
    get_mvrvcur, mvrvcur, CapMVRVCur = [get_mvrv_cur] * 3

    def get_real_cap(self, assets, start, end):
        """
        The sum USD value based on the USD closing price on the day
        that a native unit last moved (i.e., last transacted)
        for all native units. See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "CapRealUSD", start, end)

    #: An alias for :py:func:`get_real_cap`
    get_realcap, real_cap, CapRealUSD = [get_real_cap] * 3

    def get_diff_mean(self, assets, start, end):
        """
        The mean difficulty of finding a hash that meets the protocol
        designated requirement (i.e., the difficulty of finding a
        new block) that day. The requirement is unique to each
        applicable cryptocurrency protocol. Difficulty is adjusted
        periodically by the protocol as a function of how much
        hashing power is being deployed by miners.
        See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "DiffMean", start, end)

    #: An alias for :py:func:`get_diff_mean`
    get_diffmean, diff_mean, DiffMean = [get_diff_mean] * 3

    def get_fee_mean(self, assets, start, end):
        """
        The USD value of the mean fee per transaction that day.
        See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "FeeMeanUSD", start, end)

    #: An alias for :py:func:`get_fee_mean`
    get_feemean, fee_mean, FeeMeanUSD = [get_fee_mean] * 3

    def get_median_fee(self, assets, start, end):
        """
        The USD value of the median fee per transaction that day.
        See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "FeeMedUSD", start, end)

    #: An alias for :py:func:`get_median_fee`
    get_medianfee, median_fee, FeeMedUSD = [get_median_fee] * 3

    def get_fee_total(self, assets, start, end):
        """
        The sum USD value of all fees paid to miners that day. Fees do not
        include new issuance. See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "FeeTotUSD", start, end)

    #: An alias for :py:func:`get_fee_total`
    get_feetotal, fee_total, FeeTotUSD = [get_fee_total] * 3

    def get_units_issued(self, assets, start, end):
        """
        The sum of new native units issued that day. Only those
        native units that are issued by a protocol-mandated
        continuous emission schedule are included.
        See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "IssContNtv", start, end)

    #: An alias for :py:func:`get_issued`
    get_unitsissued, units_issued, IssContNtv = [get_units_issued] * 3

    def get_units_issued_ann_pct(self, assets, start, end):
        """
        The percentage of new native units (continuous) issued on
        that day, extrapolated to one year (i.e., multiplied by 365),
        and divided by the current supply on that day. Also referred
        to as the annual inflation rate. See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "IssContPctAnn", start, end)

    #: An alias for :py:func:`get_units_issued_ann_pct`
    get_unitsannpct, units_ann_pct, IssContPctAnn = [get_units_issued_ann_pct] * 3

    def get_units_issued_usd(self, assets, start, end):
        """
        The sum USD value of all new native units issued that day.
        See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "IssTotUSD", start, end)

    #: An alias for :py:func:`get_units_issued_usd`
    get_unitsissuedusd, units_issued_usd, IssTotUSD = [get_units_issued_usd] * 3

    def get_nvt_adj(self, assets, start, end):
        """
        The ratio of the network value (or market capitalization,
        current supply) divided by the adjusted transfer value.
        Also referred to as NVT. See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "NVTAdj", start, end)

    #: An alias for :py:func:`get_nvt_adj`
    get_nvtadj, nvt_adj, NVTAdj = [get_nvt_adj] * 3

    def get_nvt_adj_90(self, assets, start, end):
        """
        The ratio of the network value (or market capitalization,
        current supply) to the 90-day moving average of the adjusted
        transfer value. Also referred to as NVT. See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "NVTAdj90", start, end)

    #: An alias for :py:func:`get_nvt_adj_90`
    get_nvtadj90, nvt_adj_90, NVTAdj90 = [get_nvt_adj_90] * 3

    def get_price_btc(self, assets, start, end):
        """
        The fixed closing price of the asset as of 00:00 UTC the
        following day (i.e., midnight UTC of the current day)
        denominated in USD. This price is generated by Coin Metrics'
        fixing/reference rate service. See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "PriceBTC", start, end)

    #: An alias for :py:func:`get_price_btc`
    get_pricebtc, price_btc, NVTAdj90 = [get_price_btc] * 3

    def get_price_usd(self, assets, start, end):
        """
        The fixed closing price of the asset as of 00:00 UTC the
        following day (i.e., midnight UTC of the current day)
        denominated in BTC. See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "PriceUSD", start, end)

    #: An alias for :py:func:`get_price_usd`
    get_priceusd, price_usd, PriceUSD = [get_price_usd] * 3

    def get_cur_sply(self, assets, start, end):
        """
        The sum of all native units ever created and visible on the
        ledger (i.e., issued) as of that day. For account-based
        protocols, only accounts with positive balances are counted.
        See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """

        return self.get_asset_metric_data(assets, "SplyCur", start, end)

    #: An alias for :py:func:`get_cur_sply`
    get_cursply, cur_sply, PriceUSD = [get_cur_sply] * 3

    def get_tx_count(self, assets, start, end):
        """
        The sum count of transactions that day. Transactions
        represent a bundle of intended actions to alter the ledger
        initiated by a user (human or machine). See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """

        return self.get_asset_metric_data(assets, "TxCnt", start, end)

    #: An alias for :py:func:`get_tx_count`
    get_txcount, tx_count, TxCnt = [get_tx_count] * 3

    def get_txtfr_count(self, assets, start, end):
        """
        The sum count of transfers that day. Transfers represent
        movements of native units from one ledger entity to another
        distinct ledger entity. See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "TxTfr", start, end)

    #: An alias for :py:func:`get_txtfr_count`
    get_txtfrcount, txtfr_count, TxTfr = [get_txtfr_count] * 3

    def get_txtfr_val_adj(self, assets, start, end):
        """
        The sum of native units transferred that day removing noise and
        certain artifacts. See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "TxTfrValAdjNtv", start, end)

    #: An alias for :py:func:`get_txtfr_val_adj`
    get_txtfrvaladj, txtfr_val_adj, TxTfrValAdjNtv = [get_txtfr_val_adj] * 3

    def get_txtfr_val_adj_usd(self, assets, start, end):
        """
        The USD value of the sum of native units transferred that day removing
        noise and certain artifacts. See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "TxTfrValAdjUSD", start, end)

    #: An alias for :py:func:`get_txtfr_val_adj_usd`
    get_txtfrvaladj, txtfr_val_adj, TxTfrValAdjUSD = [get_txtfr_val_adj] * 3

    def get_txtfr_val_mean(self, assets, start, end):
        """
        The mean count of native units transferred per transaction
        (i.e., the mean "size" of a transaction) that day.
        See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "TxTfrValMeanNtv", start, end)

    #: An alias for :py:func:`get_txtfr_val_mean`
    get_txtfrvalmean, txtfr_val_mean, TxTfrValMeanNtv = [get_txtfr_val_mean] * 3

    def get_txtfr_val_mean_usd(self, assets, start, end):
        """
        The sum USD value of native units transferred divided by
        the count of transfers (i.e., the mean "size" in USD of a
        transfer) that day. See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "TxTfrValMeanUSD", start, end)

    #: An alias for :py:func:`get_txtfr_val_mean_usd`
    get_txtfrvalmeanusd, txtfr_val_mean_usd, TxTfrValMeanUSD = [get_txtfr_val_mean_usd] * 3

    def get_txtfr_val_med(self, assets, start, end):
        """
        The median count of native units transferred per transfer
        (i.e., the median "size" of a transfer) that day.
        See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "TxTfrValMedNtv", start, end)

    #: An alias for :py:func:`get_txtfr_val_med`
    get_txtfrvalmed, txtfr_val_med, TxTfrValMedNtv = [get_txtfr_val_med] * 3

    def get_txtfr_val_med_usd(self, assets, start, end):
        """
        The median USD value transferred per transfer (i.e., the
        median "size" in USD of a transfer) that day.
        See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "TxTfrValMedUSD", start, end)

    #: An alias for :py:func:`get_txtfr_val_med_usd`
    get_txtfrvalmedusd, txtfr_val_med_usd, TxTfrValMedUSD = [get_txtfr_val_med_usd] * 3

    def get_txtfr_val(self, assets, start, end):
        """
        The sum of native units transferred (i.e., the aggregate
        "size" of all transfers) that day. See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "TxTfrValNtv", start, end)

    #: An alias for :py:func:`get_txtfr_val`
    get_txtfrval, txtfr_val, TxTfrValNtv = [get_txtfr_val] * 3

    def get_txtfr_val_usd(self, assets, start, end):
        """
        The sum USD value of all native units transferred
        (i.e., the aggregate size in USD of all transfers)
        that day. See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "TxTfrValUSD", start, end)

    #: An alias for :py:func:`get_txtfr_val_usd`
    get_txtfrvalusd, txtfr_val_usd, TxTfrValUSD = [get_txtfr_val_usd] * 3

    def get_vty_ret_180d(self, assets, start, end):
        """
        The 180D volatility, measured as the deviation of
        log returns See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "VtyDayRet180d", start, end)

    #: An alias for :py:func:`get_vty_ret_180d`
    get_vtyret180d, vty_ret_180d, VtyDayRet180d = [get_vty_ret_180d] * 3

    def get_vty_ret_30d(self, assets, start, end):
        """
        The 30D volatility, measured as the deviation of log returns See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "VtyDayRet30d", start, end)

    #: An alias for :py:func:`get_vty_ret_30d`
    get_vtyret30d, vty_ret_30d, VtyDayRet30d = [get_vty_ret_30d] * 3

    def get_vty_ret_60d(self, assets, start, end):
        """
        The 60D volatility, measured as the deviation of log returns.
        See: `Data Dictionary`_.

        .. _`Data Dictionary`: https://coinmetrics.io/community-data-dictionary/

        :Parameters: See see :py:func:`get_asset_metric_data` for parameter and return details.
        """
        return self.get_asset_metric_data(assets, "VtyDayRet60d", start, end)

    #: An alias for :py:func:`get_vty_ret_60d`
    get_vtyret60d, vty_ret_60d, VtyDayRet60d = [get_vty_ret_60d] * 3
