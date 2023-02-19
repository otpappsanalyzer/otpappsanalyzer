import os
import pandas as pd
from pandas.core.indexes.base import Index
from pandas.io.parsers import read_csv

failured_source = '/home/budi/OTP_project/OTP_code/privacy_policy/report/failed_to_extract.txt'
report_path = '/home/budi/OTP_project/OTP_code/privacy_policy/report/failed_to_extract_sum.txt'

def check_failure(source,dest):
    failured_df = pd.read_csv(source,sep=',')
    print(failured_df)
    failured_df['count']=failured_df['count'].astype(int)
    with open(dest,'w') as fl:      
        for x,item in failured_df.iterrows():
            pct_x = pct(item['count'])
            fl.write(str(x+1)+' & '+item[0]+' & '+ str(item['count'])+' ('+str(pct_x)+'\%) \\\ \n')
            print(x+1,item[0],item[1],pct_x)

def pct(x):
    n = 182
    res = round((x/n)*100,1)
    return res

def main():
    check_failure(failured_source,report_path)

if __name__=='__main__':
    main()