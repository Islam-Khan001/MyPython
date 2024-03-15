# Todays Topics - Random in numpy

# 1st way to import
# import numpy as np
# np.random.rand or randn or randint(1,100)

# 2nd way to import
from numpy import random

num = random.randint(0,100)
print(num)

num1 = random.randn()
print(num1)

num2 = random.rand()
print(num2)

num3 = random.choice([1,4,67,3,6,3,6])
print(num3)

#HomeWorks

# np - mean,medain,std, var, percentile
# np.mean(agelist);
# np.medain(agelist); - mid value
# home work - np.std(agelist)
# np.var(agelist) - varianve ka square = std
# np.percentile(agelst, number)- kitni percent value kaisi hai
# mod - most frequent value - scipy module - stats- from scipy import stats

# home work  - what are pandas