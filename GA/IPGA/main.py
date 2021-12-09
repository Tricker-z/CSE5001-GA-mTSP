import time
from argparse import ArgumentParser, ArgumentTypeError
from pathlib import Path

from GA.IPGA.mtsp.ga import *
from mtsp.utils import *


def parse_args():
    '''parse arguments'''
    parser = ArgumentParser(description='IPGA for mTSP')
    parser.add_argument('-i', '--input', type=valid_path, required=True,
                        help='Path of the test input')
    parser.add_argument('-n', '--pop', type=int, default=100,
                        help='Population size')
    parser.add_argument('-m', '--sales', type=int, default=5,
                        help='Number of salesmen')
    return parser.parse_args()


def valid_path(path: str) -> Path:
    try:
        abspath = Path(path)
    except Exception as e:
        raise ArgumentTypeError(f'Invalid input path: {path}') from e
    if not abspath.exists():
        raise ArgumentTypeError(f'{abspath} not exist')
    return abspath.resolve()


def ga_start(max_iters):
    min_nodes = 2
    max_nodes = 30
    #     max_nodesodes = None
    populations, breaks = generate_populations(POPULATION, N, M, min_nodes, max_nodes)
    global_best = sys.maxsize

    fitness_val = []
    # print("min:{}, max:{}".format(min_nodes, max_nodes))
    for i in range(max_iters):
        fitness_list = [cal_fitness(populations[j], breaks[j], N, row_data) for j in range(POPULATION)]

        global_best = min(global_best, min(fitness_list))

        populations, breaks = IPGA(populations, breaks, fitness_list, N, M, min_nodes, max_nodes)

    print("Global minimum distance: {}".format(global_best))

    fitness_list = [cal_fitness(populations[j], breaks[j], N, row_data) for j in range(POPULATION)]

    minus_tmp = fitness_list[0]
    index_best = 0
    for i in range(len(fitness_list)):
        if minus_tmp < fitness_list[i]:
            minus_tmp = fitness_list[i]
            index_best = i
    population = populations[index_best]
    break_point = breaks[index_best]

    paths = [0] + break_point + [N]
    print("Route:")
    for i in range(len(paths) - 1):
        print("salesman-{}:".format(i), end="")
        begin = paths[i]  # include
        end = paths[i + 1]  # not include

        print(row_data[0], end="")

        for j in range(begin, end):
            print(row_data[population[j]], end="")

        print(row_data[0])


def main():
    global N, M, POPULATION, row_data

    args = parse_args()
    POPULATION, M = args.pop, args.sales

    file_path_tmp = args.input
    row_data = load_data(file_path_tmp)
    N = len(row_data)

    time_start = time.time()

    for i in range(RUNS):
        ga_start(MAX_ITERS)

    time_end = time.time()
    print("Running time: ", (time_end - time_start))


MAX_ITERS = 20000
RUNS = 1
file_path_tmp = "../../data/mtsp51.txt"
row_data = []
N = len(row_data)
M = 5
POPULATION = 100

if __name__ == "__main__":
    sys.exit(main())
