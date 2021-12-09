class Route:
    def __init__(self, routes, graph):
        self.routes  = routes
        self.graph   = graph
        self.v_start = graph[0]
        self.dist    = self.route_dist()
    
    def route_dist(self):
        total_dist = 0
        for route in self.routes:
            if len(route) == 0:
                continue
            for idx in range(len(route)):
                if idx < len(route) - 1:
                    total_dist += self.graph[route[idx]].distanceTo(self.graph[route[idx + 1]])
            total_dist += self.v_start.distanceTo(self.graph[route[0]])
            total_dist += self.v_start.distanceTo(self.graph[route[idx]])
        return total_dist

    def get_dist(self):
        return self.dist

    def get_fitness(self):
        return 10000 / self.dist

    def set_route(self, route, idx):
        self.routes[idx] = route

    def __str__(self):
        res = 'Route:\n'
        for i, route in enumerate(self.routes, 1):
            res += f'salesman-{i}:'
            res += str(self.v_start)
            for coord in route:
                res += str(self.graph[coord])
            res += f'{self.v_start}\n'
        return res
