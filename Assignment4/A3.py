'''
Question 3:
Given the following predictions and actual values:
y_true = [1, 0, 1, 1, 0, 0, 1, 0]
y_pred = [1, 0, 0, 1, 1, 0, 1, 1]
Calculate
● True Positives (TP): Correctly predicted positives
● False Positives (FP): Incorrectly predicted positives
● True Negatives (TN): Correctly predicted negatives
● False Negatives (FN): Incorrectly predicted negatives
● Accuracy: Overall correctness (TP + TN) / Total
● Precision: How many predicted positives were correct TP / (TP + FP)
● Recall: How many actual positives were found TP / (TP + FN)
● F1 Score: Harmonic mean of precision and recall
● Mean Squared Error (MSE) Formula: MSE = (1/n) * Σ(y_true - y_pred)²
● Root Mean Square Error (RMSE) Formula: RMSE =sqrt( (1/n) * Σ(y_true - y_pred)²)
● Mean Absolute Error (MAE) Formula: MAE = (1/n) * Σ|y_true - y_pred|
● Binary Cross-Entropy Loss : Formula: -[y_true * log(y_pred) + (1 - y_true) * log(1 -
y_pred)]

'''

import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, mean_squared_error, mean_absolute_error

# Given Data
y_true = np.array([1, 0, 1, 1, 0, 0, 1, 0])
y_pred = np.array([1, 0, 0, 1, 1, 0, 1, 1])

# Calculate TP, FP, TN, FN
TP = np.sum((y_true == 1) & (y_pred == 1))  # True Positives
FP = np.sum((y_true == 0) & (y_pred == 1))  # False Positives
TN = np.sum((y_true == 0) & (y_pred == 0))  # True Negatives
FN = np.sum((y_true == 1) & (y_pred == 0))  # False Negatives

# Accuracy: (TP + TN) / Total
accuracy = (TP + TN) / len(y_true)

# Precision: TP / (TP + FP)
precision = TP / (TP + FP) if (TP + FP) != 0 else 0

# Recall: TP / (TP + FN)
recall = TP / (TP + FN) if (TP + FN) != 0 else 0

# F1 Score: 2 * (Precision * Recall) / (Precision + Recall)
f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0

# Mean Squared Error (MSE): (1/n) * Σ(y_true - y_pred)^2
mse = np.mean((y_true - y_pred) ** 2)

# Root Mean Squared Error (RMSE): sqrt((1/n) * Σ(y_true - y_pred)^2)
rmse = np.sqrt(mse)

# Mean Absolute Error (MAE): (1/n) * Σ|y_true - y_pred|
mae = np.mean(np.abs(y_true - y_pred))

# Binary Cross-Entropy Loss: -[y_true * log(y_pred) + (1 - y_true) * log(1 - y_pred)]
bce = -np.mean(y_true * np.log(y_pred + 1e-15) + (1 - y_true) * np.log(1 - y_pred + 1e-15))

# Print Results
print(f"True Positives (TP): {TP}")
print(f"False Positives (FP): {FP}")
print(f"True Negatives (TN): {TN}")
print(f"False Negatives (FN): {FN}")
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")
print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"MAE: {mae:.2f}")
print(f"Binary Cross-Entropy Loss: {bce:.4f}")