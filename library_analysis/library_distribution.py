from operator import concat
import pandas as pd
from pandas.core.reshape.merge import merge
from pandas.io.parsers import read_csv 
import numpy as np
import statsmodels.api as sm # recommended import according to the docs
import matplotlib.pyplot as plt

lib_path = '/home/budi/OTP_project/OTP_code/library_analysis/library_detail.csv'
write_path = '/home/budi/OTP_project/OTP_code/library_analysis/'
selected_app_id = '/home/budi/OTP_project/OTP_code/metadata/csv_apk_id.csv'


tracker_path = '/home/budi/OTP_project/OTP_code/library_analysis/library_detail.csv'
write_path = '/home/budi/OTP_project/OTP_code/library_analysis/'
selected_app_id = '/home/budi/OTP_project/OTP_code/metadata/csv_apk_id.csv'
report_path='/home/budi/OTP_project/OTP_code/library_analysis/'


def sum_dominant_lib(file,write_path):
    
    lib_df = pd.read_csv(file)
    lib_df['lib_type'] = lib_df['lib_type'].replace('Utilities','Utility')
    lib_df['lib_type'] = lib_df['lib_type'].replace('Mobile analytics','Analytics')
    lib_df['lib_type'] = lib_df['lib_type'].replace('Targeted ads','ads')
    lib_df['lib_type'] = lib_df['lib_type'].replace('Social networking service','social_media')

    lib_df = lib_df[['app_id','lib_name','lib_type']]

    lib_df = lib_df[~lib_df['lib_type'].isin(['Utility','Ui component','Game engine','Development aid'])]
    x = lib_df.drop_duplicates(['lib_type'])
    # print(x)
    # print(lib_df)
    count_per_id = lib_df.groupby(['app_id']).size().reset_index(name='count').sort_values(by=['count'],ascending=False)
    print(count_per_id)
    # addition to create txt for addoption of third party per number
    sum_lib_path ='/home/budi/OTP_project/OTP_code/library_analysis/sum_per_count.txt'
    sum_per_number_df = count_per_id.groupby(['count']).size().reset_index(name='number')
    with open(sum_lib_path,'w') as fl:
        fl.write('\# of Library & \# of Apps \\\ \n' )
        total = 0
        for i,line in sum_per_number_df.iterrows():
            total = total+line['number']
            pct_item = pct(line['number']) 
            fl.write(str(line['count'])+' & '+str(line['number'])+'('+str(pct_item)+'\%)' +'\\\ \n')
        pct_total = pct(total)
        fl.write('\hline \n')
        fl.write('& Total & &'+str(total)+'('+str(pct_total)+'\%)\\\ \n')

    bin = ['1','2','3','4','5']
    group_df = []
    for x in bin:
        for index,line in count_per_id.iterrows():
            str_cmp = str(line['count'])
            if str_cmp == x:
                # count_per_id['group'] == x
                line_item = {'app_id':line['app_id'],'group':x}
                if line_item not in group_df:
                    group_df.append(line_item)
            elif line['count']>=6:
                line_item = {'app_id':line['app_id'],'group':'6+'}
                if line_item not in group_df:
                    group_df.append(line_item)

    group_df = pd.DataFrame(group_df)
    # print(group_df[group_df['group']=='5'])

    count_per_id=merge(count_per_id,group_df,left_on='app_id',right_on='app_id',how='inner')
    # print(count_per_id)

    count_per_type = lib_df.groupby(['app_id','lib_type'])['app_id','lib_type'].size().unstack().reset_index()
    # count_per_type=count_per_type[['app_id','Analytics','Payment','Targeted ads','Social networking service']]
    count_per_type=count_per_type.fillna(0)
    # print(count_per_type)

    merge1 = merge(count_per_type,count_per_id,left_on='app_id',right_on='app_id',how='inner')
    # print(merge1)

    sum_per_group = merge1[['Analytics','Payment','ads','social_media','group']]
    sum_per_group = sum_per_group.groupby(['group']).sum().reset_index()
    # print(sum_per_group)

    num_id_per_group = count_per_id.groupby(['group']).size().reset_index(name='apps_num')
    num_id_per_group = num_id_per_group[['group','apps_num']]
    # print(num_id_per_group)

    merge2 = merge(sum_per_group,num_id_per_group,left_on='group',right_on='group',how='inner')
    print(merge2)


