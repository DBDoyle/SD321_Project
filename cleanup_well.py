import pandas as pd
from mydb import db,engine
df = pd.read_csv("/home/mids/m273234/sd321/project1/london-ward-well-being.csv")
df.drop(columns=['Old Ward Code','Ward'],inplace=True)
df = df.rename(columns={'New ward code': 'New_Ward_Code'})
print(df.head())

df.to_sql('Well_Being', con=engine, if_exists='append', index=False)