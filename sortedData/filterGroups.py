import pandas as pd
import os 
import warnings
warnings.filterwarnings("ignore")
folderPath='busSchedule/'
output='filteredSchedules/'
if not os.path.exists(output):
    os.makedirs(output)
        
def filter_csv_files(row):
    stopId=row['Second Row Values']
    file=row['File Name']+'.csv'
    print(file+ '\n'+str(stopId)+'\n')
    stopId=[int(x) for x  in stopId]
    
    df = pd.read_csv(folderPath+file)
    
    filtered = df[df['stop_code'].isin(stopId)]
    group=filtered.groupby('stop_code')
    filtered=group.apply(lambda x: x.sort_values(by='arrival_time'))
    filtered.to_csv(output+file, index=False)
        
    
stop_ids=pd.read_csv('stations.csv')
stop_ids['Second Row Values']= stop_ids['Second Row Values'].str.split(',')

stop_ids.apply(filter_csv_files, axis=1)