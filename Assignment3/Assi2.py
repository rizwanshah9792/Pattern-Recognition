''''

Question 2:
Given two matrices, perform addition, subtraction, matrix multiplication, and element-wise
multiplication.
A = [3, 1]
    [2, 4]
B = [2, 5]
    [1, 3]

'''

import numpy as np

a = np.array([[3, 1],
              [2, 4]])

b = np.array([[2, 5],
              [1, 3]])

# Using numpy
addition1 = a + b
print(f"Matrix Addition: {addition1}\n")

subtraction1 = a - b
print(f"Matrix Subtraction: {subtraction1}\n")

multiplication = np.dot(a,b)
print(f"Matrix Multiplication: {multiplication}\n")

eleMulti = a * b
print(f"Matrix element-wise Multiplication: {eleMulti}\n")


# Without numpy
# creating an empty matrix
def empMatrix():
    cols = 2
    empty_mat = []

    for i in range(cols):
        inner_list = []
        for j in range(2):
            inner_list.append(0)
        empty_mat.append(inner_list)
    return empty_mat

# for addition
addition2 = []
addition2 = empMatrix()
for i in range(len(a)):
    for j in range(len(a[0])):
        addition2[i][j] = int(a[i][j] + b[i][j])
print("Addition: ", addition2)

# for Subraction
subtraction2 = []
subtraction2 = empMatrix()
for i in range(len(a)):
    for j in range(len(a[0])):
        subtraction2[i][j] = int(a[i][j] - b[i][j])
# for r in subtraction2:
#     print(r)
print("Subtraction: ", subtraction2)

# For multiplication
multiplication2 = []
multiplication2 = empMatrix()
for i in range(len(a)):
    for j in range(len(a[0])):
        for k in range(len(b)):
            multiplication2[i][j] = int(a[i][0] * b[0][j] +
                                        a[i][1] * b[1][j])
print("multiplication: ", multiplication2)

# For Element wise Multiplication
eleMulti2 = []
eleMulti2 = empMatrix()
for i in range(len(a)):
    for j in range(len(a[0])):
        eleMulti2[i][j] = int(a[i][j] * b[i][j])
print("Element-wise Multiplication: ", eleMulti2)