from operator import concat
import pandas as pd
from pandas.io.parsers import read_csv 
import numpy as np
import statsmodels.api as sm # recommended import according to the docs
import matplotlib.pyplot as plt


lib_path = '/home/budi/OTP_project/OTP_code/library_analysis/library_detail.csv'
write_path = '/home/budi/OTP_project/OTP_code/library_analysis/'
selected_app_id = '/home/budi/OTP_project/OTP_code/metadata/csv_apk_id.csv'


def ecdf_third(file,app_list_path,write_path):
    lib_df = pd.read_csv(file)
    lib_df = lib_df[lib_df['lib_type'].str.contains('Targeted ads|Payment|Social networking service|Mobile analytics')]
    lib_df['lib_type'] = lib_df['lib_type'].replace('Mobile analytics','Analytics')
    lib_df = lib_df[['app_id','lib_name']]
    print(lib_df)

    sum_df = lib_df.groupby(['app_id'])['app_id'].count().reset_index(name='count').sort_values(by=['count'],ascending=False)
    print(sum_df)

    lib_data = sum_df['count']
    lib_ecdf = sm.distributions.ECDF(lib_data) 
    lib_x = np.linspace(min(lib_data), max(lib_data))
    print(lib_x)
    lib_y = lib_ecdf(lib_x)


    fig = plt.figure(figsize=(5,4))
    plt.plot(lib_x, lib_y*100, linestyle='--', lw = 2)
    plt.xlabel('# of Libraries', size = 10)
    plt.ylabel('ECDF', size = 10)
    fig.savefig(write_path)
    # plt.show()

    # write the distribution into text
    dist_df = sum_df.groupby(['count'])['count'].count()
    print(dist_df)

def sum_dominant_lib(file,write_path):
    lib_df = pd.read_csv(file)
    lib_df['lib_type'] = lib_df['lib_type'].replace('Utilities','Utility')
    lib_df['lib_type'] = lib_df['lib_type'].replace('Mobile analytics','Analytics')
    lib_df = lib_df[['app_id','lib_name','lib_type']]
    # print(lib_df)
    anal_sum = lib_df[lib_df['lib_type']=='Analytics'].groupby(['lib_name']).size().reset_index(name='count').sort_values(by=['count'],ascending=False)
    pay_sum = lib_df[lib_df['lib_type']=='Payment'].groupby(['lib_name']).size().reset_index(name='count').sort_values(by=['count'],ascending=False)
    soc_sum = lib_df[lib_df['lib_type']=='Social networking service'].groupby(['lib_name']).size().reset_index(name='count').sort_values(by=['count'],ascending=False)
    ads_sum = lib_df[lib_df['lib_type']=='Targeted ads'].groupby(['lib_name']).size().reset_index(name='count').sort_values(by=['count'],ascending=False)

    with open(write_path,'w') as fl:
        fl.write('Analytics Libraries\n')
        fl.write('----------------------------\n')
        for x,item in anal_sum.iterrows():
            fl.write(str(item['lib_name'])+' & '+str(item['count'])+'\\\ \n')    
        fl.write('----------------------------\n')

        fl.write('Payment Libraries\n')
        fl.write('----------------------------\n')
        for x,item in pay_sum.iterrows():
            fl.write(str(item['lib_name'])+' & '+str(item['count'])+'\\\ \n')    
        fl.write('----------------------------\n')

        fl.write('Social Media Libraries\n')
        fl.write('----------------------------\n')
        for x,item in soc_sum.iterrows():
            fl.write(str(item['lib_name'])+' & '+str(item['count'])+'\\\ \n')    
        fl.write('----------------------------\n')

        fl.write('Ads and Tracker Libraries\n')
        fl.write('----------------------------\n')
        for x,item in ads_sum.iterrows():
            fl.write(str(item['lib_name'])+' & '+str(item['count'])+'\\\ \n')    
        fl.write('----------------------------\n')

def main():

    third_path = write_path+'lib_third_ecdf.pdf'
    ecdf_third(lib_path,selected_app_id ,third_path)

    # dominant_path = write_path+'lib_dominant.txt'
    # sum_dominant_lib(lib_path,dominant_path)

if __name__=='__main__':
    main()