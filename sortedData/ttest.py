import pandas as pd  
import os 
from scipy import stats
import matplotlib.pyplot as plt
folder_path = 'analysis'


dfs = []

#get all the data
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
  
        file_path = os.path.join(folder_path, file_name)
        df = pd.read_csv(file_path)
      
        dfs.append(df)


data = pd.concat(dfs, ignore_index=True)

t_statistic, p_value = stats.ttest_1samp(data['difference'], 2.4)

print("{:.2e}".format(p_value))
print(t_statistic)
plt.boxplot(data['difference'])
plt.xlabel('Data')
plt.ylabel('+- of lateness(min)')
plt.title('How late translink busses are in vancouver')
plt.savefig('boxplot.png')
plt.show()
