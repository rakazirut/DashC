import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv('iris.csv')

t1 = df[df['class'] == 'Iris-setosa']['petal_length']
t2 = df[df['class'] == 'Iris-versicolor']['petal_length']
t3 = df[df['class'] == 'Iris-virginica']['petal_length']

hist_data = [t1,t2,t3]
group_label = ['Iris Setosa', 'Iris Versicolor', 'Iris Virginica']

fig = ff.create_distplot(hist_data, group_label,bin_size=[1,1,1])

pyo.plot(fig, filename='distplotexercise.html')

