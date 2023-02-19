"""
    This script is used to scrap metatadat per Id
"""

import os
import json
import pandas as pd
import csv

node_js_path = '/home/budi//OTP_project/OTP_code/apps_screening/'
selected_app_id = '/home/budi/OTP_project/OTP_code/metadata/csv_apk_id.csv'
selected_metadata = '/home/budi/OTP_project/metadata_result/' # the file size is too big to upload to github, please contact author after publication
# sum_metadata_file = '/home/budi/OTP_project/OTP_code/metadata/sum_metadata.csv'
sum_metadata_file = '/home/budi/OTP_project/OTP_code/metadata/sum_metadata_next.csv'
apps_not_found = '/home/budi/OTP_project/OTP_code/metadata/metadata_not_found.csv'

def scrap_metadata_js (app_id, node_js_path,result_path):
    print('Change directory to node js')
    current_dir = os.getcwd()
    os.chdir(node_js_path)
    print('Scraping apps metadata Per Id : '+app_id)
    os.system('node metadata_scraper_per_id.js '+app_id+' '+result_path)
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
            app_id = json_data['appId'] if 'appId' in json_data else None
            app_title = json_data['title']
            score = json_data['scoreText'] if 'scoreText' in json_data else None
            rating =  json_data['ratings']if 'ratings' in json_data else None
            review = json_data['reviews'] if 'reviews' in json_data else None
            comment = json_data['comments'] if 'comments' in json_data else None
            priceT = json_data['priceText'] if 'priceText' in json_data else None
            install = json_data['minInstalls'] if 'minInstalls' in json_data else None
            genre = json_data['genreId'] if 'genreId' in json_data else None
            developer = json_data['developer'] if 'developer' in json_data else None
            release = json_data['released'] if 'released' in json_data else None
            email = json_data['developerEmail'] if 'developerEmail' in json_data else None
            

            item_dict = {'appId':app_id, 'title':app_title,
            'score': score,'rating': rating,'review': review,'comment':comment,
            'priceT':priceT,'install':install,'genre':genre,'developer':developer,
            'release':release,'email':email}
    except IOError:
        item_dict={'appId':app_id,'title':'error',
            'score': 'error','rating': 'error','review': 'error','comment':'error',
            'priceT':'error','install':'error','genre':'error','developer':'error',
            'release':'error','email':'error'}
    return item_dict

def check_existing_result(result_path):
    file_list=[]
    for root,dirs,files in os.walk(result_path):
        for file in files:
            file_list.append(file.rstrip('.txt'))

    return(file_list)


def main():
    existing_list = check_existing_result(selected_metadata)
    aps_list=[]
    error_list = []
    with open(selected_app_id,'r') as app_id:
        for item in app_id:           
            item_id = item.strip('\n')
            print(item_id)
            if item_id not in existing_list:
                scrap_metadata_js(item_id,node_js_path,selected_metadata)
            res_metadata=encode_metadata(item_id,selected_metadata)
            # print(res_metadata)
            aps_list.append(res_metadata)
            if res_metadata['title'] == 'error':
                error_list.append(res_metadata)
            # res_metadata=encode_metadata('com.bixin.bixin_android',selected_metadata)
            # print(res_metadata)

    metadata_df = pd.DataFrame(aps_list)
    print(metadata_df)
    metadata_df.to_csv(sum_metadata_file)

    error_df = pd.DataFrame(error_list)
    print(error_df)
    error_df.to_csv(apps_not_found)

if __name__ == "__main__":
    main()
