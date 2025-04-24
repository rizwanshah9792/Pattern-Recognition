'''
Question 3: Conditional Probability
---------------------------------
Using student data, calculate the probability of passing an exam given that
The student studied. The function should:
- Accept two lists: study_data and exam_results (both boolean)
- Return P(Pass|Studied)

Example Input:
studied = [True, True, True, False, False, True, False, True]
passed = [True, True, False, False, False, True, False, True]
Expected Output: 0.83 (4 passed out of 5 who studied)
def calculate_passing_probability(studied, passed):
# Your code here
pass

Conditional Probability of P(A|B) = P(A intersection B)/P(B)

'''

studied = [True, True, True, False, False, True, False, True]
passed = [True, True, False, False, False, True, False, True]

def calculate_passing_probability(studied, passed):
    intersection = 0
    studied_count = 0
    for i in range(len(studied)):
        if studied[i]:
            studied_count += 1
            if passed[i]:
                intersection += 1
    if studied_count == 0:
        return 0 #To avoid division by zero
    return intersection / studied_count
    
result = calculate_passing_probability(studied, passed)
print(f"P(Passed|Studied) = {result: .2f}")