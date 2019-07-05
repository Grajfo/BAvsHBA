from NiaPy.benchmarks import Benchmark


# map from real number [0, 1] to integer ranging [15, 50]
def swap_n_population(val):
    return int(val * 10 + 40)


def swap_r(val):
    return round(val, 2)


def swap_A(val):
    return round(val, 2)


# map from real number [0, 1] to integer ranging [0, 1]
def swap_Qmin(val):
    return round(val, 2)


# map from real number [0, 1] to integer ranging [1, 2]
def swap_Qmax(val):
    return round(val + 1, 2)


class BatAlgorithmBenchmarkNp(Benchmark):
    def __init__(self):
        Benchmark.__init__(self, 0, 1)

    def function(self):
        # our definition of fitness function
        def evaluate(D, sol):
            val = 0.0
            for i in range(D):
                temp = swap_n_population(sol[i])
                if temp > val:
                    val = temp

            return val

        return evaluate


class BatAlgorithmBenchmarkA(Benchmark):
    def __init__(self):
        Benchmark.__init__(self, 0, 1)

    def function(self):
        # our definition of fitness function
        def evaluate(D, sol):
            val = 0.0
            for i in range(D):
                temp = swap_A(sol[i])
                if temp > val:
                    val = temp

            return val

        return evaluate


class BatAlgorithmBenchmarkr(Benchmark):
    def __init__(self):
        Benchmark.__init__(self, 0, 1)

    def function(self):
        # our definition of fitness function
        def evaluate(D, sol):
            val = 0.0
            for i in range(D):
                temp = swap_r(sol[i])
                if temp > val:
                    val = temp

            return val
        return evaluate


class BatAlgorithmBenchmarkQmin(Benchmark):
    def __init__(self):
        Benchmark.__init__(self, 0, 1)

    def function(self):
        # our definition of fitness function
        def evaluate(D, sol):
            val = 0.0
            for i in range(D):
                temp = swap_Qmin(sol[i])
                if temp > val:
                    val = temp
            return val

        return evaluate


class BatAlgorithmBenchmarkQmax(Benchmark):
    def __init__(self):
        Benchmark.__init__(self, 0, 1)

    def function(self):
        # our definition of fitness function
        def evaluate(D, sol):
            val = 0.0
            for i in range(D):
                temp = swap_Qmax(sol[i])
                if temp > val:
                    val = temp
            return val

        return evaluate
