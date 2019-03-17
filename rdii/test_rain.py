import os.path
import unittest
import pandas as pd
from .rain import find_rain_periods

FILE_PATH = os.path.abspath(os.path.dirname(__file__))
RAINFALL_PATH = os.path.join(FILE_PATH, '../testdata/rainfall1.csv.gz')

class RainTest(unittest.TestCase):

    def test_place_stone(self):
        rainfall = self._load_rainfall(RAINFALL_PATH)
        rain_periods = find_rain_periods(rainfall)
        self.assertEqual(837, len(rain_periods))

    def _load_rainfall(self, path):
        """Helper function for loading and cleaning rainfall data
        """
        df = pd.read_csv(path, index_col='time', parse_dates=['time'])
        rainfall = df['rainfall'].fillna(0).resample('1H').sum()
        return rainfall


if __name__ == '__main__':
    unittest.main()