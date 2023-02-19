from distutils.log import error
import os
import time
import manifest_extractor as ext
import random as rd
import subprocess
import time
from subprocess import check_output, STDOUT


apk_list_file ='/home/budi/OTP_project/OTP_code/metadata/csv_apk_id_refined.csv'
# apk_list_file = '/home/budi/OTP_project/OTP_code/metadata/csv_apk_id.csv'
# apk_list_file = '/home/budi/OTP_project/OTP_code/root_detection/test.csv' 
apk_list_path = '/home/budi/OTP_project/apk_list/'
decompiled_path = '/media/budi/Seagate Expansion Drive/OTP_project/decompiled_app/'
traffic_captured_path= '/home/budi/OTP_project/new_dump_file/'
hacked_traffic_dump_path= '/home/budi/OTP_project/hacked_dump_path/'
injector_path = '/home/budi/OTP_project/AddSecurityExceptionAndroid/'
injected_apk_path = '/home/budi/OTP_project/hacked_apk/'


  
def kill_mitm():
    print ('Kill MITM dump')
    cmd = 'pkill mitmdump'
    os.system(cmd)


def runmitmdump(res_path):
  print("Running mitmdump on Terminal")
  arg = 'mitmdump -w '+res_path
  subprocess.Popen(arg,shell=True)

def add_exception(app,injector_path,apk_path,injected_apk_path):
    os.chdir(injector_path)
    cmd = './addSecurityExceptions.sh '+apk_path
    os.system(cmd)
    new_file = app+'_new.apk'
    mv_cmd = 'mv '+new_file+' '+injected_apk_path
    try:
        # os.system(mv_cmd)
        cmd_stdout = check_output(mv_cmd, stderr=STDOUT, shell=True).decode()
        new_file_path = injected_apk_path+new_file
    except Exception as e:
        new_file_path = apk_path
    return (new_file_path)

def check_injected_apk(app_id,injected_apk_path):
    for roots,folders,files in os.walk(injected_apk_path):
        injected_app = app_id+'_new.apk'
        if injected_app in files:
            return True
        else:
            return False


def main():
    event_number = 10
    delay = 0.5
    key_event = [66,61,66,66,66,61]
    text_input = ['research1','macquarie','macquarie@mq.edu.au']
    with open (apk_list_file,'r') as fl:
        fl = fl.readlines()
        for app in fl:
            try:
                print (app)
                manifest_path = decompiled_path+app.strip()+'/AndroidManifest.xml'
                package_name = ext.package_name_ex(manifest_path)
                intent_action = ext.intent_action_ex(manifest_path)

                # Check if injected apk available
                # injected_status = check_injected_apk(app,injected_apk_path)
                # if injected_status == False:
                #     print("Not injected --> Proceed with security exception injection")
                #     add_exception(app,injector_path,apk_list_path,injected_apk_path)
                    

                apk_path = injected_apk_path+app.strip()
                install_command = 'adb install '+apk_path + '_new.apk'
                # apk_path = apk_list_path+app.strip()
                # install_command = 'adb install '+apk_path + '.apk'
                os.system(install_command)

                # res_path = traffic_captured_path+app.strip()
                res_path = hacked_traffic_dump_path+app.strip()
                runmitmdump(res_path)

                for item in intent_action:
                    activity,action = item['activity'],item['action']
                    if action == 'android.intent.action.VIEW' or action == 'android.intent.action.MAIN':
                        component = package_name+'/'+activity
                        activity_start_command = 'adb shell am start '+component
                        os.system(activity_start_command)
                        time.sleep(2)
                        for x in range(event_number):
                            rand_key = rd.choice(key_event)
                            rand_text = rd.choice(text_input)
                            event_command =  'adb shell input keyevent '+str(rand_key)
                            print(event_command)
                            text_command = 'adb shell input text '+rand_text
                            print(text_command)
                            os.system(event_command)
                            # time.sleep(delay)
                            os.system(text_command)
                            # time.sleep(delay)
                uninstall_command = 'adb uninstall '+app.strip()
                os.system(uninstall_command)
                kill_mitm()
                escape_command =  'adb shell input keyevent 4'
                for y in range(10):
                    os.system(escape_command)
                time.sleep(3)
            except error:
                # print(error)
                pass

if __name__=='__main__':
    main()