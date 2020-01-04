import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('2010YumaAz.csv')
days = ['TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY', 'MONDAY']

data = []

for day in days:
    trace = go.Scatter(x=df['LST_TIME'],
                       y=df[df['DAY'] == day]['T_HR_AVG'],
                       mode='lines',
                       name=day)
    data.append(trace)

# The below is a single line declaration of data which is slightly harder to read but yields the same result
# data = [{
#     'x':df['LST_TIME'],
#     'y':df[df['DAY'] == day]['T_HR_AVG'],
#     'name': day
# }for day in df['DAY'].unique()]

layout = go.Layout(title='Daily Temp Average')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='linechartexercise.html')
