'''
Question 4:
Given a dataset matrix, calculate the mean and standard deviation of each column, normalise the
data, and find the correlation between columns.
    [5.1, 3.5, 1.4]
    [4.9, 3.0, 1.4]
A=  [4.7, 3.2, 1.3]
    [4.6, 3.1, 1.5]
    [5.0, 3.6, 1.4]

Output:
Column means: [4.86 3.28 1.4 ]
Column standard deviations: [0.19595918 0.24899799 0.07071068]
Normalized data:
[[ 1.22474487 0.88354899 0. ]
[ 0.20412414 -1.12451549 0. ]
[-0.8164966 -0.32128999 -1.41421356]
[-1.32679698 -0.72290748 1.41421356]
[ 0.71443449 1.28516397 0. ]]
Correlation matrix:
[[ 1. 0.65089018 -0.10566282]
[ 0.65089018 1. -0.00920389]
[-0.10566282 -0.00920389 1. ]]

'''
import numpy as np
import math

A = np.array([[5.1, 3.5, 1.4],
              [4.9, 3.0, 1.4],
              [4.7, 3.2, 1.3],
              [4.6, 3.1, 1.5],
              [5.0, 3.6, 1.4]])

# Using numpy
# Mean
column_means = np.mean(A, axis=0)
print(f"Column wise Mean: {column_means}")
print('_'*40)

# Standard Deviation
std_dev = np.std(A, axis=0, ddof=0)  
print("Strandard Deviation: ", std_dev)
print('_'*40)


# Normalization
normalized_A = (A - column_means) / std_dev
print("Normalized Data\n", normalized_A)
print('_'*40)

# Correlation
correlation_matrix = np.corrcoef(A, rowvar=False)  # rowvar=False to compute correlation between columns
print("Correlation Matrix: \n", correlation_matrix)
print('_'*40)

# without numpy
print('_'*40)

# Mean
mean = []
for i in range(len(A[0])):
    sum1 = 0
    for j in range(len(A)):
        sum1 += A[j, i]
    each_mean = float(round(sum1/len(A), 2))
    mean.append(each_mean)
print(f"Column wise Mean: {mean}")
print('_'*40)

# Strandrad Deviation
sd = []
for i in range(len(A[0])):
    sum1 = 0
    for j in range(len(A)):
        sum1 += (A[j, i] - mean[i])**2
    each_sd = math.sqrt(sum1/len(A))
    sd.append(each_sd)
print(f"Column wise: ", sd)
print('_'*40)

# Normalization
normalized = []
for i in range(len(A)):
    nor = []
    for j in range(len(A[0])):
        nor1 = ((A[i,j] - column_means[j]) / std_dev[j])
        nor.append(nor1)
    normalized.append(nor)
normalized = np.array(normalized)
print("normalized: \n", normalized)
print('_'*40)

# Correlation matrix
correlation_matrix1 = []
for i in range(len(A[0])):  
    row = []  
    for j in range(len(A[0])):  
        num = np.sum((normalized[:, i]) * (normalized[:, j]))  
        denom = len(A) - 1  # Degrees of freedom (for sample correlation)
        corr = num / denom
        row.append(corr)
    correlation_matrix1.append(row)

correlation_matrix1 = np.array(correlation_matrix1)  # Convert to NumPy array
print("Correlation Matrix: \n", correlation_matrix1)