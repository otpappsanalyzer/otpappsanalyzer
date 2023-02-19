"""
    This script is used to scrap metatadat per Id
"""

import os
import json
import pandas as pd
import csv

node_js_path = '/home/budi/crypto_project/crypto_code/apps_screening/'
selected_app_id = '/home/budi/OTP_project/OTP_code/metadata/csv_apk_id.csv'
comment_folder = '/home/budi/OTP_project/comment_result/'
comment_file = '/home/budi/OTP_project/OTP_code/user_review/comment_file.csv'

def scrap_comment_js (app_id, nodejs_path,result_path):
    print('Change directory to node js')
    current_dir = os.getcwd()
    os.chdir(nodejs_path)
    print('Scraping apps metadata Per Id : '+app_id)
    os.system('node comment_scraper.js '+app_id+' '+result_path)
    os.chdir(current_dir)

def encode_metadata(app_id,res_path):
    """Read JSON reasult from the scrape result folder"""
    app_id_res = res_path+app_id+'.txt'
    print(app_id_res)
    item_dict=[]
    try:
        with open(app_id_res,'r') as app_metadata:
            data=app_metadata.read()
            # print(data)
            json_data = json.loads(data)
            for x,item in enumerate(json_data['data']):              
                user_name = item['userName'] if 'userName' in item else None 
                star = item['score'] if 'score' in item else None
                comment = item['text'] if 'text' in item else None
                # print(x, item['userName'],item['text'])

                item_dict.append({'appId':app_id, 'star':star,'comment':comment}) 
    except IOError:
        item_dict.append({'appId':app_id,'star':'error',
            'comment':'error'})        
    return item_dict

def check_existing_result(result_path):
    file_list=[]
    for root,dirs,files in os.walk(result_path):
        for file in files:
            file_list.append(file.rstrip('.txt'))

    return(file_list)
def main():

    existing_result = check_existing_result(comment_folder) 
    # print(existing_result)
    
    aps_list=[]
    with open(selected_app_id,'r') as app_id:
        for x,item in enumerate(app_id):           
            item_id = item.strip('\n')
            print(x,item_id)
            if item_id in existing_result:
                print('Comment of this apps already downloaded')
            else:
                print('Download '+item_id)
                scrap_comment_js(item_id,node_js_path,comment_folder)

            res_metadata=encode_metadata(item_id,comment_folder)
            for item in res_metadata:
                # print(item)
                aps_list.append(item)

    metadata_df = pd.DataFrame(aps_list)
    # print(metadata_df)
    metadata_df.to_csv(comment_file)


if __name__ == "__main__":
    main()
