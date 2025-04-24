'''
Question 3: Moving Average
------------------------
Calculate the moving average of time series data with a specified window size. The function
should:
1. Accept a list of numbers and a window size
2. Return a list of moving averages
Example Input:
data = [1, 3, 5, 7, 9, 11, 13, 15]
window_size = 3
Expected Output: [3.0, 5.0, 7.0, 9.0, 11.0, 13.0]

___________________________________________
prerequisites:

moving average = average of a subset of data
window size = number of data points to include in the average

'''
def moving_average(data, window_size):
    moving_avg = []
    n = len(data)
    range_till = len(data) + 1 - window_size
    for i in range(range_till):
        window_sum = data[i] + data[i + 1] + data[i + 2]
        window_avg = window_sum / window_size
        moving_avg.append(window_avg)
    return moving_avg

data = [1, 3, 5, 7, 9, 11, 13, 15]
window_size = 3
print(moving_average(data, window_size))
