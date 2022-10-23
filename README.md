# Primary Data Analysis on $CO^2$ emission 

## Purpose and Description of the Project

Global warming has been a worldwide concern over the past decade, some have argued that the greenhouse gas emissions may be the main cause of this situation, and Carbon Dioxide $CO^2$ takes a great part of greenhouse gases. Therefore, this $CO^2$ emission data analysis is conducted in order to study some of the basic statistics.

## Main Features

1. The program includes several functions that can help users explore summary statistics such as mean, maximum, minimum and standard deviation.
2. The program provides a full report of all the countries' emission analysis, as well as report on country of users' entry. 
3. The program includes barplot which can visualize $CO^2$ emission over years within a conutry
4. The program compares two countries' emission in the same year, as well as two years' emission within the same country
5. The program has customizable functions feature which allows users to get summary statistics of the country and period of their choices.

## Execution instructions

All functions are executable using the name provided in the .py file, with the variables and variable types are specified in the API file (note that some of the files do not require variable entry). In addition, matplotlib and numpy are required interpreters for generating the bar plot. 

## Example of Running

```python
# returns average CO2 emission of Canada between 1990 and 2000
print(getcustavg("Canada", 1990, 2000))

# report every single countries' summary statistics  
reportall()
  
# returns bar plot of Canada's CO2 emission from 1750 to 2017
getcountrybar("Canada")
```
  
## Data and Sources

This dataset is downloaded from Kaggle from the author Yoann Boyere, the data uploading page is titled <em>CO2_GHG_emissions-datacontains<em>. 

The data contains $CO^2$ and GHG emissions for countries around the world since 1750 until 2017.
  
The source link on Kaggle is https://www.kaggle.com/datasets/yoannboyere/co2-ghg-emissionsdata, this is a updated version of original datasets, due to some mistakes in the original one, the orginal source is OurWorldInData (https://ourworldindata.org/co2-and-other-greenhouse-gas-emissions).
