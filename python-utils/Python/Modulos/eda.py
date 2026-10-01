import pandas as pd
import numpy as np

def exploracion_metadatos(df, y):
    # Obtenemos nuestras variables y sus tipos
    meta = pd.DataFrame(df.dtypes).reset_index()
    meta.columns = ['Variable', 'Tip']    

    # Calculamos algunos metadatos de nuestra data
    meta['Observaciones'] = meta['Variable'].apply(lambda x: df[x].count())
    meta['Valores_Unicos'] = meta['Variable'].apply(lambda x: len(df[x].unique()))
    meta['Valores_Nulos'] = meta['Variable'].apply(lambda x: df[x].isnull().sum())
    meta['%_Valores_Nulos'] = round(meta['Valores_Nulos']/df.shape[0]*100, 2)
    
    # Calculamos algunos valores adicionales
    
    # Kurtosis
    kurtosis = pd.DataFrame(df.kurt(numeric_only=True)).reset_index()
    kurtosis.columns = ['Variable', 'Kurtosis']
    
    # Inclinación
    skewness = pd.DataFrame(df.skew(numeric_only=True)).reset_index()
    skewness.columns = ['Variable', 'Skewness']
    
    # Correlación
    corr = df.corr().reset_index()[['index', y]]
    corr.columns = ['Variable', 'Correlacion']
    corr['Correlacion'] = corr['Correlacion'].apply(lambda x: abs(x))
    
    meta = pd.merge(meta, kurtosis, how='left')
    meta = pd.merge(meta, skewness, how='left')
    meta = pd.merge(meta, corr, how='left')

    return meta