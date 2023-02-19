import os
import json
import pandas as pd

split_apk_path = '/home/budi/OTP_project/OTP_code/mobsf_analysis/split_apk_list.txt'
apps_path = '/home/budi/OTP_project/apk_list/'
package_path = '/home/budi/OTP_project/OTP_code/package_analysis/'
apkid_res_path = package_path+'/apkid_result/'
apkid_sum = package_path+'apkid_summary.csv'

def check_APKID(roots,apk_file):
    global package_path
    file_path = roots+apk_file
    res = apkid_res_path+apk_file+'.json'
    check_apk = 'apkid -v -r -j '+file_path+' >'+res
    # os.system(check_apk)


split_apk_list=[]
with open(split_apk_path,'r') as split_apk:
    for item in split_apk:
        item = item.replace('.json','')
        split_apk_list.append(item.strip('\n'))
        # print(item)

for rt,dirs,fls in os.walk(apps_path):
    for file in fls:
        if file not in split_apk_list:
            file_path = rt+file
            # print(file_path)
            check_APKID(rt,file)

'''
    Summarize the APKID scan into csv file:
'''''
apkid_list=[]
for rt,dr,fls in os.walk(apkid_res_path):
    for file in fls:
        file_path = rt+file
        with open (file_path,'r') as ofl:
            fl_data = ofl.read()
            json_data = json.loads(fl_data)
            pkg_key =  json_data['files']
            for item in pkg_key:
                class_dex = str(item['filename'])
                class_dex=class_dex.split('!')
                dex= str('!'.join(class_dex[1:])).strip('[]')
                for comp_type in item['matches']:
                    # print(dex,comp_type,item['matches'][comp_type])
                    matches = item['matches'][comp_type]
                    apkid_list.append({'file_name':file,'class_dex':dex,'types':comp_type,'matches':matches})
df_apkid = pd.DataFrame(apkid_list)
print(df_apkid)
df_apkid.to_csv(apkid_sum,index=False,sep=';')