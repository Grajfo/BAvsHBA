from Statistics import Statistics as st
from Excel import Excel as ex
from NiaPy.task.task import StoppingTask, OptimizationType
from NiaPy.algorithms.basic import BatAlgorithm
from NiaPy.algorithms.modified import HybridBatAlgorithm
import randomGenerator as rg
from NiaPy.runner import Runner
import itertools
import collections

dimension = [10, 20, 30]
np = [20, 30, 50]
combined = list(itertools.product(dimension, np))

usebenchmarks = [
    'schwefel',
    'levy',
    'ackley',
    'sphere',
    'rosenbrock',
    'rastrigin',
    'griewank',
    'ridge',
    'salomon',
    'whitley'
]


def bat_comparison_by_benchmark(filename):
    statistic_bat_algorithm = []
    for bench in usebenchmarks:
        for x, y in combined:
            temp_list = []
            for best in range(25):
                task = StoppingTask(D=x, nFES=x*1000, optType=OptimizationType.MINIMIZATION, benchmark=bench)
                algo = BatAlgorithm(NP=y, A=0.5, r=0.5, Qmin=0.0, Qmax=2.0)
                best = algo.run(task=task)
                temp_list.append(best[1])

            print(str(x) + " " + str(y) + " " + str(temp_list))
            bat_values = st(array=temp_list,
                            benchmark_name=bench,
                            Np=str(y),
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
                algo = HybridBatAlgorithm(NP=y, F=0.50, CR=0.90)
                best = algo.run(task=task)
                temp_list.append(best[1])

            print(str(x) + " " + str(y) + " " + str(temp_list))
            hybrid_bat_values = st(array=temp_list,
                                   benchmark_name=bench,
                                   Np=str(y),
                                   dimension_name=str(x)
                                   ).vrniTupleDim()
            statistic_hybrid_bat_algorithm.append(hybrid_bat_values)

    excel = ex()
    bat_data_frame = excel.tableToDataFrame(statistic_hybrid_bat_algorithm)
    excel.export_to_sheets(bat_data_frame, filename)


def comparison_by_runner(filename):
    statistic_bat_algorithm = []
    hybrid_statistic_bat_algorithm = []

    for x, y in combined:
        valuesBA = collections.defaultdict(list)
        valuesHBA = collections.defaultdict(list)
        for i in range(25):
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

            for benchmark, values in best.get("BatAlgorithm").items():
                valuesBA[benchmark].append(values[0][1])
            for benchmark, values in best.get("HybridBatAlgorithm").items():
                valuesHBA[benchmark].append(values[0][1])

        for bench, values in valuesBA.items():
            bat_values = st(array=values, algorithm_name="BA",
                            benchmark_name=bench, dimension_name=str(x), Np=str(y)
                            ).vrniTupleDim()
            statistic_bat_algorithm.append(bat_values)

        for bench, values in valuesHBA.items():
            hybrid_bat_values = st(array=values, algorithm_name="HBA",
                                   benchmark_name=bench, dimension_name=str(x), Np=str(y)
                                   ).vrniTupleDim()
            hybrid_statistic_bat_algorithm.append(hybrid_bat_values)

    excel = ex()
    bat_data_frame = excel.tableToDataFrame(statistic_bat_algorithm)
    hbat_data_frame = excel.tableToDataFrame(hybrid_statistic_bat_algorithm)
    combined_df = bat_data_frame.append(hbat_data_frame, ignore_index=True)

    sorted_df = combined_df.sort_values(by=['Bench.', 'Meas.'])
    excel.export_to_sheets(sorted_df, filename)


if __name__ == '__main__':
    comparison_by_runner("BA%HBA" + str(rg.random_digit(6)))

