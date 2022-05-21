import pandas as pd
import numpy as np
df = pd.read_csv('icecream.csv')
icecream = df['Ice-cream Sales( ₹ )'].tolist()
temperature = df['Temperature'].tolist()
d = {'x':temperature, 'y':icecream}
correlation = np.corrcoef(d['x'],d['y'])
print(correlation)
