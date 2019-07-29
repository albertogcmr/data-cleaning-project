import pandas as pd

def extract(path, encoding='latin-1'): 
    return pd.read_csv(path, encoding=encoding)
