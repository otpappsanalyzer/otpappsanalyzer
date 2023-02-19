import os
import pandas as pd
import csv

api_app_path = '/home/budi/OTP_project/OTP_code/root_detection/androguard_api_classes.csv'
report_path = '/home/budi/OTP_project/OTP_code/root_detection/'

def pct(D):
    N = 182 # OTP apps number
    ret = round((D/N)*100,2)
    return ret

def group_root_api(data_path,report_path):
    api_app_df = pd.read_csv(data_path,index_col=False)
    non_root = ['BiometricManager','BiometricPrompt','FingerprintManager','BiometricService','FingerprintService',
        'KeyStore.getInstance','isStrongBoxBacked','StrongBoxUnavailableException','isInsideSecureHardware',
        'SafetyNet.getClient','Os.stat']
    api_app_df = api_app_df[~api_app_df['api_flag'].isin(non_root)]
    api_app_df["value"]=1
    df_trans = pd.pivot_table(api_app_df, values="value", index=["app_id"], columns="api_flag", fill_value=0).reset_index()  
    df_trans.reset_index()
    df_trans['sum'] = df_trans.sum(axis=1)
    df_trans = df_trans.sort_values(['sum'],ascending=False)
    print(df_trans)

    to_write = report_path+'root_api_per_app.csv'
    df_trans.to_csv(to_write,index=False)

    sum_path = report_path+'sum_root_api_usage.txt'
    sum_root_df = df_trans.groupby(['sum'])['sum'].count().reset_index(name='count').sort_values(by=['sum'],ascending=False) 
    # print(sum_root_df)
    with open (sum_path,'w') as fl:
        fl.write('#of Strategy  & #of Apps (\%) \\\ \n' )
        for i,line in sum_root_df.iterrows():
            pct_item = pct(line['count'])
            fl.write( str(line['sum']) +'  & '+ str(line['count']) +'(' +str(pct_item) +'\%) \\\ \n')

def main():
    group_root_api(api_app_path,report_path)

if __name__=='__main__':
    main()