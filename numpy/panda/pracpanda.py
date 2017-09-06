'''
#######################
# panda practice
#######################
'''
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys,os
import matplotlib


print('\nPython version ' + sys.version )
print('\nPandas version ' + pd.__version__ )
print('\nMatplotlib version ' + matplotlib.__version__)
'''
'''
sales = [{'account': 'Jones LLC', 'Jan': 150, 'Feb': 200, 'Mar': 140},
         {'account': 'Alpha Co',  'Jan': 200, 'Feb': 210, 'Mar': 215},
         {'account': 'Blue Inc',  'Jan': 50,  'Feb': 90,  'Mar': 95 },
         {'account': 'Max Bupa','Jan':300,'Feb':500,'Mar':4}]
print(pd.DataFrame(sales))## row oriented approach(as you see in rows)
print
print
print( pd.DataFrame.from_dict(sales)) ## column oriented approach(key specific)
df=pd.DataFrame(sales)
print
df = df[['account', 'Jan', 'Feb', 'Mar']]
#df = df[['account']] ### will list only account column values
print (df)

'''
'''
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]
BDataSet = list(zip(names,births))
print BDataSet
print
df = pd.DataFrame(data=BDataSet,columns={'Names','Number'})
print  df
df.to_csv('df.csv',index=True,header=True) # with header and index
#df.to_csv('df4.csv',index=False,header=False) # without header and index

#location = r'C:\Users\david\notebooks\update\births1880.csv'  ### use "r" as a escape sequnce for the file path
location=os.getcwd() + "/df.csv"
print(location)
df =pd.read_csv(location)
print df
print
print
df =pd.read_csv(location) ### with header values
#df =pd.read_csv(location,header=None) ### no header values
print df


sortedlist=df.sort_values(['Number'],ascending=False)
print sortedlist

print df['Number'].max()

'''
import pandas as pd
import numpy as np
import sys
from numpy import random

names = ['Bob','Jessica','Mary','John','Mel']
random.seed(100)
random_names = [names[random.randint(low=0,high=len(names))] for i in range(1000)]

# Print first 10 records
#print random_names[:10]

births = [random.randint(low=0,high=1000) for i in range(1000)]
#print births[:10]

BabyDataSet = list(zip(random_names,births))
#print (BabyDataSet)

df = pd.DataFrame(data=BabyDataSet, columns=['Names', 'Births'])
print df.head()


#df.to_csv('births1880.txt',index=False,header=False)

#print df['Names'].unique()








