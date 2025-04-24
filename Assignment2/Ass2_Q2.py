'''
Question 2: Joint Probability
----------------------------
A weather station records daily data about:
- Whether it rained (True/False)
- Whether it was cloudy (True/False)
Write a function to calculate the joint probability of it being both rainy AND cloudy.
Example Input:
rain_data = [True, False, True, True, False, False, True, False]
cloud_data = [True, False, True, False, False, True, True, False]
Expected Output: 0.375 (3 days out of 8 were both rainy and cloudy)
def calculate_weather_joint_probability(rain_data, cloud_data):
# Your code here
pass

'''
print("*"*39)
rain_data = [True, False, True, True, False, False, True, False]
cloud_data = [True, False, True, False, False, True, True, False]
def calculate_weather_joint_probability(rain_data, cloud_data):
    count = 0
    for i,j in zip(rain_data, cloud_data):
        if i == j == True:
            count += 1
    return count/len(rain_data)

print(calculate_weather_joint_probability(rain_data, cloud_data))
print("*"*39)
pass