import time
from argparse import ArgumentParser, ArgumentTypeError
from pathlib import Path

from mtsp.ga import *
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
    parser.add_argument('-t', '--time', type=int, default=300,
                        help='Max running time')
    return parser.parse_args()


def valid_path(path: str) -> Path:
    try:
        abspath = Path(path)
    except Exception as e:
        raise ArgumentTypeError(f'Invalid input path: {path}') from e
    if not abspath.exists():
        raise ArgumentTypeError(f'{abspath} not exist')
    return abspath.resolve()


def ga_start(max_iters, max_time, graph):

    global start_time

    min_nodes = N / 20
    max_nodes = N / 2
    #     max_nodesodes = Nonex
    populations, breaks = generate_populations(POPULATION, N, M, min_nodes, max_nodes)
    global_best = sys.maxsize

    fitness_val = []
    print("min:{}, max:{}".format(min_nodes, max_nodes))
    for i in range(max_iters):
        if time.time() - start_time >= max_time:
            break

        fitness_list = [cal_fitness(populations[j], breaks[j], N, row_data, graph) for j in range(POPULATION)]

        global_best = min(global_best, min(fitness_list))

        populations, breaks = IPGA(populations, breaks, fitness_list, N, M, min_nodes, max_nodes)

    print("Global minimum distance: {}".format(global_best))

    fitness_list = [cal_fitness(populations[j], breaks[j], N, row_data, graph) for j in range(POPULATION)]

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

def cal_graph(row_data):
    n = len(row_data)

    graph = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            edge = cal_dis(row_data[i], row_data[j])
            graph[i][j] = edge
            graph[j][i] = edge

    return graph

def main():
    global N, M, POPULATION, row_data, start_time, graph
    start_time = time.time()
    args = parse_args()
    POPULATION, M, max_time = args.pop, args.sales, args.time

    file_path_tmp = args.input
    row_data = load_data(file_path_tmp)
    graph = cal_graph(row_data)
    N = len(row_data)

    time_start = time.time()

    ga_start(MAX_ITERS, max_time, graph)

    time_end = time.time()
    print(f'Running time: {time_end - time_start}s')


MAX_ITERS = 20000
RUNS = 1
file_path_tmp = "../../data/mtsp51.txt"
row_data = []
graph = []
N = len(row_data)
M = 5
POPULATION = 100
start_time = 0

if __name__ == "__main__":
    sys.exit(main())
