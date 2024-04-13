import pandas as pd  
import os 
import scipy
import warnings
warnings.filterwarnings("ignore")

def toMin(val):
    val=str(val)
    ret=0
    if(val=='-'):
        return 0
    try:
        ar=val.split(':')
        ret =int(ar[0])*60+int(ar[1])
    except:
        print(val)
    return ret

def inspect(time, sched, file):
    
    time= time.applymap(toMin)
    time.fillna(0, inplace=True)

    sched['arrival_time']= sched['arrival_time'].apply(toMin)
    #sched.fillna(0, inplace=True)
    for x in range(len(time.columns)):
        ret=pd.DataFrame()
        
        #print(sched['stop_code'])
        frame= sched.loc[sched['stop_code']==int(time.columns.values[x])]
        print(frame)
        #frame = sched[(sched['stop_code'].values)==int(time.columns.values[0])]
        
        arrive=pd.to_numeric(frame['arrival_time'])
        sch=(pd.to_numeric(time.iloc[:,x]))
        arrive=pd.Series(arrive, copy=False)
        sch=pd.Series(sch, copy=False)
        print(arrive)
        print(sch)
        ret['difference']=sch.subtract(arrive, fill_value=0)
        print(ret)
        ret.to_csv('analysis/'+file+str(x)+'.csv', na_rep='0')

for file in os.listdir('../hr24'):
    a=pd.read_csv('../hr24/'+file)
    a=a.applymap(lambda x : str(x).replace('.', ':'))
    schedule =file.replace('-mf.csv_converted.csv', '.csv')
    sched=pd.read_csv('lineup/'+schedule)
    file=file.replace('.csv', '')
    inspect(a, sched, file)
