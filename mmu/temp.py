# -*- coding: utf-8 -*-
"""
Polyfit_Data.py
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mydata = pd.read_excel('Kam_Data.xlsx')
df = pd.DataFrame(mydata)
xs = (df['Volt'])
ys = (df['nAJ'])
z = np.polyfit(xs,ys,20)
p = np.poly1d(z)
print('polynomial = ', p)
plt.axis([-0.1,0.8,-100,300])
plt.xlabel('Voltage V', fontsize=15)
plt.ylabel('Current nAJ', fontsize=15)
plt.plot(xs, ys, 'r+')
plt.show()