import csv 

with open("class2.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

#Removing the header
file_data.pop(0)

total_marks=0
total_students=len(file_data)


for i in file_data:
    total_marks+=float(i[1])

mean = total_marks/total_students
print("the mean is "+str(mean))

import pandas as pd
import plotly.express as px

df = pd.read_csv("class2.csv")
fig = px.scatter(df,x="Student Number",y="Marks")

fig.update_layout(shapes=[dict(
    type="line",
    y0=mean, y1=mean,
    x0=0, x1=total_students
)])

fig.update_yaxes(rangemode="tozero")
fig.show()