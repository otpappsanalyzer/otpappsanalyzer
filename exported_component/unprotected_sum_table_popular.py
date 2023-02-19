import pandas as pd
import numpy as np


unprotected_data_path = '/home/budi/OTP_project/OTP_code/exported_component/unprotected_component.csv'
write_path = '/home/budi/OTP_project/OTP_code/exported_component/unprotected_sum_popular.txt'
top_install_path = '/home/budi/OTP_project/OTP_code/metadata/top_install.csv'

def pct(x):
    N = 182
    ret = round(((x/N)*100),2)
    return ret

def find_app_number(df, vulnerable,comp_type,popular):
    print(df)
    print ('------->',vulnerable,'-------------',comp_type,'----------------',popular)
    for i,row in df.iterrows():
        print(row['vulnerable'],'====',row['comp_type'],'=======',row['popular'])
        if row['vulnerable'] == vulnerable and row['comp_type']==comp_type and row['popular'] == popular:
        # if row['vulnerable'] == vulnerable and row['comp_type']==comp_type:
            # print('+++++++++++++++++++++'+row['no_app'])
            return row['no_app']

unprotected_df = pd.read_csv(unprotected_data_path)

pop_df = pd.read_csv(top_install_path)

result_df = unprotected_df.merge(pop_df, left_on='app_id',right_on='appId',how='left')
result_df['popular'] = np.where(result_df['appId']==result_df['app_id'],True,False)
result_df = result_df[["app_id","vulnerable","comp_type",'popular']]
# print(result_df)

# to find number of component group by vulnerability, component type and popular status
no_comp_group = result_df.groupby(["vulnerable","comp_type",'popular']).size().reset_index(name="no_comp")
# print(no_comp_group)

# to find number of apps group by vulnerability, component type and popular status
per_id_group = result_df.groupby(['app_id',"vulnerable","comp_type",'popular']).size().reset_index(name="no_comp")
no_app_group = per_id_group.groupby(["vulnerable","comp_type",'popular']).size().reset_index(name="no_app")
# print(no_app_group)


# no_app_group = result_df.groupby(["vulnerable","comp_type",'popular']).size().reset_index(name="no_comp")
# print(type_group)


with open (write_path,'w') as fl:
    fl.write('Vulnerability & Component Type & Popular & # of component & # of apps (\%) \\\ \n' )
    for x,line in no_comp_group.iterrows():
        vuln = line['vulnerable']
        comp_type = line['comp_type']
        popular = line['popular']

        no_app = find_app_number(no_app_group,vuln,comp_type,popular)
        pct_app = pct(no_app)

        fl.write( vuln+ ' & ' + comp_type + ' & ' + str(popular) + ' & ' + str(line['no_comp'])+ ' & ' + str(no_app) +'(' +str(pct_app)+'\%)'+ '\\\ \n')