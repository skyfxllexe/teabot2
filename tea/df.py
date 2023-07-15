import pandas as pd

import os
df = pd.read_excel(f'{os.getcwd()}/teabot2/tea/tea2.xlsx')

df.drop('Unnamed: 8', axis = 1, inplace = True)
df.drop('Unnamed: 9', axis = 1, inplace = True)
df.drop('Unnamed: 10', axis = 1, inplace = True)
df.drop('Столбец1', axis = 1, inplace = True)
df.drop('Столбец2', axis = 1, inplace= True)
if __name__ == '__main__':
    print(df.head())