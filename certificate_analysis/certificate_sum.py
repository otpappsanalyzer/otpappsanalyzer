"""
    This script use to summarize the result given by keytool and apksigner
    """

import os
import json
import pandas as pd

certificate_path = '/home/budi/OTP_project/OTP_code/certificate_analysis/'
keytool_path = certificate_path+'keytool_extraction.csv'
apksigner_path = certificate_path+'apksigner_extraction.csv'
cert_sum = certificate_path+'cert_sum.txt'


df_key = pd.read_csv(keytool_path,sep=';')
df_key= df_key.replace(r'\n','',regex=True)

by_signature = df_key.groupby('signature')['signature'].count().reset_index(name="count")
by_length = df_key.groupby('key_length')['key_length'].count().reset_index(name='count')
print(by_signature)
print(by_length)

df_apksigner = pd.read_csv(apksigner_path,sep=';')
by_mech = df_apksigner.groupby(['version1','version2','version3'])['name'].count().reset_index(name="count")
print(by_mech)

with open (cert_sum,'w') as fl:
    fl.write('signature & count  \\\ \n')
    for index, row in by_signature.iterrows():
        # print(row[0])
        str_row = str(row[0]) + ' & ' + str(row[1]) + '\\\ \n'
        fl.write(str_row)
    fl.write('----------------------  \n')

    fl.write('key length & count \\\ \n')   
    for index,row in by_length.iterrows():
        str_row = str(row[0]) + ' & ' + str(row[1]) + '\\\  \n'
        fl.write(str_row)
    fl.write('----------------------  \n')

    fl.write('version1 & version2 & version3 & count \\\ \n')
    for index,row in by_mech.iterrows():
        str_row = str(row[0]) + ' & ' + str(row[1]) + ' & ' + str(row[2]) + ' & ' + str(row[3]) + '\\\  \n'
        fl.write(str_row)
