"""
Coin Metrics API Conversion Utilities
"""

class Utils:
    """
    A few utilities to convert the data gathered from the APIs into more
    useful forms for processing.
    """

    def pandas(self, data):
        """
        Convert an object output from :py:func:`Community.get_asset_metric_data`
        to a Pandas object for further processing.

        :param object: Raw data object to convert to Pandas datagram.
        :type object: dict

        :return: Pandas dataframe form of original object.
        :rtype: pandas dataframe
        """
        import pandas as pd
        if type(data) is not pd.DataFrame:
            raw_index = [row['time'] for row in data['series']]
            raw_values = [row['values'] for row in data['series']]
            pandas_dataframe = pd.DataFrame(index=raw_index, data=raw_values, columns=data['metrics'])
            return pandas_dataframe
        else:
            return data

    def normalize(self, data):
        """
        # TODO: STUB
        Convert an object output from :py:func:`Community.get_asset_metric_data`
        to a standard list of dictionaries for further processing.

        :param object: Raw data object to convert to list of dict.
        :type object: dict

        :return: A normalized list of dictionaries
        :rtype: list
        """

    def csv(self, data, path):
        """
        # TODO: STUB
        Convert an object output from :py:func:`Community.get_asset_metric_data`
        to a standard list of dictionaries for further processing.

        :param object: Raw data object to convert to Pandas datagram.
        :type object: dict

        :param path: Location to save the CSV file to.
        :type path: str, optional
        """
        data = self.pandas(data)
        data.to_csv(path_or_buf=path)




        