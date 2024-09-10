import pandas

ROWSPERDAY = 24 * 4 * 2

class readFluvius(object):

    def __init__(self, fn) -> None:
        self._fn = fn
        # self._readData()

    def readData(self):
        self._df = pandas.read_csv(self._fn, delimiter=';')   
        self._df.Volume = self._df.Volume.str.replace(',', '.').astype(float)
        return self._df

