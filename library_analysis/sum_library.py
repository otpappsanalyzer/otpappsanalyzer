from library_extractor import check_lib
import os
import pandas as pd

decompiled_path = "/media/budi/Seagate Expansion Drive/OTP_project/decompiled_app/"
report_path = '/home/budi/OTP_project/OTP_code/library_analysis/'
apk_path = '/home/budi/OTP_project/apk_list'

def third_party_lib_summarize(apk_path,decompiled_path,report_path):
    third_party_lib_list=[]
    not_found_folder=[]
    for roots,dirs,files in os.walk(apk_path):
        for file in files:
            apk_path = roots+ file
            app_id = file.rstrip('apk')
            app_id = app_id.rstrip('.')
            check_res = check_folder(decompiled_path,app_id) 
            if  check_res == True:
                try:
                    folder_path = decompiled_path+app_id
                    lib_list = check_lib(folder_path)
                    for x in lib_list:
                        app_id_x = {'app_id':app_id}
                        x_item = dict(app_id_x,**x)
                        # print(x_item)
                        third_party_lib_list.append(x_item)
                except:
                    pass
            else:
                print(app_id+' Decompiled folder not found')
                not_found_folder.append(file)

    """ Summarizing detail third party libraries"""
    df_lib = pd.DataFrame(third_party_lib_list)
    print(df_lib)
    lib_detail_path = report_path+'library_detail.csv'
    df_lib.to_csv(lib_detail_path,index=False)

    """ Summarizing third party libraries per apps"""
    lib_sum_per_app_path = report_path+'library_sum_per_app.csv'
    lib_per_app = df_lib.groupby(['app_id'])[['TargetedAds','MobileAnalytics','AnyTrackingLibrary','Analytics']].sum().reset_index()
    # print(lib_per_app)
    lib_per_app.to_csv(lib_sum_per_app_path,index=False)
   
    """Summarizing third party library per name"""
    lib_per_name = df_lib.groupby(['lib_name'])['lib_name'].count().reset_index(name='count').sort_values('count',ascending=False)
    lib_per_name_path = report_path+'lib_per_name_'+file_sufix
    lib_per_name.to_csv(lib_per_name_path,index=False)
    print(lib_per_name)
    return third_party_lib_list

def check_folder(path,folder):
    print(folder)
    for roots,dirs,files in os.walk(path):
        if folder in dirs:
            return True
        else:
            return False
        del dirs[:] # delete next level of directory 

def main():
    third_party_lib_summarize(apk_path,decompiled_path,report_path)
if __name__=='__main__':
    main()