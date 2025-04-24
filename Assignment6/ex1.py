import numpy as np
import matplotlib.pyplot as plt

# Sigmoid Function and its derivative
def sigmoid(x):
    sig = 1 / (1 + np.exp(-x))
    return sig

def sigmoid_derivative(x):
    der_sig = (1 - sigmoid(x)) * sigmoid(x)
    return der_sig

# Tanh Function and its derivative
def tanh(x):
    tanhf = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
    return tanhf

def tanh_derivative(x):
    tanhd = (1 - tanh(x)**2)
    return tanhd

# ReLU Function and its derivative
def relu(x):
    reluf = np.maximum(0, x)
    return reluf

def relu_derivative(x):
    return np.where(x > 0, 1, 0)

# Leaky ReLU Function and its derivative
def leakyrelu(x, alpha=0.1):
    return np.where(x > 0, x, alpha * x)

def leakyrelu_derivative(x, alpha=0.1):
    return np.where(x > 0, 1, alpha)

# ELU Function and its derivative
def elu(x, alpha=1.0):
    return np.where(x > 0, x, alpha * (np.exp(x) - 1))

def elu_derivative(x, alpha=1.0):
    return np.where(x > 0, 1, alpha * np.exp(x))

# Plotting function
def plot_activation_functions():
    x = np.linspace(-5, 5, 100)
    plt.figure(figsize=(15, 8))

    # Sigmoid
    plt.subplot(2, 5, 1)
    plt.plot(x, sigmoid(x), label='Sigmoid', color='blue')
    plt.title('Sigmoid')
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 5, 6)
    plt.plot(x, sigmoid_derivative(x), label='Sigmoid Derivative', color='blue', linestyle='--')
    plt.title('Sigmoid Derivative')
    plt.grid(True)
    plt.legend()

    # Tanh
    plt.subplot(2, 5, 2)
    plt.plot(x, tanh(x), label='Tanh', color='green')
    plt.title('Tanh')
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 5, 7)
    plt.plot(x, tanh_derivative(x), label='Tanh Derivative', color='green', linestyle='--')
    plt.title('Tanh Derivative')
    plt.grid(True)
    plt.legend()

    # ReLU
    plt.subplot(2, 5, 3)
    plt.plot(x, relu(x), label='ReLU', color='purple')
    plt.title('ReLU')
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 5, 8)
    plt.plot(x, relu_derivative(x), label='ReLU Derivative', color='purple', linestyle='--')
    plt.title('ReLU Derivative')
    plt.grid(True)
    plt.legend()

    # Leaky ReLU
    plt.subplot(2, 5, 4)
    plt.plot(x, leakyrelu(x), label='Leaky ReLU', color='brown')
    plt.title('Leaky ReLU')
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 5, 9)
    plt.plot(x, leakyrelu_derivative(x), label='Leaky ReLU Derivative', color='brown', linestyle='--')
    plt.title('Leaky ReLU Derivative')
    plt.grid(True)
    plt.legend()

    # ELU
    plt.subplot(2, 5, 5)
    plt.plot(x, elu(x), label='ELU', color='cyan')
    plt.title('ELU')
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 5, 10)
    plt.plot(x, elu_derivative(x), label='ELU Derivative', color='cyan', linestyle='--')
    plt.title('ELU Derivative')
    plt.grid(True)
    plt.legend()

    plt.suptitle('Activation Functions and Their Derivatives', fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

# Run the plotting function
if __name__ == "__main__":
    plot_activation_functions()