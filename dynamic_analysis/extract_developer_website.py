import os 
import json
import pandas as pd


metadata_path = '/home/budi/OTP_project/metadata_result/'
list_app_path = '/home/budi/OTP_project/OTP_code/metadata/csv_apk_id.csv'
report_path = '/home/budi/OTP_project/OTP_code/dynamic_analysis/report/'

def extract_dev_web(metadata_path,app_id):
    app_meta_path = metadata_path+app_id+'.txt'
    return_meta=[]
    print(app_meta_path)
    try:
        with open(app_meta_path,'r') as fl:
            try:
                json_data = json.load(fl)
                try:
                    dev_web = json_data['developerWebsite']
                    return_item = {'app_id':app_id,'dev_web':dev_web}
                    if return_item not in return_meta:
                        return_meta.append(return_item)
                        # print(line['name'],line['value'])

                except IndexError:
                    # print('empty entries')
                    return_meta.append({'app_id':app_id,'dev_web':'website unavailable'})
            except :
                return_meta.append({'app_id':app_id,'dev_web':'metadata unavailable'})
    except :
        return_meta.append({'app_id':app_id,'dev_web':'file unavailable'})


    return return_meta

def listing_app(app_list_path):
    app_list=[]
    with open (app_list_path,'r') as fl:
        for line in fl:
            app_list.append(line.strip())
    return app_list


def main():

    dev_web_list=[]
    empty_dev_web_list=[]
    contained_dev_web_list=[]
    app_list = listing_app(list_app_path)
    for item in app_list:
        print("extracting --> " + item)
        dev_web = extract_dev_web(metadata_path,item)
        for item in dev_web:
            dev_web_list.append(item)
            if 'unavailable' in item['dev_web']:
                empty_dev_web_list.append(item)
            else:
                contained_dev_web_list.append(item)

    dev_web_df = pd.DataFrame(dev_web_list)
    dev_web_write_path = report_path+'all_dev_web.csv'
    dev_web_df.to_csv(dev_web_write_path,index=False)

    empty_dev_web_df = pd.DataFrame(empty_dev_web_list)
    empty_dev_web_write_path = report_path+'empty_dev_web.csv'
    empty_dev_web_df.to_csv(empty_dev_web_write_path,index=False)

    contained_dev_web_df = pd.DataFrame(contained_dev_web_list)
    contained_dev_web_write_path = report_path+'contained_dev_web.csv'
    contained_dev_web_df.to_csv(contained_dev_web_write_path,index=False)

if __name__=='__main__':
    main()