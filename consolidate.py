import pandas as pd
from pathlib import Path

source_files = sorted(Path('C:/User/Desktop/').glob('*.csv'))

dataframes = []
for file in source_files:
    df = pd.read_csv(file) 
    df['source'] = file.name
    dataframes.append(df)

all = pd.concat(dataframes)

all.to_csv('consolidated.csv')
