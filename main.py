# imports
import pandas as pd
import os
from functions import extract, transform, load

# variables
INPUT_FILE_PATH = './input/GSAF5.csv'
OUTPUT_FILE_PATH = './output/GSAF5-clean.csv'


def main(): 
    df = extract(INPUT_FILE_PATH)
    df = transform(df)
    load(df, OUTPUT_FILE_PATH)
    return df
    

if __name__ == '__main__': 
    main()