import pandas as pd
import numpy as np

sum_path = '/home/budi/OTP_project/OTP_code/user_review/sum_negative_review.csv'
detail_path = '/home/budi/OTP_project/OTP_code/user_review/comment_file.csv'
write_path = '/home/budi/OTP_project/OTP_code/user_review/table_content.txt'
top_install_path = '/home/budi/OTP_project/OTP_code/metadata/top_install.csv'


def pct(x,y):
    res = round((x/y)*100,1)
    return res


detail_df = pd.read_csv(detail_path,low_memory=False)
detail_df= detail_df[~detail_df['star'].isin(['error'])]
detail_df['star'] = detail_df['star'].astype(int)

negative_length = len(detail_df[detail_df['star']<3])
# print(negative_length)

n = 182 # number of crypto wallet apps
sum_df = pd.read_csv(sum_path)
# print(sum_df)

fraud = sum_df[['appId','fraudulent']]
fraud = fraud[fraud['fraudulent']>0]
fraud_sum = fraud['fraudulent'].sum()
pct_sum_fr = pct(fraud_sum,negative_length)
pct_app_fr = pct(len(fraud),n)

bugs = sum_df[['appId','bugs']]
bugs = bugs[bugs['bugs']>0]
bugs_sum = bugs['bugs'].sum()
pct_sum_bg = pct(bugs_sum,negative_length)
pct_app_bg = pct(len(bugs),n)

auth = sum_df[['appId','authentication']]
auth = auth[auth['authentication']>0]
auth_sum = auth['authentication'].sum()
pct_sum_au = pct(auth_sum,negative_length)
pct_app_au = pct(len(auth),n)

sec = sum_df[['appId','security']]
sec = sec[sec['security']>0]
sec_sum = sec['security'].sum()
pct_sum_se = pct(sec_sum,negative_length)
pct_app_se = pct(len(sec),n)

usa = sum_df[['appId','usability']]
usa = usa[usa['usability']>0]
usa_sum = usa['usability'].sum()
pct_sum_us = pct(usa_sum,negative_length)
pct_app_us = pct(len(usa),n)

ads = sum_df[['appId','ads_tracker']]
ads = ads[ads['ads_tracker']>0]
ads_sum = ads['ads_tracker'].sum()
pct_sum_ad = pct(ads_sum,negative_length)
pct_app_ad = pct(len(ads),n)


with open(write_path,'w') as fl:
    fl.write('Category & \# of Complaint (\%) & \# of Apps (\%) \\\ \n')
    fl.write('Authentication'+' & '+str(auth_sum)+' ('+str(pct_sum_au)+'\%)'+' & '+str(len(auth))+' ('+str(pct_app_au)+'\%) & \n') 
    fl.write('Bugs'+' & '+str(bugs_sum)+' ('+str(pct_sum_bg)+'\%)'+' & '+str(len(bugs))+' ('+str(pct_app_bg)+'\%) & \n')   
    fl.write('Usability'+' & '+str(usa_sum)+' ('+str(pct_sum_us)+'\%)'+' & '+str(len(usa))+' ('+str(pct_app_us)+'\%) & \n')
    fl.write('Security'+' & '+str(sec_sum)+' ('+str(pct_sum_se)+'\%)'+' & '+str(len(sec))+' ('+str(pct_app_se)+'\%) & \n')
    fl.write('Fraudulent'+' & '+str(fraud_sum)+' ('+str(pct_sum_fr)+'\%)'+' & '+str(len(fraud))+' ('+str(pct_app_fr)+'\%) & \n')
    fl.write('Ads and Tracker'+' & '+str(ads_sum)+' ('+str(pct_sum_ad)+'\%)'+' & '+str(len(ads))+' ('+str(pct_app_ad)+'\%) & \n')

# Next part is popular apps
top_df = pd.read_csv(top_install_path)

result_df = sum_df.merge(top_df, left_on='appId',right_on='appId',how='left')
result_df['popular'] = np.where(result_df['appId']==result_df['appId'],True,False)

