# A Country GDP Vs. Its Fertility and Mortality Rates

I want to see whether there is a relationship between a country GDP and its fertility and mortality rates. I recreated this project from my CMSE class but improved it by apply a fundamental data science project's outline.

## Background and Motivation

I stumbled across this question when I was studying in my social science class about the prosperity of different countries. Especially, we looked at three types of nation: core nations, semi-periphery nations, and periphery nations. 

To summarize, a core nation is one that has strong power, both politically and economically (GDP > 1.5 trillions). While the periphery nation is a complete opposite (GDP < 250 billions). Hence, the semi-periphery nation is the one in between the two groups (1.5 trillions >= GDP > 250 billions). 

After learning about the differences between the three types, I started to form my curiosity around whether there are any trends that lead to the differences the way it is.

I finished this project once ([CMSE201_FinalProject.ipynb](https://github.com/chilam27/P01_GDP_Fertility_Mortality_Relation/blob/master/CMSE201_FinalProject.ipynb), original project file, can be found in this repository). I redid it with added step, such as: data cleaning and exploratory data analysis. I also practiced using `sklearn` package for statistical interpretation and building polynomial regression model.

## Prerequisites
Python Version: 3.7.4

Packages: pandas, numpy, sklearn, matplotlib, random

## Project Outline
1. Project planning: determine the necessary variables to compute statistical analysis to answer our question
    - List of variables: _GDP_ (Gross Domestic Product), _fertility rate_ (average number of children that would be born to a woman over her lifetime), _mortality rate_ (can be called death rate; is a measure of the number of deaths in a particular population)
2. Data cleaning: read the dataset in to get farmiliar with columns and values, modify the dataframes, delete null and unnecessary data values, extracting data from original to cleaned csv files
3. Exploratory data analysis: observe the cleaned data set and understand the general trend of the data
4. Regression model: perform polynomial regression and caculate mean squared error (MSE) and coefficient of determination (R**2)

As I am doing my research for the data source, I find the page [World Bank Group](https://www.worldbank.org/). Based on my findings, they have a very accountable data bank that I can use for my project. I also do some checking to see if the data is clean and whether there is an empty/ incomplete data point. Although there are incomplete data, I does not seem to affect my analysis too much. Here are the sources for data I collected:

* [The World Bank Group: GDP (current US$)](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD?most_recent_year_desc=false&view=map&year=2018)

* [The World Bank Group: Fertility rate, total (births per woman)](https://data.worldbank.org/indicator/SP.DYN.TFRT.IN/)

* [The World Bank Group: Death rate, crude (per 1,000 people)](https://data.worldbank.org/indicator/sp.dyn.cdrt.in)

### Data Cleaning

* Modify the dataframe: rename columns' names, delete unnecessary rows and columns
* Remove unrelated values: ex: 'World', 'Arab World', 'Caribbean small states', etc.
* Remove countries with incomplete data (complete: has data from 1960 to 2018)
* Make sure all three dataset (GDP, fertility, and mortality) have the same countries; if not, take countries that all three have in common
* Extracting cleaned data to new csv files: _gdp_data_cleaned.csv_, _fer_data_cleaned.csv_, _mor_data_cleaned.csv_

### Exploratory Data Analysis

In this stage, I want to specifcially look at United States and analyze its data and trend before applying the math and algorithm to other countries.

* Observe data: using methods, such as: `pandas.DataFrame.columns`, `pandas.DataFrame.describe`, etc.
* Check for null value or incomplete data
* Evalutae United States' GDP, fertility and mortality rates trend based on the data given
* Perform polynomial regression model
* Caculate the MSE and R**2 of the two graphs

(add pictures of graphs)

### Polynomial Regression Model (extended)

* Separate countries into 3 groups: core, semi-periphery, and periphery
* Randomly choose 5 countries from each group
* Creating a polynomial regression loop function to graph and caculate MSE and R**2

(add pictures of graphs)

### Overall Model Performance



## Conclusion



## Author

* **Chi Lam**, _student_ at Michigan State University - [chilam27](https://github.com/chilam27)

## Acknowledgments

* [Pritchard, Adam. "Markdown Cheatsheet."](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* [Thompson, Billie. "A template to make good README.md"](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [Wikipedia contributors. "List of countries by GDP (nominal)." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 9 Jun. 2020. Web. 13 Jun. 2020.](https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29)
* [World Population Review. "GDP Ranked by Country 2020."](https://worldpopulationreview.com/countries/countries-by-gdp/)
* [“machine learning with python video 14 Polynomial Regression.” YouTube, uploaded by 
I know python, 3 Apr. 2020, www.youtube.com/watch?v=2wzxzHoW-sg&t=381s.](https://www.youtube.com/watch?v=2wzxzHoW-sg&t=381s)
