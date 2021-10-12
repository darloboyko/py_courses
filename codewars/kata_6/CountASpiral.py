#Your task is to return the amount of white rectangles in a NxN spiral.
#Your font may differ, if we talk of white rectangles, we talk about the symboles in the top row.
#For example, a spiral with size 5 should look like this:
#⬜⬜⬜⬜⬜
#⬛⬛⬛⬛⬜
#⬜⬜⬜⬛⬜
#⬜⬛⬛⬛⬜
#⬜⬜⬜⬜⬜
#And return the value 17 because the total amount of white rectangles is 17.
#As a general rule, the white snake cannot touch itself.
#The size will be at least 5.
#The test cases can get very large, it is not feasible to calculate the whole spiral.


def spiral_sum(size):
    iter = size//4
    whole_spiral = 0
    for i in range(0, iter+1):
        whole_spiral += abs((4 * size) - 5) 
        size -= 4
    return whole_spiral + iter


size = int(input("Number: "))

print(spiral_sum(size)) 