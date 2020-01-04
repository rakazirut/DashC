import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('C:/Users/Robert/Documents/Github/DashC/Course/PlotlyLearn/BubblePlot/BubblePlotIntro/mpg.csv')

data = [go.Histogram(x=df['mpg'], xbins=dict(start=0, end=50, size=5))]

layout = go.Layout(title='Miles Per Gallon',
                   xaxis=dict(title='MPG'),
                   yaxis=dict(title='Quantity'))

fig = go.Figure(data=data, layout=layout)
fig.layout.paper_bgcolor = '#000'
fig.layout.plot_bgcolor = '#000'

pyo.plot(fig, filename='histogram.html')