'''
Question 1: Simple Probability Calculation
----------------------------------------
Write a function to calculate the probability of rolling a six on a die
based on experimental data. The function should:
- Accept a list of die roll results (1-6)
- Return the probability of rolling a six
Example Input: [1, 6, 3, 6, 2, 6, 4, 5, 6, 1]
Expected Output: 0.4 (4 sixes out of 10 rolls)
def calculate_six_probability(roll_results):
# Your code here
pass

'''

print("*"*39)

data = [1, 6, 3, 6, 2, 6, 4, 5, 6, 1]
def calculate_six_probability(roll_results):
    count = 0
    for i in roll_results:
        if i == 6:
            count += 1
    return count/len(data)
print("Probability of rolling a six: ", calculate_six_probability(data))
pass
print("*"*39)