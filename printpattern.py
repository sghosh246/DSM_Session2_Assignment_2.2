# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 12:17:29 2018
@author: Sourav Ghosh
"""
counter = 0
for iteration in range (0,5):
    counter += 1
    for pattern in range (0, counter-1):
        print ('*', end = ' ')
    print()
for iteration in range (0,5):
    counter -= 1
    for pattern in range (0, counter+1):
        print ('*', end = ' ')
    print()     
