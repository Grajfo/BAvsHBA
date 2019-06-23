from NiaPy import Runner
import run
from NiaPy.benchmarks import (
    Ackley
)
from NiaPy.algorithms.modified import HybridBatAlgorithm
from NiaPy.algorithms.basic import BatAlgorithm
from NiaPy.task.task import StoppingTask, OptimizationType
from NiaPy.benchmarks import Benchmark


class MyBenchmark(Benchmark):
    def __init__(self):
        Benchmark.__init__(self, -1, 1)

    def function(self):
        def evaluate(D, sol):
            val = 0.0
            for i in range(D):
                val += sol[i] ** 2
            return val

        return evaluate


def hba():
    for i in range(5):
        task = StoppingTask(D=10, nFES=4000, optType=OptimizationType.MINIMIZATION,
                            benchmark=MyBenchmark())
        algo = HybridBatAlgorithm(F=0.5, CR=0.9)
        best = algo.run(task=task)
        print(best)


if __name__ == '__main__':
    runner = Runner(
        D=40,
        nFES=100,
        nRuns=1,
        useAlgorithms=["HybridBatAlgorithm"],
        useBenchmarks=["rastrigin"])
    runner.run()
    print(runner.results)
