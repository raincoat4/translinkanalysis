import pandas as pd  
import warnings
import os
from datetime import datetime
warnings.filterwarnings("ignore")
folder='filteredSchedules'
output='lineup'


def filter(df):
    df['arrival_time'] = pd.to_datetime(df['arrival_time'].str.strip(), format='%H:%M:%S')
    # Calculate time difference between consecutive rows
    time_diff = df['arrival_time'] - df['arrival_time'].shift()

    # If the time difference is NaN, set it to 0 seconds
    time_diff.fillna(pd.Timedelta(seconds=0), inplace=True)

    df_filtered = df[time_diff >= pd.Timedelta(minutes=5)]
    df_filtered.drop_duplicates(subset=['arrival_time'], keep='first', inplace=True)
    return df_filtered

def tt(d):
    arrival_time_only = d.strftime("%H:%M")
    return arrival_time_only
#what is happeninggggggggg
for file in os.listdir(folder):
    filePath=os.path.join(folder, file)
    df = pd.read_csv(filePath)
    df = df[df['arrival_time'].str.split(':').str[0].astype(int) < 24]
    ret = filter(df)
    ret['arrival_time']=ret['arrival_time'].apply(tt)
    ret.to_csv(os.path.join(output, file))