import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../BubblePlotIntro/mpg.csv')

data = [go.Scatter(x=df['displacement'],
                   y=df['acceleration'],
                   text=df['name'],
                   mode='markers',
                   marker=dict(size=df['weight']/400))]


layout = go.Layout(title='Acceleration vs. Displacement: Bubble Chart',
                   xaxis=dict(title='Displacement'),
                   yaxis=dict(title='Acceleration (Seconds to reach 60 MPH)'),
                   hovermode='closest')
fig = go.Figure(data=data, layout=layout)
fig.layout.paper_bgcolor = '#000'
fig.layout.plot_bgcolor = '#000'
pyo.plot(fig, filename='bubbleplotexercise2.html')
