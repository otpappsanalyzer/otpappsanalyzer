import os
import csv
import pandas as pd
from pandas.core.arrays import integer
from pandas.core.arrays.integer import Int64Dtype
import numpy as np
import statsmodels.api as sm # recommended import according to the docs
import matplotlib.pyplot as plt

comment_file = '/home/budi/OTP_project/OTP_code/user_review/comment_file.csv'

def contains_any(x, exps):
    for exp in exps:
        if exp in x:
            return True
    return False
def contains_all(x, exps):
    for exp in exps:
        # print(type(exp),exp,x)
        if exp not in x:
            return False
    return True

def summarize_rating(comment_file):
    df_comment = pd.read_csv(comment_file,low_memory=False)
    # print(type(df_comment['star']))
    selected_col = df_comment[['appId','star']].sort_values(by='appId')
    # selected_col = pd.DataFrame(selected_col)
    no_comment = selected_col.loc[selected_col['star']=='error']
    # df_group = df_group.drop(df_group[df_group.star == 'error'].index)
    selected_col = selected_col.drop(selected_col[selected_col.star == 'error'].index)
    selected_col = selected_col.drop(selected_col[selected_col.star == '0'].index)
    star_sum = selected_col.groupby(['appId']).star.value_counts().unstack(fill_value=0).reset_index()
    star_sum = star_sum.rename(columns={'1':'1_star','2':'2_star','3':'3_star','4':'4_star','5':'5_star'})
    # print(star_sum)
    # star_sum = selected_col.groupby(['appId']).size().reset_index(name = 'total').sort_values(by='appId')
    # one_star = selected_col.groupby(['appId','star']).size().reset_index(name='count')    
    # print(star_sum[0:20])
    # group_and_count = selected_col.groupby(['appId','star']).size().reset_index(name='count')
    # print(group_and_count[0:30])

    # # print(df_group)
    # no_comment = df_group.loc[df_group['star']=='error']
    # # print(no_comment)
    # df_group = df_group.drop(df_group[df_group.star == 'error'].index)
    # sum_dic=[]
    # for index, row in df_group.iterrows():
    #     if row['appId'] not in sum_dic:
    #         sum_dic.append(row['appId'])
    #     print(sum_dic)

