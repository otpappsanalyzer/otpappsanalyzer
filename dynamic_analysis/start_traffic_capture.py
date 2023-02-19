""" This script is use to : 
    - installing apps to devices
    - run mitm dump and capture the traffic
"""

import os, sys
import time

apk_path = '/home/budi/OTP_project/apk_list/at.tugraz.iaik.signapp.apk'
injector_path = '/home/budi/OTP_project/OTP_code/AddSecurityExceptionAndroid'
hacked_apk_path = '/home/budi/OTP_project/hacked_apk/'
dump_path = '/home/budi/OTP_project/dump_file/'

def start_capture(app_id,app_path,traffic_path):
    print(app_path)
    install = 'adb install '+app_path
    mitm_cmd = 'mitmdump -w '+traffic_path+app_id
    print(install)
    print(mitm_cmd)
    os.system(install)
    os.system(mitm_cmd)
    

def add_security_exception(app,injector_path,apk_path,injected_apk_path):
    os.chdir(injector_path)
    # print(injector_path)
    cmd = './addSecurityExceptions.sh '+apk_path
    os.system(cmd)
    new_file = app.replace('.apk','_new.apk')
    new_file_path = injector_path+'/'+new_file
    mv_cmd = 'mv '+new_file_path+' '+injected_apk_path
    print(mv_cmd)
    try:
        os.system(mv_cmd)
        # cmd_stdout = check_output(mv_cmd, stderr=STDOUT, shell=True).decode()
    except Exception as e:
        print(e)
    
    # return new_file_path 

def main():
    global apk_path
    app_id = apk_path.split('/')
    app_id = app_id[-1]
    print(app_id)
    # add_security_exception(app_id,injector_path,apk_path,hacked_apk_path)
    apk_path = hacked_apk_path+app_id.replace('.apk','_new.apk')
    start_capture(app_id,apk_path,dump_path)

if __name__=='__main__':
    main()