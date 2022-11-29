import pandas as pd

df = pd.read_excel(r'C:\Users\Logan\Dropbox (MIT)\_MIT_mengm_2022_fred_monterrey\FrEDFactoryModel\Fred python scripts\FrEDFactory_Parameters.xlsx')
df = df.fillna(value='N/A')
df = df.loc[df.index.repeat(df['quantity'])].reset_index(drop=False)  # if quantity is >1 make duplicates
df['quantity'] = df['quantity'].mask(df['quantity']> 1, 1)
