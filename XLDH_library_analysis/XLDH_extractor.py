import os
import pandas as pd

xldh_path = '/home/budi/OTP_project/OTP_code/XLDH_library_analysis/XLDH Libraries.csv'
selected_app_id = '/home/budi/OTP_project/OTP_code/metadata/csv_apk_id.csv'
report_path = '/home/budi/OTP_project/OTP_code/XLDH_library_analysis/'
decompiled_path = "/media/budi/Seagate Expansion Drive/OTP_project/decompiled_app/"


def smali_finder(folder_path):
    smali_list = []
    for roots,dirs,files in os.walk(folder_path):
        for dir in dirs:
            if 'smali' in dir:
                smali_path = roots+'/'+dir
                smali_list.append(smali_path)
    return smali_list

def find_xldh(xldh_list,decompile_apps_path,app_id):
    smali_list = smali_finder(decompile_apps_path)
    app_with_xldh=[]
    for dir in smali_list:
        # print('smali path :' + dir)
        for roots,dirs,files in os.walk(dir):
            for sub_dir in dirs:
                path = roots+sub_dir
                # print(path)
                for lib in xldh_list:
                    # print(lib)
                    # print(lib,path)
                    if lib in path:
                        # print(lib)
                        xldh_item = {'app_id':app_id,'xldh_lib':lib}
                        # print(xldh_item)
                        if xldh_item not in app_with_xldh:
                            app_with_xldh.append(xldh_item)
    return app_with_xldh

def check_decompiled(item,decompiled_path):
    status = False
    for roots,dirs,files in os.walk(decompiled_path):
        for dir in dirs:
            if item in dirs:
                return True
    return status

def main():
    app_with_xldh=[]
    no_decompile_list=[]
    xldh_df = pd.read_csv(xldh_path)
    xldh_df = xldh_df.dropna(how='all', axis='columns')
    xldh_list = xldh_df['XLDH Library Name'].tolist()
    for x,lib in enumerate(xldh_list):
        xldh_list[x] = lib.replace('.','/')
    # print(xldh_list) 
    with open(selected_app_id,'r') as app_list:
        for item in app_list:
            item = item.strip('\n')
            print('Examining of : '+item)
            decom_status = check_decompiled(item,decompiled_path)
            if decom_status == False:
                print('Decompiled Folder Not available')
                print('Decompiling : '+item)
                no_decompile_list.append(item)
            else:
                print('Extracting XLDH of :'+item)
                decompiled_apps_path = decompiled_path+item
                xldh_res = find_xldh(xldh_list,decompiled_apps_path,item)
                for xldh_item in xldh_res:
                    app_with_xldh.append(xldh_item)
    app_xldh = pd.DataFrame(app_with_xldh)
    print(app_xldh)
    xldh_write_path = report_path+'library_xldh.csv'
    app_xldh.to_csv(xldh_write_path,index=False)

if __name__=='__main__':
    main()