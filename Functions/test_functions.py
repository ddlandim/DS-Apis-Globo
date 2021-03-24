import unittest
import pandas as pd
import numpy as np
import functions as functions

class test_functions(unittest.TestCase):

    def test_median_even(self):
        df = pd.DataFrame({"target": [1,2,3,4,5,6,7,8]})
        df_assert = pd.DataFrame( {"target": [1,1,1,1.5,2.5,3.5,4.5,5.5]})
        df_test = functions.median_window(df,'target',4)
        comparison = np.array(df_assert['target']) == df_test
        equal_arrays = comparison.all()
        assert equal_arrays

    def test_median_odd(self):
        df = pd.DataFrame({"target": [1,2,3,4,5,6,7,8]})
        df_assert = pd.DataFrame( {"target": [1,1,1,2,3,4,5,6]})
        df_test = functions.median_window(df,'target',3)
        comparison = np.array(df_assert['target']) == df_test
        equal_arrays = comparison.all()
        assert equal_arrays

    def test_df_predicted_audience(self):
        df_test = pd.read_csv('./Data/tvaberta_program_audience(1)_test.csv')
        df_test['predicted_audience'] = -1
        np_assert = np.array([1, 1, 1, 1.5, 2.5, 3.5, 4.5, 5.5, 1, 10, 1, 1, 1, 1.5, 5, 5, 5])
        np_test = np.array(functions.df_predicted_audience(df_test)['predicted_audience'].values)
        comparison = np_assert == np_test
        equal_arrays = comparison.all()
        assert equal_arrays

if __name__ == '__main__':
    unittest.main()
