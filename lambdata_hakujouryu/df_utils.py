"""
utilitiy funcs for working with DataFrames
"""

import pandas as pd
import numpy as np


class DateFunctions:
    """ Contains useful functions for manipulating Dates """
    def __init__(self):
        pass

    def split_dates(self, df, column):
        """ Converts dates into DatTime then into columns """
        df[column] = pd.to_datetime(df[column])

#        Break time up into columns: Month day etc
        df[f'{column}_month'] = df[column].dt.month
        df[f'{column}_dow'] = df[column].dt.weekday
        df[f'{column}_year'] = df[column].dt.year
        return df

    def time_to_string(self, df, column):
        """  Convert back into strings so that we can pass to model """
        df[column] = df[column].astype(str)
        return df


def list_to_col(ls, df, list_name='old_list'):
    """ Converts ls (list) to a Series then joins
         to df as column 'list_name' """

    df[list_name] = pd.Series(ls)
    return df
