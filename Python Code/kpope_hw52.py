# -*- coding: utf-8 -*-
# kpope_hw52.py
# Authors: Logan Smith Kimon Pope
# Andrew ID: kpope & logansmi
# Homework 5 Part 2

# Problem 1
print('*****Problem 1*****')
print()
import numpy as np
change = [[.8, .2, .1],[.1,.7, .3],[.1, .1, .6]]
M = np.array(change)

original = [[.2],[.3],[.5]]
x = np.array(original)

print(M)
print(x)

mLabel = np.sum(M, axis=0)
xLabel = np.sum(x)


print('M:%d\nx:%d' %(mLabel[0], xLabel))

print('-----------------------------')
print('------------------------------------------------------------------------')
print()
print()

# Problem 2
print('*****Problem 2*****')
print()
# Conclusion: The conclusion that can be drawn from the data is that Alice will have a majority of the market share after two years
#             Additionally, Bob will gain 5 percent, whereas, Carrie will lose a majority of the market share. 
#             Lastly, after 10 months the outputs will remain the same for the remaining months of a two year period.  
mTimesx = M.dot(x)
month = 0
percent = '%'
print('%6s\t%8s\t%6s\t%8s' %('Month:', 'Alice\'s', 'Bob\'s', 'Carrie\'s'))
for i in range(0, 24):
    newVal = (x*100)
    print("%6d\t%7.1f%s\t%5.1f%s\t%7.1f%s"%(month, newVal[0], percent, newVal[1], percent, newVal[2], percent))
    month += 1
    x = M.dot(x)   

print('------------------------------')
print('------------------------------------------------------------------------')
print()
print()

# Problem 3
print('*****Problem 3*****')
print()
# Conclusion: The conclusion that can be drawn from the data is that after month 7
#             the percentage change of customers retained and gained will be the exact same through a two year period. 
#             Lastly, each individual will experience large changes between customers retained and gained. 

month = 0
for i in range (0, 24):
    print('Month   %d' %(month))
    print(M)
    M = M.dot(M)
    month += 1