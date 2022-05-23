# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 08:41:03 2022

@author: jhazy
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,10,0.2)
y1 = np.cos(x)

plt.plot(x, y1, 'o', linewidth=3, color=(0.2,0.1,0.4))
plt.grid()
plt.xlabel('x')
plt.title('Grafica 2')
plt.show()