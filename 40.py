import numpy as np
import random

def determinans(x):
    jo = 0
    while jo < x:
        matrix = np.random.randint(0,20,(2,2))
        DETERMINANS = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        if DETERMINANS > 10 and DETERMINANS < 20:
            print(matrix)
            print("Determinánsa: ", DETERMINANS)
            jo = jo + 1
            break
print(determinans(1))

