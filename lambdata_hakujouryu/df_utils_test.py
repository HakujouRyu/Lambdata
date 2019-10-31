""" Testing functions from the df_utils module"""


import unittest

import pandas as pd

from df_utils import  list_to_col


TEST_DF = pd.DataFrame(
    {'one': [1, 1, 1, 1], 
    'two': [2, 2, 2, 2],
    'dates': ['09/09/1988', '04/02/1992', '01/10/2009', '04/20/1920']})

VER_DF = pd.DataFrame(
    {'one': [1, 1, 1, 1], 
    'two': [2, 2, 2, 2],
    'dates': ['09/09/1988', '04/02/1992', '01/10/2009', '04/20/1920'],
    'old_list': [9, 9, 9, 9]})


TEST_LIST = [9, 9, 9, 9]

class DateFunctionsTest(unittest.TestCase):
    """ Tests for the DateFunctions class"""
    def test_test(self):
        assert True

    def test_split_dates(self):
        self.assertEqual(list_to_col(TEST_LIST, TEST_DF).shape, VER_DF.shape)

if __name__ == '__main__':
    unittest.main()
