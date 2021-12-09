import random
import sys

from mtsp.mutation import *
from mtsp.utils import *


def generate_breaks(n, m, min_nodes, max_nodes=None):
    #     breakpoints = sorted(random.sample(range(n), m - 1))

    valid = False
    while valid is False:
        valid = True
        #         sorted
        breakpoints = sorted(random.sample(range(n), m - 1))

        #          first
        if breakpoints[0] < min_nodes or (max_nodes is not None and breakpoints[0] > max_nodes):
            valid = False
            continue

        #         middle
        for i in range(0, len(breakpoints) - 1):
            if breakpoints[i + 1] - breakpoints[i] < min_nodes or (
                    max_nodes is not None and breakpoints[i + 1] - breakpoints[i] > max_nodes):
                valid = False
                break

        if not valid:
            continue
        # last
        if n - breakpoints[-1] < min_nodes or (max_nodes is not None and n - breakpoints[-1] > max_nodes):
            valid = False

    return breakpoints


def generate_populations(population_size, n, m, min_nodes, max_nodes=None):
    populations = [random.sample(range(n), n) for i in range(population_size)]
    breaks = [generate_breaks(n, m, min_nodes, max_nodes) for i in range(population_size)]
    return populations, breaks


def cal_fitness(population, break_points, n, row_data):
    paths = [0] + break_points + [n]
    fitness_tmp = 0
    for i in range(len(paths) - 1):
        begin = paths[i]  # include
        end = paths[i + 1]  # not include
        tmp_index = 0
        for j in range(begin, end):
            fitness_tmp += cal_dis(row_data[population[j]], row_data[tmp_index])
            tmp_index = population[j]
        fitness_tmp += cal_dis(row_data[0], row_data[tmp_index])
    return fitness_tmp


def IPGA(populations, breaks, fitness_list, n, m, min_nodes, max_nodes):
    #     print("-------------------IPGA----------------------")
    #     print('in IPGA',min(fitness_list))
    best_index_global = 0
    for i in range(len(fitness_list)):
        if fitness_list[i] == min(fitness_list):
            best_index_global = i

    #     fitness_list_tmp = [cal_fitness(populations[j], breaks[j], N) for j in range(POPULATION)]
    #     print('in IPGA Cal',min(fitness_list_tmp))
    offspring = []
    breaks_offspring = []

    #     print("********************shuffle****************")

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

        #         1, nothing

        #         2. FlipInsert
        flip_insert(best_populations[1], ij, p)

        #         3. SwapInsert
        swap_insert(best_populations[2], ij, p)

        #         4. LSlideInsert

        left_lide_insert(best_populations[3], ij, p)

        #         5. RSlideInsert
        right_lide_insert(best_populations[4], ij, p)

        #         6.modify breaks
        breaks_offspring_tmp[5] = generate_breaks(n, m, min_nodes, max_nodes)

        #         7. breaks + flip
        flip_insert(best_populations[6], ij, p)
        breaks_offspring_tmp[6] = generate_breaks(n, m, min_nodes, max_nodes)

        #         8. breaks + swap
        swap_insert(best_populations[7], ij, p)
        breaks_offspring_tmp[7] = generate_breaks(n, m, min_nodes, max_nodes)

        #         9. breaks + left slide
        left_lide_insert(best_populations[8], ij, p)
        breaks_offspring_tmp[8] = generate_breaks(n, m, min_nodes, max_nodes)

        #         10. breaks + right slide
        right_lide_insert(best_populations[9], ij, p)
        breaks_offspring_tmp[9] = generate_breaks(n, m, min_nodes, max_nodes)

        breaks_offspring += [copy.deepcopy(breaks_offspring_tmp[t]) for t in range(len(breaks_offspring_tmp))]
        offspring = offspring + [copy.deepcopy(best_populations[t]) for t in range(len(best_populations))]

    return offspring, breaks_offspring
