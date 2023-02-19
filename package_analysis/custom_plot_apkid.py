import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

nc_path = '/home/budi/OTP_project/OTP_code/package_analysis/custom_detail_apkid.csv'
plot_path =  '/home/budi/OTP_project/OTP_code/package_analysis/binary_protection.pdf'
nc_df = pd.read_csv(nc_path)
type_list = []
for x, line in nc_df.iterrows():
    type = line['types'] 
    if 'anti_vm' in type or 'anti_debug' in type or 'packer' in type or 'obfuscator' in type or 'anti_disassembly':
        type_list.append({'app_id':line['app_name'],'types':type})

type_df = pd.DataFrame(type_list)
type_df = type_df.drop_duplicates()
# print(type_df)

N = 182
by_type_df = type_df.groupby(['types']).size().reset_index(name='Adopting').sort_values(by=['Adopting'],ascending=False)
by_type_df = by_type_df[by_type_df['types'].str.contains('compiler|manipulator') == False]
by_type_df['Not_adopting'] = N - by_type_df['Adopting']
print(by_type_df)

  
  
# plot a Stacked Bar Chart using matplotlib
by_type_df.plot(
  x = 'types', 
  kind = 'barh', 
  stacked = True, 
#   title = 'Percentage Stacked Bar Graph', 
  mark_right = True,
  figsize=(5,3)
 )
  

df_total = N
df_rel = by_type_df[by_type_df.columns[1:]].div(df_total, 0) * 100

# print(df_rel)  

for n in df_rel:
    for i, (cs, ab) in enumerate(zip(by_type_df.iloc[:, 1:].cumsum(1)[n], 
    # for i, (cs, ab,pc) in enumerate(zip(by_type_df.iloc[:, 1:].cumsum(1)[n], 
                                         by_type_df[n])):
                                        #  by_type_df[n], df_rel[n])):
        # plt.text(cs - ab / 2, i, str(np.round(pc, 1)) + '%', 
        plt.text(cs - ab / 2, i, str(ab), 
                 va = 'center', ha = 'center', fontsize = 8)
plt.ylabel("Binary Protection Type")
plt.xlabel("# of Apps")
plt.tight_layout()
plt.savefig(plot_path)
plt.show()


# df_total = N
# df_rel = by_type_df[by_type_df.columns[1:]].div(df_total, 0) * 100

# print(df_rel)  


# for n in df_rel:
#     for i, (cs, ab) in enumerate(zip(by_type_df.iloc[:, 1:].cumsum(1)[n], 
#     # for i, (cs, ab,pc) in enumerate(zip(by_type_df.iloc[:, 1:].cumsum(1)[n], 
#                                          by_type_df[n])):
#                                         #  by_type_df[n], df_rel[n])):
#         # plt.text(cs - ab / 2, i, str(np.round(pc, 1)) + '%', 
#         plt.text(cs - ab / 2, i, str(np.round(cs, 1)), 
#                  va = 'center', ha = 'center', rotation = 20, fontsize = 8)

# plt.show()