"""This script is use to inject security exception """
import os
import subprocess
import time
from subprocess import check_output, STDOUT


# apk_path = '/home/budi/adblocker_project/apps_list/2021/to.freedom.android2.apk'
apk_path = '/home/budi/OTP_project/apk_list/'
# injected_apk_path = '/media/budi/Seagate Expansion Drive/OTP_project/hacked_apk/'
injected_apk_path = '/home/budi/OTP_project/hacked_apk/'
injector_path = '/home/budi/OTP_project/AddSecurityExceptionAndroid/'
list_app_path = '/home/budi/OTP_project/OTP_code/metadata/csv_apk_id.csv'



def add_exeption(apk_name,injector_path,apk_path,injected_apk_path):
    original_apk_path = apk_path+apk_name+'.apk'
    temp_file_path = injector_path+apk_name+'_new.apk'
    os.chdir(injector_path)
    cmd = './addSecurityExceptions.sh '+original_apk_path
    os.system(cmd)
    mv_cmd = 'mv '+temp_file_path+' '+injected_apk_path
    try:
        # os.system(mv_cmd)
        cmd_stdout = check_output(mv_cmd, stderr=STDOUT, shell=True).decode()
    except Exception as e:
        print(e)

def check_injected_app (apk_name, injected_apk_path):
    # print(apk_name)
    for rt,drs,fls in os.walk(injected_apk_path):
        for file in fls:
            if file ==apk_name:
                # print (file + '======'+apk_name)
                return True
    return False

def listing_app(app_list_path):
    app_list=[]
    with open (app_list_path,'r') as fl:
        for line in fl:
            app_list.append(line.strip())
    return app_list


def main():

    app_list = listing_app(list_app_path)
    for item in app_list:
        injected_apk_name = item+'_new.apk'

        check_injected = check_injected_app(injected_apk_name,injected_apk_path)
        if check_injected is True:
            print(injected_apk_name + ' -------------->  True')
        else:
           print(injected_apk_name  + '-------------->  False')
           add_exeption(item,injector_path,apk_path,injected_apk_path)


if __name__ == "__main__":
    main()
