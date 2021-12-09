import copy


def flip_insert(population, ij, p):
    population_tmp = copy.deepcopy(population[ij[0]:ij[1] + 1])
    population_tmp.reverse()

    del population[ij[0]:ij[1] + 1]

    population[p: p] = population_tmp


def swap_insert(population, ij, p):
    population_tmp = copy.deepcopy(population[ij[0]:ij[1] + 1])
    population_tmp[0], population_tmp[-1] = population_tmp[-1], population_tmp[0]

    del population[ij[0]:ij[1] + 1]

    population[p: p] = population_tmp


def left_lide_insert(population, ij, p):
    population_tmp = copy.deepcopy(population[ij[0]:ij[1] + 1])
    population_tmp.append(population_tmp.pop(0))

    del population[ij[0]:ij[1] + 1]

    population[p: p] = population_tmp


def right_lide_insert(population, ij, p):
    population_tmp = copy.deepcopy(population[ij[0]:ij[1] + 1])
    population_tmp.insert(0, population_tmp.pop(0))

    del population[ij[0]:ij[1] + 1]

    population[p: p] = population_tmp
