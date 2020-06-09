# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 18:53:39 2020

@author: theon
"""

#DataExploration

##Importing modules
import pandas as pd


##Read in the data
gdp_data = pd.read_csv('API_NY.GDP.MKTP.CD_DS2_en_excel_v2_1068823.csv', header = None, skiprows = 3)
print(gdp_data)

fer_data = pd.read_csv('API_SP.DYN.TFRT.IN_DS2_en_excel_v2_1068800.csv', header = None, skiprows = 3)
print(fer_data)

mor_data = pd.read_csv('API_SP.DYN.CDRT.IN_DS2_en_excel_v2_1069297.csv', header = None, skiprows = 3)
print(mor_data)


##Explore data
gdp_data.columns #not much use because we cleared the header, instead:
gdp_data.iloc[0,:]

gdp_data.describe()
gdp_data.dtypes


##Check for null value
gdp_data.isnull().any(axis = 1) #we want to check nulls of rows instead because it let us see how many countries have null values to them
null_gdp = gdp_data.isnull().sum(axis = 1) / gdp_data.shape[0]
pd.Series.nsmallest(null_gdp) #it seems like even for countries with the least null value, there is still a value that is missing


##Check for trend: trend of US's GDP
gdp_data.iloc[253,4:62].plot()
fer_data.iloc[253,4:62].plot()
mor_data.iloc[253,4:62].plot() #from this, we get a general sense that: for US, the higher the GDP, the lower the fer and mor rates

###Fertility and Mortality data is similar to GDP data, we can explore it by repeating steps above