# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:15:59 2020

@author: theon
"""

#Regression Models

##Importing Modules
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


##Read in the data
gdp_data = pd.read_csv('gdp_data_cleaned.csv')
fer_data = pd.read_csv('fer_data_cleaned.csv')
mor_data = pd.read_csv('mor_data_cleaned.csv')


##Create lists for 3 groups: Core nations, semi-periphery nations, periphery nations 
core = [] #Core countries requirement: GDP > 200000000000
semi_peri= [] # Semi periphery countries requirement: GDP <= 200000000000 and GDP > 250000000000
peri = [] #Periphery countries requirement: GDP < 250000000000

for i in range(gdp_data.shape[0]):
    recent_data = gdp_data.iloc[i, -1]
    if recent_data > 200000000000:
        core.append(gdp_data.iloc[i, 0])    
    elif recent_data <= 200000000000 and recent_data > 250000000000:
        semi_peri.append(gdp_data.iloc[i, 0])
    else:
        peri.append(gdp_data.iloc[i, 0])
        

##Perform regression: let first examine the data of United States

###Find US index
gdp_country = gdp_data.iloc[:,0].tolist()
us_index = gdp_country.index('United States')


##Regression

###GDP vs. Fer
x = gdp_data.iloc[us_index,4:-1].values.reshape(-1, 1)
y = fer_data.iloc[us_index,4:-1].values.reshape(-1, 1)

poly = PolynomialFeatures(degree = 2)
x_poly = poly.fit_transform(x)

pilreg = LinearRegression()
pilreg.fit(x_poly, y)

plt.scatter(x, y, color = 'r')
plt.plot(x, pilreg.predict(poly.fit_transform(x)), color = 'b')


###GDP vs. Mor
z = mor_data.iloc[us_index,4:-1].values.reshape(-1, 1)

poly = PolynomialFeatures(degree = 2)
x_poly = poly.fit_transform(x)

pilreg = LinearRegression()
pilreg.fit(x_poly, z)

plt.scatter(x, z, color = 'r')
plt.plot(x, pilreg.predict(poly.fit_transform(x)), color = 'b')


