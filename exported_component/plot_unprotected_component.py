import pandas as pd 
import numpy as np
import statsmodels.api as sm # recommended import according to the docs
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import seaborn as sns



unprotected_data_path = '/home/budi/OTP_project/OTP_code/exported_component/unprotected_component.csv'
app_list = '/home/budi/OTP_project/OTP_code/metadata/csv_apk_id.csv'
exp_path = '/home/budi/OTP_project/OTP_code/exported_component/'


unprotected_df =pd.read_csv(unprotected_data_path)
# print(unprotected_df)

vulnerable_df = unprotected_df.groupby(['app_id','vulnerable']).size().reset_index(name='count')
vulnerable_df = vulnerable_df.pivot(index='app_id',columns='vulnerable',values='count').reset_index().fillna(0)
vulnerable_df = vulnerable_df.reindex(columns = ['app_id', 'Unprotected exported component','Unprotected intent-filter'])

original_df = pd.read_csv(app_list,header=None,names=['app_id'])
# print(original_df)

merge_df = original_df.merge(vulnerable_df,left_on='app_id',right_on='app_id',how='left').fillna(0)
# print(merge_df)

df = vulnerable_df[['Unprotected exported component','Unprotected intent-filter']].rename({'Unprotected exported component':'X','Unprotected intent-filter':'Y'},axis=1)
# print(df)

x_values = list(df['X'])
x_values = [i for i in x_values if i != 0]
y_values = list(df['Y'])
y_values = [i for i in y_values if i != 0]

print(x_values)

bins = np.linspace(1, 25, 25)

fig = plt.figure(figsize=(6,2.5))
counts,edges,bars = plt.hist([x_values, y_values], bins, label=['Unprotected exported component', 'Unprotected intent-filter'])
plt.ylabel("# of Apps",size=14)
plt.xlabel("# of Vulnerable Components",size=14)

plt.legend(loc='upper right')
plt.tight_layout()
plt.show()
write_path = exp_path+'histogram_vulnerable_component.pdf'
fig.savefig(write_path)

# percentiles = np.array([25,50 , 85])
# unprotect_export = merge_df['Unprotected exported component']
# exp_ecdf = sm.distributions.ECDF(unprotect_export) 
# exp_x = np.linspace(min(unprotect_export), max(unprotect_export))
# exp_y = exp_ecdf(exp_x)
# exp_val = np.percentile(unprotect_export, percentiles)

# unprotected_intent = merge_df['Unprotected intent-filter']
# intent_ecdf = sm.distributions.ECDF(unprotect_export) 
# intent_x = np.linspace(min(unprotected_intent), max(unprotected_intent))
# intent_y = intent_ecdf(intent_x)
# intent_val = np.percentile(unprotected_intent, percentiles)


# fig = plt.figure(figsize=(5,4))
# ax = fig.gca()
# ax.xaxis.set_major_locator(MaxNLocator(integer=True))
# plt.plot(exp_x, exp_y*100, marker='o', lw = 2, color='red')
# plt.plot(intent_x, intent_y*100, marker='^', lw = 2, color='green')
# # plt.xlim(0,max(cst_x))
# # plt.ylim(0,max(cst_y)*100)
# plt.legend(("Unprotected Exported Component", "Unprotected Intent-Filter"))
# # plt.rc('axes', labelsize=18)
# # plt.rc('legend', fontsize=18) 
# plt.xlabel('# of Exported Component', size = 14)
# plt.ylabel('CDF', size = 14)
# plt.tight_layout()
# # fig.savefig(write_path)
# plt.show()



# fig = plt.figure(figsize=(5,4))
# ax = fig.gca()
# ax.xaxis.set_major_locator(MaxNLocator(integer=True))
# plt.plot(exp_x, exp_y*100, marker='o', lw = 2, color='red')
# plt.plot(intent_x, intent_y*100, marker='^', lw = 2, color='green')
# # plt.xlim(0,max(cst_x))
# # plt.ylim(0,max(cst_y)*100)
# plt.legend(("Unprotected Exported Component", "Unprotected Intent-Filter"))
# # plt.rc('axes', labelsize=18)
# # plt.rc('legend', fontsize=18) 
# plt.xlabel('# of Exported Component', size = 14)
# plt.ylabel('CDF', size = 14)
# plt.tight_layout()
# # fig.savefig(write_path)
# plt.show()
