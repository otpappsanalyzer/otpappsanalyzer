import os
import json
import pandas as pd
import csv
import numpy as np
from tld import get_fld,get_tld

# app_list_path ='/home/budi/crypto_project/crypto_code/static_analysis/test.csv'
app_list_path = '/home/budi/OTP_project/OTP_code/metadata/csv_apk_id.csv'
har_dir_path = '/home/budi/OTP_project/har_file/'
domain_report_path = '/home/budi/OTP_project/OTP_code/dynamic_analysis/report/'

def find_traffic_on_har (har_file_path):
    url_list=[]
    fld_list=[]
    netloc_list=[]
    with open (har_file_path) as rsf:
        data = rsf.read()
        json_data = json.loads(data)
        json_log = json_data['log']
        for item in json_log:
            json_item = json_log['entries']
            for sub_item in json_item:
                url_ori = sub_item['request']['url']
                url_list.append(url_ori)
                try:
                    res_tld = get_tld(url_ori,as_object=True)
                    # fld_item = {'app_id':file,'first_level_domain':res_tld.fld}
                    # netloc_item = {'app_id':file,'first_level_domain':res_tld.parsed_url.netloc}
                    fld_item = res_tld.fld
                    netloc_item = res_tld.parsed_url.netloc

                    if fld_item not in fld_list:
                        fld_list.append(fld_item)
                    if netloc_item not in netloc_list:
                        netloc_list.append(netloc_item)
                except:
                    pass
    return url_list,fld_list,netloc_list



def listing_app(app_path):
    app_list=[]
    with open(app_path,'r') as fl:
        for item in fl:
            app_list.append(item.strip())
            # print(item)
    return app_list

def check_har_file(har_path,har_file):
    for roots,dirs,files in os.walk(har_path):
        har_check = har_file+'.har'
        if har_check in files:
            return True
        else:
            return False

def main():
    app_list = listing_app(app_list_path)
    no_har_list =[]
    # print(app_list)
    url_data=[]
    netloc_data =[]
    fld_data =[]
    for app in app_list:
        res = check_har_file(har_dir_path,app)
        if res == True:
            har_file_path = har_dir_path+app+'.har'
            url_list,fld_list,netloc_list = find_traffic_on_har(har_file_path)
            for url in url_list:
                url_item = {'app_id':app,'url':url}
                if url_item not in url_data:
                    url_data.append(url_item)            
            for netloc in netloc_list:
                netloc_item = {'app_id':app,'netloc':netloc}
                if netloc_item not in netloc_data:
                    netloc_data.append(netloc_item)            
        
            for fld in fld_list:
                fld_item = {'app_id':app,'fld':fld}
                if fld_item not in fld_data:
                    fld_data.append(fld_item) 
        else:
            no_har_list.append(app)
            print('No har file')

    url_df = pd.DataFrame(url_data)
    write_url_path = domain_report_path+'url_per_app.csv'
    url_df.to_csv(write_url_path)
    print(url_df)

    netloc_df = pd.DataFrame(netloc_data)
    write_netloc_path = domain_report_path+'netloc_per_app.csv'
    netloc_df.to_csv(write_netloc_path)
    print(netloc_df)

    fld_df = pd.DataFrame(fld_data)
    write_fld_path = domain_report_path+'fld_per_app.csv'
    fld_df.to_csv(write_fld_path)

    no_har_df = pd.DataFrame(no_har_list)
    write_no_har_path = domain_report_path+'no_har_app.csv'
    no_har_df.to_csv(write_no_har_path)

if __name__=='__main__':
    main()