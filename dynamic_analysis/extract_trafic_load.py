import json
import os
import pandas as pd


# app_list = {'com.dreammirae.otp.android.mirae.multiid.market','cy.nbg.nbgcyotp'}
# har_path = '/home/budi/OTP_project/har_file/'
har_path = '/home/budi/OTP_project/new_har_file/'
list_app_path = '/home/budi/OTP_project/OTP_code/metadata/csv_apk_id.csv'
report_path = '/home/budi/OTP_project/OTP_code/dynamic_analysis/report/'

def extract_load(har_path,app_id):
    app_har_path = har_path+app_id+'.har'
    return_load=[]
    print(app_har_path)
    with open(app_har_path,'r') as fl:
        json_data = json.load(fl)
        entries = json_data['log']['entries']
        try:
            header_load = entries[0]['request']['headers'] 
            for line in header_load:
                header_item = {'app_id':app_id,'request_comp':'header','name':line['name'],'value':line['value']}
                if header_item not in return_load:
                    return_load.append(header_item)
                # print(line['name'],line['value'])

            query_load = entries[0]['request']['queryString']
            for line in query_load:
                query_item = {'app_id':app_id,'request_comp':'queryString','name':line['name'],'value':line['value']}
                if query_item not in return_load:
                    return_load.append(query_item)
                    # print(line['name'],line['value'])


        except IndexError:
            # print('empty entries')
            return_load.append(app_id)

    return return_load

def listing_app(app_list_path):
    app_list=[]
    with open (app_list_path,'r') as fl:
        for line in fl:
            app_list.append(line.strip())
    return app_list

def check_har(har_path,app_id):
    for roots, folders, files in os.walk(har_path):
        har_file = app_id+'.har'
        if har_file in files:
            return True
        else:
            return False

def main():

    app_list = listing_app(list_app_path)
    # print(app_list)

    no_har = []
    empty_load =[]
    app_load_list=[]
    for item in app_list:
        har_status = check_har(har_path,item)
        if har_status == True:
            print("extracting --> " + item)
            app_load = extract_load(har_path,item)
            for load in app_load:
                if load ==item:
                    empty_load.append(item)
                    # print('This is return empty load')
                else:
                    app_load_list.append(load)
                    # print(load)
        else:
            no_har.append(item)

    print(len(no_har))
    empty_load_df = pd.DataFrame(empty_load)
    # empty_write_path = report_path + 'empty_load.csv'
    empty_write_path = report_path + 'new_empty_load.csv'
    empty_load_df.to_csv(empty_write_path,index=False)

    app_load_df = pd.DataFrame(app_load_list)
    # load_write_path = report_path+ 'app_containing_load.csv'
    load_write_path = report_path+ 'new_app_containing_load.csv'
    app_load_df.to_csv(load_write_path,index=False)

if __name__=='__main__':
    main()