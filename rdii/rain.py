
from collections import namedtuple
import pandas as pd

class RainPeriod(namedtuple('RainPeriod' , ['start_date', 'end_date', 'intensity'])):
    pass


def find_rain_periods(rainfall):
    """Find all periods with rain.
    Params:
    rainfall - Pandas Series with rainfall data
    """
    rains = []
    rain_start = None
    max_intensity = 0.0
    for index, value in rainfall.iteritems():
        if value > 0:
            if rain_start == None:
                rain_start = index
            if value > max_intensity:
                max_intensity = value
        elif rain_start != None:
            rains.append([rain_start, index, max_intensity])
            rain_start = None
            max_intensity = 0.0
    return pd.DataFrame.from_records(rains, columns=['start_date', 'end_date', 'intensity'])