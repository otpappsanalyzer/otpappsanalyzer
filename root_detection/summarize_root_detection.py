import pandas as pd
from pandas.core import groupby
import numpy as np

root_detection_detail = '/home/budi/OTP_project/OTP_code/root_detection/androguard_api_classes.csv'
report_path = '/home/budi/OTP_project/OTP_code/root_detection/'
meta_path = '/home/budi/OTP_project/OTP_code/metadata/csv_apk_id.csv'
top_install_path = '/home/budi/OTP_project/OTP_code/metadata/top_install.csv'


def pct(x):
    n = 182 # number of OTP apps 
    res = (x/n)*100
    return round(res,2)

def sum_popular_app(detail_path,popular_path,report_path):
    root_df = pd.read_csv(detail_path)
    popular_df = pd.read_csv(popular_path)
    # print(popular_df)
    result_df = root_df.merge(popular_df, left_on='app_id',right_on='appId',how='left')
    result_df['popular'] = np.where(result_df['appId']==result_df['app_id'],True,False)
    result_df = result_df[["app_id","api_flag",'popular']]
    print(result_df)

    groupby_df = result_df.groupby(['api_flag','popular']).size().reset_index(name = 'count')
    with open (report_path,'w') as fl:
        fl.write('API Flag  & Popular & # of Apps (\%) \\\ \n')
        for index,line in groupby_df.iterrows():
            pct_x = pct(line['count'])
            # print(pct_x)
            fl.write(str(line['api_flag']) + '() & ' +str(line['popular'])+ ' & ' +str(line['count']) + ' (' + str(pct_x) + '\%) \\\ \n')


def sum_mechanism(detail_path,groupby_report):
    root_detail = pd.read_csv(detail_path)
    root_df = pd.DataFrame(root_detail)
    groupby_df = root_df.groupby(['api_flag'])['api_flag'].count().reset_index(name = 'count')
    with open (groupby_report,'w') as fl:
        for index,line in groupby_df.iterrows():
            pct_x = pct(line['count'])
            print(pct_x)
            fl.write(str(line['api_flag']) + '() & ' +str(line['count']) + ' (' + str(pct_x) + ' %) \\\ \n')

def check_no_rooted_detection(meta_path,root_detail,report):
    meta_list = pd.read_csv(meta_path,header=None)
    detail_list = pd.read_csv(root_detail)
    detail_list=detail_list['app_id'].drop_duplicates().reset_index()
    detail_list=detail_list['app_id']
    diff_df = pd.concat([meta_list,detail_list]).drop_duplicates(keep=False)
    print(diff_df)
    diff_df.to_csv(report,index=None)

def main():
    # groupby_path = report_path+'group_by_flag.txt'
    # sum_mechanism(root_detection_detail,groupby_path)
    
    popular_path = report_path+'sum_flag_with_popular.txt'
    sum_popular_app(root_detection_detail,top_install_path,popular_path)

    # no_rooted_report = report_path+'no_rooted_detection.csv'
    # check_no_rooted_detection(meta_path,root_detection_detail,no_rooted_report)

if __name__=='__main__':
    main()