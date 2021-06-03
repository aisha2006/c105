import csv 
import math

with open("data.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

#Finding mean
data=file_data[0]
def mean(data):
    n = len(data)
    sum=0
    for x in data:
        sum+=int(x)
    mean=sum/n
    return mean 

#subtracting from mean and squaring
squaredList = []
for i in data:
    a=int(i)-mean(data)
    a=a**2
    squaredList.append(a)

    
#Summing 
total=0
for n in squaredList:
    total=total+n

#Dividing sum by total values
result=total/(len(data)-1)

#Getting square root of the result
standardDeviation = math.sqrt(result)
print(standardDeviation)
