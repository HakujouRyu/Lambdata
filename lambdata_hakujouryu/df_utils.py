""" 
utilitiy funcs for working with DataFrames
"""

import pandas as pd
import numpy as np

TEST_DF = pd.DataFrame({'one': [1,1,1,1], 'two': [2,2,2,2], 'dates': ['09091988', '04021992', '01102009', '04201420']})
TEST_LIST = [9,9,9,9]

def split_dates(df, column):
    """ Converts ['created_at', 'dealdine', 'launched_at'] into pandas.dt, 
        and creates columns for month day and year.
        Also creates 'days_to_launch' and 'campaign_length' columns """

    df[column] = pd.to_datetime(df[column], unit='s')

    #Break time up into columns Month day etc
    df[column] = df[column].dt.month
    df[column] = df[column].dt.weekday
    df[column] = df[column].dt.year
    return df


def time_to_string(df, column):
    """  Convert back into strings so that we can pass to model """    
    df[column] = df[column].astype(str)

def list_to_col(ls, df, list_name):
    """ Converts ls (list) to a Series then joins to df as column 'list_name' """

    df[list_name] = pd.Series(ls)
    return df