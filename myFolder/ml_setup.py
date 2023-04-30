import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import os







# data_file_path = os.path.join(cwd, "data", "raw", "auto-mpg.data")

names = ['spg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'modelyear',
'origin', 'carname']
# df = pd.read_csv(os.path.abspath("./data/raw/auto-mpg.data"), sep = '\s+', header = None, names = names)

df = pd.read_csv("./data/raw/auto-mpg.data", sep = '\s+', header = None, names = names)
# df = pd.read_csv(data_file_path, sep = '\s+', header = None, names = names)

print(df.head())

print(os.getcwd())

# print(cwd,data_file_path,sep = "\n")