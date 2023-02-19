from operator import index
import os 
import pandas as pd
import numpy as np

apksigner_result_path = '/home/budi/OTP_project/OTP_code/certificate_analysis/apksigner_extraction.csv'
write_path = '/home/budi/OTP_project/OTP_code/certificate_analysis/apksigner_cert_sum_pop.txt'
top_install_path = '/home/budi/OTP_project/OTP_code/metadata/top_install.csv'


detail_df = pd.read_csv(apksigner_result_path,index_col=False)
pop_df = pd.read_csv(top_install_path)
# print(pop_df)

result_df = detail_df.merge(pop_df, left_on='app_id',right_on='appId',how='left')
result_df['popular'] = np.where(result_df['appId']==result_df['app_id'],True,False)
result_df = result_df[['app_id','key_algorithm','key_size','version1','version2','version3','protected','popular']]
print(result_df)

keysize_df = result_df[['key_algorithm','key_size','popular']]
keysize_df = keysize_df.groupby(['key_algorithm','key_size','popular']).size().reset_index(name='count')
keysize_df['pct'] = round(keysize_df['count'].apply(lambda x : (x/182)*100),2)
print(keysize_df)

version_df = result_df[['version1','version2','version3','popular']]
version_df = version_df.groupby(['version1','version2','version3','popular']).size().reset_index(name='count')
version_df['pct'] = round(version_df['count'].apply(lambda x : (x/182)*100),2)
print(version_df)

protected_df = result_df[['protected','popular']]
protected_df = protected_df.groupby(['protected','popular']).size().reset_index(name='count')
protected_df['pct'] = round(protected_df['count'].apply(lambda x : (x/182)*100),2)
print(protected_df)

with open (write_path,'w') as fl:
    fl.write('Key Algorithm & Key Size & Popular & \#of Apps (\%) \\\ \n')
    for x,line in keysize_df.iterrows():
        fl.write(str(line['key_algorithm']) + ' & '+ str(line['key_size']) + ' & '+ str(line['popular']) \
           + ' & ' + str(line['count'])+'('+str(line['pct'])+'\%)\\\ \n')
    
    fl.write('-------------------------------------------------------------------- \\\ \n')
    fl.write('Version1 & Version2 & Version3 & popular & \#of Apps (\%) \\\ \n')
    for i, item in version_df.iterrows():
        fl.write(str(item['version1']) + ' & ' + str(item['version2'])+ ' & '+ str(item['version3'])  + ' & '+ str(item['popular'])\
            +' & '+ str(item['count'])+'('+ str(item['pct'])+'\%)\\\ \n')

    fl.write('-------------------------------------------------------------------- \\\ \n')
    fl.write('Status & popular &  \#of Apps (\%) \\\ \n')
    for y, prot in protected_df.iterrows():
        fl.write(str(prot['protected']) + ' & '+ str(prot['popular'])+ ' & '+ str(prot['count'])+'('+ str(prot['pct'])+'\%)\\\ \n')