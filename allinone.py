import csv
import pandas as pd

df = pd.read_csv('after_clean111.csv')
dd = pd.read_csv('NGC13-01.csv')

data = pd.merge(df,dd, on=['SerialNumber'], how = 'left')

data.to_csv('all_in_one.csv')