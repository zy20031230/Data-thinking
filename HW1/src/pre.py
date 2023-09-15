import pandas as pd
import numpy as np

# read data from csv file and it has some data lost
data = pd.read_csv('../doc/profile.csv', encoding='utf-8')#17000 row
# rename  columns[0] to 'id'
data = data.rename(columns={data.columns[0]: 'number'})
# drop the rows which has NaN 
data = data.dropna(axis=0, how='any')
# drop the rows which has below 0 and over 100 in 'age' column
data = data.drop(data[(data.age < 0) | (data.age > 100)].index)
