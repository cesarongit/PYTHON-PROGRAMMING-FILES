
import warnings 
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


advertising = pd.DataFrame(pd.read_csv("advertising.csv"))
advertising.head()


advertising.shape


advertising.info()


advertising.describe()


advertising.isnull().sum()*100/advertising.shape[0]


fig, axs = plt.subplots(3, figsize = (5,5))
plt1 = sns.boxplot(advertising['TV'], ax = axs[0])
plt2 = sns.boxplot(advertising['Newspaper'], ax = axs[1])
plt3 = sns.boxplot(advertising['Radio'], ax = axs[2])
plt.tight_layout()


sns.boxplot(advertising['Sales'])
plt.show()


sns.pairplot(advertising, x_vars=['TV','Newspaper','Radio'], y_vars='Sales', height=4, aspect=1, kind='scatter')
plt.show()


sns.heatmap(advertising.corr(), cmap="YlGnBu", annot = True)
plt.show()

X = advertising ['TV']
Y = advertising ['Sales']

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size= 0.7, test_size=0.3, random_state=100)

X_train.head()
Y_train.head()

import statsmodels.api as sm

X_train_sm = sm.add_constant(X_train)
lr = sm.OLS(Y_train, X_train_sm).fit()

lr.params

print(lr.summary())

plt.scatter(X_train, Y_train)
plt.plot(X_train, 6.948 + 0.054*X_train, 'r')
plt.show()

Y_train_pred = lr.predict(X_train_sm)
res = (Y_train - Y_train_pred)

fig = plt.figure()
sns.distplot(res, bins = 15)
fig.suptitle('Error Terms', fontsize = 15)
plt.xlabel('Y_train - Y_Train_pred', fontsize = 15)
plt.show()

plt.scatter(X_train, res)
plt.show()

X_test_sm = sm.add_constant(X_test)

Y_pred = lr.predict(X_test_sm)

Y_pred.head()

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

np.sqrt(mean_squared_error(Y_test,Y_pred))

r_squared = r2_score(Y_test, Y_pred)
r_squared

plt.scatter(X_test, Y_test)
plt.plot(X_test, 6.948 + 0.054*X_test, 'r')
plt.show()

print(advertising)