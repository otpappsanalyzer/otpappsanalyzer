from operator import concat
import pandas as pd
from pandas.core.reshape.merge import merge
from pandas.io.parsers import read_csv 
import numpy as np
import statsmodels.api as sm # recommended import according to the docs
import matplotlib.pyplot as plt

lib_path = '/home/budi/OTP_project/OTP_code/library_analysis/library_detail.csv'
clean_library_path = '/home/budi/OTP_project/OTP_code/library_analysis/clean_library_detail.csv'
tracker_path = '/home/budi/OTP_project/OTP_code/library_analysis/library_detail.csv'
selected_app_id = '/home/budi/OTP_project/OTP_code/metadata/csv_apk_id.csv'
report_path='/home/budi/OTP_project/OTP_code/library_analysis/'

top_install_path = '/home/budi/OTP_project/OTP_code/metadata/top_install.csv'


def clean_library_detail(dirty_detail_path,clean_library_path):
    lib_df = pd.read_csv(dirty_detail_path)
    lib_df['lib_type'] = lib_df['lib_type'].replace('Utilities','Utility')
    lib_df['lib_type'] = lib_df['lib_type'].replace('Mobile analytics','Analytics')
    lib_df['lib_type'] = lib_df['lib_type'].replace('Targeted ads','ads')
    lib_df['lib_type'] = lib_df['lib_type'].replace('Social networking service','social_media')

    lib_df = lib_df[['app_id','lib_name','lib_type']]

    lib_df = lib_df[~lib_df['lib_type'].isin(['Utility','Ui component','Game engine','Development aid'])]
    # print(lib_df)
    lib_df.to_csv(clean_library_path,index=False)


def count_lib_distribution(detail_lib,write_path,top_path):
    lib_df = pd.read_csv(detail_lib)
    top_df = pd.read_csv(top_path)

    # number of apps apperance (row) is similar to number of library adopted
    group_per_id = lib_df.groupby(['app_id']).size().reset_index(name='lib_no').sort_values(by=['lib_no'],ascending=False)
    group_per_lib_no = group_per_id.groupby(['lib_no']).size().reset_index(name='count').sort_values(by=['lib_no'])
    # print(group_per_lib_no)

    with open (write_path,'w') as fl:
        fl.write('# of library adopted & \# of Apps(\%) \\\ \n')
        for x, line in group_per_lib_no.iterrows():
            count = line['count']
            pct_lib = pct(count)
            fl.write(str(line['lib_no'])+ '  & ' + str(count) + '(' + str(pct_lib) +'\%)' + ' \\\ \n')

    # just need to get the app_id and number of library since the previous operation have the result 
    result_df = group_per_id.merge(top_df, left_on='app_id',right_on='appId',how='left')
    result_df['popular'] = np.where(result_df['appId']==result_df['app_id'],True,False)
    result_df = result_df[["app_id",'lib_no','popular']]
    # print(result_df)

    group_per_lib_no_popular = result_df.groupby(['lib_no','popular']).size().reset_index(name='count').sort_values(by=['lib_no'])
    print(group_per_lib_no_popular)
    with open (write_path,'a') as fl:
        fl.write('------------------------------------------------------------- \\\ \n')
        fl.write('-------------------------------------------------------------\\\ \n')
        fl.write('this is for the lib distribution with popular apps \\\ \n')
        fl.write('------------------------------------------------------------- \\\ \n')
        fl.write('Lib_No & Popular & \# of Apps(\%) \\\ \n')
        for x, line in group_per_lib_no_popular.iterrows():
            count = line['count']
            pct_lib = pct(count)
            fl.write(str(line['lib_no']) + '  & ' + str(line['popular']) + '  & ' + str(count) + '(' + str(pct_lib) +'\%)' + ' \\\ \n')
    


def sum_per_lib(detail_lib,write_path,top_path):
    lib_df = pd.read_csv(detail_lib)
    top_df = pd.read_csv(top_path)

    group_per_lib = lib_df.groupby(['lib_name','lib_type']).size().reset_index(name='count').sort_values(by=['count'],ascending=False)
    # print(group_per_lib)

    with open (write_path,'w') as fl:
        fl.write('Lib_name & Lib_type & \# of Apps(\%) \\\ \n')
        for x, line in group_per_lib.iterrows():
            count = line['count']
            pct_lib = pct(count)
            fl.write(line['lib_name']+ ' & ' + line['lib_type'] + '  & ' + str(count) + '(' + str(pct_lib) +'\%)' + ' \\\ \n')

    result_df = lib_df.merge(top_df, left_on='app_id',right_on='appId',how='left')
    result_df['popular'] = np.where(result_df['appId']==result_df['app_id'],True,False)
    result_df = result_df[["app_id",'lib_name','lib_type','popular']]

    group_per_lib_popular = result_df.groupby(['lib_name','lib_type','popular']).size().reset_index(name='count').sort_values(by=['count'],ascending=False)
    with open (write_path,'a') as fl:
        fl.write('------------------------------------------------------------- \\\ \n')
        fl.write('-------------------------------------------------------------\\\ \n')
        fl.write('this is for the classification with popular apps \\\ \n')
        fl.write('------------------------------------------------------------- \\\ \n')
        fl.write('Lib_name & Lib_type & Popular & \# of Apps(\%) \\\ \n')
        for x, line in group_per_lib_popular.iterrows():
            count = line['count']
            pct_lib = pct(count)
            fl.write(line['lib_name']+ ' & ' + line['lib_type'] + ' & ' + str(line['popular']) + '  & ' + str(count) + '(' + str(pct_lib) +'\%)' + ' \\\ \n')

def pct(val):
    n = 182
    p = round((val/n)*100,1)
    return p

def main():

    # clean_library_detail(lib_path,clean_library_path)
    
    # group_per_lib_path = report_path+'library_per_name_popular.txt'
    # sum_per_lib(clean_library_path,group_per_lib_path,top_install_path)

    lib_distribution_path = report_path+'lib_distribution_popular.txt'
    count_lib_distribution(clean_library_path,lib_distribution_path,top_install_path)


if __name__=='__main__':
    main()