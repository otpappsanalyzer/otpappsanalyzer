# This script is used to check the object domain (URL,netloc, fld)to easy list and easy privacy

from time import sleep
import pandas as pd

easy_list_path = '/home/budi/OTP_project/OTP_code/dynamic_analysis/easylist.txt'
easy_privacy_path = '/home/budi/OTP_project/OTP_code/dynamic_analysis/easyprivacy.txt'
fld_path = '/home/budi/OTP_project/OTP_code/dynamic_analysis/report/fld_per_app.csv'
netloc_path = '/home/budi/OTP_project/OTP_code/dynamic_analysis/report/netloc_per_app.csv'
url_path = '/home/budi/OTP_project/OTP_code/dynamic_analysis/report/url_per_app.csv'
report_path = '/home/budi/OTP_project/OTP_code/dynamic_analysis/report/'

def extract_EL (EL_path):
    EL_list=[]
    with open(EL_path,'r') as fl:
        for item in fl:
            EL_list.append(item.strip())
    return EL_list 

def extract_EP (EP_path):
    EP_list=[]
    with open(EP_path,'r') as fl:
        for item in fl:
            EP_list.append(item.strip())
    return EP_list


def main():
    EL_list = extract_EL(easy_list_path)
    EP_list = extract_EP(easy_privacy_path)
    detection_list = []
    fld_df = pd.read_csv(fld_path,index_col=False)
    fld_df = fld_df[["app_id","fld"]]

    # check fld 
    for i, fld in fld_df.iterrows():
        app_id = fld["app_id"].strip()
        fld_item = fld["fld"].strip()
        # to easy list
        for el in EL_list:
            if fld_item in el:
                # print (fld_item + '-------------------->' + el)
                EL_stat = 'TP'
                # ref = 'easylist'
                break
            else:
                EL_stat = 'FP'
                # ref = 'N'
        line_stat = {'app_id':app_id,'type': 'fld' ,'object':fld_item,'status':EL_stat,'reference':'easylist'}
        if line_stat not in detection_list:
            detection_list.append(line_stat)
        # to easy privacy
        for ep in EP_list:
            if fld_item in ep:
                # print (fld_item + '-------------------->' + ep)
                EP_stat = 'TP'
                # ref = 'easylist'
                break
            else:
                EP_stat = 'FP'
                # ref = 'N'
        line_stat = {'app_id':app_id,'type': 'fld' ,'object':fld_item,'status':EP_stat,'reference':'easyprivacy'}
        if line_stat not in detection_list:
            detection_list.append(line_stat)
        # sleep(1)

    # check netloc
    netloc_df = pd.read_csv(netloc_path,index_col=False)
    netloc_df = netloc_df[["app_id","netloc"]]
    for i, netloc in netloc_df.iterrows():
        app_id = netloc["app_id"].strip()
        netloc_item = netloc["netloc"].strip()
        # to easy list
        for el in EL_list:
            if netloc_item in el:
                # print (netloc_item + '-------------------->' + el)
                EL_stat = 'TP'
                # ref = 'easylist'
                break
            else:
                EL_stat = 'FP'
                # ref = 'N'
        line_stat = {'app_id':app_id,'type': 'netloc' ,'object':netloc_item,'status':EL_stat,'reference':'easylist'}
        if line_stat not in detection_list:
            detection_list.append(line_stat)
        # to easy privacy
        for ep in EP_list:
            if netloc_item in ep:
                # print (netloc_item + '-------------------->' + ep)
                EP_stat = 'TP'
                # ref = 'easylist'
                break
            else:
                EP_stat = 'FP'
                # ref = 'N'
        line_stat = {'app_id':app_id,'type': 'netloc' ,'object':netloc_item,'status':EP_stat,'reference':'easyprivacy'}
        if line_stat not in detection_list:
            detection_list.append(line_stat)
        # sleep(1)

    # check URL
    url_df = pd.read_csv(url_path,index_col=False)
    url_df = url_df[["app_id","url"]]
    for i, url in url_df.iterrows():
        app_id = url["app_id"].strip()
        url_item = url["url"].strip()
        # to easy list
        for el in EL_list:
            if url_item in el:
                # print (url_item + '-------------------->' + el)
                EL_stat = 'TP'
                break
            else:
                EL_stat = 'FP'
        line_stat = {'app_id':app_id,'type': 'url' ,'object':url_item,'status':EL_stat,'reference':'easylist'}
        if line_stat not in detection_list:
            detection_list.append(line_stat)
        # to easy privacy
        for ep in EP_list:
            if url_item in ep:
                # print (url_item + '-------------------->' + ep)
                EP_stat = 'TP'
                # ref = 'easylist'
                break
            else:
                EP_stat = 'FP'
                # ref = 'N'
        line_stat = {'app_id':app_id,'type': 'url' ,'object':url_item,'status':EP_stat,'reference':'easyprivacy'}
        if line_stat not in detection_list:
            detection_list.append(line_stat)


    write_path = report_path + 'TP_domain_check_detail.csv'
    detection_df = pd.DataFrame(detection_list)
    detection_df.to_csv(write_path,index=False)

    sum_domain_df = detection_df.groupby(['app_id','type','status','reference']).size().reset_index(name='count').sort_values(by=['type'])
    sum_per_app_path = report_path+'sum_TP_domain_chek_per_app.csv'
    sum_domain_df.to_csv(sum_per_app_path,index=False)
    # print(sum_domain_df) 

    sum_per_domain_level_df = sum_domain_df.groupby(['type','status','reference']).size().reset_index(name='count')
    sum_per_domain_level_path = report_path+'sum_TP_domain_check_perl_domain_level.csv'
    sum_per_domain_level_df['pct'] = round((sum_per_domain_level_df['count'] / 182)*100,2)
    sum_per_domain_level_df.to_csv(sum_per_domain_level_path,index=False)
    print(sum_per_domain_level_df)
if __name__=="__main__":
    main()