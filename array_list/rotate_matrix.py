# Given an n*n matrix, rotate the matrix array

# # pseudocode ->
# for i = 0 to n
#     temp = topleft[i]
#     topleft[i]=bottomleft[i]
#     bottomleft[i]=bottomright[i]
#     bottomright[i]=topright[i]
#     topright[i]=temp

# soltuion:

import numpy as np

twoDarray = np.array([[1, 2, 3], [4, 5, 6], [7,8, 9]])
print(twoDarray)


def rotate_matrix(matrix):
    n = len(matrix)                                         #consider n= 3
    for layer in range(n//2):                               #layer =0,1
        first_layer = layer
        last_layer = n - layer - 1
        for i in range(first_layer, last_layer):            #i = 0 -> 0,1,2; i = 1 -> 1
            temp = matrix[layer][i]                         # topleft to temp
            matrix[layer][i] = matrix[-i-1][layer]          # bottomleft to topleft
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]    # bottomright to bottom left
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]    # topright to bottomright
            matrix[i][-layer-1] = temp                      # temp to topright
    return matrix


print(rotate_matrix(twoDarray))
