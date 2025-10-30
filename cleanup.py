import pandas as pd
from mydb import db,engine

df = pd.read_csv("London Housing Data.csv")
df = df.drop(columns=['no_of_crimes'])
df = df.dropna()
print(df.isnull().sum())
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
df['date'] = df['date'].dt.strftime('%m/%Y')
print("\n")
print(df.head())

#df.to_sql('Housing', con=engine, if_exists='append', index=False)


