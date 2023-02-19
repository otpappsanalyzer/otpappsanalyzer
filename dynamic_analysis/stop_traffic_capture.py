""" This script is use to : 
    - stop mitmdump
    - uninstall apps from device

    input for the script : package name without "_new" and "apk"
"""

import os, sys

def stop_capture():
    uninstall = 'adb uninstall '+apps_
    mitm_cmd = 'pkill mitmdump '
    print(mitm_cmd)
    os.system(mitm_cmd)
    print(uninstall)
    os.system(uninstall)
    

apps_ = sys.argv[1]
# dirname = os.getcwd()
# apps_path = dirname + '/security_exception_added_apps/'+apps_+'_new.apk'
# traffic_path = dirname+'/dump_file/'
# print (apps_path)
stop_capture()
