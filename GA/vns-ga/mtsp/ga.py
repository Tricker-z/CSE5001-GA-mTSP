
import random

from mtsp.route import Route


class GA:

    @classmethod
    def evolve_population(self, pop):

        for idx in range(int(pop.pop_size / 4)):
            parent_1 = pop.get_route(2 * idx)
            parent_2 = pop.get_route(2 * idx + 1)
            offspring = self.cross_over(parent_1, parent_2)
            pop.add_route(offspring)


    @classmethod
    def cross_over(self, parent_1, parent_2):
        parent1 = parent_1.merge_routes()
        parent2 = parent_2.merge_routes()

        start_pos, end_pos = 0, 0
        while (start_pos >= end_pos):
            start_pos = random.randint(0, len(parent1))
            end_pos   = random.randint(0, len(parent1))
        
        child = [0] * len(parent1)
        for i in range(start_pos, end_pos):
            child[i] = parent1[i]
        
        child_idx = 0
        for i in range(len(parent2)):
            val = parent2[i]
            if val not in child:
                if child_idx == start_pos:
                    child_idx = end_pos
                child[child_idx] = val
                child_idx += 1
        
        return Route(parent_1.splite_route(child),
                     parent_1.graph)


    @classmethod
    def mutate(self):
        pass