import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import array as arr
import array
import xarray
%matplotlib inline
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
from sklearn.metrics import classification_report, confusion_matrix
x = np.arange(10).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
model.fit(x, y)
LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                   intercept_scaling=1, l1_ratio=None, max_iter=100,
                   multi_class='warn', n_jobs=None, penalty='l2',
                   random_state=0, solver='liblinear', tol=0.0001, verbose=0,
                   warm_start=False)
model = LogisticRegression(solver='liblinear', random_state=0).fit(x, y)
train = pd.read_csv('train.py')
train.head()
from sklearn.metrics import classification_report
train.isnull()
train.shape
train.info()
train.boxplot()
plt.show()
sns.set_style('whitegrid')
sns.countplot(x='Survived', data=train, palette='RdBu_r')
