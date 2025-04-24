'''
Implement Perceptron for the AND Gate

How the Perceptron Works
A perceptron is the simplest form of artificial neural network. For the AND gate:
1. Inputs: Two binary inputs (0 or 1)
2. Output: Single binary output (0 or 1)
3. Learning Rule: Adjusts weights based on error between predicted and actual output

Key Components of the Implementation
1. Weights and Bias: The perceptron learns two weights (one for each input) and a bias
term
2. Activation Function: A simple step function that returns 1 if the weighted sum is
positive, 0 otherwise

3. Training Algorithm:
○ For each input pattern, calculate the predicted output
○ Compare with the expected output and compute error
○ Adjust weights and bias if there's an error
○ Repeat until convergence (no errors) or max iterations reached
4. Decision Boundary: The perceptron creates a linear boundary that separates the
input space

'''

import numpy as np

# Step activation function
def step_function(x):
    return np.where(x >= 0, 1, 0)

# Perceptron training function
def train_perceptron(X, y, learning_rate=0.1, epochs=10):
    bias_column = np.ones((len(X), 1)) 
    X_with_bias = np.hstack((X, bias_column))  

    weights = np.zeros(3)

    for epoch in range(epochs):
        for i in range(len(X_with_bias)): 
            x_i = X_with_bias[i]
            y_i = y[i]
            output = step_function(np.dot(x_i, weights))
            error = y_i - output
            weights += learning_rate * error * x_i
    return weights

def predict(X, weights):
    bias_column = np.ones((len(X), 1))
    X_with_bias = np.hstack((X, bias_column))
    return step_function(np.dot(X_with_bias, weights))

# Input data for AND gate
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Expected output
y = np.array([0, 0, 0, 1])

print("Implement Perceptron for the AND Gate\n")
# Train the perceptron
weights = train_perceptron(X, y)
print("Trained weights:", weights)

# Test prediction
outputs = predict(X, weights)
print("Predictions:", outputs)