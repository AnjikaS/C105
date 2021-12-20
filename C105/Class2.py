import csv
import pandas as pd
import plotly_express as px

with open("class2.csv") as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

totalmarks = 0
totalentries = len(file_data)

for marks in file_data:
    totalmarks = totalmarks + float(marks[1])

Mean = totalmarks/totalentries
print("The mean is " + str(Mean))

df = pd.read_csv("class2.csv")
fig = px.scatter(df,x="Student Number",y="Marks")
fig.update_layout(shapes=[dict(type='line',y0=Mean,y1=Mean,x0=0,x1=totalentries)])
fig.update_yaxes(rangemode="tozero")
fig.show()