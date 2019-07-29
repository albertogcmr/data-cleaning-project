import pandas as pd
from .cleaning import clean_fatal, clean_age, clean_sex


def transform(df): 
    # cambiamos los nombres de las columnas: a minusculas y eliminando espacios
    df.columns = df.columns.str.lower().str.strip()

    df['fatal (y/n)'] = df['fatal (y/n)'].apply(clean_fatal)
    df['age'] = df['age'].apply(clean_age)
    df.sex = df.sex.apply(clean_sex)
    # df['shark'] = df.species.apply(shark_type)




    return df