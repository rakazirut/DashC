import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('C:/Users/Robert/Documents/Github/DashC/Course/PlotlyLearn/BoxPlot/BoxPlotExercise/abalone.csv')

data = [go.Histogram(x=df['length'], xbins=dict(start=0, end=1, size=0.02))]

layout = go.Layout(title='Abalone Length',
                   xaxis=dict(title='Length'),
                   yaxis=dict(title='Quantity'))

fig = go.Figure(data=data, layout=layout)
fig.layout.paper_bgcolor = '#000'
fig.layout.plot_bgcolor = '#000'

pyo.plot(fig, filename='histogramexercise.html')