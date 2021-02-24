import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

pen_id = [0, 18, 41, 48, 49, 75, 78, 87, 89, 90, 91, 92, 94, 95, 98, 99, 100, 101, 103, 104, 105, 107, 109, 110, 112, 115, 116, 117, 118, 121, 123, 125, 127, 128, 129, 131, 133, 136, 140, 145, 146, 155, 156, 157, 158, 160, 161, 164, 165, 166, 167, 169, 170, 172, 175, 176, 178, 180, 181, 182, 183, 187, 189, 192, 193, 195, 196, 200, 202, 203, 205, 207, 208, 209, 213, 216, 219, 224, 225, 226, 230, 231, 232, 234, 235, 239, 240, 241, 245, 250, 251, 252, 253, 257, 259, 261, 264, 265, 266, 268]

cumulative_cell_count = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

x = np.array(pen_id)
y = np.array(cumulative_cell_count)
x = x.reshape(-1,1)

linreg = LinearRegression(fit_intercept=False)

obj = linreg.fit(x,y)
trendline = linreg.predict(x)
plt.plot(x,y)
plt.plot(x,trendline,color='red')
plt.xlabel('Pen index')
plt.ylabel('Cumulative Sum of Cell Counts')
plt.show()



slope = linreg.coef_[0]

print()
