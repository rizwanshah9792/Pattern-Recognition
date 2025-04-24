'''
Qestion 1: Write a Program
● Calculate Euclidian distance between two 2D points
● Calculate Manhattan (taxicab) distance between two 2D points
● Calculate Chebyshev (chessboard) distance between two 2D points.
● Calculate Minkowski distance with parameter p between two 2D points.
When p=1: Manhattan distance
When p=2: Euclidean distance
When p→∞: Chebyshev distance
● Calculate Hamming distance between two binary vectors.
● Calculate cosine distance between two vectors
● Calculate Mahalanobis distance between two vectors.

'''
import math
import numpy as np


# Calculate Euclidian distance between two 2D points
# Using numpy
p1 = np.array([1, 2])
p2 = np.array([3, 6])

dist = np.linalg.norm(p1 - p2)
print(f"Distance between two points using numpy: {dist:.2f}")

# Without numpy
def euclidian_distance(point1, point2):
    if (len(point1) != len(point2)):
        raise ValueError("You must be kidding, to find out the distance you must be give the same dimension in both points.")
    
    squared_distance = sum((x - y)**2 for x, y in zip(point1, point2))
    distance = math.sqrt(squared_distance)
    return distance

point_a = (1, 2)
point_b = (3, 6)

distance = euclidian_distance(point_a, point_b)
print(f"The distance between points {point_a} and {point_b} is {distance:.2f}")



# Calculate Manhattan (taxicab) distance between two 2D points
# Using numpy.
Mp1 = np.array([1, 2])
Mp2 = np.array([3, 6])

Mdist = np.sum(np.abs(Mp1 - Mp2))
print(f"The Manhattan (taxicab) distance between two 2D points are {Mp1} and {Mp2} is: {Mdist}.")

# Without numpy.
Map1 = (1, 2)
Map2 = (3, 6)

Madist = sum(abs(x - y) for x, y in zip(Map1, Map2))
print(f"The Manhattan (taxicab) distance between two 2D points are {Mp1} and {Mp2} is: {Mdist}.")



# Calculate Chebyshev (chessboard) distance between two 2D points.
# Using numpy
def chebyshev_distance(point1, point2):
    point1 = np.array(point1)
    point2 = np.array(point2)
    return np.max(np.abs(point1 - point2))
ChA = [1, 2]
ChB = [3, 6]

distance = chebyshev_distance(ChA, ChB)
print(f"The Chebyshev distance between {ChA} and {ChB} is {distance}")

# Without numpy
ex = []
for x, y in zip(ChA, ChB):
    cd = abs(x - y)
    ex.append(cd)

if (ex[0] > ex[1]):
    print(f"The Chebyshev distance between {ChA} and {ChB} is {ex[0]}")
else:
    print(f"The Chebyshev distance between {ChA} and {ChB} is {ex[1]}")


'''
Calculate Minkowski distance with parameter p between two 2D points.
When p=1: Manhattan distance
When p=2: Euclidean distance
When p→∞: Chebyshev distance

MINKOWSKI DISTANCE
-- Minkowski distance provides a way to measure the distance
between two points in a multi-dimensional space. It has ability to
encompass other distance metrics as special cases, primarily through 
a parameter p.

'''
def minkowski_dis(point1, point2, p):
    return np.sum(np.abs(point1 - point2)**p)**(1/p)

p1 = np.array([1, 2])
p2 = np.array([3, 6])
# When p=1: Manhattan distance
p_value = 1

distance_manhattan = minkowski_dis(p1, p2, p_value)
print(f"The Minkowski\nWhen(p = 1) - Manhattan distance is {distance_manhattan}")

# When p=2: Euclidean distance
distance_euclidean = minkowski_dis(p1, p2, 2)
print(f"The Minkowski\nWhen(p = 2) - Euclidean distance is {distance_euclidean:.2f}")

# When p→∞: Chebyshev distance
distance_chebysheb = np.max(np.abs(p1 - p2))
print(f"The Minkowski\nWhen(p = ∞) Chebyshev distance = {distance_chebysheb}")


# Calculate Hamming distance between two binary vectors.
b1 = [1, 1, 1, 0, 0]
b2 = [0, 1, 1, 0, 1]
result = []

for i, j in zip(b1, b2):
    '''
    XOR Operation:
    1 XOR 1 = 0
    0 XOR 0 = 0
    1 XOR 0 = 1
    0 XOR 1 = 1
    '''
    result.append(i ^ j)
count = 0
for i in result:
    if (i == True):
        count += 1
print(f"The Hamming distance of two binary vectors is {count}")

# Calculate cosine distance between two vectors
'''
Cosine Distanc(A, B) = 1 - ((A dot B) / (magnitude A * magnitude B))
magnitude A = (a1**2 + a2**2 + ... + an**2)**(1/2)
'''
Va = np.array([5, 4])
Vb = np.array([1, 2])

cosine_similarity = np.dot(Va, Vb) / (np.linalg.norm(Va) * np.linalg.norm(Vb))

cosine_dist = 1 - cosine_similarity
print("Consine Distance: {:.2f}".format(cosine_dist))

# Calculate Mahalanobis distance between two vectors.
def mahalanobis_distance(x, y, cov=None):
    x = np.array(x)
    y = np.array(y)

    if cov is None:
        cov = np.eye(len(x))
    
    cov_inv = np.linalg.inv(cov)
    diff = x - y
    distance = np.sqrt(diff.T @ cov_inv @ diff)

    return distance
x = [1, 2, 3]
y = [2, 4, 5]

MahaDist = mahalanobis_distance(x,y)
print(f"Mahalanobis Distance: {MahaDist}")