def summarize_negative_comment(comment_file):
    # fraudulent = ['scam','fake','balance','money','buy','bought','invest','purchase','payment','credit card','debit card','cash','manipulation']
    fraudulent = ['scam','fake','liar','manipulation']
    bugs = ['bug','error','crash','update','upgrade','not responding','freeze','stuck']
    authentication = ['verification','verify','verified','account','login','register']
    security = ['security','secure','hack','bot','insecure']
    usability = ['confuse','confusing','bad','slow','rubbish','junk','user interface']
    ads_tracker = ['advertisement','advert','video ads','tracker','intrusive ads','massive ads','ads']
    customer_support = ['customer service','support']

    df_comment = pd.read_csv(comment_file,low_memory=False)
    # error_line = df_comment[df_comment['star'].str.contains('error')]
    # print(error_line)
    df_comment = df_comment.drop(df_comment[df_comment.star == 'error'].index)
    # print(df_comment)
    df_comment.star = df_comment.star.astype(int)
    df_comment.comment = df_comment.comment.astype(str)
    total = df_comment.groupby(["appId"])['appId'].count().reset_index(name="total")
    negative_review = df_comment.loc[df_comment.star<=2]
    negative_review = negative_review[['appId','star','comment']]
    negative_review['fraudulent'] = negative_review['comment'].apply(lambda x: (contains_any(x, fraudulent)))
    negative_review['bugs'] = negative_review['comment'].apply(lambda x: (contains_any(x, bugs)))
    negative_review['authentication'] = negative_review['comment'].apply(lambda x: (contains_any(x, authentication)))
    negative_review['security'] = negative_review['comment'].apply(lambda x: (contains_any(x, security)))
    negative_review['usability'] = negative_review['comment'].apply(lambda x: (contains_any(x, usability)))
    negative_review['ads_tracker'] = negative_review['comment'].apply(lambda x: (contains_any(x, ads_tracker)))
    negative_review['cust_support'] = negative_review['comment'].apply(lambda x: (contains_any(x, customer_support)))
    total_negative = negative_review.groupby(["appId"])['appId'].count().reset_index(name="total_negative")
    # print(test)
    # negative_review = negative_review.sort_values()
    sum_negative_review = negative_review.drop(columns=['star','comment'])
    sum_negative_review = sum_negative_review.groupby(['appId']).sum()
    sum_negative_review = sum_negative_review.merge(total_negative,left_on='appId', right_on='appId')
    sum_negative_review = sum_negative_review.merge(total,left_on='appId', right_on='appId')
    sum_negative_review['pct_negative'] = round((sum_negative_review['total_negative']/sum_negative_review['total'])*100,2)
    sum_negative_review['pct_fraud'] = round((sum_negative_review['fraudulent']/sum_negative_review['total_negative'])*100,2)
    sum_negative_review['pct_bugs'] = round((sum_negative_review['bugs']/sum_negative_review['total_negative'])*100,2)
    sum_negative_review['pct_auth'] = round((sum_negative_review['authentication']/sum_negative_review['total_negative'])*100,2)
    sum_negative_review['pct_sec'] = round((sum_negative_review['security']/sum_negative_review['total_negative'])*100,2)
    sum_negative_review['pct_usa'] = round((sum_negative_review['usability']/sum_negative_review['total_negative'])*100,2)
    sum_negative_review['pct_ads'] = round((sum_negative_review['ads_tracker']/sum_negative_review['total_negative'])*100,2)
    sum_negative_review['pct_cust'] = round((sum_negative_review['cust_support']/sum_negative_review['total_negative'])*100,2)
    # fft_pct_neg = sum_negative_review[sum_negative_review['pct_negative']>50]
    # print(len(fft_pct_neg[['appId','pct_negative']]))
    # print(negative_review)
    print(sum_negative_review)
    # sum_non_empty = (sum_negative_review==0).sum()
    sum_negative_review_path = '/home/budi/OTP_project/OTP_code/user_review/sum_negative_review.csv'
    sum_negative_review.to_csv(sum_negative_review_path)
    # percentiles = np.array([25,50 , 85])
    # fraud_dt = sum_negative_review['pct_fraud']
    # fraud_ecdf = sm.distributions.ECDF(fraud_dt)
    # fraud_x = np.linspace(min(fraud_dt), max(fraud_dt))
    # fraud_y = fraud_ecdf(fraud_x)
    # fraud_pct_val = np.percentile(fraud_dt, percentiles)

    # bugs_dt = sum_negative_review['pct_bugs']
    # bugs_ecdf = sm.distributions.ECDF(bugs_dt)
    # bugs_x = np.linspace(min(bugs_dt), max(bugs_dt))
    # bugs_y = bugs_ecdf(bugs_x)
    # bugs_pct_val = np.percentile(bugs_dt, percentiles)

    # auth_dt = sum_negative_review['pct_auth']
    # auth_ecdf = sm.distributions.ECDF(auth_dt)
    # auth_x = np.linspace(min(auth_dt), max(auth_dt))
    # auth_y = auth_ecdf(auth_x)
    # auth_pct_val = np.percentile(auth_dt, percentiles)

    # sec_dt = sum_negative_review['pct_sec']
    # sec_ecdf = sm.distributions.ECDF(sec_dt)
    # sec_x = np.linspace(min(sec_dt), max(sec_dt))
    # sec_y = sec_ecdf(sec_x)
    # sec_pct_val = np.percentile(sec_dt, percentiles)

    # usa_dt = sum_negative_review['pct_usa']
    # usa_ecdf = sm.distributions.ECDF(usa_dt)
    # usa_x = np.linspace(min(usa_dt), max(usa_dt))
    # usa_y = usa_ecdf(usa_x)
    # usa_pct_val = np.percentile(usa_dt, percentiles)

    # ads_dt = sum_negative_review['pct_ads']
    # ads_ecdf = sm.distributions.ECDF(ads_dt)
    # ads_x = np.linspace(min(ads_dt), max(ads_dt))
    # ads_y = ads_ecdf(ads_x)
    # ads_pct_val = np.percentile(ads_dt, percentiles)

    # negative_dt = sum_negative_review['pct_negative']
    # negative_ecdf = sm.distributions.ECDF(negative_dt)
    # negative_x = np.linspace(min(negative_dt), max(negative_dt))
    # negative_y = negative_ecdf(negative_x)
    # negative_pct_val = np.percentile(negative_dt, percentiles)

    # fig = plt.figure(figsize=(5,4))
    # plt.plot(fraud_x, fraud_y*100, linestyle='--', lw = 2)
    # plt.plot(bugs_x, bugs_y*100, linestyle='--', lw = 2)# Label axes and show plot
    # plt.plot(auth_x, auth_y*100, linestyle='--', lw = 2)# Label axes and show plot
    # plt.plot(sec_x, sec_y*100, linestyle='--', lw = 2)# Label axes and show plot
    # plt.plot(usa_x, usa_y*100, linestyle='--', lw = 2)# Label axes and show plot
    # plt.plot(ads_x, ads_y*100, linestyle='--', lw = 2)# Label axes and show plot
    # # plt.plot(negative_x, negative_y*100, linestyle='--', lw = 2)# Label axes and show plot
    # plt.legend(("Fraud", "Bugs","Authentication","Security","Usability", "Ads and Tracker"))
    # # plt.legend(("Fraud", "Bugs","Authentication","Security","Usability", "Ads and Tracker","Negative Review"))
    # plt.xlabel('Complaint(%))', size = 10)
    # plt.ylabel('ECDF', size = 10)
    # plt.plot(fraud_pct_val, percentiles, marker='o', color='red',linestyle='none')
    # plt.plot(bugs_pct_val, percentiles, marker='o', color='red',linestyle='none')
    # plt.plot(auth_pct_val, percentiles, marker='o', color='red',linestyle='none')
    # plt.plot(sec_pct_val, percentiles, marker='o', color='red',linestyle='none')
    # plt.plot(usa_pct_val, percentiles, marker='o', color='red',linestyle='none')
    # plt.plot(ads_pct_val, percentiles, marker='o', color='red',linestyle='none')
    # # plt.plot(negative_pct_val, percentiles, marker='o', color='red',linestyle='none')
    # fig.savefig('/home/budi/crypto_project/crypto_code/metadata_crawling/user_review_ecdf.pdf')
    # plt.show()


def main():
    # summarize_rating(comment_file)
    summarize_negative_comment(comment_file)

if __name__=='__main__':
    main()