fraud_pop = result_df[['appId','fraudulent','popular']]
# print(len(fraud_pop))
fraud_pop = fraud_pop[(fraud_pop['fraudulent']>0) & (fraud_pop['popular']==True)]
# print(fraud_pop)
# print(len(fraud_pop))
fraud_pop_sum = fraud_pop['fraudulent'].sum()
pct_sum_fraud_pop = pct(fraud_pop_sum,negative_length)
pct_app_fraud_pop = pct(len(fraud_pop),n)

bugs_pop = result_df[['appId','bugs','popular']]
bugs_pop = bugs_pop[(bugs_pop['bugs']>0) & (fraud_pop['popular']==True)]
bugs_pop_sum = bugs_pop['bugs'].sum()
pct_sum_bugs_pop = pct(bugs_pop_sum,negative_length)
pct_app_bugs_pop = pct(len(bugs_pop),n)

auth_pop = result_df[['appId','authentication','popular']]
auth_pop = auth_pop[(auth_pop['authentication']>0) & (auth_pop['popular']==True)]
auth_pop_sum = auth_pop['authentication'].sum()
pct_sum_auth_pop = pct(auth_pop_sum,negative_length)
pct_app_auth_pop = pct(len(auth_pop),n)

sec_pop = result_df[['appId','security','popular']]
sec_pop = sec_pop[(sec_pop['security']>0)  & (sec_pop['popular']==True)]
sec_pop_sum = sec_pop['security'].sum()
pct_sum_sec_pop = pct(sec_pop_sum,negative_length)
pct_app_sec_pop = pct(len(sec_pop),n)

usa_pop = result_df[['appId','usability','popular']]
usa_pop = usa_pop[(usa_pop['usability']>0) & (usa_pop['popular']==True)]
usa_pop_sum = usa_pop['usability'].sum()
pct_sum_usa_pop = pct(usa_pop_sum,negative_length)
pct_app_usa_pop = pct(len(usa_pop),n)

ads_pop = result_df[['appId','ads_tracker','popular']]
ads_pop = ads_pop[(ads_pop['ads_tracker']>0) & (ads_pop['popular']==True)]
ads_pop_sum = ads_pop['ads_tracker'].sum()
pct_sum_ads_pop = pct(ads_pop_sum,negative_length)
pct_app_ads_pop = pct(len(ads_pop),n)


with open(write_path,'a') as fl:
    fl.write('---------------------------------- \\\ \n')
    fl.write('Next is for the popular apps \\\ \n')
    fl.write('---------------------------------- \\\ \n')
    fl.write('Category & \# of Complaint (\%) & \# of Apps (\%) \\\ \n')
    fl.write('---------------------------------- \\\ \n')
    fl.write('Authentication'+' & '+str(auth_pop_sum)+' ('+str(pct_sum_auth_pop)+'\%)'+' & '+str(len(auth_pop))+' ('+str(pct_app_auth_pop)+'\%) & \n') 
    fl.write('Bugs'+' & '+str(bugs_pop_sum)+' ('+str(pct_sum_bugs_pop)+'\%)'+' & '+str(len(bugs_pop))+' ('+str(pct_app_bugs_pop)+'\%) & \n')   
    fl.write('Usability'+' & '+str(usa_pop_sum)+' ('+str(pct_sum_usa_pop)+'\%)'+' & '+str(len(usa_pop))+' ('+str(pct_app_usa_pop)+'\%) & \n')
    fl.write('Security'+' & '+str(sec_pop_sum)+' ('+str(pct_sum_sec_pop)+'\%)'+' & '+str(len(sec_pop))+' ('+str(pct_app_sec_pop)+'\%) & \n')
    fl.write('Fraudulent'+' & '+str(fraud_pop_sum)+' ('+str(pct_sum_fraud_pop)+'\%)'+' & '+str(len(fraud_pop))+' ('+str(pct_app_fraud_pop)+'\%) & \n')
    fl.write('Ads and Tracker'+' & '+str(ads_pop_sum)+' ('+str(pct_sum_ads_pop)+'\%)'+' & '+str(len(ads_pop))+' ('+str(pct_app_ads_pop)+'\%) & \n')