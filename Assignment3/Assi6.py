'''
Question 6:
Calculate the covariance matrix for the following set of 2D data points:
(1,2), (2,3), (3,5), (4,7), (5,8).

----------------------------------------------------------------------------------------------------------------------------
output:
Means: x = 3.0 , y = 5.0
Covariance matrix (manual calculation): [[2.5 3.5]
[3.5 6.5]]

Devitions from mean: Xi - X_mean = devi_of_x
                     Yi = Y_mean = devi_of_y

Now compute covariances
Cov(X,Y)
Cov(X,X)
Cov(Y,Y)

Cov(X,Y) = (sum of (Xi - mean of x)(Yi - mean of y)) / (n - 1)

'''
import numpy as np
# Set NumPy print options to show 1 decimal place
np.set_printoptions(formatter={'float': '{:.1f}'.format})

points = [(1, 2), (2, 3), (3, 5), (4, 7), (5, 8)]

x_values = []
y_values = []

for p in points:
    x_values.append(p[0])  # Extract x-coordinates
    y_values.append(p[1])  # Extract y-coordinates
# x, y are the means
x = sum(x_values)/len(x_values)
y = sum(y_values)/len(y_values)
print(f"Means: x = {x}, y = {y}")
print("-"*50)

devi_of_x = []
devi_of_y = []
for i in points:
    devi_of_x.append(i[0] - x)
for j in points:
    devi_of_y.append(j[1] - y)
# print(devi_of_x)
# print(devi_of_y)

'''
sum1 = 0
for k, l in zip(devi_of_x, devi_of_y):
    sum1 += (k*l)
covXY = sum1/(len(x_values) - 1)
print(covXY)

sum2 = 0
for i in devi_of_x:
    sum2 += (i*i)
covXX = sum2/(len(x_values) - 1)
print(covXX)

sum3 = 0
for i in devi_of_y:
    sum3 += (i*i)
covYY = sum3/(len(y_values) - 1)
print(covYY)
'''
def compute_covariance(devi_x, devi_y):
    sum_cov = sum(k * l for k , l in zip(devi_x, devi_y))
    return sum_cov / (len(devi_x) - 1)

covXY = compute_covariance(devi_of_x, devi_of_y)
covXX = compute_covariance(devi_of_x, devi_of_x)
covYY = compute_covariance(devi_of_y, devi_of_y)

cov_Matrix = np.array([[covXX, covXY],
                       [covXY, covYY]])

print(f"Covariance matrix (manual calculation): {cov_Matrix}")
print("-"*50)