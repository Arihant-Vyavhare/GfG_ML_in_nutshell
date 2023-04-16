import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

names = ['spg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'modelyear',
'origin', 'carname']

df = pd.read_csv("auto-mpg.data", sep = '\s+', header = None, names = names)

df.head()