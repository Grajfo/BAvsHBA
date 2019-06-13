from Statistics import Statistics as st
from Excel import Excel as ex
from NiaPy.task.task import StoppingTask, OptimizationType
from NiaPy.algorithms.basic import BatAlgorithm
from NiaPy.algorithms.modified import HybridBatAlgorithm
import randomGenerator as rg
from NiaPy.runner import Runner

dimension = [10, 20, 30]
usebenchmarks = [
    'schwefel',
    'happyCat',
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
        for dim in dimension:
            temp_list = []
            for best in range(25):
                task = StoppingTask(D=dim, nFES=dim*1000, optType=OptimizationType.MINIMIZATION, benchmark=bench)
                algo = BatAlgorithm(NP=15, A=0.5, r=0.5, Qmin=0.0, Qmax=2.0)
                best = algo.run(task=task)
                temp_list.append(best[1])

            print(str(bench) + str(dim))
            bat_values = st(array=temp_list,
                            algorithm_name="BatAlgorithm",
                            benchmark_name=bench,
                            dimension_name=str(dim)
                            ).vrniTupleDim()
            statistic_bat_algorithm.append(bat_values)

    excel = ex()
    bat_data_frame = excel.tableToDataFrame(statistic_bat_algorithm)
    excel.export_to_sheets(bat_data_frame, filename)


def hybrid_comparison_by_benchmarks(filename):

    statistic_hybrid_bat_algorithm = []
    for bench in usebenchmarks:
        for dim in dimension:
            temp_list = []
            for best in range(25):
                task = StoppingTask(D=dim, nFES=dim*1000, optType=OptimizationType.MINIMIZATION, benchmark=bench)
                algo = HybridBatAlgorithm(NP=15, A=0.5, r=0.5, F=0.5, CR=0.9, Qmin=0.0, Qmax=2.0)
                best = algo.run(task=task)
                temp_list.append(best[1])

            print(str(bench) + str(dim))
            hybrid_bat_values = st(array=temp_list,
                                   algorithm_name="HybridBatAlgorithm",
                                   benchmark_name=bench,
                                   dimension_name=str(dim)
                                   ).vrniTupleDim()
            statistic_hybrid_bat_algorithm.append(hybrid_bat_values)

    excel = ex()
    bat_data_frame = excel.tableToDataFrame(statistic_hybrid_bat_algorithm)
    excel.export_to_sheets(bat_data_frame, filename)


def comparison_by_runner(filename):
    statistic_bat_algorithm = []

    runner = Runner(
        D=40,
        NP=15,
        nFES=10*1000,
        nRuns=1,
        useAlgorithms=["BatAlgorithm", "HybridBatAlgorithm"],
        useBenchmarks=usebenchmarks
    )
    best = runner.run(verbose=True)

    for key, value in best.items():
        for key1, value2 in value():
            if key == "BatAlgorithm":
                bat_values = st(array=value2, algorithm_name=key,
                                benchmark_name=key1, dimension_name="10"
                                ).vrniTupleDim()
                statistic_bat_algorithm.append(bat_values)

        excel = ex()
        bat_data_frame = excel.tableToDataFrame(statistic_bat_algorithm)
        excel.export_to_sheets(bat_data_frame, filename)


if __name__ == '__main__':

    #bat_comparison_by_benchmark("BA" + str(rg.random_digit(6)))
    hybrid_comparison_by_benchmarks("HBA" + str(rg.random_digit(6)))
