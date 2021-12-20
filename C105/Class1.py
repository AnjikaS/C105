import csv
import pandas as pd
import plotly_express as px
with open("class1.csv",newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)

file_data.pop(0)

totalmarks = 0
totalentries = len(file_data) 

for marks in file_data:
    totalmarks = totalmarks + float(marks[1])

mean = totalmarks/totalentries
print("Mean: " + str(mean))

df = pd.read_csv("class1.csv")
fig = px.scatter(df,x="Student Number",y="Marks")
#starting line = x0, y0 and ending line is x1,y1; line is very long so 2 coord points for x and y
fig.update_layout(shapes=[dict(type='line',y0=mean,y1=mean,x0=0,x1=totalentries)]) #used to show a shape or line in the graph for statistics
fig.update_yaxes(rangemode="tozero")
fig.show()
