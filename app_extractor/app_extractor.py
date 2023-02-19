import os,shutil
import time

decompiled_path = "/media/budi/Seagate Expansion Drive/OTP_project/decompiled_app"
apk_list_path = '/home/budi/OTP_project/apk_list/'
temp_path = '/home/budi/OTP_project/temp_path/'

def extract_apk(apk_path,decompiled_path,temp_path):
    package_name = apk_path.split('/')
    package_name= package_name[-1]
    package_name = package_name.rstrip('apk')
    package_name = package_name.rstrip('.')
    print('Decompiling '+package_name)
    # apk_path = apk_path+'.apk'
    os.chdir(temp_path)
    shutil.copy2(apk_path,temp_path)
    comm  = 'apktool d -f '+package_name+'.apk'
    os.system(comm)
    time.sleep(1)
    print('moving '+temp_path+package_name + ' to decompiled folder')
    shutil.move(temp_path+package_name,decompiled_path)
    time.sleep(1)
    os.remove(temp_path+package_name+'.apk')
    time.sleep(1)

def check_folder(path,folder):
    print(folder)
    for roots,dirs,files in os.walk(path):
        if folder in dirs:
            return True
        else:
            return False
        del dirs[:] # delete next level of directory 

def main():
    for roots,dirs,files in os.walk(apk_list_path):
        for file in files:
            apk_path = roots+ file
            app_id = file.rstrip('apk')
            app_id = app_id.rstrip('.')
            check_res = check_folder(decompiled_path,app_id) 
            if  check_res == False:
                extract_apk(apk_path,decompiled_path,temp_path)
            else:
                print(file + ' already decompiled')

if __name__=='__main__':
    main()