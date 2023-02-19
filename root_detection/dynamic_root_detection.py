import os
import time
import manifest_extractor as ext
import random as rd
# from ppadb.client import Client as AdbClient
# from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

apk_list_file = '/home/budi/OTP_project/OTP_code/metadata/csv_apk_id.csv'
# apk_list_file = '/home/budi/OTP_project/OTP_code/root_detection/test.csv' 
apk_list_path = '/home/budi/OTP_project/apk_list/'
decompiled_path = '/media/budi/Seagate Expansion Drive/OTP_project/decompiled_app/'

def run_custom(list_file,apk_list_path,decompiled_path):
    event_number = 10
    delay = 0.5
    key_event = [66,61,66,66,66,61]
    text_input = ['research1','macquarie','macquarie@mq.edu.au']
    with open (list_file,'r') as fl:
        fl = fl.readlines()
        for app in fl[147:]:
            manifest_path = decompiled_path+app.strip()+'/AndroidManifest.xml'
            package_name = ext.package_name_ex(manifest_path)
            intent_action = ext.intent_action_ex(manifest_path)

            apk_path = apk_list_path+app.strip()
            install_command = 'adb install '+apk_path + '.apk'
            os.system(install_command)

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
                        time.sleep(delay)
                        os.system(text_command)
                        time.sleep(delay)
            uninstall_command = 'adb uninstall '+app.strip()
            os.system(uninstall_command)
            escape_command =  'adb shell input keyevent 4'
            for y in range(4):
                os.system(escape_command)
            time.sleep(3)



# def run_monkey(list_file,apk_list_path):
#     with open (list_file,'r') as fl:
#         for item in fl:
#             apk_path = apk_list_path+item.strip()
#             install_command = 'adb install '+apk_path + '.apk'
#             os.system(install_command)
#             run_monkey_command = 'adb shell monkey -p '+item.strip() + ' 1000 -c android.intent.category.LAUNCHER --throttle 500000000000000000 --kill-process-after-error --pct-appswitch 25 --pct-syskeys 0 COUNT'
#             print(run_monkey_command)
#             os.system(run_monkey_command)
#             uninstall_command = 'adb uninstall '+item
#             os.system(uninstall_command)
#             time.sleep(5)

def main():
    # run_monkey(apk_list_file,apk_list_path)
    run_custom(apk_list_file,apk_list_path,decompiled_path)

if __name__=='__main__':
    main()