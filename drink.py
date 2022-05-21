import pandas as pd
import numpy as np
df = pd.read_csv('icecream.csv')
drink = df['Cold drink sales( ₹ )'].tolist()
temperature = df['Temperature'].tolist()
d = {'x':temperature, 'y':drink}
corr = np.corrcoef(d['x'],d['y'])
print(corr)