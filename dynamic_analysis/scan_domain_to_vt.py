# This script is used to check if the domain/url found in dynamic analysis of OTP apps to the VIrus total
# First checking using first level domain
# Need to understand the API respons first.

import os 
import json

from matplotlib.font_manager import json_dump
from vt_work import search_vt_domain, upload_vt_domain
import time
import pandas as pd 

# vt_domain_result_path = '/home/budi/OTP_project/vt_domain_result/'
# url_list_path = '/home/budi/OTP_project/OTP_code/dynamic_analysis/report/url_per_app.csv'
vt_fld_result_path = '/home/budi/OTP_project/vt_domain_result/fld/'
fld_list_path = '/home/budi/OTP_project/OTP_code/dynamic_analysis/report/fld_per_app.csv'
apps_list = '/home/budi/OTP_project/OTP_code/metadata/csv_apk_id.csv'
report_path = '/home/budi/OTP_project/OTP_code/dynamic_analysis/report/'

def check_vt_status(item,vt_result_path):
    for roots,dirs,files in os.walk(vt_result_path):
        if item in files:
            return True
        else:
            return False

def write_to_csv(file_name,file_path):
    to_write = pd.DataFrame(file_name)
    to_write.to_csv(file_path,index=False)

def main():
    vt_fld_positive_list = []
    fld_df = pd.read_csv(fld_list_path,index_col=False)
    fld_df=fld_df[["app_id","fld"]]
    for i, fld in fld_df.iterrows():
        app_id = fld["app_id"]
        fld_item = fld["fld"]
        file_name = app_id + " | "+fld_item
        status = check_vt_status(file_name,vt_fld_result_path)
        if status == False:
            path_name = vt_fld_result_path + file_name + '.txt'
            res = search_vt_domain(fld_item)    
            try:
                if res['response_code']!=0:
                    print('Write result to Disk : ' + app_id + ' | '+fld_item)
                    with open(path_name,'w') as vtj:
                        json.dump(res,vtj)
            except:
                print(res)
        time.sleep(10)


if __name__ == '__main__':
    main()