def sum_per_lib(file,write_path):
    
    lib_df = pd.read_csv(file)
    lib_df['lib_type'] = lib_df['lib_type'].replace('Utilities','Utility')
    lib_df['lib_type'] = lib_df['lib_type'].replace('Mobile analytics','Analytics')
    lib_df['lib_type'] = lib_df['lib_type'].replace('Targeted ads','ads')
    lib_df['lib_type'] = lib_df['lib_type'].replace('Social networking service','social_media')

    lib_df = lib_df[['app_id','lib_name','lib_type']]

    lib_df = lib_df[~lib_df['lib_type'].isin(['Utility','Ui component','Game engine','Development aid'])]
    # x = lib_df.drop_duplicates(['lib_type'])
    # print(x)
    # print(lib_df)

    anal_df = lib_df[lib_df['lib_type']=='Analytics']
    anal_count = anal_df.groupby(['app_id']).size().reset_index(name='group').sort_values(by=['group'])
    anal_count = anal_count.fillna(0)
    anal_count['group'].values[anal_count['group'] > 5] = 6
    anal_group = anal_count.groupby(['group']).size().reset_index(name='analytics')
    # print(anal_group)

    payment_df = lib_df[lib_df['lib_type']=='Payment']
    payment_count = payment_df.groupby(['app_id']).size().reset_index(name='group').sort_values(by=['group'])
    payment_count = payment_count.fillna(0)
    payment_count['group'].values[payment_count['group'] > 5] = 6
    payment_group = payment_count.groupby(['group']).size().reset_index(name='payment')
    # print(payment_group)

    socmed_df = lib_df[lib_df['lib_type']=='social_media']
    socmed_count = socmed_df.groupby(['app_id']).size().reset_index(name='group').sort_values(by=['group'])
    socmed_count = socmed_count.fillna(0)
    socmed_count['group'].values[socmed_count['group'] > 5] = 6
    socmed_group = socmed_count.groupby(['group']).size().reset_index(name='social_media')
    # print(socmed_group)

    ads_df = lib_df[lib_df['lib_type']=='ads']
    ads_count = ads_df.groupby(['app_id']).size().reset_index(name='group').sort_values(by=['group'])
    ads_count = ads_count.fillna(0)
    ads_count['group'].values[ads_count['group'] > 5] = 6
    ads_group = ads_count.groupby(['group']).size().reset_index(name='ads')
    # print(ads_group)

    merge_lib = merge(anal_group,payment_group,left_on='group',right_on='group',how='outer')
    merge_lib = merge(merge_lib,socmed_group,left_on='group',right_on='group',how='outer')
    merge_lib = merge(merge_lib,ads_group,left_on='group',right_on='group',how='outer')
    merge_lib = merge_lib.fillna(0)
    print(merge_lib)

    with open(write_path,'w') as fl:
        fl.write('Group & Analytics & Payment & Social Media & Ads\n')
        fl.write('----------------------------\n')
        for x,item in merge_lib.iterrows():
            group = int(item['group'])
            anal = int(item['analytics'])
            payment = int(item['payment'])
            socmed = int(item['social_media'])
            ads = int(item['ads'])
            pct_anal = pct(anal)
            pct_pay = pct(payment)
            pct_soc = pct(socmed)
            pct_ads = pct(ads)

            fl.write(str(group)+' & '+str(anal)+' ('+str(pct_anal)+'\%)' +' & '+str(payment)+' ('+str(pct_pay)+'\%)' 
            +' & '+str(socmed)+' ('+str(pct_soc)+'\%)' +' & '+str(ads)+' ('+str(pct_ads)+'\%)' +'\\\ \n')    
            # fl.write(str(item['group'])+' & '+str(item['analytics'])+'\\\ \n')    
        fl.write('----------------------------\n')

def pct(val):
    n = 182
    p = round((val/n)*100,1)
    return p

def main():

    dominant_path = report_path+'lib_dominant.txt'
    sum_dominant_lib(tracker_path,dominant_path)

    dominant_path = report_path+'lib_distribution.txt'
    sum_per_lib(tracker_path,dominant_path)


if __name__=='__main__':
    main()