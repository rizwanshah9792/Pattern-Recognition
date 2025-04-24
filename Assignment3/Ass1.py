# 1. Create a 3*3 matrix of integers from 1-9, then calculate its 
# transpose, determinant, and trace.

import numpy as np

mat = np.array([[1,4,7],
                [2,5,8],
                [3,6,9]])

transposed1 = mat.T
determinant1 = np.linalg.det(mat)
trace1 = np.trace(mat)

# using numpy to perform the operations
print("Transpose Matrix: ", transposed1)
print("Determinant: ", determinant1)
print("Trace", trace1)

print('*'*35)

# Without numpy how its works

# Transpose
rows = len(mat)
cols = len(mat[0])
# transposed2 = [[0 for _ in range(rows)] for _ in range(cols)]
transposed2 = []
for i in range(cols):
    inner_list = []
    for j in range(rows):
        inner_list.append(0)
    transposed2.append(inner_list)

for i in range(rows):
    for j in range(cols):
        transposed2[j][i] = int(mat[i][j])
print("Transposed: ", transposed2)

# Determinant
a, b, c = mat[0]
d, e, f = mat[1]
g, h, i = mat[2]

det = (a*(i*e - h*f) - b*(i*d - g*f) + c*(h*d - g*e))
print(f"Determinant2: {det:.1f}")

# Trace
trace2 = 0
for i in range(len(mat)):
    trace2 = trace2 + mat[i][i]
print("Trace: ", trace2)