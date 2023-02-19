from operator import index
import os 
import pandas as pd

apksigner_result_path = '/home/budi/OTP_project/OTP_code/certificate_analysis/apksigner_extraction.csv'
write_path = '/home/budi/OTP_project/OTP_code/certificate_analysis/apksigner_cert_sum.txt'

result_df = pd.read_csv(apksigner_result_path,index_col=False)
keysize_df = result_df[['key_algorithm','key_size']]
keysize_df = keysize_df.groupby(['key_algorithm','key_size']).size().reset_index(name='count')
keysize_df['pct'] = round(keysize_df['count'].apply(lambda x : (x/182)*100),2)
print(keysize_df)

version_df = result_df[['version1','version2','version3']]
version_df = version_df.groupby(['version1','version2','version3']).size().reset_index(name='count')
version_df['pct'] = round(version_df['count'].apply(lambda x : (x/182)*100),2)
print(version_df)

protected_df = result_df[['protected']]
protected_df = protected_df.groupby(['protected']).size().reset_index(name='count')
protected_df['pct'] = round(protected_df['count'].apply(lambda x : (x/182)*100),2)
print(protected_df)

with open (write_path,'w') as fl:
    fl.write('Key Algorithm & Key Size & \#of Apps (\%) \\\ \n')
    for x,line in keysize_df.iterrows():
        fl.write(str(line['key_algorithm']) + ' & '+ str(line['key_size'])+ ' & ' + str(line['count'])+'('+str(line['pct'])+'\%)\\\ \n')
    
    fl.write('-------------------------------------------------------------------- \\\ \n')
    fl.write('Version1 & Version2 & Version3 & \#of Apps (\%) \\\ \n')
    for i, item in version_df.iterrows():
        fl.write(str(item['version1']) + ' & ' + str(item['version2'])+ ' & '+ str(item['version3'])+' & '+ str(item['count'])+'('+ str(item['pct'])+'\%)\\\ \n')

    fl.write('-------------------------------------------------------------------- \\\ \n')
    fl.write('Status & \#of Apps (\%) \\\ \n')
    for y, prot in protected_df.iterrows():
        fl.write(str(prot['protected']) + ' & '+ str(prot['count'])+'('+ str(prot['pct'])+'\%)\\\ \n')