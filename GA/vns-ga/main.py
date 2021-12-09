import re
import sys
import time
import progressbar

from argparse import ArgumentParser, ArgumentTypeError
from pathlib import Path

from mtsp.vertex import Vertex
from mtsp.population import Population
from mtsp.galogic import GA

NUM_GENERATIONS = 5000

def parse_args():
    '''parse arguments'''
    parser = ArgumentParser(description='VNS-GA for mTSP')
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


def init_graph(input_path):
    '''initialize graph as input'''
    graph = list()
    coordPattern = re.compile(r'^(?P<idx>\d+) (?P<x>\d+) (?P<y>\d+)$')

    fp = open(input_path, 'r')
    for line in fp.read().splitlines()[1:]:
        matcher = coordPattern.match(line)
        if matcher is None:
            continue
        x = int(matcher.groupdict()['x'])
        y = int(matcher.groupdict()['y'])
        graph.append(Vertex(x, y))

    fp.close()
    return graph


def main() -> int:
    args = parse_args()

    graph = init_graph(args.input)
    pop = Population(args.pop, args.sales, graph)
    pop.init_polar_coord()

    global_route = pop.get_fittest()
    print(f'Initial minimum distance: {global_route.get_dist()}')

    start_time = time.time()
    pbar = progressbar.ProgressBar()
    for _ in pbar(range(NUM_GENERATIONS)):
        local_route = GA.evolve_population(pop)
        if global_route.get_dist() > local_route.get_dist():
            global_route = local_route
    
    print(f'Global minimum distance: {global_route.get_dist()}')
    print(f'Running time: {time.time() - start_time}s')
    print(global_route)

    return 0


if __name__ == '__main__':
    sys.exit(main())