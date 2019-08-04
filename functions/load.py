import pandas as pd

def load(df, path): 
    df.to_csv(path,index=False)