# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 18:53:39 2020

@author: theon
"""

#Importing modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


#Read in the data
gdp_data = pd.read_csv('gdp_data_cleaned.csv')
fer_data = pd.read_csv('fer_data_cleaned.csv')
mor_data = pd.read_csv('mor_data_cleaned.csv')


#Explore data
gdp_data.columns
gdp_data.iloc[:,0]

gdp_data.describe()
gdp_data.dtypes


#Check for null value
gdp_data.isnull().any(axis = 1) #we want to check nulls of rows instead because it let us see how many countries have null values to them


#Check for trend: trend of United States data
Years = np.arange(1960,2019)

##Find US index
gdp_country = gdp_data.iloc[:,0].tolist()
us_index = gdp_country.index('United States')


##Fertility and Mortality data is similar to GDP data, we can explore it by repeating steps above
gdp_data.iloc[us_index,4:62].plot()
plt.title('US GDP from 1960 - 2018')
plt.ylabel('GDP')
plt.xlabel('Years')
plt.show()

fer_data.iloc[us_index,4:62].plot()
mor_data.iloc[us_index,4:62].plot() #from this, we get a general sense that: for US, the higher the GDP, the lower the fer and mor rates


#Perform regression: let first examine the data of United States

##GDP vs. Fer
x = gdp_data.iloc[us_index,4:].values.reshape(-1, 1)
y = fer_data.iloc[us_index,4:].values.reshape(-1, 1)

poly = PolynomialFeatures(degree = 2)
x_poly = poly.fit_transform(x) #transform x from being an independent variable to a polynomial curve

pilreg_y = LinearRegression() #training the dataset
pilreg_y.fit(x_poly, y)

plt.subplot(321)
plt.scatter(x, y, color = 'r', label = 'Data')
plt.plot(x, pilreg_y.predict(poly.fit_transform(x)), color = 'b', label = 'Fit')
plt.title('US GDP Vs. Fertility Rate')
plt.ylabel('US Fertility Rates')
plt.xlabel('US GDP')
plt.legend()

plt.subplot(322)
plt.scatter(Years, y)
plt.title('US Fertility from 1960 - 2018')
plt.ylabel('Fertility Rates')
plt.xlabel('Years')
plt.show()


##GDP vs. Mor
z = mor_data.iloc[us_index,4:].values.reshape(-1, 1)

pilreg_z = LinearRegression()
pilreg_z.fit(x_poly, z)

plt.subplot(321)
plt.scatter(x, z, color = 'r', label = 'Data')
plt.plot(x, pilreg_z.predict(poly.fit_transform(x)), color = 'b', label = 'Fit')
plt.title('US GDP Vs. Mortality Rate')
plt.ylabel('Mortality Rates')
plt.xlabel('GDP')
plt.legend()

plt.subplot(322)
plt.scatter(Years, z)
plt.title('US Mortality from 1960 - 2018')
plt.ylabel('Mortality Rates')
plt.xlabel('Years')
plt.show()


##Check MSE and R**2
print('US GDP vs. Fertility: MSE =', round(mean_squared_error(y, pilreg_y.predict(poly.fit_transform(x))), 3), ', R2 =', round(r2_score(y, pilreg_y.predict(poly.fit_transform(x))), 3))
print('US GDP vs. Mortality: MSE =', round(mean_squared_error(z, pilreg_z.predict(poly.fit_transform(x))), 3), ', R2 =', round(r2_score(z, pilreg_z.predict(poly.fit_transform(x))), 3))