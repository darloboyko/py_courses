def first_shot(pp_1, pp_2):
    p1_i = pp_1.index("B")
    p2_i = pp_2.index("B")
    if p1_i > p2_i:
        return 1
    elif p2_i > p1_i:
        return 2
    else:
        return 0


pp_1 = str(input(" ")) 
pp_2 = str(input(" "))

print(first_shot())  