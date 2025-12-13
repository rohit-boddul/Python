# PANDAS (Panel Data)

# 1. data ingestion - csv, json, excel etc. (to read the data)
# 2. data cleaning - missing values, wrong data, duplicates, fixing invalid values
# 3. data transformation like ETL - modifying data by creating new columns, reshaping tables, and analysis
# 4. data aggregation - group by etc
# 5. data validation - data meets expected rows by checking anamolies 
# 6. loading data
# 7. performance optimization for fast data processing 

from loguru import logger
import pandas as pd

data = {
    "name":['rohit', 'rachana', 'aditya'],
    'age':[27, 27, 25],
    'city':['hyderabad', 'pune', 'banglore']
}

df = pd.DataFrame(data)
print(df)
