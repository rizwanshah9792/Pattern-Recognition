'''
Question 3: Solving Linear Equations
Solve the system of linear equations using NumPy:
2x + y + z = 10
3x + 2y + 3z = 18
x + 4y + 9z = 16

Solution:
x = 4.0
y = 2.0
z = 0.0

Actual Solutions: 
x = 7.0
y = -9.0
z = 5.0
Verification (A x solution):
[10. 18. 16.]

'''

# First of all we have to write the equation in matrix form "Ax = b"
import numpy as np

A = np.array([[2, 1, 1],
              [3, 2, 3],
              [1, 4, 9]])

b = np.array([[10],
              [18],
              [16]])

xyz = np.linalg.solve(A, b)

print("Solution: ")
print(f"x = {xyz[0][0]:.1f}")
print(f"y = {xyz[1][0]:.1f}")
print(f"z = {xyz[2][0]:.1f}")

verfication = np.dot(A, xyz)
print("\nVerification (A x solution): ")
print(verfication.flatten())