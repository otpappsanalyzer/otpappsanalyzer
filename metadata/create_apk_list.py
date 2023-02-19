import os

apk_path = '/home/budi/OTP_project/apk_list/'
csv_apk_file =  '/home/budi/OTP_project/OTP_code/metadata/csv_apk_file.csv'
csv_apk_id =  '/home/budi/OTP_project/OTP_code/metadata/csv_apk_id.csv'

apk_file_list = []
apk_id_list = []
for roots,dirs,files in os.walk(apk_path):
    for file in files:
        apk_id = file.rstrip('apk')
        apk_id = apk_id.rstrip('.')
        apk_file_list.append(file)
        apk_id_list.append(apk_id)

with open (csv_apk_file,'w') as fl_file:
    for file in apk_file_list:
      fl_file.write(file+'\n')

with open(csv_apk_id,'w') as fl_id:
    for id in apk_id_list:
        fl_id.write(id+'\n')