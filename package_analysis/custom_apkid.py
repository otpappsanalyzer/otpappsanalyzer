
import os
import json
import subprocess
import pandas as pd

apk_path = '/home/budi/OTP_project/apk_list/'
report_path = '/home/budi/OTP_project/OTP_code/package_analysis/'

def extract_APKID(apk_file):
    check_apk = 'apkid -v -r -j '+apk_file #+' >'+res
    res = subprocess.getoutput(check_apk)
    # print(res)
    return res

def find_package(apk_file):
    split_apk = apk_file.split('/')
    app_name = split_apk[-1]
    return app_name

def apkid_analysis(apk_file):
    # print(apk_file)
    app_name = find_package(apk_file)
    apkid_list=[]
    print('Extracting apps apkid : '+app_name)
    result = extract_APKID(apk_file)
    try:
        json_data = json.loads(result)
        pkg_key =  json_data['files']
        for item in pkg_key:
            class_dex = str(item['filename'])
            class_dex=class_dex.split('!')
            dex= str('!'.join(class_dex[1:])).strip('[]')
            for comp_type in item['matches']:
                # print(dex,comp_type,item['matches'][comp_type])
                matches = item['matches'][comp_type]
                apkid_list.append({'app_name':app_name,'class_dex':dex,'types':comp_type,'matches':matches})
    except:
        apkid_list.append({'app_name':app_name,'class_dex':'error','types':'error','matches':'error'})

    return(apkid_list)

def main():  
    detail_list=[]
    apkid_sum=[]
    for roots,dirs,files in os.walk(apk_path):
        for file in files:
            apk_file = roots+file
            print(apk_file)
            apkid = apkid_analysis(apk_file)
            for line in apkid:
                detail_list.append(line)

                anti_vm = 0
                obfuscator= 0
                anti_debug= 0
                anti_disassembly= 0
                manipulator=packer = 0
                if 'anti_vm' in line['types']:
                    anti_vm = 1
                elif 'obfuscator' in line['types']:
                    obfuscator = 1
                elif 'anti_debug' in line['types']:
                    anti_debug = 1
                elif 'anti_disassembly' in line['types']:
                    anti_disassembly = 1
                elif 'packer' in line['types']:
                    packer = 1
                elif 'manipulator' in line['types']:
                    manipulator = 1
            
            apkid_sum.append({'app_name':file,'anti_vm':anti_vm,'obfuscator':obfuscator,'anti_debug':anti_debug,'anti_disassembly':anti_disassembly,
            'manipulator':manipulator,'packer':packer})
    
    detail_df = pd.DataFrame(detail_list)
    detail_path = report_path+'custom_detail_apkid.csv'
    detail_df.to_csv(detail_path,index=False)

    sum_df = pd.DataFrame(apkid_sum)
    # sum_df = sum_df.drop_duplicates()
    sum_path = report_path+'custom_sum_apkid.csv'
    sum_df.to_csv(sum_path,index=False)

if __name__ == "__main__":
    main()
