# imports
import pandas as pd
from functions import extract, transform, load

# variables
INPUT_FILE_PATH = './input/GSAF5.csv'
OUTPUT_FILE_PATH = './output/GSAF5-clean.csv'


def main(): 
    df = extract(INPUT_FILE_PATH)
    df = transform(df)
    load(df, OUTPUT_FILE_PATH)
    

if __name__ == '__main__': 
    main()