import pandas as pd
from requests import head

df = pd.read_csv("filtered_version.csv")

star = df["Star_name"].tolist()
mass = df["mass"].tolist()
radius=df["radius"].tolist()
gravity = df["gravity"].tolist()
distance = df["distance"].tolist()

final_list=[]

temp={}
for i in range(0,len(star)):
    temp['Star_name']=star[i]
    temp['mass']=mass[i]
    temp['radius']=radius[i]
    temp['gravity']=gravity[i]
    temp['distance']=distance[i]
    final_list.append(temp)
    temp={}



