import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('mpg.csv')

data = [go.Scatter(x=df['horsepower'],
                   y=df['mpg'],
                   text=df['name'],
                   mode='markers',
                   marker=dict(size=df['weight']/100,
                               color=df['cylinders'],
                               showscale=True))]

layout = go.Layout(title='Miles Per Gallon: Bubble Chart',
                   xaxis=dict(title='Weight (Divided by 100)'),
                   yaxis=dict(title='MPG'))
fig = go.Figure(data=data, layout=layout)
fig.layout.paper_bgcolor = '#000'
fig.layout.plot_bgcolor = '#000'
pyo.plot(fig, filename='bubbleplot.html')
