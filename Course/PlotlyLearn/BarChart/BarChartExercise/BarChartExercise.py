import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('mocksurvey.csv', index_col=0)
# Horizontal stacked bar chart
data = [go.Bar(y=df.index, x=df[response], orientation='h', name=response) for response in df.columns]

layout = go.Layout(title='Survey Results', barmode='stack')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='barchartexercise.html')
