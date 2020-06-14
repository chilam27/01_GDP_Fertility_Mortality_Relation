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
core_selected = random.sample(core, 3)
semi_peri_selected = random.sample(semi_peri, 3)
peri_selected = random.sample(peri, 3)


#Creating polynomial regression loop function: to help repeat the same procedure for 9 different countries (4 countries from each group)
gdp_country = gdp_data.iloc[:,0].tolist()

mse_gdp_fer = []
mse_gdp_mor = []
r_gdp_fer = []
r_gdp_mor = []

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
        
        mse_gdp_fer.append(mean_squared_error(y, pilreg_y.predict(poly.fit_transform(x))))
        mse_gdp_mor.append(mean_squared_error(z, pilreg_z.predict(poly.fit_transform(x))))
        r_gdp_fer.append(r2_score(y, pilreg_y.predict(poly.fit_transform(x))))
        r_gdp_mor.append(r2_score(z, pilreg_z.predict(poly.fit_transform(x))))
        
        plt.figure()
        plt.suptitle(country_list[i])
        
        plt.subplot(211)
        plt.scatter(x, y, color = 'r', s = 15, label = 'Data')
        plt.plot(x, pilreg_y.predict(poly.fit_transform(x)), color = 'b', label = 'Fit')
        plt.title('GDP Vs. Fertility Rate & GDP Vs. Mortality Rate')
        plt.ylabel('Fertility Rates')
        plt.legend()
            
        plt.subplot(212)
        plt.scatter(x, z, color = 'r', s = 15, label = 'Data')
        plt.plot(x, pilreg_z.predict(poly.fit_transform(x)), color = 'b', label = 'Fit')
        plt.ylabel('Mortality Rates')
        plt.xlabel('GDP')
        plt.legend()
        
    plt.show()


#Test out 'PolyRegressionLoop' function
PolyRegressionLoop(core_selected)
PolyRegressionLoop(semi_peri_selected)
PolyRegressionLoop(peri_selected)


#Average MSE and R**2
print('Average of MSE for GDP vs. Fertility:', round(sum(mse_gdp_fer)/ len(mse_gdp_fer), 3))
print('Average of MSE for GDP vs. Mortality:', round(sum(mse_gdp_mor)/ len(mse_gdp_mor),3))
print('Average of R**2 for GDP vs. Fertility:', round(sum(r_gdp_fer)/ len(r_gdp_fer),3))
print('Average of R**2 for GDP vs. Mortality:', round(sum(r_gdp_mor)/ len(r_gdp_mor),3))
