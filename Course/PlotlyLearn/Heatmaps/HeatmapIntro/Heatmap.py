import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('2010SantaBarbaraCA.csv')
df2 = pd.read_csv('C:/Users/Robert/Documents/Github/DashC/Course/PlotlyLearn/LineChart/LineChartExercise/2010YumaAZ.csv')

data = [go.Heatmap(x=df['DAY'], y=df['LST_TIME'], z=(df['T_HR_AVG'] * (9 / 5)) + 32, colorscale='Jet')]

layout = go.Layout(title='Santa Barbara, CA Temperature')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename='Heatmap.html')