import random

from mtsp.utils import *
from mtsp.route import Route

MUTATE_RATE = 0.02

class GA:
    @classmethod
    def evolve_population(self, pop):
        '''single evolution iteration'''
        for idx in range(int(pop.pop_size / 4)):
            parent_1 = pop.get_route(2 * idx)
            parent_2 = pop.get_route(2 * idx + 1)
            offspring = self.cross_over(parent_1, parent_2)
            offspring = self.mutate(offspring)
            pop.add_route(offspring)
        return pop.get_fittest()


    @classmethod
    def cross_over(self, parent1, parent2):
        '''neighbor action-1'''
        graph = parent1.graph
        parent1 = self.merge_route(parent1)
        parent2 = self.merge_route(parent2)
        # gene fragment from parent 1
        offspring = [0] * len(parent1)
        start_pos, end_pos = double_rand(0, len(parent1))
        for i in range(start_pos, end_pos):
            offspring[i] = parent1[i]
        # other gene from parent 2 in sequence
        idx = 0
        for i in range(len(parent2)):
            val = parent2[i]
            if val not in offspring:
                if idx == start_pos:
                    idx = end_pos
                offspring[idx] = val
                idx += 1
        
        return Route(self.splite_route(offspring, len(graph)), graph)


    @classmethod
    def mutate(self, offspring):
        '''neighbor action-2'''
        if random.random() > MUTATE_RATE:
            return offspring
        idx1, idx2 = double_rand(0, len(offspring.routes) - 1)
        route1 = offspring.routes[idx1]
        route2 = offspring.routes[idx2]

        mutate_num = random.randint(0, min(len(route1), len(route2))-1)
        # swap specific genes
        for _ in range(mutate_num):
            rand_idx1 = random.randint(1, len(route1)-1)
            rand_idx2 = random.randint(1, len(route2)-1)

            tmp = route1[rand_idx1]
            route1[rand_idx1] = route2[rand_idx2]
            route2[rand_idx2] = tmp

        offspring.set_route(route1, idx1)
        offspring.set_route(route2, idx2)
        return offspring


    @classmethod
    def merge_route(self, parent):
        '''tool function for crossover'''
        merge_route = list()
        # fill incremental id as segmentation
        fill_id = len(parent.graph)
        for i, route in enumerate(parent.routes):
            if i > 0:
                merge_route.append(fill_id)
                fill_id += 1
            merge_route.extend(route)
        return merge_route
    

    @classmethod
    def splite_route(self, offspring, fill_id):
        '''tool function for crossover'''
        routes, middle = list(), list()
        for idx in offspring:
            # check the segmentation
            if idx >= fill_id:
                routes.append(middle.copy())
                middle.clear()
                continue
            middle.append(idx)
        routes.append(middle.copy())
        return routes
