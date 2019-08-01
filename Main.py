from Statistics import Statistics as st
from Excel import Excel as ex
from NiaPy.task.task import StoppingTask, OptimizationType
from NiaPy.algorithms.basic import BatAlgorithm
from NiaPy.algorithms.modified import HybridBatAlgorithm
import randomGenerator as rg
from NiaPy.runner import Runner
import itertools

dimension = [10, 20, 30]
np = [20, 30, 50]
combined = list(itertools.product(dimension, np))


usebenchmarks = [
    'schwefel',
    'xin-She',
    'ackley',
    'whitley',
    'rosenbrock',
    'rastrigin',
    'griewank',
    'ridge',
    'salomon',
    'sphere'
]


def bat_comparison_by_benchmark(filename):
    statistic_bat_algorithm = []
    for bench in usebenchmarks:
        for x, y in combined:
            temp_list = []
            for best in range(25):
                task = StoppingTask(D=x, nFES=x*1000, optType=OptimizationType.MINIMIZATION, benchmark=bench)
                algo = HybridBatAlgorithm(NP=y, A=0.5, r=0.5, Qmin=0.0, Qmax=2.0)
                best = algo.run(task=task)
                temp_list.append(best[1])

            bat_values = st(array=temp_list,
                            algorithm_name="BatAlgorithm",
                            benchmark_name=bench,
                            Np=y,
                            dimension_name=str(x)
                            ).vrniTupleDim()
            statistic_bat_algorithm.append(bat_values)

    excel = ex()
    bat_data_frame = excel.tableToDataFrame(statistic_bat_algorithm)
    excel.export_to_sheets(bat_data_frame, filename)


def hybrid_comparison_by_benchmarks(filename):

    statistic_hybrid_bat_algorithm = []
    for bench in usebenchmarks:
        for x, y in combined:
            temp_list = []
            for best in range(25):
                task = StoppingTask(D=x, nFES=x*1000, optType=OptimizationType.MINIMIZATION, benchmark=bench)
                algo = HybridBatAlgorithm(NP=y, A=0.5, r=0.5, F=0.5, CR=0.9, Qmin=0.0, Qmax=2.0)
                best = algo.run(task=task)
                temp_list.append(best[1])

            hybrid_bat_values = st(array=temp_list,
                                   algorithm_name="HybridBatAlgorithm",
                                   benchmark_name=bench,
                                   Np=y,
                                   dimension_name=str(x)
                                   ).vrniTupleDim()
            statistic_hybrid_bat_algorithm.append(hybrid_bat_values)

    excel = ex()
    bat_data_frame = excel.tableToDataFrame(statistic_hybrid_bat_algorithm)
    excel.export_to_sheets(bat_data_frame, filename)


def comparison_by_runner(filename):
    statistic_bat_algorithm = []
    statistic_hybrid_bat_algorithm = []

    for x, y in combined:
        runner = Runner(
            D=x,
            NP=y,
            nFES=x*1000,
            nRuns=1,
            useAlgorithms=["BatAlgorithm", "HybridBatAlgorithm"],
            useBenchmarks=usebenchmarks
        )
        runner.run(verbose=True)
        best = runner.results
        for algorithm, array in best.items():
            for benchmark, value in array.items():
                if algorithm == "BatAlgorithm":
                    bat_values = st(array=value[0][0], algorithm_name="BatAlgorithm",
                                    benchmark_name=benchmark, dimension_name=x, Np=y
                                    ).vrniTupleDim()
                    statistic_bat_algorithm.append(bat_values)
                elif algorithm == "HybridBatAlgorithm":
                    hybrid_bat_values = st(array=value[0][0], algorithm_name="HybridBatAlgorithm",
                                           benchmark_name=benchmark, dimension_name=x, Np=y
                                           ).vrniTupleDim()
                    statistic_hybrid_bat_algorithm.append(hybrid_bat_values)

    excel = ex()
    bat_data_frame = excel.tableToDataFrame(statistic_bat_algorithm)
    hybrid_bat_data_frame = excel.tableToDataFrame(statistic_hybrid_bat_algorithm)

    excel.export_to_sheets(bat_data_frame, filename, BatAlgorithm)
    excel.export_to_sheets(hybrid_bat_data_frame, filename, HybridBatAlgorithm)


if __name__ == '__main__':
  comparison_by_runner("BA&HBA" + str(rg.random_digit(6)))
