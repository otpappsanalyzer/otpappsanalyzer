from operator import concat
import pandas as pd
import numpy as np

TP_domain_check_path = '/home/budi/OTP_project/OTP_code/dynamic_analysis/report/TP_domain_check_detail.csv'
top_install_path = '/home/budi/OTP_project/OTP_code/metadata/top_install.csv'
write_path = '/home/budi/OTP_project/OTP_code/dynamic_analysis/report/TP_domain_check_popular.txt'

def pct(val):
    n = 182
    p = round((val/n)*100,1)
    return p


tp_df = pd.read_csv(TP_domain_check_path)
top_df = pd.read_csv(top_install_path)

# Take only third party domain
tp_df = tp_df.loc[tp_df['status']=='TP']
# Just need to find apps number request for the TP not the number of request
tp_df = tp_df[['app_id','type','reference']].drop_duplicates()
# print(tp_df)

per_domain_df = tp_df.groupby(['type','reference']).size().reset_index(name='count').sort_values(by=['count'],ascending=False)
# print(per_domain_df)


with open (write_path,'w') as fl:
    fl.write('Domain Level & Reference & \# of Apps(\%) \\\ \n')
    for x, line in per_domain_df.iterrows():
        count = line['count']
        pct_tp = pct(count)
        fl.write(str(line['type'])+ '  & ' + line['reference'] + '  & ' + str(count) + '(' + str(pct_tp) +'\%)' + ' \\\ \n')


# just need to get the app_id and number of library since the previous operation have the result 
result_df = tp_df.merge(top_df, left_on='app_id',right_on='appId',how='left')
result_df['popular'] = np.where(result_df['appId']==result_df['app_id'],True,False)
result_df = result_df[['app_id','type','reference','popular']]
# print(result_df)

per_domain_pop_df = result_df.groupby(['type','reference','popular']).size().reset_index(name='count').sort_values(by=['type'],ascending=False)

with open (write_path,'a') as fl:
    fl.write('-------------------------------------------------------- \\\ \n')
    fl.write('-------------------------------------------------------- \\\ \n')
    fl.write('Domain Level & Reference & Popular & \# of Apps(\%) \\\ \n')
    for x, line in per_domain_pop_df.iterrows():
        count = line['count']
        pct_tp = pct(count)
        fl.write(str(line['type'])+ '  & ' + line['reference'] + '  & ' +str(line['popular'])+  '  & ' + str(count) + '(' + str(pct_tp) +'\%)' + ' \\\ \n')
