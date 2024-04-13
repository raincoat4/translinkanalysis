import pandas as pd
import numpy as np

df=pd.read_csv('stop_times.txt')
df1=pd.read_csv('trips.txt')
startDay=False
day=0
df=df[['trip_id','arrival_time', 'stop_id']]
df1=df1[['trip_id', 'trip_headsign']]

df= df.join(df1.set_index('trip_id'), on='trip_id')
print(df)

sorted=df.groupby('trip_headsign').apply(lambda x: x.sort_values(['trip_id', 'arrival_time'], ascending=True)).reset_index(drop=True)
print(sorted)

#sorted.drop(columns=['Unnamed: 0'], inplace=True)
sorted.to_csv('sorted.csv')
