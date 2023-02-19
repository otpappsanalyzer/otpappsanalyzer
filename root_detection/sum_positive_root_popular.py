import os,random
import pandas as pd
import numpy as np
import pandas as pd
import csv

api_app_path = '/home/budi/OTP_project/OTP_code/root_detection/androguard_api_classes.csv'
dynamic_path = '/home/budi/OTP_project/OTP_code/root_detection/dynamic_observation.csv'
seed_list_path = '/home/budi/OTP_project/OTP_code/metadata/csv_apk_id.csv'
report_path = '/home/budi/OTP_project/OTP_code/root_detection/'
top_install_path = '/home/budi/OTP_project/OTP_code/metadata/top_install.csv'

# read the api call extracted  from androguard
api_app_df = pd.read_csv(api_app_path,index_col=False)
non_root = ['BiometricManager','BiometricPrompt','FingerprintManager','BiometricService','FingerprintService',
    'KeyStore.getInstance','KeyGenParameterSpec.Builder.isStrongBoxBacked','StrongBoxUnavailableException','isInsideSecureHardware',
    'isStrongBoxBacked','SafetyNetApi']
api_app_df = api_app_df[~api_app_df['api_flag'].isin(non_root)]

# read the original list of OTP apps
seed_list_df = pd.read_csv(seed_list_path,names=['app_id'],header=None)

# read the result of dynamic analysis
dynamic_df = pd.read_csv(dynamic_path)
ref_dynamic_df = dynamic_df[['app_id','root_detection(10)']].dropna()
ref_dynamic_df.rename(columns={'root_detection(10)':'rooted'}, inplace=True)
ref_dynamic_df['rooted'] = ref_dynamic_df['rooted'].replace(['n','y'],['(-) ','(+) '])
# print(ref_dynamic_df)


# merge the two dataframe
rooted_merge = api_app_df.merge(ref_dynamic_df, left_on='app_id',right_on='app_id',how='inner').fillna(0)
# print(rooted_merge)

ref_rooted_slice = rooted_merge[['api_flag','rooted']]
ref_rooted_merge = ref_rooted_slice.groupby(['api_flag','rooted']).size().reset_index(name='value').sort_values(by=['api_flag'],ascending=False)
ref_rooted_merge['source_count'] = ref_rooted_merge.groupby('api_flag')['value'].transform('sum')
# ref_rooted_merge['destination_count'] = ref_rooted_merge.groupby('rooted')['value'].transform('sum')
# print(ref_rooted_merge)



def pct(N,X):
    res = (X/N)*100
    return round(res,2)

api_root_sum_path = report_path+'api_to_root_popular.txt'
with open(api_root_sum_path,'w') as fl:
    fl.write('API/System Call Flag & Total & Detection & \# of Apps \\\ \n')
    for i,line in ref_rooted_merge.iterrows():
        x_pct = pct(line['source_count'],line['value'])
        fl.write(line['api_flag'] + ' & ' + str(line['source_count']) + ' & '+line['rooted']+' & '+str(line['value'])+ '(' +str(x_pct)+'\%)  \\\ \n')
        
# just need to get the app_id and number of library since the previous operation have the result 
top_df = pd.read_csv(top_install_path)

result_df = rooted_merge.merge(top_df, left_on='app_id',right_on='appId',how='left')
result_df['popular'] = np.where(result_df['appId']==result_df['app_id'],True,False)
result_df = result_df[["app_id",'api_flag','rooted','popular']]
ref_rooted_merge_pop = result_df.groupby(['api_flag','rooted','popular']).size().reset_index(name='value_pop').sort_values(by=['api_flag'],ascending=False)
ref_rooted_merge_pop['source_count'] = ref_rooted_merge_pop.groupby('api_flag')['value_pop'].transform('sum')
print(ref_rooted_merge_pop)

with open (api_root_sum_path,'a') as fl:
    fl.write('------------------------------------------------------------- \\\ \n')
    fl.write('-------------------------------------------------------------\\\ \n')
    fl.write('API/System Call Flag & Total & Detection & Popular & \# of Apps \\\ \n')
    for i,line in ref_rooted_merge_pop.iterrows():
        x_pct = pct(line['source_count'],line['value_pop'])
        fl.write(line['api_flag'] + ' & ' + str(line['source_count']) + ' & '+line['rooted']+ ' & '+ str(line['popular'])+' & '+str(line['value_pop'])+ '(' +str(x_pct)+'\%)  \\\ \n')

