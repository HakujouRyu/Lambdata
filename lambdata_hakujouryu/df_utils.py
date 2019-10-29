"""
utilitiy funcs for working with DataFrames
"""

import pandas as pd
import numpy as np


TEST_DF = pd.DataFrame(
    {'one': [1, 1, 1, 1], 'two': [2, 2, 2, 2],
     'dates': ['09/09/1988', '04/02/1992', '01/10/2009', '04/20/1920']})


TEST_LIST = [9, 9, 9, 9]


class DateFunctions:
    """ Contains useful functions for manipulating Dates """
    def __init__(self):
        pass

    def split_dates(self, df, column):
        """ Converts ['created_at', 'dealdine', 'launched_at'] into pandas.dt,
            and creates columns for month day and year.
            Also creates 'days_to_launch' and 'campaign_length' columns """
        df[column] = pd.to_datetime(df[column])

#        Break time up into columns Month day etc
        df[f'{column}_month'] = df[column].dt.month
        df[f'{column}_dow'] = df[column].dt.weekday
        df[f'{column}_year'] = df[column].dt.year
        return df

    def time_to_string(self, df, column):
        """  Convert back into strings so that we can pass to model """
        df[column] = df[column].astype(str)
        return df


def list_to_col(ls, df, list_name):
    """ Converts ls (list) to a Series then joins
         to df as column 'list_name' """

    df[list_name] = pd.Series(ls)
    return df
