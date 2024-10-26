import pandas as pd 
import numpy as np
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv('test.csv') 
categorical_cols = ['RestBP','Chol','Fbs','RestECG']
for col in categorical_cols:
  le = preprocessing.LabelEncoder()
  df[col] = le.fit_transform(df[col])

variables = df.iloc[:,:-1]
HeartDisease = df.iloc[:,-1]

model = GaussianNB()
model.fit(variables,HeartDisease)

print(f"Creating Predictions on the following data....")
predict_data = variables.iloc[0:5]
display(predict_data)
predicted_output = model.predict(predict_data)
print('+'*50)
print(f"Model Predictions: {predicted_output}")