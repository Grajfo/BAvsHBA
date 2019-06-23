from NiaPy.benchmarks import Benchmark


# map from real number [0, 1] to integer ranging [5, 15]
def swap_n_population(val):
    return int(val * 10 + 5)


def swap_r(val):
    return int(val)


def swap_A(val):
    return int(val)


# map from real number [0, 1] to integer ranging [0, 1]
def swap_Qmin(val):
    if val == 1:
        return 3
    return int(val * 3 + 1)


# map from real number [0, 1] to integer ranging [1, 2]
def swap_Qmax(val):
    return int(val + 1)


class BatAlgorithmBenchmark(Benchmark):
    def __init__(self):
        Benchmark.__init__(self, -1, 1)

    def function(self):
        # our definition of fitness function
        def evaluate(D, sol):

            np = swap_n_population(sol[0])
            r = swap_r(sol[1])
            a = swap_A(sol[2])
            Qmin = swap_Qmin(sol[3])
            Qmax = swap_Qmax(sol[4])

            return np
            #Nevem kaj moram vrnit tu kakšne razultate

        return evaluate

