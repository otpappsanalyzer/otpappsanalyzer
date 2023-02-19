"""This script is use to find anti analysis technique from the result of MOBSF
"""

import os 
import json
import pandas as pd
import csv

result_path = '/home/budi/OTP_project/OTP_code/mobsf_analysis/mobsf_result/'
package_path = '/home/budi/OTP_project/OTP_code/package_analysis/'

package_list=[]
for rt,drs,fls in os.walk(result_path):
    for file in fls:
        file_path = rt+file
        print(file_path)
        file_name = file.rstrip('.json')
        with open(file_path,'r') as pkg_file:
            try:
                pkg_data = pkg_file.read()
                json_data = json.loads(pkg_data)
                pkg_key =  json_data['apkid']
                for line in pkg_key:
                    # print(line) 
                    for item in json_data['apkid'][line]:
                        class_name = line
                        pkg_comp = item
                        detail = json_data['apkid'][line][item]
                        # print(file_name,line,item,json_data['apkid'][line][item])                       
                        package_item = {'file_name':file_name,'class_name':class_name,'package_component':pkg_comp,'detail':detail}
                        package_list.append(package_item)
            except:
                pass

    pkg_df = pd.DataFrame(package_list)
    print(pkg_df)
    csv_file = package_path+'package_result.csv'
    pkg_df.to_csv(csv_file,index=False)

