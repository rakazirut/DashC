import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import tools
import pandas as pd

df1 = pd.read_csv('2010SitkaAK.csv')
df2 = pd.read_csv('2010SantaBarbaraCA.csv')
df3 = pd.read_csv('C:/Users/Robert/Documents/Github/DashC/Course/PlotlyLearn/LineChart/LineChartExercise/2010YumaAZ.csv')

t1 = go.Heatmap(x=df1['DAY'], y=df1['LST_TIME'], z=df1['T_HR_AVG'], colorscale='Jet', zmin=5, zmax=40)
t2 = go.Heatmap(x=df2['DAY'], y=df2['LST_TIME'], z=df2['T_HR_AVG'], colorscale='Jet', zmin=5, zmax=40)
t3 = go.Heatmap(x=df3['DAY'], y=df3['LST_TIME'], z=df3['T_HR_AVG'], colorscale='Jet', zmin=5, zmax=40)

fig = tools.make_subplots(rows=1, cols=3, subplot_titles=['Sitka AK', 'Santa Barbara CA', 'Yuma AZ'], shared_yaxes=True)
fig.append_trace(t1, 1, 1)
fig.append_trace(t2, 1, 2)
fig.append_trace(t3, 1, 3)

fig['layout'].update(title = 'Temperature for 3 Cities')

pyo.plot(fig, filename='MultHeatmap.html')

