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
        angle_list = list()
        for idx, v in enumerate(self.graph[1:], 1):
            angle = clockwise_angle(v, self.graph[0])
            angle_list.append((idx, angle))
        
        routes_idx = [idx for idx, _ in sorted(angle_list, key=lambda x: x[1])]
        routes_base = split_list(routes_idx, self.sales_num)
        self.routes.append(Route(routes_base, self.graph))
        
        while len(self.routes) < self.pop_size:
            route = list()
            for r in routes_base:
                r = r.copy()
                random.shuffle(r)
                route.append(r)
            self.routes.append(Route(route, self.graph))
    
    
    def get_fittest(self):
        self.routes.sort(key=lambda x: x.get_fitenss(), reverse=True)
        self.routes = self.routes[:self.pop_size]
        return self.routes[0]        
    

    def add_route(self, route):
        self.routes.append(route)


    def get_route(self, idx):
        return self.routes[idx]

    

        