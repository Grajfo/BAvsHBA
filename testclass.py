from NiaPy import Runner
from NiaPy.algorithms.modified import HybridBatAlgorithm
from NiaPy.algorithms.basic import BatAlgorithm
from NiaPy.task.task import StoppingTask, OptimizationType
from NiaPy.benchmarks import Benchmark
import run


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
                            benchmark=run.BatAlgorithmBenchmarkA())
        algo = BatAlgorithm()
        best = algo.run(task=task)
        print(best)


if __name__ == '__main__':
    runner = Runner(
        D=20,
        nFES=1000*20,
        nRuns=1,
        useAlgorithms=["BatAlgorithm", "HybridBatAlgorithm"],
        useBenchmarks=[run.BatAlgorithmBenchmarkQmin(), run.BatAlgorithmBenchmarkQmax(), run.BatAlgorithmBenchmarkNp(),
                       run.BatAlgorithmBenchmarkA(), run.BatAlgorithmBenchmarkr()])
    runner.run()
