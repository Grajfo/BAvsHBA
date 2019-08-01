from NiaPy import Runner
from Statistics import Statistics as st
from Excel import Excel as ex
import itertools



dimension = [10, 20, 30]
np = [20, 30, 50]
combined = list(itertools.product(dimension, np))


def comparison_by_runner(filename):
    statistic_bat_algorithm = []
    for x, y in combined:
        runner = Runner(
            D=x,
            NP=y,
            nFES=x*1000,
            nRuns=1,
            useAlgorithms=["BatAlgorithm"],
            useBenchmarks=["schwefel"]
            )
        runner.run(verbose=True)
        best = runner.results
        print(next(iter(best)))

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
                    statistic_bat_algorithm.append(hybrid_bat_values)

    excel = ex()
    bat_data_frame = excel.tableToDataFrame(statistic_bat_algorithm)
    excel.export_to_sheets(bat_data_frame, filename)


if __name__ == '__main__':
   comparison_by_runner("testiramo")

