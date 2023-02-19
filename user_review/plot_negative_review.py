import pandas as pd
from pandas.core.reshape.merge import merge
from pandas.io.parsers import read_csv 
import numpy as np
import statsmodels.api as sm # recommended import according to the docs
import matplotlib.pyplot as plt


sum_negative_review_path = '/home/budi/OTP_project/OTP_code/user_review/sum_negative_review.csv'
total_write_path = '/home/budi/OTP_project/OTP_code/user_review/total_review.txt'

def plot_negative_review(file):

    ori_path = '/home/budi/OTP_project/OTP_code/metadata/csv_apk_id.csv'
    ori_df = pd.read_csv(ori_path,names =['appId'] ,header=None)
    # print(ori_df)

    sum_negative_review = read_csv(file)
    sum_negative_review = merge(sum_negative_review,ori_df,left_on='appId',right_on='appId',how='right')
    sum_negative_review =sum_negative_review.fillna(0)
    print(sum_negative_review)

    percentiles = np.array([25,50 , 85])
    fraud_dt = sum_negative_review['pct_fraud']
    fraud_ecdf = sm.distributions.ECDF(fraud_dt)
    fraud_x = np.linspace(min(fraud_dt), max(fraud_dt))
    fraud_y = fraud_ecdf(fraud_x)
    fraud_pct_val = np.percentile(fraud_dt, percentiles)

    bugs_dt = sum_negative_review['pct_bugs']
    bugs_ecdf = sm.distributions.ECDF(bugs_dt)
    bugs_x = np.linspace(min(bugs_dt), max(bugs_dt))
    bugs_y = bugs_ecdf(bugs_x)
    bugs_pct_val = np.percentile(bugs_dt, percentiles)

    auth_dt = sum_negative_review['pct_auth']
    auth_ecdf = sm.distributions.ECDF(auth_dt)
    auth_x = np.linspace(min(auth_dt), max(auth_dt))
    auth_y = auth_ecdf(auth_x)
    auth_pct_val = np.percentile(auth_dt, percentiles)

    sec_dt = sum_negative_review['pct_sec']
    sec_ecdf = sm.distributions.ECDF(sec_dt)
    sec_x = np.linspace(min(sec_dt), max(sec_dt))
    sec_y = sec_ecdf(sec_x)
    sec_pct_val = np.percentile(sec_dt, percentiles)

    usa_dt = sum_negative_review['pct_usa']
    usa_ecdf = sm.distributions.ECDF(usa_dt)
    usa_x = np.linspace(min(usa_dt), max(usa_dt))
    usa_y = usa_ecdf(usa_x)
    usa_pct_val = np.percentile(usa_dt, percentiles)

    ads_dt = sum_negative_review['pct_ads']
    ads_ecdf = sm.distributions.ECDF(ads_dt)
    ads_x = np.linspace(min(ads_dt), max(ads_dt))
    ads_y = ads_ecdf(ads_x)
    ads_pct_val = np.percentile(ads_dt, percentiles)

    negative_dt = sum_negative_review['pct_negative']
    negative_ecdf = sm.distributions.ECDF(negative_dt)
    negative_x = np.linspace(min(negative_dt), max(negative_dt))
    negative_y = negative_ecdf(negative_x)
    negative_pct_val = np.percentile(negative_dt, percentiles)

    fig = plt.figure(figsize=(6,2.5))
    plt.plot(fraud_x, fraud_y*100, marker='^', lw = 2)
    plt.plot(bugs_x, bugs_y*100, marker='o', lw = 2)# Label axes and show plot
    plt.plot(auth_x, auth_y*100, marker='s', lw = 2)# Label axes and show plot
    plt.plot(sec_x, sec_y*100, marker='X', lw = 2)# Label axes and show plot
    plt.plot(usa_x, usa_y*100, marker='D', lw = 2)# Label axes and show plot
    plt.plot(ads_x, ads_y*100, marker='v', lw = 2)# Label axes and show plot
     # plt.plot(fraud_x, fraud_y*100, linestyle='--', lw = 2)
    # plt.plot(bugs_x, bugs_y*100, linestyle='--', lw = 2)# Label axes and show plot
    # plt.plot(auth_x, auth_y*100, linestyle='--', lw = 2)# Label axes and show plot
    # plt.plot(sec_x, sec_y*100, linestyle='--', lw = 2)# Label axes and show plot
    # plt.plot(usa_x, usa_y*100, linestyle='--', lw = 2)# Label axes and show plot
    # plt.plot(ads_x, ads_y*100, linestyle='--', lw = 2)# Label axes and show plot
    # plt.plot(negative_x, negative_y*100, linestyle='--', lw = 2)# Label axes and show plot
    # plt.legend(("Fraud", "Bugs","Authentication","Security","Usability", "Ads and Tracker"))
    plt.legend(("Fraud", "Bugs","Authentication","Security","Usability", "Ads and Tracker","Negative Review"))
    plt.xlabel('Complaint Ratio (%)', size = 14)
    plt.ylabel('ECDF', size = 14)
    plt.xlim(0,max(negative_x))
    # plt.ylim(0,max(negative_y)*100)
    # plt.plot(fraud_pct_val, percentiles, marker='o', color='red',linestyle='none')
    # plt.plot(bugs_pct_val, percentiles, marker='o', color='red',linestyle='none')
    # plt.plot(auth_pct_val, percentiles, marker='o', color='red',linestyle='none')
    # plt.plot(sec_pct_val, percentiles, marker='o', color='red',linestyle='none')
    # plt.plot(usa_pct_val, percentiles, marker='o', color='red',linestyle='none')
    # plt.plot(ads_pct_val, percentiles, marker='o', color='red',linestyle='none')
    # plt.plot(negative_pct_val, percentiles, marker='o', color='red',linestyle='none')
    plt.tight_layout()
    fig.savefig('/home/budi/OTP_project/OTP_code/user_review/user_review_ecdf.pdf')
    plt.show()

