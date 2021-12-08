class Route:
    def __init__(self, routes, graph):
        self.routes  = routes
        self.graph   = graph
        self.v_start = graph[0]
        self.dist    = self.route_dist()
    

    def route_dist(self):
        route_dist = 0
        for route in self.routes:
            for idx in range(len(route)):
                if idx + 1 < len(route):
                    route_dist += self.graph[route[idx]].distanceTo(self.graph[route[idx+1]])
            route_dist += self.v_start.distanceTo(self.graph[route[0]])
            route_dist += self.v_start.distanceTo(self.graph[route[idx]])
        return route_dist


    def get_dist(self):
        return self.dist


    def get_fitenss(self):
        return 10000 / self.dist

    
    def merge_routes(self):
        merge_route = list()
        fill_id = len(self.graph)
        for i, route in enumerate(self.routes):
            if i > 0:
                merge_route.append(fill_id)
                fill_id += 1
            merge_route.extend(route)
        return merge_route
    
    def splite_route(self, route_list):
        split_lb = len(self.graph)
        routes, middle = list(), list()
        for route in route_list:
            if route >= split_lb:
                routes.append(middle.copy())
                middle.clear()
                continue
            middle.append(route)
        routes.append(middle.copy())
        return routes

    
    def __str__(self):
        res = 'Route:\n'
        for i, route in enumerate(self.routes, 1):
            res += f'salesman-{i}:'
            res += str(self.v_start)
            for coord in route:
                res += str(self.graph[coord])
            res += f'{self.v_start}\n'
        return res

    
