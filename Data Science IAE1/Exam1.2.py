#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 14:25:51 2022

@author: sjcet
"""

import numpy as np
x=np.array( [[2, 3, 5],[1, 2, 4],[7, 8, 9]])
y=np.array( [[5, 6, 3],[8, 1, 2],[3, 1, 4]])
print("perform the operation 7x+Y^3=: \n",np.add((np.multiply(7,x)),(np.power(y,3))))
np.add((np.multiply(7,x)),(np.power(y,3)))
res=x.dot(y)
print ("Multiplication result:\n",res)
x_diag=np.diag(x)
y_diag=np.diag(y)
print("x's Diagonal Elements:",x_diag)
print("y's Diagonal Elements:",y_diag)
print("Rank of x:",np.linalg.matrix_rank(x))
print("Rank of y:",np.linalg.matrix_rank(y))

