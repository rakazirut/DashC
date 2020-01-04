import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../BubblePlotIntro/mpg.csv')

data = [go.Scatter(x=df['horsepower'],
                   y=df['acceleration'],
                   text=df['name'],
                   mode='markers',
                   marker=dict(size=df['weight']/100,
                               color=df['model_year'],
                               showscale=True))]

layout = go.Layout(title='Acceleration: Bubble Chart',
                   xaxis=dict(title='Horsepower'),
                   yaxis=dict(title='Acceleration (Seconds to reach 60 MPH'))
fig = go.Figure(data=data, layout=layout)
fig.layout.paper_bgcolor = '#000'
fig.layout.plot_bgcolor = '#000'
pyo.plot(fig, filename='bubbleplotexercise.html')