def sum_negative_review(file,write_path):
    negative_review = read_csv(file)
    hit = negative_review[['fraudulent','bugs','authentication','security','usability','ads_tracker','cust_support']]
    sum_hit = hit.sum(axis=0)
    pct_hit = negative_review[['pct_fraud','pct_bugs','pct_auth','pct_sec','pct_usa','pct_ads','pct_cust']]
    avg_pct = round(pct_hit.mean(axis=0),2)
    result = pd.concat([sum_hit,avg_pct],axis=0)
    print(result)    
    result.to_csv(write_path)

def plot_total_negative_review(file):
    sum_negative_review = read_csv(file)
    print(sum_negative_review[sum_negative_review.columns[[1,2,3,4,5,6,7]]])
    sum_negative_review['fraudulent'].where(sum_negative_review['fraudulent'] <= 100, 101, inplace=True)
    sum_negative_review['bugs'].where(sum_negative_review['bugs'] <= 100, 101, inplace=True)
    sum_negative_review['authentication'].where(sum_negative_review['authentication'] <= 100, 101, inplace=True)
    sum_negative_review['security'].where(sum_negative_review['security'] <= 100, 101, inplace=True)
    sum_negative_review['usability'].where(sum_negative_review['usability'] <= 100, 101, inplace=True)
    sum_negative_review['ads_tracker'].where(sum_negative_review['ads_tracker'] <= 100, 101, inplace=True)
    print(sum_negative_review)

    percentiles = np.array([25,50 , 85])
    fraud_dt = sum_negative_review['fraudulent']
    fraud_ecdf = sm.distributions.ECDF(fraud_dt)
    fraud_x = np.linspace(min(fraud_dt), max(fraud_dt))
    fraud_y = fraud_ecdf(fraud_x)
    fraud_pct_val = np.percentile(fraud_dt, percentiles)

    bugs_dt = sum_negative_review['bugs']
    bugs_ecdf = sm.distributions.ECDF(bugs_dt)
    bugs_x = np.linspace(min(bugs_dt), max(bugs_dt))
    bugs_y = bugs_ecdf(bugs_x)
    bugs_pct_val = np.percentile(bugs_dt, percentiles)

    auth_dt = sum_negative_review['authentication']
    auth_ecdf = sm.distributions.ECDF(auth_dt)
    auth_x = np.linspace(min(auth_dt), max(auth_dt))
    auth_y = auth_ecdf(auth_x)
    auth_pct_val = np.percentile(auth_dt, percentiles)

    sec_dt = sum_negative_review['security']
    sec_ecdf = sm.distributions.ECDF(sec_dt)
    sec_x = np.linspace(min(sec_dt), max(sec_dt))
    sec_y = sec_ecdf(sec_x)
    sec_pct_val = np.percentile(sec_dt, percentiles)

    usa_dt = sum_negative_review['usability']
    usa_ecdf = sm.distributions.ECDF(usa_dt)
    usa_x = np.linspace(min(usa_dt), max(usa_dt))
    usa_y = usa_ecdf(usa_x)
    usa_pct_val = np.percentile(usa_dt, percentiles)

    ads_dt = sum_negative_review['ads_tracker']
    ads_ecdf = sm.distributions.ECDF(ads_dt)
    ads_x = np.linspace(min(ads_dt), max(ads_dt))
    ads_y = ads_ecdf(ads_x)
    ads_pct_val = np.percentile(ads_dt, percentiles)


    fig = plt.figure(figsize=(8,4))
    plt.plot(fraud_x, fraud_y*100, marker='o', lw = 2)
    plt.plot(bugs_x, bugs_y*100, marker='^', lw = 2)# Label axes and show plot
    plt.plot(auth_x, auth_y*100, marker='s', lw = 2)# Label axes and show plot
    plt.plot(sec_x, sec_y*100, marker='X', lw = 2)# Label axes and show plot
    plt.plot(usa_x, usa_y*100, marker='D', lw = 2)# Label axes and show plot
    plt.plot(ads_x, ads_y*100, marker='v', lw = 2)# Label axes and show plot
    # plt.plot(fraud_x, fraud_y*100, linestyle='--', lw = 2)
    # plt.plot(bugs_x, bugs_y*100, linestyle='--', lw = 2)# Label axes and show plot
    # plt.plot(auth_x, auth_y*100, linestyle='--', lw = 2)# Label axes and show plot
    # plt.plot(sec_x, sec_y*100, linestyle='--', lw = 2)# Label axes and show plot
    # plt.plot(usa_x, usa_y*100, linestyle='--', lw = 2)# Label axes and show plot
    # plt.plot(ads_x, ads_y*100, linestyle='--', lw = 2)# Label axes and show plot
    plt.legend(("Fraud", "Bugs","Authentication","Security","Usability", "Ads and Tracker"))
    plt.xlabel('Complaint(%)', size = 14)
    plt.ylabel('ECDF', size = 14)
    # plt.plot(fraud_pct_val, percentiles, marker='o', color='red',linestyle='none')
    # plt.plot(bugs_pct_val, percentiles, marker='o', color='red',linestyle='none')
    # plt.plot(auth_pct_val, percentiles, marker='o', color='red',linestyle='none')
    # plt.plot(sec_pct_val, percentiles, marker='o', color='red',linestyle='none')
    # plt.plot(usa_pct_val, percentiles, marker='o', color='red',linestyle='none')
    # plt.plot(ads_pct_val, percentiles, marker='o', color='red',linestyle='none')
    # fig.savefig('/home/budi/crypto_project/crypto_code/metadata_crawling/total_negative_review_ecdf.pdf')
    plt.show()

def plot_by_range(file):
    df = pd.read_csv(file)
    df_half = df[['fraudulent','bugs','authentication','security','usability','ads_tracker','cust_support']]
    # print(df_half)
    # range = [0, 25, 50, 75, 100, 125, 150, 175, 200]
    # count_fraud = df_half['fraudulent'].value_counts(bins=range, sort=False)
    # count_fraud.plot(kind='hist')
    count_fraud = pd.cut(df_half['cust_support'],bins=10).value_counts() 
    print(count_fraud) 


 
def main():
    plot_negative_review(sum_negative_review_path)
    sum_negative_review(sum_negative_review_path,total_write_path)
    plot_total_negative_review(sum_negative_review_path)
    plot_by_range(sum_negative_review_path)

if __name__=='__main__':
    main()