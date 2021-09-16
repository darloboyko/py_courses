china = ('Shanghai', 'China', 23_400000)
india = ('Mumbai', 'India', 15_400000)
turkey = ('Istanbul', 'Turkey', 15_000000)
japan = ('Tokyo', 'Japan', 14_000000)
nigeria = ('Lagos', 'Nigeria', 13_700000)
cities = [china, india, turkey, japan, nigeria]
population = 0
for city in cities:
    population += city[2]
print(population)
