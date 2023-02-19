"""
    This script use to check the signing algorithm used by apk
    and using keytool
    keytool can detect the key length and algoritm but cannot check the signing mechanism version
    this tool also failed if the apk disabling (set to false) their version 1 signing mechanism
"""

import os
import json
import pandas as pd

split_apk_path = '/home/budi/OTP_project/OTP_code/mobsf_analysis/split_apk_list.txt'
apps_path = '/home/budi/OTP_project/apk_list/'
certificate_path = '/home/budi/OTP_project/OTP_code/certificate_analysis/'
cert_res_path = 'keytool_result/'

split_apk_list=[]
with open(split_apk_path,'r') as split_apk:
    for item in split_apk:
        item = item.replace('.json','.txt')
        split_apk_list.append(item.strip('\n'))

for root,folder,files in os.walk(apps_path):       
    for file in files:
        apk_name = root+file
        res_name = certificate_path+cert_res_path+file+'.txt'
        print(res_name)
        # os.system('keytool -printcert -jarfile '+apk_name+'>'+res_name )


folder_path = certificate_path+cert_res_path
cert_peryear=[]
for root,folder,files in os.walk(folder_path):
    for file in files:
        if file not in split_apk_list:
            temp = file.split('-')
            app_id = temp[0]
            file_dir = root+file
            print(file_dir) 
            with open(file_dir,'r') as file_name: 
                signature = '' 
                key_length = ''
                for line in file_name:
                    if 'Signature algorithm' in line:
                        signature = line.lstrip('Signature algorithm name ')
                        signature = signature.lstrip(':')
                        signature = signature.replace('with', ' + ').strip('\n')
                    if 'Public Key' in line:
                        key_length = line.lstrip('Subject Public Key Algorithm')
                        key_length = key_length.lstrip(':')
                        # key_length = key_length.replace('-bit RSA key','').strip('\n')
                cert_item_list = {'file_name':app_id,'signature':signature,'key_length':key_length}
                cert_peryear.append(cert_item_list)

df_cert = pd.DataFrame(cert_peryear)  
csv_file = certificate_path+'keytool_extraction.csv'
df_cert.to_csv(csv_file,index=False,sep=';')    
