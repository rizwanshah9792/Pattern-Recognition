import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score

# Perceptron Class Implementation
class Perceptron:
    def __init__(self, learning_rate=0.1, n_iters=100):
        """Initialize Perceptron with learning rate and number of iterations."""
        self.lr = learning_rate
        self.n_iters = n_iters
        self.activation_func = self._unit_step_function
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        """Train the Perceptron on input data X and labels y."""
        # Input validation
        if X.shape[0] != y.shape[0]:
            raise ValueError("X and y must have the same number of samples")
        if not np.all(np.isin(y, [0, 1])):
            raise ValueError("Labels must be binary (0 or 1)")

        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        # Training loop
        for _ in range(self.n_iters):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activation_func(linear_output)
                update = self.lr * (y[idx] - y_predicted)
                self.weights += update * x_i
                self.bias += update

    def predict(self, X):
        """Predict labels for input data X."""
        linear_output = np.dot(X, self.weights) + self.bias
        return self.activation_func(linear_output)

    def _unit_step_function(self, x):
        """Step function: returns 1 if x >= 0, else 0."""
        return np.where(x >= 0, 1, 0)

# Function to test and evaluate Perceptron
def test_perceptron(name, X, y, plot=True):
    print(f"\nTesting {name}:")
    perceptron = Perceptron(learning_rate=0.1, n_iters=100)
    perceptron.fit(X, y)
    predictions = perceptron.predict(X)
    
    # Calculate accuracy
    accuracy = accuracy_score(y, predictions)
    print("Predictions:", predictions)
    print("Expected   :", y)
    print("Accuracy   :", accuracy)
    print("Weights    :", perceptron.weights)
    print("Bias       :", perceptron.bias)

    # Plot decision boundary if 2D and requested
    if plot and X.shape[1] == 2:
        plt.figure(figsize=(6, 4))
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr', label='Data Points')
        
        # Plot decision boundary: w1*x1 + w2*x2 + b = 0
        x1 = np.array([min(X[:, 0]) - 0.5, max(X[:, 0]) + 0.5])
        if perceptron.weights[1] != 0:  # Avoid division by zero
            x2 = -(perceptron.weights[0] * x1 + perceptron.bias) / perceptron.weights[1]
            plt.plot(x1, x2, 'k-', label='Decision Boundary')
        plt.title(f"{name} - Perceptron Decision Boundary")
        plt.xlabel("Feature 1")
        plt.ylabel("Feature 2")
        plt.legend()
        plt.grid(True)
        plt.show()

# Logic Gate Datasets
X_logic = np.array([[0,0], [0,1], [1,0], [1,1]])

# AND Gate
y_and = np.array([0, 0, 0, 1])
test_perceptron("AND Gate", X_logic, y_and)

# OR Gate
y_or = np.array([0, 1, 1, 1])
test_perceptron("OR Gate", X_logic, y_or)

# XOR Gate (not linearly separable)
y_xor = np.array([0, 1, 1, 0])
test_perceptron("XOR Gate", X_logic, y_xor)

# Synthetic Dataset
X_synth, y_synth = make_classification(n_samples=100, n_features=2, n_informative=2, 
                                      n_redundant=0, n_clusters_per_class=1, random_state=42)
test_perceptron("Synthetic Dataset", X_synth, y_synth)