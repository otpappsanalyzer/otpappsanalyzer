"""
    This script used to check the apps that containing unprotected file
    """

import os
import json
import pandas as pd
from matplotlib import pyplot as plt


certificate_path = '/home/budi/OTP_project/OTP_code/certificate_analysis/'
apksigner_res_path = certificate_path+'apksigner_v3_result/'
apksigner_ext_path = certificate_path+'apksigner_extraction.csv'
unprotected_list_path = certificate_path+'unprotected_list.csv'

ext_df = pd.read_csv(apksigner_ext_path,sep=';')
unprotected_list=[]
for index,line in ext_df.iterrows():
    vers = 'version1'
    if line[2]==True:
        vers = 'version2'
    if line[3]==True:
        vers='version3'
    
    apksigner_file = apksigner_res_path+line[0]+'.txt'
    with open (apksigner_file,'r') as fl:
        for item in fl:
            if 'not protected by signature' in item:
                unprotected = True
                protected= False
                pass
            else:
                 unprotected= False
                 protected= True


    # unprotected_list.append({'app_name':line[0],'version':vers,'unprotected':unprotected})
    unprotected_list.append({'app_name':line[0],'version':vers,'unprotected':unprotected,'protected':protected})

unprotected_df = pd.DataFrame(unprotected_list)
# print(unprotected_df)
# by_unprotected = unprotected_df.groupby(['version','unprotected'])['version'].count().reset_index(name="count")
by_unprotected = unprotected_df.groupby(['version','unprotected','protected'])['version'].count().reset_index(name="count")
# print(by_unprotected)

new_dict=[]
protected =[]
unprotected = []
for index,row in by_unprotected.iterrows():
    if row['unprotected'] == True :
        unprotected.append(int(row[3]))
    elif row['protected'] == True:
        protected.append(int(row[3]))

sum_df=pd.DataFrame({'Signature Protected Files':['version1','version2','version3'],
                'Fully protected':protected,
                'Partially protected':unprotected})
print(sum_df)

bars=sum_df.plot.bar(x='Signature Protected Files',width=0.9,figsize=(5,4))
plt.axis('tight')
plt.xticks(rotation=0)
plt.ylabel(' # of Apps')
plt.legend(bbox_to_anchor=(0.5, 1), loc='upper right')
# plt.savefig(dest_fig)
plt.show()

