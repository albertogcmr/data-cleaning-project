import pandas as pd
from .cleaning import clean_fatal, clean_age, clean_sex, shark_name, is_provoked, clean_activity, delete_columns, get_units_qty, translate_month, get_day_month

MIN_YEAR = 1920

def transform(df): 
    # cambiamos los nombres de las columnas: a minusculas y eliminando espacios
    df.columns = df.columns.str.lower().str.strip()

    # Filtramos las fechas anteriores a 1920
    df = df[df['year']>MIN_YEAR].copy()

    df['fatal (y/n)'] = df['fatal (y/n)'].apply(clean_fatal)
    df['age'] = df['age'].apply(clean_age)
    df.sex = df.sex.apply(clean_sex)

    with open('./shark-data/shark-types.txt', 'r') as f:
        sharks = f.read().split()
    df['shark_name'] = df.species.apply(lambda x: shark_name(x, sharks=sharks))

    df['is_provoked'] = df.type.apply(is_provoked)
    df['activity'] = df.activity.apply(clean_activity)
    df = delete_columns(df, columns=['type', 'pdf', 'href formula', 'href', 'case number.1', 
                                     'case number.2', 'original order', 'unnamed: 22', 'unnamed: 23'])

    df["sizes"], df["units"]= zip(*df["species"].map(get_units_qty))
    df['date'] = df['date'].apply(translate_month)
    df['day'], df['month'] = zip(*df['date'].map(get_day_month))

    return df