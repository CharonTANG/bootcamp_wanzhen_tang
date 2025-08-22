#the cleaning process for this file
1. inspect the data first
2. identify all na
3. handling na
* drop the line with more than 50% na
* age, income, score are numbers, fillna with median
* drop the line with na in city
* extra_data with too many na, let it be
* extra_data missing too many, leave it to be
4. change form
* age is int, change it
* city is category, change it


# reflection:
1. how to identify all na in large dataset?
2. assuming income, age, score, city are MCAR or MAR
