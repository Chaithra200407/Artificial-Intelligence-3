# -*- coding: utf-8 -*-
"""Untitled15.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CWbnCNTabbWcn0QP1_0xCK_THFpmEf0V
"""

#step1 : Import library
import pandas as pd

#step2 : import data
Salary = pd.read_csv('https://github.com/YBI-Foundation/Dataset/raw/refs/heads/main/Salary%20Data.csv')

#step3 : define target(X) and feature(Y)

Salary.columns

y = Salary['Salary']
x = Salary[['Experience Years']]

#step4 : split
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=2529)

#step5 : select model
from sklearn.linear_model import LinearRegression
model = LinearRegression()

#step6 : train model (fit model)
model.fit(x_train,y_train)

#step7 : prediction
y_pred = model.predict(x_test)

x_test

#step8 : accuracy
from sklearn.metrics import mean_absolute_percentage_error
mean_absolute_percentage_error(y_test,y_pred)