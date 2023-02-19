"""this script is use to get permission from MobSF result"""
import os
import json
import pandas as pd

result_path = '/home/budi/OTP_project/OTP_code/mobsf_analysis/mobsf_result/'
permission_path = '/home/budi/OTP_project/OTP_code/permission_analysis/'
split_apk_path = '/home/budi/OTP_project/OTP_code/mobsf_analysis/split_apk_list.txt'


split_apk_list=[]
with open(split_apk_path,'r') as split_apk:
    for item in split_apk:
        split_apk_list.append(item.strip('\n'))

# folder_list =['test']

for root,dirs,files in os.walk(result_path):
    permission_peryear=[]
    for file in files:
        if file not in split_apk_list:
            file_path = root+file
            with open (file_path,'r') as pf:
                try:
                    perm_file = pf.read()
                    json_data = json.loads(perm_file)
                    json_perm = json_data['permissions']
                    for line in json_perm:
                        status = json_perm[line]['status']
                        info = json_perm[line]['info']
                        file_name = file.split('-')
                        file_name = file_name[0]
                        perm_item = {'file_name':file_name,'permission':line,'status':status,'info':info}
                        permission_peryear.append(perm_item)
                except:
                    pass

df_perm = pd.DataFrame(permission_peryear)  
csv_file = permission_path+'permission_result.csv'
df_perm.to_csv(csv_file,index=False)