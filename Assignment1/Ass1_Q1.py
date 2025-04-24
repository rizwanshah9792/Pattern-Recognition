'''
Question 1: Class Grade Analysis
------------------------------
A teacher has recorded the following grades for a class:
grades = [85, 92, 78, 65, 88, 72, 90, 85, 83, 72]
Write a program to calculate and display:
1. The mean grade
2. The median grade
3. The standard deviation
4. The highest and lowest grades
5. The range of grades (max-min)
Expected Output:
Mean: 81.0
Median: 84.0
Standard Deviation: ~8.64
Highest Grade: 92
Lowest Grade: 65
Range: 27
__________________________________

perequisites:

Mean = sum of all grades / number of grades
Median = middle value of the sorted grades
Standard deviation = sqrt(sum of (each grade - mean) squared / number of grades)
Highest grade = max(grades)
Lowest grade = min(grades)
Range = max(grades) - min(grades)

'''
import math

grade = [85, 92, 78, 65, 88, 72, 90, 85, 83, 72]
print("*"*39)

def mean(g):
    sum = 0
    for i in g:
        sum += i
    return sum/len(g)
print("Mean: ", mean(grade))
print("*"*39)

def median(g):
    g.sort()
    if len(g) % 2 == 0:
        return (g[len(g)//2] + g[len(g)//2 - 1])/2
    else:
        return g[len(g)//2]
print("Median: ", median(grade))
print("*"*39)

def standard_deviation(g):
    sum = 0
    m = mean(g)
    for i in g:
        sum += (i - m)**2
    return math.sqrt(sum/len(g))
print("Standard Deviation: ", standard_deviation(grade))
print("*"*39)

def highest_grade(g):
    return max(g)
print("Highest Grade: ", highest_grade(grade))
print("*"*39)

def lowest_grade(g):
    return min(g)
print("Lowest Grade: ", lowest_grade(grade))
print("*"*39)

def range_grade(g):
    return max(g) - min(g)
print("Range: ", range_grade(grade))
print("*"*39)