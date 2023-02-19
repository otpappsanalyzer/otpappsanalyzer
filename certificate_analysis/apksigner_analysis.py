"""
    This script use to check signing mechanism version by leveraging apksigner
    apksigner version 0.8 will failed to detect or verify apps certificate
    that buit using version 3 signing mechanism.
    Need apksigner version 0.9 to verify certificate built on version 3.
    apksigner version 0.9 need at least Ubuntu 20
"""

import os
import json
import pandas as pd

split_apk_path = '/home/budi/OTP_project/OTP_code/mobsf_analysis/split_apk_list.txt'
apps_path = '/home/budi/OTP_project/apk_list/'
certificate_path = '/home/budi/OTP_project/OTP_code/certificate_analysis/'
cert_res_path = 'apksigner_v3_result/'
# cert_res_path = 'apksigner_result/'


folder_path = certificate_path+cert_res_path
vers_perapp=[]
for root,folder,files in os.walk(folder_path):
    for file in files:
        file_dir = root+file
        print(file_dir) 
        with open(file_dir,'r') as file_name: 
            ver_list=[]
            vec_line=False
            val1=val2=val3=''
            protected = True
            name = file.rstrip('.txt')
            for x,line in enumerate(file_name):
                if '(JAR signing)' in line:
                    par1,val1 = map(str.strip,line.split(':'))
                    # print('Version 1 is :'+ val1)
                    vec_line=True
                elif 'Scheme v2)' in line:
                    par2,val2 = map(str.strip,line.split(':'))
                    # print('Version 2 is :'+ val2)
                elif 'Scheme v3)' in line:
                    par3,val3 = map(str.strip,line.split(':'))
                    # print('Version 2 is :'+ val2)
                elif 'key algorithm' in line:
                    keyl,keyval = map(str.strip,line.split(':'))
                elif 'key size' in line:
                    sizel,sizeval = map(str.strip,line.split(':'))
                elif 'WARNING: META-INF/' in line:
                    protected = False

            ver_list={'app_id':name,'key_algorithm':keyval,'key_size':sizeval,'version1':val1,'version2':val2,'version3':val3,'protected':protected}

            vers_perapp.append(ver_list)

df_ver = pd.DataFrame(vers_perapp)  
csv_file = certificate_path+'apksigner_extraction.csv'
df_ver.to_csv(csv_file,index=False)    
# df_ver.to_csv(csv_file,index=False,sep=';',header=['name','version1','version2','version3'])    




# split_apk_list=[]
# with open(split_apk_path,'r') as split_apk:
#     for item in split_apk:
#         item = item.replace('.json','.txt')
#         split_apk_list.append(item.strip('\n'))

# for root,folder,files in os.walk(apps_path):       
#     for file in files:
#         apk_name = root+file
#         res_name = certificate_path+cert_res_path+file+'.txt'
        # print(res_name)
        # os.system('apksigner verify --verbose --print-certs '+apk_name+'>'+res_name )


# folder_path = certificate_path+cert_res_path
# vers_perapp=[]
# for root,folder,files in os.walk(folder_path):
#     for file in files:
#         if file not in split_apk_list:
#             file_dir = root+file
#             print(file_dir) 
#             with open(file_dir,'r') as file_name: 
#                 ver_list=[]
#                 vec_line=False
#                 val1=val2=''
#                 name = file.rstrip('.txt')
#                 for x,line in enumerate(file_name):
#                     if '(JAR signing)' in line:
#                         par1,val1 = map(str.strip,line.split(':'))
#                         # print('Version 1 is :'+ val1)
#                         vec_line=True
#                     elif 'Scheme v2)' in line:
#                         par2,val2 = map(str.strip,line.split(':'))
#                         # print('Version 2 is :'+ val2)
#                     elif 'Scheme v3)' in line:
#                         par3,val3 = map(str.strip,line.split(':'))
#                         # print('Version 2 is :'+ val2)

#                 ver_list={'name':name,'version1':val1,'version2':val2,'version3':val3}
#             # if vec_line==False:
#             #     ver_list={'name':name,'version1':'true','version2':'true','version3':'true'}
#             # print(ver_list)

#             vers_perapp.append(ver_list)

# df_ver = pd.DataFrame(vers_perapp)  
# csv_file = certificate_path+'apksigner_extraction.csv'
# df_ver.to_csv(csv_file,index=False,sep=';',header=['name','version1','version2','version3'])    
