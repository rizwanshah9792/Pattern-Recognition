'''
Question 5:
Calculate eigenvalues and eigenvectors of a given matrix, then reconstruct the original matrix.
[4, 2, 2]
A= [2, 5, 1]
[2, 1, 6]

Eigenvalues:
[2.34563298 4. 8.65436702]
Eigenvectors (as columns):
[[-0.5697282 0.81741256 0.08519846]
[-0.43976496 -0.28616193 0.85065781]
[-0.69597618 -0.5 -0.5185347 ]]
Matrix reconstruction:
[[4. 2. 2.]
[2. 5. 1.]
[2. 1. 6.]]
Verification of Av = λv for eigenvector 3
Av: [ 0.73731518 7.36364422 -4.48732634]
λv: [ 0.73731518 7.36364422 -4.48732634]

Prerequities
------------------------------------------
For EigenValues |A-λI| = 0
Here A is the given Matrix, I is identity Matrix, and λ is the Eigenvalues

For EigneVector [A - λI]X = 0
Here X will the EigenVectors corrosponding each of λ(Eigenvalue)

For Reconstruct the matrix using eigen decomposition
A = VD*inverse(V)
V = Use each Eigenvectors and make the nxn matrix
D = Use the Eigenvalues as diagonal value and make the matrix

For Verification of Av = λv for eigenvector 3
Take v3 eigenvector and λ3 eigenvalue for eigenvector 3
Check multiplication of matrix A and v3 = multiplication of λ3 and v3

'''
import numpy as np

# Given matrix A
A = np.array([[4, 2, 2],
              [2, 5, 1],
              [2, 1, 6]])

eigenvalues, eigenvectors = np.linalg.eig(A)

# Reconstruct the matrix using eigen decomposition
D = np.diag(eigenvalues)  # Diagonal matrix of eigenvalues
V = eigenvectors  # Matrix of eigenvectors
A_reconstructed = V @ D @ np.linalg.inv(V) # @ use for matrix multiplication

# Verify Av = λv for the third eigenvector
v3 = eigenvectors[:, 2]  # Third eigenvector
lambda3 = eigenvalues[2]  # Corresponding eigenvalue
Av3 = A @ v3
lambda_v3 = lambda3 * v3

# Display results
print("Eigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)
print("\nReconstructed Matrix:")
print(A_reconstructed)
print("\nVerification of Av = λv for eigenvector 3:")
print("Av:", Av3)
print("λv:", lambda_v3)