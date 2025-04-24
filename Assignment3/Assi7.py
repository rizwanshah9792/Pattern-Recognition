'''
Question 7:
Calculate the correlation matrix for the data in Question 6 and interpret the results.
# Interpretation
corr_xy > 0.8:
The correlation coefficient indicating a strong positive linear relationship.
corr_xy > 0.5:
"The correlation coefficient indicates a moderately positive linear relationship.
corr_xy > 0:
The correlation coefficient indicates a weak positive linear relationship.
corr_xy == 0:
The correlation coefficient indicates no linear relationship.
Else:
The correlation coefficient indicates a negative linear relationship.

'''

import numpy as np
import math

# Set NumPy print options to show 1 decimal place
np.set_printoptions(formatter={'float': '{:.2f}'.format})

sd_x = math.sqrt(2.5)
sd_y = math.sqrt(6.5)
covXY = 4.0

correlation = covXY / (sd_x * sd_y)
corr_matrix = np.array([[1, correlation],
                        [correlation, 1]])

print(f"Correlation Matrix:\n{corr_matrix}")