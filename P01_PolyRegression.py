# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:15:59 2020

@author: theon
"""

#Importing Modules
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import random
random.seed(1)


#Read in the data
gdp_data = pd.read_csv('gdp_data_cleaned.csv')
fer_data = pd.read_csv('fer_data_cleaned.csv')
mor_data = pd.read_csv('mor_data_cleaned.csv')


#Create lists for 3 groups: Core nations, semi-periphery nations, periphery nations 
core = [] #Core countries requirement: GDP > 1500000000000
semi_peri= [] # Semi periphery countries requirement: 1500000000000 >= GDP > 250000000000
peri = [] #Periphery countries requirement: GDP < 250000000000

for i in range(gdp_data.shape[0]):
    recent_data = gdp_data.iloc[i, -1]
    if recent_data > 1500000000000:
        core.append(gdp_data.iloc[i, 0])    
    elif recent_data <= 1500000000000 and recent_data > 250000000000:
        semi_peri.append(gdp_data.iloc[i, 0])
    else:
        peri.append(gdp_data.iloc[i, 0])
        

#Find random countries from core nations and periphery nations
core_selected = random.sample(core, 5)
semi_peri_selected = random.sample(semi_peri, 5)
peri_selected = random.sample(peri, 5)


#Creating polynomial regression loop function: to help repeat the same procedure for 15 different countries (5 countries from each group)
gdp_country = gdp_data.iloc[:,0].tolist()

def PolyRegressionLoop(country_list):
    for i in range(len(country_list)):
        country_index = gdp_country.index(country_list[i])
        
        x = gdp_data.iloc[country_index,4:].values.reshape(-1, 1)
        y = fer_data.iloc[country_index,4:].values.reshape(-1, 1)
        z = mor_data.iloc[country_index,4:].values.reshape(-1, 1)
            
        poly = PolynomialFeatures(degree = 2)
        x_poly = poly.fit_transform(x)
    
        pilreg_y = LinearRegression()
        pilreg_y.fit(x_poly, y)
    
        pilreg_z = LinearRegression()
        pilreg_z.fit(x_poly, z)
        
        print(country_list[i], 'GDP vs. Fertility: MSE =', round(mean_squared_error(y, pilreg_y.predict(poly.fit_transform(x))), 3), ', R2 =', round(r2_score(y, pilreg_y.predict(poly.fit_transform(x))), 3))
        print(country_list[i], 'GDP vs. Mortality: MSE =', round(mean_squared_error(z, pilreg_z.predict(poly.fit_transform(x))), 3), ', R2 =', round(r2_score(z, pilreg_z.predict(poly.fit_transform(x))), 3))
        
        plt.figure()
        plt.suptitle(country_list[i])
        
        plt.subplot(2,2,1)
        plt.scatter(x, y, color = 'r', s = 15, label = 'Data')
        plt.plot(x, pilreg_y.predict(poly.fit_transform(x)), color = 'b', label = 'Fit')
        plt.title('GDP Vs. Fertility Rate')
        plt.ylabel('Fertility Rates')
        plt.xlabel('GDP')
        plt.legend()
            
        plt.subplot(2,2,2)
        plt.scatter(x, z, color = 'r', s = 15, label = 'Data')
        plt.plot(x, pilreg_z.predict(poly.fit_transform(x)), color = 'b', label = 'Fit')
        plt.title('GDP Vs. Mortality Rate')
        plt.ylabel('Mortality Rates')
        plt.xlabel('GDP')
        plt.legend()
        
    plt.show()


#Test out 'PolyRegressionLoop' function
PolyRegressionLoop(core_selected)
PolyRegressionLoop(semi_peri_selected)
PolyRegressionLoop(peri_selected)
