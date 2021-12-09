import random

from mtsp.utils import *
from mtsp.route import Route


class Population:
    def __init__(self, pop_size, sales_num, graph):
        self.graph = graph
        self.pop_size = pop_size   
        self.routes = list()
        self.sales_num = sales_num

    def init_polar_coord(self):
        '''polar coordinate classification'''
        vetex_angle = list()
        for idx, v in enumerate(self.graph[1:], 1):
            angle = clockwise_angle(v, self.graph[0])
            vetex_angle.append((idx, angle))
        
        routes_base = [idx for idx, _ in sorted(vetex_angle, key=lambda x: x[1])]
        routes_base = split_list(routes_base, self.sales_num)
        self.routes.append(Route(routes_base, self.graph))
        
        while len(self.routes) < self.pop_size:
            routes_variant = list()
            for route in routes_base:
                route_cpy = route.copy()
                random.shuffle(route_cpy)
                routes_variant.append(route_cpy)
            self.routes.append(Route(routes_variant, self.graph))

    def get_fittest(self):
        self.routes.sort(key=lambda x: x.get_fitness(), reverse=True)
        self.routes = self.routes[:self.pop_size]
        return self.routes[0]

    def add_route(self, route):
        self.routes.append(route)

    def get_route(self, idx):
        return self.routes[idx]
