import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np

df = pd.read_csv('abalone.csv')

d1 = np.random.choice(df['rings'], 10, replace=False)
d2 = np.random.choice(df['rings'], 30, replace=False)

data = [go.Box(y=d1,
               name='Data Set 1'),
        go.Box(y=d2,
               name='Data Set 2')]

layout = go.Layout(title='Two Random Samples From Abalone.csv')

fig = go.Figure(data=data, layout=layout)
fig.layout.paper_bgcolor = '#000'
fig.layout.plot_bgcolor = '#000'

pyo.plot(fig, filename='boxplotexercise.html')
