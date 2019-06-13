#!/usr/bin/env python3
"""
Unit Tests for the Coin Metrics API
"""
from coinmetrics import community

import logging
FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)

cm = community()
logging.getLogger('coinmetrics').setLevel(logging.INFO)
logging.getLogger('coinmetrics.api').setLevel(logging.INFO)

asset = "btc"
data_type = "medianfee"
begin_timestamp = 1514764800
end_timestamp = 1515283200

# print("supported assets:", cm.get_supported_assets())
# print("type supported assets:", type(cm.get_supported_assets()))

# print("available data types:", cm.get_available_data_types_for_asset(asset))
# print("available data types:", type(cm.get_available_data_types_for_asset(asset)))
# print("available data types:", cm.get_available_data_types_for_asset("asdf"))

# print("data given timerange:", cm.get_asset_data_for_time_range(asset, data_type, begin_timestamp, end_timestamp))
# print("data given timerange:", cm.get_asset_data_for_time_range(asset, "not_real", begin_timestamp, end_timestamp))
# print("data given timerange:", cm.get_asset_data_for_time_range(asset, data_type, end_timestamp, begin_timestamp))

print("get_fees:", cm.get_fees(asset, begin_timestamp, end_timestamp))

# print("get_active_addresses:", cm.get_active_addresses(asset, begin_timestamp, end_timestamp))
# print("activeaddresses", cm.activeaddresses(asset, begin_timestamp, end_timestamp))


#print("get_average_difficulty", cm.get_average_difficulty(asset, begin_timestamp, end_timestamp))
#print("averagedifficulty", cm.averagedifficulty(asset, begin_timestamp, end_timestamp))





#print("get_activeaddresses:", cm.get_activeaddresses(asset, begin_timestamp, end_timestamp))