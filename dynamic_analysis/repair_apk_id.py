import os

# apps_path = '/home/budi/OTP_project/apk_list'
apps_path ='/home/budi/OTP_project/OTP_code/certificate_analysis/apksigner_v3_result'

for roots,dirs,files in os.walk(apps_path):
    for file in files:
        new_file = file.split('-')
        new_file = new_file[0]+'.txt'
        # new_file = new_file[0]+'.apk'
        old_path = roots+'/'+file
        new_path = roots+'/'+new_file
        print(old_path)
        print(new_path)
        os.rename(old_path,new_path)