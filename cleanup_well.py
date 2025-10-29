import pandas as pd
df = pd.read_csv("/home/mids/m273234/sd321/project1/london-ward-well-being.csv")
df.drop(columns=['Old Ward Code','Ward'],inplace=True)
print(df.head())