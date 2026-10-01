import pandas as pd

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 9, 8]
})

print(df)

df.to_json('./JSON/prueba.json')
df.to_json('./JSON/prueba_split.json', orient='split')
df.to_json('./JSON/prueba_index.json', orient='index')

# df = pd.read_json('./JSON/prueba.json')
# df = pd.read_json('./JSON/prueba_split.json', orient='split')
# df = pd.read_json('./JSON/prueba_index.json', orient='index')
print(df)