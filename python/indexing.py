import numpy as np

# grid of
# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12]
# ]
practice_grid_2D = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])


print(practice_grid_2D.shape) # (4, 3)

num_rows = practice_grid_2D.shape[0]
print(num_rows) # 4
num_cols = practice_grid_2D.shape[1]
print(num_cols) # 3

first_col = list(practice_grid_2D[0:4, 0])
print(first_col) # [1, 4, 7, 10]

last_col = list(practice_grid_2D[0:4, 2])
print(last_col) # [3, 6, 9, 12]
last_col = practice_grid_2D[0:4, 2]
first_row = list(practice_grid_2D[0, 0:4])
print(first_row) # [1, 2, 3]
last_row = list(practice_grid_2D[3, 0:4])
print(last_row) # [10, 11, 12]

random_slice_2D = practice_grid_2D[:2, 1:4]
print(random_slice_2D) 
# [[2, 3],
# [5, 6]])

# grid of
# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10, 11, 12]
# ]


positive_diagonal = list(practice_grid_2D[[2, 1, 0], [0, 1, 2]])
print(positive_diagonal) # [7, 5, 3]

negative_diagonal = list(practice_grid_2D[[0, 1, 2], [0, 1, 2]])
print(negative_diagonal) # [1, 5, 9]


# https://towardsdatascience.com/numpy-indexing-explained-c376abb2440d

# grid of
# [
    # [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9],
    #     [10, 11, 12]
    # ],
    # [
    #     [101, 102, 103],
    #     [104, 105, 106],
    #     [107, 108, 109],
    #     [1010, 1011, 1012]
    # ],
    # [
    #     [201, 202, 203],
    #     [204, 205, 206],
    #     [207, 208, 209],
    #     [2010, 2011, 2012]
    # ],
# ]

practice_grid_3D = np.array([[[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]],[[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]],[[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]],])


print("3D SHAPE:", practice_grid_3D.shape) # (3, 4, 3)

print(practice_grid_3D[0, 1, 2]) # 6 <- expected

print(practice_grid_3D[[0, 1, 2], [0, 1, 2], [0, 1, 2]]) # [1, 5, 9] <- not expected, would have thought [1, 105, 209], non?

# SEE ADVANCED SECTION OF: https://towardsdatascience.com/numpy-indexing-explained-c376abb2440d

for n in range(6):
    print(n)

