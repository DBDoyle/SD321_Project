import pandas as pd
df = pd.read_csv("London Housing Data.csv")
df = df.drop(columns=['no_of_crimes'])
df = df.dropna()
print('\n')
print(df.info())
print('\n')
print(df.isnull().sum())
df['Date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
df['Date'] = df['Date'].dt.strftime('%m/%Y')
print("\n")
print(df.head())

