import os,random
import csv
from unicodedata import name
from anyio import open_cancel_scope
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import plotly.graph_objects as go

import os
import pandas as pd
import csv

api_app_path = '/home/budi/OTP_project/OTP_code/root_detection/androguard_api_classes.csv'
dynamic_path = '/home/budi/OTP_project/OTP_code/root_detection/dynamic_observation.csv'
seed_list_path = '/home/budi/OTP_project/OTP_code/metadata/csv_apk_id.csv'

report_path = '/home/budi/OTP_project/OTP_code/root_detection/'

# read the api call extracted  from androguard
api_app_df = pd.read_csv(api_app_path,index_col=False)
non_root = ['BiometricManager','BiometricPrompt','FingerprintManager','BiometricService','FingerprintService',
    'KeyStore.getInstance','KeyGenParameterSpec.Builder.isStrongBoxBacked','StrongBoxUnavailableException','isInsideSecureHardware',
    'isStrongBoxBacked','SafetyNetApi']
# non_root = ['BiometricManager','BiometricPrompt','FingerprintManager','BiometricService','FingerprintService',
    # 'KeyStore.getInstance','KeyGenParameterSpec.Builder.isStrongBoxBacked','StrongBoxUnavailableException',
    # 'SafetyNet.getClient','Os.stat']
api_app_df = api_app_df[~api_app_df['api_flag'].isin(non_root)]

# read the original list of OTP apps
seed_list_df = pd.read_csv(seed_list_path,names=['app_id'],header=None)

# read the result of dynamic analysis
dynamic_df = pd.read_csv(dynamic_path)
ref_dynamic_df = dynamic_df[['app_id','root_detection(10)']]
ref_dynamic_df.rename(columns={'root_detection(10)':'rooted'}, inplace=True)
ref_dynamic_df['root_sign'] = ref_dynamic_df['rooted'].replace(['n','y'],['(-)','(+)'])

# cannot assign the number of + and - detection because ref dynamic containing all apps including apps without rooted api call 
ref_dynamic_df['rooted'] = ref_dynamic_df['rooted'].replace(['n','y'],['(-) Root Detection','(+) Root Detection'])
# print(ref_dynamic_df)

# merge the three dataframe
# rooted_merge = seed_list_df.merge(api_app_df,left_on='app_id',right_on='app_id',how='outer').merge(ref_dynamic_df,
#     left_on='app_id',right_on='app_id',how='outer').fillna(0)

# merge the two dataframe
rooted_merge = api_app_df.merge(ref_dynamic_df, left_on='app_id',right_on='app_id',how='inner').fillna(0)
# print(rooted_merge)
app_number_df = rooted_merge.groupby(['app_id','rooted'])['app_id','rooted'].size().reset_index(name='count')
# app_number_df = app_number_df.groupby(['rooted'])['rooted'].size().reset_index(name='count')
# print(app_number_df)
app_pos_val = sum(app_number_df['rooted']== '(+) Root Detection')
app_neg_val = sum(app_number_df['rooted']== '(-) Root Detection')
# print('this is '+ str(app_pos_val)+ str(app_neg_val))
# Note : the destination is the THE NUMBER OF APPS containing + and - root detection, not the number of api/system call that contribute to + or - detection
# So assign the number of + and - here, after merge between dynamic result and api call result
rooted_merge = rooted_merge.replace(['(+) Root Detection','(-) Root Detection'],\
    ['(+) Root Detection | ('+str(app_pos_val) + ' Apps )','(-) Root Detection | ('+str(app_neg_val)+ ' Apps )'])

ref_rooted_slice = rooted_merge[['api_flag','rooted','root_sign']]
ref_rooted_merge = ref_rooted_slice.groupby(['api_flag','rooted','root_sign'])['api_flag','rooted','root_sign'].size().reset_index(name='value')
ref_rooted_merge['source_count'] = ref_rooted_merge.groupby('api_flag')['value'].transform('sum')
# ref_rooted_merge['destination_count'] = ref_rooted_merge.groupby('root_sign')['value'].transform('sum')
ref_rooted_merge['source_label'] =  '('+ref_rooted_merge['source_count'].astype(str)+' Calls) | ' + ref_rooted_merge.api_flag + '()'  \
# ref_rooted_merge['source_label'] =  ref_rooted_merge.api_flag + '()' + ' | #of Call: ' + ref_rooted_merge['source_count'].astype(str) \
    # + ref_rooted_merge['value'].astype(str) + ref_rooted_merge['source_count'].astype(str)
# ref_rooted_merge['destination_label'] =  ref_rooted_merge['rooted']+' | ('+ ref_rooted_merge.destination_count.astype(str) +' )' 

# ref_rooted_merge['source_negation'] = ref_rooted_merge.source_count - ref_rooted_merge.value
# ref_rooted_merge['source_label'] = ref_rooted_merge.api_flag + '() (Total: ' + ref_rooted_merge['source_count'].astype(str) + '| (+): ' + \
    # (ref_rooted_merge.source_count - ref_rooted_merge.value).astype(str)
print(ref_rooted_merge)


all_nodes = ref_rooted_merge.source_label.values.tolist() + ref_rooted_merge.rooted.values.tolist()
# print(all_nodes)
source_indices = [all_nodes.index(source_label) for source_label in ref_rooted_merge.source_label]
# print(source_indices)
target_indices = [all_nodes.index(rooted) for rooted in ref_rooted_merge.rooted]
# print(target_indices)

def pct(N,X):
    res = (X/N)*100
    return round(res,2)

api_root_sum_path = report_path+'api_to_root_sum.txt'
with open(api_root_sum_path,'w') as fl:
    fl.write('API/System Call Flag & Total & Detection & \# of Apps \\\ \n')
    for i,line in ref_rooted_merge.iterrows():
        x_pct = pct(line['source_count'],line['value'])
        fl.write(line['api_flag'] + ' & ' + str(line['source_count']) + ' & '+line['root_sign']+' & '+str(line['value'])+ '(' +str(x_pct)+'\%)  \\\ \n')
        

# sort_group_by_app.to_csv(write_path,header=None,index=None,sep='&')

number_of_colors = 12

colors = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(number_of_colors)]
fig = go.Figure(data=[go.Sankey(
    node = dict(
        pad = 20,
        thickness = 20,
        line = dict(color = "black", width = 1.0),
        label =  all_nodes,
        color = colors,
    ),

    link = dict(
      source =  source_indices,
      target =  target_indices,
      value =  ref_rooted_merge.value,
))])

fig.update_layout(#title_text="API/System Call to Root Detection Result",
                  font_size=16)
fig.show()

