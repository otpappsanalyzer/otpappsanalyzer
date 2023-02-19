import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

def pct(x):
    N = 182
    ret = round(((x/N)*100),2)
    return ret

nc_path = '/home/budi/OTP_project/OTP_code/package_analysis/custom_detail_apkid.csv'
top_install_path = '/home/budi/OTP_project/OTP_code/metadata/top_install.csv'
report_path = '/home/budi/OTP_project/OTP_code/package_analysis/custom_table_report.txt'

nc_df = pd.read_csv(nc_path)
type_list = []
for x, line in nc_df.iterrows():
    type = line['types'] 
    app_id = str(line['app_name']).rstrip('apk')
    app_id = app_id.rstrip('.')
    if 'anti_vm' in type or 'anti_debug' in type or 'packer' in type or 'obfuscator' in type or 'anti_disassembly':
        type_list.append({'app_id': app_id,'types':type})

type_df = pd.DataFrame(type_list)
type_df = type_df.drop_duplicates()
type_df = type_df[type_df['types'].str.contains("compiler|manipulator")==False]
# print(type_df)

top_df = pd.read_csv(top_install_path)
top_df = top_df['appId']
# print(top_df)

merge_df = type_df.merge(top_df,right_on='appId',left_on='app_id',how='left')
merge_df['popular'] = np.where(merge_df['appId']==merge_df['app_id'],True,False)
merge_df=merge_df[['app_id','types','popular']]

by_type_df = merge_df.groupby(['types']).size().reset_index(name='count_type').sort_values(by=['count_type'],ascending=False)
# print(by_type_df)
by_type_popular_df = merge_df.groupby(['types','popular']).size().reset_index(name='count_pop').sort_values(by=['count_pop'],ascending=False)
by_type_popular_df=by_type_popular_df[by_type_popular_df['popular']==True]
# print(by_type_popular_df)

merge_type_pop = by_type_df.merge(by_type_popular_df,right_on='types',left_on='types',how='inner')
# print(merge_type_pop)

with open(report_path,'w') as fl:
    fl.write('Types  & #of Apps (\%) & # of Popular apps (\%) \\\ \n')
    for y,item in merge_type_pop.iterrows():
        pct_all_app = pct(item['count_type'])
        pct_pop_app = pct(item['count_pop'])
        fl.write(item['types'] + ' & ' + str(item['count_type']) +'('+str(pct_all_app) + '\%) ' + ' & ' + str(item['count_pop']) +'('+str(pct_pop_app) + '\%) \\\ \n' )
