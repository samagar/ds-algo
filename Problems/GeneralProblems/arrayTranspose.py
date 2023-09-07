# Problem
# Transpose an Array

import numpy as np
my_list = [[1,2,3],[4,5,6],[7,8,9]]
print("original Array \n",np.array(my_list))

def arrayRotationLC(my_list):
    result = [[my_list[j][i] for j in range(len(my_list))] for i in range(len(my_list[0]))]

    print("Transpose \n",np.array(result))
    print("Image Transpose \n", np.array([i[::-1] for i in result]))

arrayRotationLC(my_list)