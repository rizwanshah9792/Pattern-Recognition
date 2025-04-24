'''
Question 2: Mode Calculator
-------------------------
Write a function that finds the mode (most frequent value) in a dataset.
The function should handle:
1. Single mode
2. Multiple modes (if they exist)
3. No mode (if all values appear equally often)

___________________________________________

perequisites:

mode = value that appears most frequently in a dataset
single mode = only one value appears most frequently
multiple modes = multiple values appear most frequently
no mode = all values appear equally often

'''

def find_mode(data):
    frequency = dict() 
    
    for num in data:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    max_count = max(frequency.values()) 
    
    modes = []
    for key, value in frequency.items():
        if value == max_count:
            modes.append(key)

    if len(modes) == len(frequency):
        return "No mode"
    
    if len(modes) == 1:
        return modes[0]  
    else:
        return modes 

print(find_mode([3, 2, 1, 6, 9, 0, 4, 7, 3, 3, 4, 4, 5, 3])) 
print(find_mode([1, 9, 0,  2, 2, 3, 3, 5, 4]))  
print(find_mode([5, 1, 2, 3, 4, 7, 9]))  