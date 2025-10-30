import pandas as pd
from mydb import db,engine
df = pd.read_csv("/home/mids/m273234/sd321/project1/crime_by_lsoa.csv")
print(len(df))
print('\n')
print(df.isnull().sum())
#df = df[(df['year'] > 2009) & (df['year'] < 2014) ]
df = df[df['year']==2013]
df['month'] = df['month'].astype(str).str.zfill(2)
df['year'] = df['year'].astype(str)
df['Date'] = df['month'].str.cat(df['year'],sep='/')

df.drop(columns=['month','year','minor_category','borough'],inplace=True)
df = df.sample(frac=0.5,random_state=1).reset_index(drop=True)
print(len(df))
print('\n')




total_memory_bytes = df.memory_usage(index=True).sum()
print(f"Total DataFrame memory usage: {total_memory_bytes} bytes")


df.to_sql('Crime', con=engine, if_exists='append', index=False)