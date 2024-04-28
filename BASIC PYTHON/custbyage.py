import pandas as pd
import matplotlib.pyplot as plt

data = { 
    'Customer ID': [1,2,3,4,5,6,7,8,9,10], 
    'Age' : [25,32,28,40,50,45,38,27,33,29] 
}

df = pd.DataFrame(data)

plt.hist(df['Age'],bins=10,edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Number of customers')
plt.title('Distributuon of customers by age')

plt.show()