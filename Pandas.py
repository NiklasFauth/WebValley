'''
Created on 24.06.2015

@author: niklas
'''

import pandas as pd
import numpy as np
import matplotlib.pylab as plt

df1 = pd.DataFrame(np.random.randn(6, 3), index = list('abcdef'),
                  columns = ['A', 'B', 'C'])

df2 = pd.DataFrame(np.random.randn(6, 3), index = list('cdefgh'),
                  columns = ['D', 'E', 'F'])

df3 = df1.copy()

df = pd.concat([df1, df2], axis=1)
print df


'''
data = np.random.randn(5,2)
df = pd.DataFrame(data, index = list('abcde'),
                  columns = ['one', 'two'])
col = df.one
row = df.xs('b')

print df
df_copy = df.copy()

df.query('one > 0')
df.index = [1,2,3,4,5]
df.query('1 < index < 4')

df * df
np.exp(df)
df.mean()

df.apply(np.mean)
df.plot()
plt.show()
'''
