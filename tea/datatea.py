
import pandas as pd
from df import *
token = '6035481042:AAEoILf63t7Hpw90afRahjYjDV0oPI9DDWQ'

hello_message_rus = """
Добро пожаловать в мир чая, мы занимаемся продажей чаев
"""

    

class Tea():
    def __init__(self, raw: pd.core.series.Series):
        self.name = raw[0]
        self.desc = raw[3]
        self.price1 = raw[4]
        self.price50 = raw[5]
    def get(self):
        return f'Название: {self.name}\nОписание: {self.desc}\nЦена за 50гр: {self.price50}'
names_of_tea_desc = []

dictObject = {}
for i in range(len(df)):
    object = Tea(df.iloc[i])
    dictObject[object.name] = object
    names_of_tea_desc.append(object.name)


dictTea = {
    
}