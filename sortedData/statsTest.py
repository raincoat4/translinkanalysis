import pandas as pd  
import os 
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
folder_path = 'analysis'


dfs = []

#get all the data
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
  
        file_path = os.path.join(folder_path, file_name)
        df = pd.read_csv(file_path)
      
        dfs.append(df)



    
data = pd.concat(dfs, ignore_index=True)
print(data)

# testing normallicy of data
stat, p_value = stats.normaltest(data['difference'])
print('normal test')
print("{:.2e}".format(p_value))
print(stat,('\nfails the normal test'),'\n\n')

# fails normal test 
# found that our data cannot be transformed to fit a normal distribution so resort to non-parametric tests
# can use -0.1 and 0.1 as bounds since we have no decimal values
dfs = []
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
  
        file_path = os.path.join(folder_path, file_name)
        df = pd.read_csv(file_path)
        categories = ['early', 'on time', 'late']    
        categories = pd.cut(df['difference'], bins=[-float('inf'), -0.1, 0.1, float('inf')], labels=categories, right=False)
        counts_df = pd.crosstab(index=categories, columns='count')
        counts_df = counts_df.T  # Transpose the dataframe
        counts_df.reset_index(drop=True, inplace=True)  # Reset index and drop old index
        dfs.append(counts_df)

table = pd.concat(dfs, ignore_index=True)
table.fillna(0, inplace=True)
print(table)
stat, p_value, _, e = stats.chi2_contingency(table)

print('chi2 test')
print("{:.2e}".format(p_value))

print('we fail to reject the null hypothesis suggesting that the data is independent\n\n\n')
#we fail to reject the null hypothesis suggesting that the data is independent

# checking to see if when busses are more early when early or more late when late

early=-1*data[data['difference']<0]
late=data[data['difference']>0]
print(early['difference'].mean())
print(late['difference'].mean())
statistic, p_value= stats.mannwhitneyu((late['difference']),early['difference'])
print('null hypothesis: when busses are not on time, there is no difference between how late or early busses are (late busses are as late as early busses are early)')
print("{:.2e}".format(p_value))
print(statistic)
print('we reject the null hypothesis and there is a difference between how late or early busses are when not on time\n\n')

statistic, p_value= stats.mannwhitneyu((data['difference']),[0]*len(data['difference']))
print("{:.2e}".format(p_value))

#we reject the null hypotheses 

plt.boxplot(data['difference'])
plt.xlabel('Data')
plt.ylabel('+- of lateness(min)')
plt.title('How late translink busses are in vancouver')
plt.savefig('boxplot.png')
#plt.show()
mean_values = data['difference'].mean()
median_values = data['difference'].median()
q1 = data['difference'].quantile(0.25)
q3 = data['difference'].quantile(0.75)
max_values = data['difference'].max()
min_values = data['difference'].min()

print("Mean values:")
print(mean_values)
print("Median values:")
print(median_values)
print("\nQ1 (25th percentile):")
print(q1)
print("\nQ3 (75th percentile):")
print(q3)
print("\nMaximum values:")
print(max_values)
print("\nMinimum values:")
print(min_values)