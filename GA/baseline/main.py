import re
import sys
import time
import progressbar
# import matplotlib.pyplot as plt

from argparse import ArgumentParser, ArgumentTypeError
from pathlib import Path
from mtsp.galogic import *


def parse_args():
    parser = ArgumentParser(description='Baseline GA for mTSP')
    parser.add_argument('-i', '--input', type=valid_path, required=True,
                        help='Path of the test input')
    return parser.parse_args()


def valid_path(path: str) -> Path:
    try:
        abspath = Path(path)
    except Exception as e:
        raise ArgumentTypeError(f'Invalid input path: {path}') from e
    if not abspath.exists():
        raise ArgumentTypeError(f'{abspath} not exist')
    return abspath.resolve()


def main() -> int:
    args = parse_args()
    
    # Add Dustibins    
    coordPattern = re.compile(r'^(?P<idx>\d+) (?P<x>\d+) (?P<y>\d+)$')
    with open(args.input, 'r') as fp:
        for line in fp.read().splitlines()[1:]:
            matcher = coordPattern.match(line)
            if matcher is None:
                continue
            x = int(matcher.groupdict()['x'])
            y = int(matcher.groupdict()['y'])
            RouteManager.addDustbin(Dustbin(x, y))
            
    yaxis = list() # Fittest value (distance)
    xaxis = list() # Generation count
    
    pop = Population(populationSize, True)
    globalRoute = pop.getFittest()
    print ('Initial minimum distance: ' + str(globalRoute.getDistance()))
    
    start_time = time.time()
    # Start evolving
    pbar = progressbar.ProgressBar()
    for i in pbar(range(numGenerations)):
        pop = GA.evolvePopulation(pop)
        localRoute = pop.getFittest()
        if globalRoute.getDistance() > localRoute.getDistance():
            globalRoute = localRoute
        yaxis.append(localRoute.getDistance())
        xaxis.append(i)
    
    print ('Global minimum distance: ' + str(globalRoute.getDistance()))
    print (f'Running time: {(time.time() - start_time)}s')
    print ('Final Route: ' + globalRoute.toString())

    # fig = plt.figure()
    # plt.plot(xaxis, yaxis, 'r-')
    # plt.show()
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
