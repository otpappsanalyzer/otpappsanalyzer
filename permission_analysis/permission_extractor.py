import os
import pandas as pd
from manifest_extractor import permission_ex
from permission_level import find_permission_level


selected_app_id = '/home/budi/OTP_project/OTP_code/metadata/csv_apk_id.csv'
report_path = '/home/budi/OTP_project/OTP_code/XLDH_library_analysis/'
decompiled_path = "/media/budi/Seagate Expansion Drive/OTP_project/decompiled_app/"

def check_decompiled(item,decompiled_path):
    status = False
    for roots,dirs,files in os.walk(decompiled_path):
        if item in dirs:
            return True
    return status

def check_manifest(manifest_path):
    status = False
    path = manifest_path.replace('/AndroidManifest.xml','')
    for roots,dirs,files in os.walk(path):
        if 'AndroidManifest.xml' in files:
            status = True
    return status

def write_to_csv(file_name,file_path):
    to_write = pd.DataFrame(file_name)
    to_write.to_csv(file_path,index=False)


def permission_sumarize(apps_list,decompiled_path,report_path):
    no_manifest=[]
    permission_level=[]
    with open(apps_list,'r') as app_list:
        for item in app_list:
            item = item.strip('\n')
            manifest_path = decompiled_path+item+'/AndroidManifest.xml'
            mfs_status = check_manifest(manifest_path)           
            if mfs_status == True:
                print('Extracting permission of : '+item)
                permission_list = permission_ex(manifest_path)
                permission_level_list = find_permission_level(permission_list) 
                for perm in permission_level_list:
                    perm_item = {'app_id':item,'permission':perm['permission'],'level':perm['level']}
                    permission_level.append(perm_item)
            else:
                no_manifest.append(item)
                print('No Manifest available for :'+item)
    
    """ Summarizing detail permission"""
    perm_detail_path = report_path+'permission_detail.csv'
    write_to_csv(permission_level,perm_detail_path)

    """ Summarizing permission per app"""
    df_perm_detail = pd.DataFrame(permission_level)
    df_sum_app = df_perm_detail.groupby(['app_id','level'])['level'].count().unstack().reset_index()
    # print(df_sum_app)
    perm_sum_per_app_path = report_path+'permission_sum_per_app.csv'
    write_to_csv(df_sum_app,perm_sum_per_app_path)

    """Summarizing permission per access level"""
    df_sum_total = df_perm_detail.groupby(['level'])['level'].count().reset_index(name='count')
    print(df_sum_total)
    perm_sum_total = report_path+'permission_sum_total.csv'
    write_to_csv(df_sum_total,perm_sum_total)


def main():
    permission_sumarize(selected_app_id,decompiled_path,report_path)

if __name__=='__main__':
    main()
