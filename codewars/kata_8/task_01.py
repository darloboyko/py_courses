'''David wants to travel, but he doesn't like long routes. He wants to decide where he will go, can you tell him 
the shortest routes to all the cities?
Clarifications:
David can go from a city to another crossing more cities
Cities will be represented with numbers
David's city is always the number 0
If there isn't any route to a city, the distance will be infinite (float("inf"))
There's only one road between two cities
Routes are one-way (start city -> end city)
The arguments are:
n: the number of cities (so the cities are numbers from 0 to n-1 inclusive)
routes: a list of routes (tuples): (start city, end city, length)
The output is a list of shortest routes (tuples) from David's city to all the others, sorted by city number:
(city number, distance)
Example:
shortest_routes(3, [(0, 1, 1), (0, 2, 10), (1, 2, 2)]) # return [(1, 1), (2, 3)]'''

routes = list[(0, 1, 1), (0, 2, 10), (1, 2, 2)]
distance = [] 
visited_city = [] 

#def shortestRoutes(n=3):
for rout in len(routes):
    if routes[rout][2]<routes[rout+1][2]:
        distance.append(routes[rout][2])
        visited_city.append(routes[rout][1])
        print(distance)
        print(visited_city)