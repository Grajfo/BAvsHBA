import numpy as np

'#Za izračun statističnih podatkov'
class Statistics:

    def __init__(self, array, algorithm_name, benchmark_name, dimension_name=None, Np=None, minFreq=None, maxFreq=None):
        self.algorithmName = algorithm_name
        self.dimensionName = dimension_name
        self.population = Np
        self.minFrequency = minFreq
        self.maxFrequency = maxFreq
        self.benchName = benchmark_name
        self.array = array if isinstance(array, np.ndarray) else np.asarray(array)
        self.__minvalue = self.array.min()
        self.__maxvalue = self.array.max()
        self.__mean = self.array.mean()
        self.__median = np.median(self.array)
        self.__std = self.array.std(ddof=1)

    @property
    def minvalue(self):
        return self.__minvalue

    @property
    def maxvalue(self):
        return self.__maxvalue

    @property
    def mean(self):
        return self.__mean

    @property
    def median(self):
        return self.__median

    @property
    def std(self):
        return self.__std

    def vrniTupleDim(self):
        tup = (self.algorithmName,
               self.dimensionName,
               self.benchName,
               self.__minvalue,
               self.__maxvalue,
               self.__mean,
               self.__median,
               self.std)
        return tup
