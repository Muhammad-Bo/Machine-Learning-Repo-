
from itertools import islice
import numpy as np


#
# pure_training_set = np.loadtxt("assignment1.txt", delimiter=',')
# np.set_printoptions(precision=6, suppress=True)
# data_1 = pure_training_set.tolist()
#
# length_to_split = [19,1]
# # print(data)
# for i in range(1151):
#     Inputt = iter(data_1[i])
#     data_1[i] = Output = [list(islice(Inputt, elem))
#           for elem in length_to_split]
#
# print(data_1[0][1])
# print(data_1[100][1])
#
# for i in range(50): # Training set without Target
#     print(data_1[i][0])
#
# for i in range(50): # Target
#     print(data_1[i][1])
#
#
#
# print("#####################################")
# training_sets = [
#     [['0', '0'], ['0']],
#     [['1', '1'], ['1']],
#     [['1', '0'], ['1']],
#     [['1', '1'], ['0']]
# ]

n = 10
matrix = np.zeros((n,4)) # Pre-allocate matrix
for i in range(1,n):
    matrix[i,:] = [i, i*2, 2*i, i*1]

print(matrix)


def find_max(matrix):
    return matrix.argmax()

# for rows in matrix:
#     print(matrix.argmax())

res = np.apply_along_axis(find_max, 1, matrix)
print(res)
for i in range(len(res)):
    res[i] += 1
print(res)