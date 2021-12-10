import random
import sys

from mtsp.mutation import *
from mtsp.utils import *


def generate_breaks(n, m, min_nodes, max_nodes=None):
    '''generate and return a the new breakpoints based on the rules'''

    #     breakpoints = sorted(random.sample(range(n), m - 1))

    valid = False
    while valid is False:
        valid = True
        # rule 1: sorted as ascending order for the breakpoints
        breakpoints = sorted(random.sample(range(n), m - 1))

        # rule 2: the first route segment should not less than the minimum depots
        if breakpoints[0] < min_nodes or (max_nodes is not None and breakpoints[0] > max_nodes):
            valid = False
            continue

        # rule 3: each route segment should not less than the minimum depots
        for i in range(0, len(breakpoints) - 1):
            if breakpoints[i + 1] - breakpoints[i] < min_nodes or (
                    max_nodes is not None and breakpoints[i + 1] - breakpoints[i] > max_nodes):
                valid = False
                break

        if not valid:
            continue

        # rule 4: the last route segment should not less than the minimum depots
        if n - breakpoints[-1] < min_nodes or (max_nodes is not None and n - breakpoints[-1] > max_nodes):
            valid = False

    return breakpoints


def generate_populations(population_size, n, m, min_nodes, max_nodes=None):
    '''generate the populations and corresponding breakpoints'''

    # random generate populations and breakpoints, each breakpoints has a length of m - 1
    populations = [random.sample(range(n), n) for i in range(population_size)]
    breaks = [generate_breaks(n, m, min_nodes, max_nodes) for i in range(population_size)]
    return populations, breaks


def cal_fitness(population, break_points, n, row_data, graph):
    '''calculate the fitness value of each population individual'''

    paths = [0] + break_points + [n]
    fitness_tmp = 0
    for i in range(len(paths) - 1):
        begin = paths[i]  # include
        end = paths[i + 1]  # not include
        tmp_index = 0
        for j in range(begin, end):
            # fitness value is the sum of distance for each salesman
            fitness_tmp += graph[tmp_index][population[j]]
            tmp_index = population[j]
        fitness_tmp += graph[0][tmp_index]
    return fitness_tmp


def IPGA(populations, breaks, fitness_list, n, m, min_nodes, max_nodes):
    '''run the IPGA algorithm'''

    offspring = []
    breaks_offspring = []

    shuffle = random.sample(range(len(populations)), len(populations))

    for i in range(0, len(populations), 10):
        ij = sorted(random.sample(range(n), 2))
        p = random.randint(0, n)

        index_tmp = shuffle[i:i + 10]
        minus = sys.maxsize
        index_best = -1

        for j in range(10):
            index = index_tmp[j]

            if fitness_list[index] <= minus:
                minus = fitness_list[index]
                index_best = index

        best_populations = [copy.deepcopy(populations[index_best]) for j in range(10)]
        breaks_offspring_tmp = [copy.deepcopy(breaks[index_best]) for j in range(10)]

        # 1. do nothing for the first offspring

        # 2. FlipInsert for the second offspring
        flip_insert(best_populations[1], ij, p)

        # 3. SwapInsert for the third offspring
        swap_insert(best_populations[2], ij, p)

        # 4. LSlideInsert for the fourth offspring

        left_lide_insert(best_populations[3], ij, p)

        # 5. RSlideInsert for the fifth offspring
        right_lide_insert(best_populations[4], ij, p)

        # 6.modify breakpoints for the sixth offspring
        breaks_offspring_tmp[5] = generate_breaks(n, m, min_nodes, max_nodes)

        # 7. modify breakpoints and FlipInsert for the seventh offspring
        flip_insert(best_populations[6], ij, p)
        breaks_offspring_tmp[6] = generate_breaks(n, m, min_nodes, max_nodes)

        # 8. modify breakpoints and SwapInsert for the eighth offspring
        swap_insert(best_populations[7], ij, p)
        breaks_offspring_tmp[7] = generate_breaks(n, m, min_nodes, max_nodes)

        # 9. modify breakpoints and LSlideInsert for the ninth offspring
        left_lide_insert(best_populations[8], ij, p)
        breaks_offspring_tmp[8] = generate_breaks(n, m, min_nodes, max_nodes)

        # 10. modify breakpoints and RSlideInsert for the tenth offspring
        right_lide_insert(best_populations[9], ij, p)
        breaks_offspring_tmp[9] = generate_breaks(n, m, min_nodes, max_nodes)

        breaks_offspring += [copy.deepcopy(breaks_offspring_tmp[t]) for t in range(len(breaks_offspring_tmp))]
        offspring = offspring + [copy.deepcopy(best_populations[t]) for t in range(len(best_populations))]

    return offspring, breaks_offspring
