import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = np.random.randint(0, 100, size=(10, 2)) 
columns = ['A', 'B']

df = pd.DataFrame(data, columns=columns)

mean_A = np.mean(df['A']) 

plt.scatter(df['A'], df['B'])
plt.xlabel('A')
plt.ylabel('B')

plt.title('Scatter Plot')

plt.show()