from Statistics import Statistics as st
from Excel import Excel as ex
import randomGenerator as rg
from NiaPy.runner import Runner
import itertools
import collections


dimension = [10]
np = [20, 50]
combined = list(itertools.product(dimension, np))


def comparison_by_runner(filename):
    statistic_bat_algorithm = []
    hybrid_statistic_bat_algorithm = []

    for x, y in combined:
        valuesBA = collections.defaultdict(list)
        valuesHBA = collections.defaultdict(list)
        for i in range(5):
            runner = Runner(
                D=x,
                NP=y,
                nFES=x*1000,
                nRuns=1,
                useAlgorithms=["BatAlgorithm", "HybridBatAlgorithm"],
                useBenchmarks=["sphere", "levy", "rosenbrock"]
            )
            runner.run(verbose=True)
            best = runner.results

            for benchmark, values in best.get("BatAlgorithm").items():
                valuesBA[benchmark].append(values[0][1])
            for benchmark, values in best.get("HybridBatAlgorithm").items():
                valuesHBA[benchmark].append(values[0][1])

            print(valuesBA)
            print(valuesHBA)

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
    comparison_by_runner("BA&HBA" + str(rg.random_digit(6)))
