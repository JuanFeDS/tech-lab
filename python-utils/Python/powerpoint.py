import pandas as pd
import matplotlib.pyplot as plt

import requests

from datetime import datetime

import json

datetime_now = datetime.now()

# Llamando los datos
try:
    df = pd.read_csv('./Datos/currencies.csv')
except:
    full_list_url = 'https://finance.yahoo.com/currencies'
    full_list_page = requests.get(full_list_url)

    df = pd.read_html(full_list_page.text)[0].drop_duplicates()
    df['pct_change'] = df['% Change'].str.slice(stop=-1).astype('float')
    
    df.to_csv('./Datos/currencies.csv', index=False)

# Ajustando los datos para el análisis

## Identificamos el top 5 por el mayor cambio porcentual   
sort_df = df.sort_values('pct_change', ascending=False)
sort_df = sort_df[['Name', 'Last Price', 'Change', 'pct_change']]

top_df = sort_df.head(5).reset_index(drop=True)
bottom_df = sort_df.tail(5).reset_index(drop=True)

# Nos quedamos con los nombres
top_name = top_df['Name'][0].replace('/', '')
botton_name = bottom_df['Name'][0].replace('/', '')

print(top_name)
print(botton_name)
