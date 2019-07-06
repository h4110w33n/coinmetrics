"""
Coin Metrics API Conversion Utilities

The functions below are not internally used by the :samp:`coinmetrics` library. They are
transformations to allow data that was fetched to be more easily processed by another
process.

Usage Examples: :ref:`usage`
"""

def cm_to_pandas(data):
    """
    Convert an object output from :py:func:`coinmetrics.community.Community.get_asset_metric_data`
    to a Pandas object for further processing.

    :param object: Raw data object to convert to Pandas datagram.
    :type object: dict

    :return: Pandas dataframe form of original object.
    :rtype: pandas dataframe
    """
    import pandas as pd
    if not isinstance(data, pd.DataFrame):
        raw_index = [row['time'] for row in data['series']]
        raw_values = [row['values'] for row in data['series']]
        pandas_dataframe = pd.DataFrame(index=raw_index,
                                        data=raw_values,
                                        columns=data['metrics'])
        pandas_dataframe = pandas_dataframe.astype(float)
        return pandas_dataframe
    return data

def normalize(data):
    """
    Convert an object output from :py:func:`coinmetrics.community.Community.get_asset_metric_data`
    to a standard list of dictionaries for further processing.

    :param object: Raw data object to convert to list of dict.
    :type object: dict

    :return: A normalized list of dictionaries
    :rtype: list
    """
    return [{**{'time': row['time']}, **dict(zip(data['metrics'], row['values']))}
            for row in data['series']]

def csv(data, path):
    """
    Convert an object output from :py:func:`coinmetrics.community.Community.get_asset_metric_data`
    to a standard list of dictionaries for further processing.

    :param object: Raw data object to convert to Pandas datagram.
    :type object: dict

    :param path: Location to save the CSV file to.
    :type path: str, optional
    """
    data = cm_to_pandas(data)
    data.to_csv(path_or_buf=path)
