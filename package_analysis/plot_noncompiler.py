import pandas as pd 
import numpy as numpy
import os
import csv
from matplotlib import pyplot as plt

nc_path = '/home/budi/OTP_project/OTP_code/package_analysis/custom_sum_apkid.csv'

nc_df = pd.read_csv(nc_path)
print
sum_df = nc_df.drop(['app_name'],axis=1)
print(sum_df)
sum_df= sum_df.sum(0)
print(sum_df)  
# dest_fig = exp_path+'perc_exp_comp.pdf'


# sum_df.plot.bar(x='component types',width=0.9,figsize=(5,4))
# plt.axis('tight')
# # sum_df.plot.bar(x='Average # of Component and Exported Component per Apps', logy=True)
# plt.xticks(rotation=0)
# plt.ylabel('Average appearance per Apps')
# plt.legend(bbox_to_anchor=(0.4, 1), loc='upper left')
# plt.savefig(dest_fig)
# plt.show()