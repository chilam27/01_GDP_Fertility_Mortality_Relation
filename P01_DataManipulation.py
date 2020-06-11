# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 19:20:41 2020

@author: theon
"""

#DataManipulation/ DataCleaning

##Importing modules
import pandas as pd


##Read in the data
gdp_data = pd.read_csv('API_NY.GDP.MKTP.CD_DS2_en_excel_v2_1068823.csv', header = None, skiprows = 3)

fer_data = pd.read_csv('API_SP.DYN.TFRT.IN_DS2_en_excel_v2_1068800.csv', header = None, skiprows = 3)

mor_data = pd.read_csv('API_SP.DYN.CDRT.IN_DS2_en_excel_v2_1069297.csv', header = None, skiprows = 3)


##Modify the data frame
gdp_data.columns = gdp_data.iloc[0]
gdp_data.drop([0], axis = 0, inplace = True)
gdp_data.drop(2019, axis = 1, inplace = True) #Drop 2019 columns because it doesnt have any value

fer_data.columns = fer_data.iloc[0]
fer_data.drop([0], axis = 0, inplace = True)
fer_data.drop(2019, axis = 1, inplace = True) #Drop 2019 columns because it doesnt have any value

mor_data.columns = mor_data.iloc[0]
mor_data.drop([0], axis = 0, inplace = True)
mor_data.drop(2019, axis = 1, inplace = True) #Drop 2019 columns because it doesnt have any value


##Delete unnecessary data, only keep the countries
country_original = gdp_data["Country Name"].tolist() #'country_original' is important because it has the original index

no_use_data = ['World', 'Arab World', 'Caribbean small states', 'Central Europe and the Baltics', 'East Asia & Pacific', 'East Asia & Pacific (excluding high income)', 'Euro area', 'Europe & Central Asia', 'Europe & Central Asia (excluding high income)', 'European Union', 'Fragile and conflict affected situations', 'Heavily indebted poor countries (HIPC)', 'Latin America & Caribbean', 'Latin America & Caribbean (excluding high income)', 'Least developed countries: UN classification', 'Middle East & North Africa', 'Middle East & North Africa (excluding high income)', 'North America', 'OECD members', 'Other small states', 'Pacific island small states', 'Small states', 'South Asia', 'Sub-Saharan Africa', 'Sub-Saharan Africa (excluding high income)', 'High income', 'Low & middle income', 'Low income', 'Lower middle income', 'Middle income', 'Upper middle income', 'IBRD only', 'IDA & IBRD total', 'IDA blend', 'IDA only', 'IDA total', 'Not classified', 'Pre-demographic dividend', 'Late-demographic dividend', 'Post-demographic dividend', 'East Asia & Pacific (IDA & IBRD countries)', 'Europe & Central Asia (IDA & IBRD countries)', 'Middle East & North Africa (IDA & IBRD countries)', 'Latin America & the Caribbean (IDA & IBRD countries)', 'South Asia (IDA & IBRD)', 'Sub-Saharan Africa (IDA & IBRD countries)', 'Early-demographic dividend']
no_use_index = []
for i in range(len(no_use_data)):
    x = country_original.index(no_use_data[i])
    no_use_index.append(x + 1)
    
gdp_data.drop(no_use_index, axis = 0, inplace = True)
fer_data.drop(no_use_index, axis = 0, inplace = True)
mor_data.drop(no_use_index, axis = 0, inplace = True)



##List of countries that have all data
gdp_data.dropna(axis = 0, inplace = True)

fer_data.dropna(axis = 0, inplace = True)

mor_data.dropna(axis = 0, inplace = True)

##Check if the three lists have the same countries: False means some no null values countries in one data set has null value in other data set
all(item in fer_data.iloc[:,0] for item in gdp_data.iloc[:,0])
all(item in mor_data.iloc[:,0] for item in gdp_data.iloc[:,0])

###Because they all have different values, perform task to take countries they have in common
test = set(gdp_data.iloc[:,0]).intersection(fer_data.iloc[:,0])
test2 = set(test).intersection(mor_data.iloc[:,0])
country_nonull = list(test2) #list of countries that does not have any null in three data set

gdp_data.reset_index(drop = True, inplace = True) #reset index
fer_data.reset_index(drop = True, inplace = True)
mor_data.reset_index(drop = True, inplace = True)

gdp_country_original = gdp_data["Country Name"].tolist()
fer_country_original = fer_data["Country Name"].tolist()
mor_country_original = mor_data["Country Name"].tolist()

##Based on 'country_nonull' list, seperate countries into 3 groups

###Create lists for 3 groups
core = [] #Core countries requirement: GDP > 200000000000
semi_peri= [] # Semi periphery countries requirement: GDP  <= 200000000000 and GDP > 250000000000
peri = [] #Periphery countries requirement: GDP < 250000000000

gdp_total_index = [] #collect index of 'country_nonull' from gdp_data
fer_total_index = []
mor_total_index = []

for i in range(len(country_nonull)):
    x = gdp_country_original.index(country_nonull[i])
    y = fer_country_original.index(country_nonull[i])
    z = mor_country_original.index(country_nonull[i])
    gdp_total_index.append(x) #utilizing for loop to create 'total_index' list for GDP
    fer_total_index.append(y)
    mor_total_index.append(z)
    
    recent_data = gdp_data.iloc[x,-1]
    if recent_data > 200000000000:
        core.append(country_nonull[i])    
    elif recent_data <= 200000000000 and recent_data > 250000000000:
        semi_peri.append(country_nonull[i])
    else:
        peri.append(country_nonull[i])
        
        
        
##Filter out all data set to have same values
gdp_data_cleaned = gdp_data.loc[gdp_total_index]
gdp_data_cleaned.sort_values(axis = 0, by = 'Country Name', inplace = True)

fer_data_cleaned = fer_data.loc[fer_total_index]
fer_data_cleaned.sort_values(axis = 0, by = 'Country Name', inplace = True)

mor_data_cleaned = mor_data.loc[mor_total_index]
mor_data_cleaned.sort_values(axis = 0, by = 'Country Name', inplace = True)


##Extracting cleaned csv files
gdp_data_cleaned.to_csv('gdp_data_cleaned.csv', index = False)
