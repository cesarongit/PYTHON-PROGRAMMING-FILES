import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

df = pd.DataFrame(data, columns=['A', 'B', 'C'])

column_sum = np.sum(df['A'])

column_mean = np.mean(df['B'])

filtered_data = df[df['C'] > 5]

plt.scatter(df['B'], df['C'])

plt.xlabel('B')
plt.ylabel('C')

plt.title('Scatter Plot of Columns B and C')

plt.show()
