import pandas as pd
import numpy as np
import plotly.express as px
df = pd.read_csv('cup to sleep.csv')
coffee = df['Coffee in ml'].tolist()
sleep = df['sleep in hours'].tolist()
graph = px.scatter(x = coffee, y = sleep)
graph.show()
d = {'x':coffee,'y':sleep}
corr = np.corrcoef(d['x'],d['y'])
print(corr)