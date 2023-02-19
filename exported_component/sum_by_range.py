""""
    This script is used to find the percentage of exported component
    group by range
"""

import pandas as pd 
import numpy as numpy
import os
import csv


exp_path = '/home/budi/OTP_project/OTP_code/exported_component/'

# file_path = exp_path+'exported_component_result.csv'
perc_path = exp_path+'percentage_exp_comp.csv'
df = pd.read_csv(perc_path)

# percentage range [0%-25%, 26-50%, 51-75%, 76-100%]

range_0  = [0,0,0,0]
range_25 = [0,0,0,0]  
range_50 = [0,0,0,0]  
range_75 = [0,0,0,0]  
range_100 = [0,0,0,0]  
for index,row in df.iterrows():
    for i,val in enumerate(range_25):
        if row[i+1] <=25 and row[i+1] >=1 :
            range_25[i]+=1
        elif row[i+1] <=50 and row[i+1] >=26 :
            range_50[i]+=1
        elif row[i+1] <=75 and row[i+1] >=51 :
            range_75[i]+=1
        elif row[i+1] >=76 :
            range_100[i]+=1
        elif row[i+1] ==0 :
            range_0[i]+=1

sum_path = exp_path+'sum_exported_by_range.txt'

with open (sum_path,'w') as fl:
    fl.write('range_percentage & Activities & Service, & Receiver & Provider \\\ \n')
    fl.write('76-100 & '+ str(range_100[0]) + ' & ' + str(range_100[1]) + ' &  '+ str(range_100[2]) + ' & '+ str(range_100[3])+'\\\ \n')
    fl.write('51-75 & '+ str(range_75[0]) + ' & ' + str(range_75[1]) + ' &  '+ str(range_75[2]) + ' & '+ str(range_75[3])+'\\\ \n')
    fl.write('26-50 & '+ str(range_50[0]) + ' & ' + str(range_50[1]) + ' &  '+ str(range_50[2]) + ' & '+ str(range_50[3])+'\\\ \n')
    fl.write('1-25 & '+ str(range_25[0]) + ' & ' + str(range_25[1]) + ' &  '+ str(range_25[2]) + ' & '+ str(range_25[3])+'\\\ \n')
    fl.write('0 & '+ str(range_0[0]) + ' & ' + str(range_0[1]) + ' &  '+ str(range_0[2]) + ' & '+ str(range_0[3])+'\\\ \n')
