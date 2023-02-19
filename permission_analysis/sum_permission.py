import pandas as pd
from pandas.core.reshape.merge import merge 

perm_source = '/home/budi/OTP_project/OTP_code/permission_analysis/permission_result.csv'
report_path = '/home/budi/OTP_project/OTP_code/permission_analysis/'

def count_per_perm_name(source,report_path):
    df_perm = pd.read_csv(source)
    df_perm = df_perm[['permission','status','info']]
    # print(df_perm)
    count_perm = df_perm.groupby(['permission'])['permission'].count().reset_index(name='count').sort_values(by=['count'],ascending=False)
    # print(count_perm)
    df_ref = df_perm.drop_duplicates()
    # print(df_ref)
    df_merge = merge(count_perm,df_ref,left_on='permission',right_on='permission',how='left')
    df_merge = df_merge.sort_values(by=['status','count'],ascending=False)
    print(df_merge)

    write_path = report_path+'permission_sum_per_name.csv'
    df_merge.to_csv(write_path,index=False)

def count_per_app(detail_path,report_path):
    
    df_perm_detail = pd.read_csv(detail_path)
    df_sum_app = df_perm_detail.groupby(['file_name','status'])['status'].count().unstack().reset_index()
    # print(df_sum_app)
    perm_sum_per_app_path = report_path+'permission_sum_per_app.csv'    
    df_sum_app.to_csv(perm_sum_per_app_path)

    """Summarizing permission per access level"""
    df_sum_total = df_perm_detail.groupby(['status'])['status'].count().reset_index(name='count')
    print(df_sum_total)
    perm_sum_total = report_path+'permission_sum_total.csv'
    df_sum_total.to_csv(perm_sum_total)


def main():
    count_per_perm_name(perm_source,report_path)
    count_per_app(perm_source,report_path)
if __name__=='__main__':
    main()    