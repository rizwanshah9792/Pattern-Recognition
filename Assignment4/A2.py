'''
Qestion 2: Data Transformation
(Min max Transformation )
● Generate sample data
np.random.seed(42)
original_data = np.random.normal(loc=50, scale=15, size=100)
● Manual min-max scaling (0 to 1)
Manually perform min-max scaling on a numpy array or list
Formula: X_scaled = (X - X_min) / (X_max - X_min)
Parameters:
X: numpy array or list to be normalized
Returns:
numpy array with normalized values between 0 and 1
● Custom range min-max scaling (-1 to 1)
Scale data to a custom range [new_min, new_max]
Formula: X_scaled = (X - X_min) / (X_max - X_min) * (new_max - new_min) + new_min
Parameters:
X: numpy array or list to be normalized
new_min: minimum value of the new range
new_max: maximum value of the new range
Returns:
numpy array with normalized values between new_min and new_max
● Using scikit-learn's MinMaxScaler
● Display results
Min:
Max:
Mean:
Standard Deviation:
● Create a DataFrame for easy comparison
First 5 rows of all datasets
● Visualize the transformations

'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Generate sample data
np.random.seed(42)
original_data = np.round(np.random.normal(loc=50, scale=15, size=100), 2)

# Manual min-max scaling (0 to 1)
min_val = np.min(original_data)
max_val = np.max(original_data)
X_scaled = (original_data - min_val) / (max_val - min_val)

# Manual min-max scaling (-1 to 1)
new_min, new_max = -1, 1
X_scaled_new = X_scaled * (new_max - new_min) + new_min

# Using scikit-learn's MinMaxScaler (0 to 1)
original_data_2D = original_data.reshape(-1, 1)
scaler_0_1 = MinMaxScaler(feature_range=(0, 1))
sklearn_scaled_0_1 = scaler_0_1.fit_transform(original_data_2D).flatten()

# Using scikit-learn's MinMaxScaler (-1 to 1)
scaler_neg1_1 = MinMaxScaler(feature_range=(-1, 1))
sklearn_scaled_neg1_1 = scaler_neg1_1.fit_transform(original_data_2D).flatten()

# Create a DataFrame for easy comparison
df = pd.DataFrame({
    "Original Data": original_data,
    "Manual Scaled (0-1)": X_scaled,
    "Manual Scaled (-1 to 1)": X_scaled_new,
    "Sklearn Scaled (0-1)": sklearn_scaled_0_1,
    "Sklearn Scaled (-1 to 1)": sklearn_scaled_neg1_1
})

# Display first 5 rows
print(df.head())

# Display results
print(f"\nMin: {np.min(original_data)}")
print(f"Max: {np.max(original_data)}")
print(f"Mean: {np.mean(original_data):.2f}")
print(f"Standard Deviation: {np.std(original_data):.2f}")

# Visualization
plt.figure(figsize=(12, 6))

# Visualization: Separate histograms for each transformation
fig, axes = plt.subplots(3, 2, figsize=(12, 10))

axes[0, 0].hist(original_data, bins=15, color='blue', alpha=0.7)
axes[0, 0].set_title("Original Data")

axes[0, 1].hist(X_scaled, bins=15, color='orange', alpha=0.7)
axes[0, 1].set_title("Manual Min-Max Scaling (0-1)")

axes[1, 0].hist(X_scaled_new, bins=15, color='green', alpha=0.7)
axes[1, 0].set_title("Manual Min-Max Scaling (-1 to 1)")

axes[1, 1].hist(sklearn_scaled_0_1, bins=15, color='red', alpha=0.7)
axes[1, 1].set_title("Sklearn MinMaxScaler (0-1)")

axes[2, 0].hist(sklearn_scaled_neg1_1, bins=15, color='purple', alpha=0.7)
axes[2, 0].set_title("Sklearn MinMaxScaler (-1 to 1)")

# Hide empty subplot
axes[2, 1].axis('off')

plt.tight_layout()
plt.show()
