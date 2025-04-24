import numpy as np
import matplotlib.pyplot as plt

def minimum_distance_classifier(X_train, y_train, X_test):
    # Compute centroids
    X0 = X_train[y_train == 0]
    X1 = X_train[y_train == 1]

    μ0 = np.mean(X0, axis=0)
    μ1 = np.mean(X1, axis=0)

    # Compute distances and classify
    d0 = np.linalg.norm(X_test - μ0, axis=1)
    d1 = np.linalg.norm(X_test - μ1, axis=1)

    y_pred = np.where(d1 < d0, 1, 0)
    return y_pred

# Example usage
if __name__ == "__main__":

    # Generate synthetic data
    np.random.seed(42)

    # Class 0
    mean0 = [0, 1]
    cov0 = [[1, 0], [0, 1]]
    X0 = np.random.multivariate_normal(mean0, cov0, 100)

    # Class 1
    mean1 = [3, 3]
    cov1 = [[1, 0], [0, 1]]
    X1 = np.random.multivariate_normal(mean1, cov1, 100)

    # Combine data
    X = np.vstack((X0, X1))
    y = np.hstack((np.zeros(100), np.ones(100)))

    # Shuffle
    indices = np.random.permutation(len(X))
    X = X[indices]
    y = y[indices]

    # Split train/test
    train_size = int(0.8 * len(X))
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]

    # Apply classifier
    y_pred = minimum_distance_classifier(X_train, y_train, X_test)

    # Accuracy
    accuracy = np.mean(y_pred == y_test)
    print("Minimum Distance Classifier Accuracy:", accuracy)

    # Plot
    plt.figure(figsize=(8, 6))
    plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='coolwarm', edgecolors='k')
    plt.title('Minimum Distance Classifier (Test Set)')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.grid(True)
    plt.show()
