"""
    This script is used to convert dump file into HAR file
"""

from mitmproxy.io import FlowReader
from mitmproxy import http
import time
import os

# dump_path = '/home/budi/OTP_project/dump_file/'
# har_path = '/home/budi/OTP_project/har_file/'
dump_path = '/home/budi/OTP_project/new_dump_file/'
har_path = '/home/budi/OTP_project/new_har_file/'
parser_path = '/home/budi/OTP_project/OTP_code/dynamic_analysis/har_dump.py'


def har_parser(dump_path,parser_path,har_path):
    parse_cmd = 'mitmdump -n -r '+dump_path+ ' -s ' +parser_path +' --set hardump='+har_path
    os.system(parse_cmd)


def main():
    global har_path
    for rt,dr,fls in os.walk(dump_path):
        for fl in fls:
            # fl_n = fl.replace('apk','har')
            file_har_path = har_path+fl+'.har'
            file_dump_path = dump_path+fl

            # print(file_har_path)
            # print(file_dump_path)
            har_parser(file_dump_path,parser_path,file_har_path)
            print (file_har_path+ ' >>>>> Converstion Finish ------------------------------------------')
            time.sleep(3)

if __name__ == '__main__':
    main()

