import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df=pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['Matt', 'Michelle', 'Fil', 'Joanne'])

df2 = df[df['Matt']<0]

print(df)
