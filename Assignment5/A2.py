import numpy as np
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt

def bayes_maximum_likelihood(X_train, y_train, X_test):
    # Separate data by class
    X0 = X_train[y_train == 0]
    X1 = X_train[y_train == 1]

    # Compute mean and covariance (ML estimates)
    μ0 = np.mean(X0, axis=0)
    μ1 = np.mean(X1, axis=0)
    Σ0 = np.cov(X0, rowvar=False)
    Σ1 = np.cov(X1, rowvar=False)

    # Create multivariate Gaussian distributions
    dist0 = multivariate_normal(mean=μ0, cov=Σ0)
    dist1 = multivariate_normal(mean=μ1, cov=Σ1)

    # Calculate likelihoods
    likelihood0 = dist0.pdf(X_test)
    likelihood1 = dist1.pdf(X_test)

    # Assign to class with maximum likelihood
    y_pred = np.where(likelihood1 > likelihood0, 1, 0)

    return y_pred

# Example usage
if __name__ == "__main__":

    # Generate synthetic data
    np.random.seed(42)

    # Class 0
    mean0 = [0, 1]
    cov0 = [[1, 0.2], [0.2, 1]]
    X0 = np.random.multivariate_normal(mean0, cov0, 100)

    # Class 1
    mean1 = [2, 3]
    cov1 = [[1, -0.2], [-0.2, 1]]
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
    y_pred = bayes_maximum_likelihood(X_train, y_train, X_test)

    # Accuracy
    accuracy = np.mean(y_pred == y_test)
    print("Maximum Likelihood Classifier Accuracy:", accuracy)

    # Plot
    plt.figure(figsize=(8, 6))
    plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='coolwarm', edgecolors='k')
    plt.title('Bayes Maximum Likelihood Classifier (Test Set)')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.grid(True)
    plt.show()
