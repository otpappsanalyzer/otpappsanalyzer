import pandas as pd 
import numpy as numpy
import os
import csv
from matplotlib import pyplot as plt


exp_path = '/home/budi/OTP_project/OTP_code/exported_component/'

file_path = exp_path+'exported_component_result.csv'
perc_path = exp_path+'percentage_exp_comp.csv'
df = pd.read_csv(file_path)
average = round((df.mean(axis=0)),2)
num_act = average[0]
num_ser = average[2]
num_rec = average[4]
num_pro = average[6]

df_per = pd.read_csv(perc_path)
percent = round(df_per.mean(axis=0),2)

sum_df=pd.DataFrame({'component types':['activities','services','receivers','providers'],
                'components':[average[0], average[2], average[4],average[6]],
                'exported_components':[average[1],average[3],average[5],average[7]]})

print(sum_df)
# sum_df=pd.DataFrame({'component':['activities','services','receivers','providers'],
#                 'number':[average[0], average[2], average[4],average[6]],
#                 'exported':[average[1],average[3],average[5],average[7]],
#                 'percentage':[percent[0],percent[1],percent[2],percent[3]]})


dest_path = exp_path+'exp_summary.txt'
dest_fig = exp_path+'perc_exp_comp.pdf'

sum_df.to_csv(dest_path,index=None,sep='&')
# print(sum_df)

sum_df.plot.bar(x='component types',width=0.9,figsize=(5,4))
plt.axis('tight')
# sum_df.plot.bar(x='Average # of Component and Exported Component per Apps', logy=True)
plt.xticks(rotation=0)
plt.ylabel('Average # per Apps')
plt.legend(bbox_to_anchor=(0.4, 1), loc='upper left')
plt.savefig(dest_fig)
plt.tight_layout()
plt.show()