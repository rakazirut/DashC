import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('flights.csv')

data = [go.Heatmap(x=df['year'], y=df['month'], z=df['passengers'], colorscale='Jet')]

layout = go.Layout(title='Flight Heatmap')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename='HeatmapExercise.html')