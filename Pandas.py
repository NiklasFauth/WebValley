'''
Created on 24.06.2015

@author: niklas
'''
import pandas as pd

data = [1,2,3,4,5]
s = pd.Series(data, index = ['a', 'b', 'c', 'd', 'd'])
s.index = [1,2,3,4,5]


