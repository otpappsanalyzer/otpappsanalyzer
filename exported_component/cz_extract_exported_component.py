import pandas as pd
from manifest_extractor import permission_ex
from manifest_extractor import exported_activity_ex, exported_service_ex, exported_receiver_ex, exported_provider_ex
from manifest_extractor import activity_ex, service_ex, receiver_ex, provider_ex
import os


decomp_path = '/media/budi/Seagate Expansion Drive/OTP_project/decompiled_app/'
app_list = '/home/budi/OTP_project/OTP_code/metadata/csv_apk_id.csv'
report_path = '/home/budi/OTP_project/OTP_code/exported_component/'


def exported_component_summarize(apps_list,decompiled_path,report_path):
    component_list=[]
    with open(apps_list,'r') as app_list:
        for item in app_list:
            item = item.strip('\n')
            manifest_path = decompiled_path+item+'/AndroidManifest.xml'
            print('Checking Exported Component : '+item)
            mfs_status = check_manifest(manifest_path)
            if mfs_status == True:
                ex_act_list = exported_activity_ex(manifest_path)
                for e_act in ex_act_list:
                    component_list.append({'app_id':item,'com_type':'exp_activity','act_name':e_act}) 
                ex_serv_list = exported_service_ex(manifest_path)
                for e_serv in ex_serv_list:
                    component_list.append({'app_id':item,'com_type':'exp_service','act_name':e_serv}) 
                ex_rec_list = exported_receiver_ex(manifest_path)
                for e_rec in ex_rec_list:
                    component_list.append({'app_id':item,'com_type':'exp_receiver','act_name':e_rec}) 
                ex_prov_list = exported_provider_ex(manifest_path)
                for e_prov in ex_prov_list:
                    component_list.append({'app_id':item,'com_type':'exp_provider','act_name':e_prov}) 
                act_list = activity_ex(manifest_path)
                for act in act_list:
                    component_list.append({'app_id':item,'com_type':'activity','act_name':act}) 
                serv_list = service_ex(manifest_path)
                for serv in serv_list:
                    component_list.append({'app_id':item,'com_type':'service','act_name':serv}) 
                rec_list = receiver_ex(manifest_path)
                for rec in rec_list:
                    component_list.append({'app_id':item,'com_type':'receiver','act_name':rec}) 
                prov_list = provider_ex(manifest_path)
                for prov in prov_list:
                    component_list.append({'app_id':item,'com_type':'provider','act_name':prov}) 
    
    
    """ Summarizing detail component analysis"""
    file_sufix = apps_list.split('/')
    file_sufix=file_sufix[-1]
    exp_comp_detail_path = report_path+'cz_exported_component_detail_'+file_sufix
    write_to_csv(component_list,exp_comp_detail_path)

    """Summarizing exported component per apps"""
    df_comp = pd.DataFrame(component_list)
    exp_comp_sum = df_comp.groupby(['app_id','com_type'])['com_type'].count().unstack().reset_index()
    exp_comp_sum['pct_exp_act'] = round((exp_comp_sum['exp_activity']/exp_comp_sum['activity']),2)
    exp_comp_sum['pct_exp_serv'] = round((exp_comp_sum['exp_service']/exp_comp_sum['service']),2)
    exp_comp_sum['pct_exp_rec'] = round((exp_comp_sum['exp_receiver']/exp_comp_sum['receiver']),2)
    exp_comp_sum['pct_exp_prov'] = round((exp_comp_sum['exp_provider']/exp_comp_sum['provider']),2)
    exp_comp_sum_path = report_path+'cz_exported_component_sum_per_app_'+file_sufix
    write_to_csv(exp_comp_sum,exp_comp_sum_path)
    print(exp_comp_sum)

    """Summarizing exported component per component"""
    exp_comp_total = df_comp.groupby(['com_type'])['com_type'].count().reset_index(name='count')
    exp_comp_total_path = report_path+'cz_exported_component_total_'+file_sufix
    write_to_csv(exp_comp_total,exp_comp_total_path)
    # print(exp_comp_total)
    return component_list

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


def main():
    exported_component_summarize(app_list,decomp_path,report_path)

if __name__=="__main__":
    main()