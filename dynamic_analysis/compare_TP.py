# This script is used to compared FLD extracted from har file and FLD from developer website extracted from metadata
# Cleaned the traffic that going to the first party

import os
from signal import SIG_DFL
import time 
import pandas as pd
from tld import get_fld,get_tld


# This file containing the list of developer website extracted from metadata
dev_web_path = '/home/budi/OTP_project/OTP_code/dynamic_analysis/report/contained_dev_web.csv'

# This file containing the list of domain (FLD) accessed by otp apps extracted from network traffic interception
traffic_fld_path ='/home/budi/OTP_project/OTP_code/dynamic_analysis/report/fld_per_app.csv'
report_path = '/home/budi/OTP_project/OTP_code/dynamic_analysis/report/'



def compare_TP(dev_web,traffic,report_path):
    dev_web_df = pd.read_csv(dev_web)
    traffic_df = pd.read_csv(traffic)
    TP_fld_traffic=[]
    FP_fld_traffic=[]
    dev_web_fld=[]
    for i,item in dev_web_df.iterrows():
        dev_web_item = item['dev_web'] 
        dev_web_fld_item = get_fld(dev_web_item)
        dev_web_fld.append(dev_web_fld_item)
    for x,line in traffic_df.iterrows():
        traffic_fld = line['fld']
        # print(traffic_fld)
        if traffic_fld not in dev_web_fld:
            TP_item = {'app_id':line['app_id'],'fld':line['fld']}
            if TP_item not in TP_fld_traffic:
                TP_fld_traffic.append(TP_item)
        else:
            FP_item = {'app_id':line['app_id'],'fld':line['fld']}
            if FP_item not in FP_fld_traffic:
                FP_fld_traffic.append(FP_item)
           
    # write the result of first party domain to csv
    FP_fld_df = pd.DataFrame(FP_fld_traffic)
    FP_fld_write_path = report_path+'FP_fld_after_comparation.csv'
    FP_fld_df.to_csv(FP_fld_write_path,index=False)

    # write the result of third party domain to csv
    TP_fld_df = pd.DataFrame(TP_fld_traffic)
    TP_fld_write_path = report_path+'TP_fld_after_comparation.csv'
    TP_fld_df.to_csv(TP_fld_write_path,index=False)
  
    # sum the third pary domain
    sum_write_path = report_path + "sum_TP_domain.txt"
    group_by_app = TP_fld_df.groupby(['fld']).size().reset_index(name='count').sort_values(by=['count'],ascending=False)
    print(group_by_app)


def main():
    compare_TP(dev_web_path,traffic_fld_path,report_path)

if __name__ == '__main__':
    main()
