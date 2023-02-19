"""This script is use to find anti analysis technique from the result of MOBSF
"""

import os 
import json
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np

package_path = '/home/budi/OTP_project/OTP_code/package_analysis/'
csv_file = package_path+'custom_detail_apkid.csv'

package_df = pd.read_csv(csv_file)
# print(package_df)

compiler_list=[]
noncompiler_list=[]
for index,row in package_df.iterrows():
    # print(row[2])
    if row[2]=='compiler':
        compiler_list.append({'file_name':row[0],'classes':row[1],'compiler':row[3]})
        # if row[0] not in compiler_list:
        #     compiler_list.append({'file_name':row[0],'compiler':row[3]})
    else:
        noncompiler_list.append({'file_name':row[0],'classes':row[2],'component':row[3]})

compiler_df = pd.DataFrame(compiler_list)
print(compiler_df)
compiler_csv = package_path+'compiler_list.csv'
compiler_df.to_csv(compiler_csv,index=False)

noncompiler_df = pd.DataFrame(noncompiler_list)
noncompiler_df=noncompiler_df.drop_duplicates()

noncompiler_csv = package_path+'noncompiler_list.csv'
noncompiler_df.to_csv(noncompiler_csv,index=False)

noncompiler_df=noncompiler_df[['file_name','classes']]
noncompiler_df=noncompiler_df.drop_duplicates()
print(noncompiler_df)

dest_fig = '/home/budi/OTP_project/OTP_code/package_analysis/anti_analysis.pdf'
by_component = noncompiler_df.groupby(['classes'])['classes'].count().reset_index(name='adopting').sort_values(by=['adopting'],ascending=False)
apps_number = 182
by_component['not adopting'] = apps_number - by_component['adopting']
print(by_component) 

by_component.plot.barh(x='classes',y='adopting',width=0.9,figsize=(5,4))
plt.axis('tight')
plt.xticks(rotation=0)
plt.ylabel('Mechanism')
plt.xlabel('# of Apps')
# plt.legend(bbox_to_anchor=(0.4, 1), loc='upper left')
plt.savefig(dest_fig)
plt.tight_layout()
plt.show()
# by_component.plot(
#   x = 'classes', 
#   kind = 'barh', 
#   stacked = True, 
# #   title = 'Percentage of Anti-Analysis Adoption', 
#   mark_right = True,
#   figsize = (5,3.5))
  
# df_total = by_component["adopting"] + by_component["not adopting"] 
# df_rel = by_component[by_component.columns[1:]].div(df_total, 0)*100
  
# for n in df_rel:
#     for i, (cs, ab, pc) in enumerate(zip(by_component.iloc[:, 1:].cumsum(1)[n], 
#                                          by_component[n], df_rel[n])):
#         plt.text(cs - ab / 2, i, str(np.round(pc, 1)) + '%', 
#                  va = 'center', ha = 'center',size=7)
# plt.legend(loc="upper left",bbox_to_anchor=(0.55,1),prop={"size":10})
# plt.xlabel('# of Apps (N = 182)')
# plt.ylabel('Mechanism')
# plt.tight_layout()
# plt.show()