import pandas as pd
import numpy as np

# read data from csv file and it has some data lost
data = pd.read_csv('../doc/profile.csv', encoding='utf-8')#17000 row
# rename  columns[0] to 'id'
data = data.rename(columns={data.columns[0]: 'number'})
#可以发现data用字典类型进行存储同时分别是前几行的值
# drop the rows which has NaN 
data = data.dropna(axis=0, how='any')
# drop the rows which has below 0 and over 100 in 'age' column
data = data.drop(data[(data.age < 0) | (data.age > 100)].index)#14820 row

# drop the same rows in 'id' column
data = data.drop_duplicates(subset='id', keep='first')#

transcript = pd.read_csv('../doc/transcript.csv', encoding='utf-8')
transcript = transcript.rename(columns={transcript.columns[0]: 'number'})
transcript = transcript.rename(columns={transcript.columns[1]: 'id'})
transcript = transcript.dropna(axis=0, how='any')

# merge data and transcipt by 'id'
data = pd.merge(data, transcript, on='id', how='left')
data = data.drop(['number_y'],axis=1)
data = data.rename(columns={data.columns[0]: 'number'})
#保留数据集中的id,age,gender,income,合并其他数据到相同的id里

data = data.groupby(['number','id','gender','age','income','became_member_on'])[['event','time','value']].apply(lambda x: x.values.tolist()).reset_index()
data = data.rename(columns={data.columns[6]: 'event-time-value'})

portfolio = pd.read_csv('../doc/portfolio.csv', encoding='utf-8')
#删除掉没有命名的列也就是列0 同时也就是可以直接用
portfolio = portfolio.drop(['Unnamed: 0'],axis=1)
portfolio = portfolio.rename(columns={portfolio.columns[5] : 'offer_id'})
test= list(portfolio.keys())
print(test)

# 把相同的id行合并

    



