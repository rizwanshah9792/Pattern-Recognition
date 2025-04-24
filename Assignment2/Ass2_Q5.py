'''
Question 5: Probability Distribution
----------------------------------
Write a function that:
1. Generates 1000 random numbers following a normal distribution
2. Calculates the probability that a number falls within one standard
deviation of the mean
3. Plots the distribution with matplotlib
Expected Output:
- A probability value close to 0.68 (theoretical value)
- A histogram showing the normal distribution
def analyze_normal_distribution(sample_size=1000):
# Your code here
pass

'''
import numpy as np
import matplotlib.pyplot as plt

def analyze_normal_distribution(sample_size=1000):
    mean = 0
    std_dev = 1

    # Generate random numbers
    numbers = np.random.normal(mean, std_dev, sample_size)

    # Calculate probability within 1 std deviation
    within_1_std = ((numbers >= mean - std_dev) & (numbers <= mean + std_dev)).sum()
    probability = within_1_std / sample_size

    print(f"Probability: {probability:.2f}")

    # Plot histogram
    plt.figure(figsize=(10, 6))
    plt.hist(numbers, bins=30, density=True, color='royalblue', alpha=0.6, edgecolor='black')

    # Add vertical line for mean
    plt.axvline(mean, color='red', linestyle='dashed', linewidth=3, label='Mean')

    # Display probability on the histogram
    plt.text(mean + 1, 0.35, f'P = {probability:.2f}', fontsize=14, color='black', 
             bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

    # Titles and labels
    plt.title('Normal Distribution', fontsize=18, weight='bold', color='darkblue')
    plt.xlabel('Value', fontsize=14, weight='bold', color='darkgreen')
    plt.ylabel('Density', fontsize=14, weight='bold', color='darkgreen')

    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    plt.show()

    return probability

analyze_normal_distribution()
pass