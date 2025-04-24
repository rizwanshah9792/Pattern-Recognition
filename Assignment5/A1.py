import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

def bayes_decision_rule(X_train, y_train, X_test, prior_0=0.5, prior_1=0.5): 
    """
    Bayes Decision Rule for Two-Class Problems
    """

    # Step 1: Separate the data by class
    X0 = X_train[y_train == 0]
    X1 = X_train[y_train == 1]

    # Step 2: Calculate mean vectors
    μ0 = np.mean(X0, axis=0)
    μ1 = np.mean(X1, axis=0)

    # Step 2: Calculate covariance matrices
    Σ0 = np.cov(X0, rowvar=False)
    Σ1 = np.cov(X1, rowvar=False)

    # Step 3: Create probability distribution for each class
    dist0 = multivariate_normal(mean=μ0, cov=Σ0)
    dist1 = multivariate_normal(mean=μ1, cov=Σ1)

    # Step 3: Calculate likelihoods for each test point
    P_x_given_C0 = dist0.pdf(X_test)
    P_x_given_C1 = dist1.pdf(X_test)

    # Step 4: Calculate posteriors using Bayes rule
    P_C0_given_x = P_x_given_C0 * prior_0
    P_C1_given_x = P_x_given_C1 * prior_1

    # Step 5: Classify based on highest posterior probability
    predicted_labels = np.where(P_C1_given_x > P_C0_given_x, 1, 0)

    return predicted_labels


if __name__ == "__main__": 
    # Generate some example data 
    np.random.seed(42) 

    # Class 0 data (100 points) 
    mean0 = [0, 0] 
    cov0 = [[1, 0], [0, 1]] 
    class0_data = np.random.multivariate_normal(mean0, cov0, 100) 

    # Class 1 data (100 points) 
    mean1 = [3, 3] 
    cov1 = [[1, 0], [0, 1]] 
    class1_data = np.random.multivariate_normal(mean1, cov1, 100) 

    # Combine data 
    X = np.vstack((class0_data, class1_data)) 
    y = np.hstack((np.zeros(100), np.ones(100))) 

    # Use first 80% for training, last 20% for testing 
    split = int(0.8 * len(X)) 
    X_train, X_test = X[:split], X[split:] 
    y_train, y_test = y[:split], y[split:] 

    # Apply Bayes decision rule 
    y_pred = bayes_decision_rule(X_train, y_train, X_test)

    # Calculate accuracy
    accuracy = np.mean(y_pred == y_test)
    print("Accuracy:", accuracy)

    # Plot results
    plt.figure(figsize=(8, 6))
    plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='coolwarm', edgecolors='k', label='Predicted')
    plt.title('Bayes Decision Rule Classification (Test Set)')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.grid(True)
    plt.show()
