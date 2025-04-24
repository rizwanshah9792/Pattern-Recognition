'''
Question 4: Bayes' Theorem Application
------------------------------------
A medical test for a rare disease has the following properties:
- 1% of the population has the disease (prior probability)
- The test is 95% accurate for people who have the disease (sensitivity)
- The test is 90% accurate for people who don't have the disease (specificity)
Write a function to calculate the probability that a person has the disease
given a positive test result using Bayes' Theorem.
Expected Output: ~0.087 (8.7%)
def calculate_disease_probability(prior_prob, sensitivity, specificity):
# Your code here
pass

Prerequisites
----------------------------------

Given Data:
P(A)=0.01 (1% of the population has the disease)
P(B|A)=0.95 (Test is 95% accurate for diseased people)
P(¬A)=0.99 (99% of the population does not have the disease)
P(B|¬A)=1-0.90=0.10 (False positive rate, since the test is 90% accurate for non-diseased people)
P(B) = Total probability of testing positive, calculated using Law of Total Probability.
P(B)=P(B|A)P(A)+P(B|¬A)P(¬A)

'''

def calculate_disease_probability(prior_prob, sensitivity, specificity):
    # Total probability of testing positive
    test_positive = (sensitivity * prior_prob) + ((1 - specificity)*(1 - prior_prob))
    # Probability that a person has the diseas
    has_disease = (sensitivity * prior_prob) / test_positive
    return has_disease
result = calculate_disease_probability(0.01, 0.95, 0.90)
percentage = result * 100
print("-"*42)
print(f"P(Has disease) = {result: .4f}")
print(f"Means {percentage: .2f}% that a person has the disease")
print("-"*42)
pass