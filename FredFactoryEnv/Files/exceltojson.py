import json
import pandas as pd


df = pd.read_excel(io=r"C:\Users\Logan\Dropbox (MIT)\_MIT_mengm_2022_fred_monterrey\FrEDFactoryModel\Fred python scripts\FrEDFactory_Parameters.xlsx")
df = df.fillna(value='')
df = df.loc[df.index.repeat(df['quantity'])].reset_index(drop=True)  # if quantity is >1 make duplicates
df['quantity'] = df['quantity'].mask(df['quantity'] > 1, 1)
data = {"Part Attributes": df.to_dict('records')}

json_string = json.dumps(data, indent=4)
with open('fred_parts.json', 'w') as f:
    f.write(json_string)
    f.close()
