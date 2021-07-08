import pandas as pd
import csv
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
figure = ff.create_distplot([df["Mobile Brand"].tolist()],
["Brand"],
show_hist=False)
figure.show()