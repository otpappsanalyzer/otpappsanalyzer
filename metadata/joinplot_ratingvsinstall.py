import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

meta_path = '/home/budi/OTP_project/OTP_code/metadata/sum_metadata.csv'

bins = [0,5000,10000,50000,100000,500000,1000000,5000000,10000000,50000000]
labels = ['0-5K','5K-10K','10K-50K','50K-100K','100K-500K','500K-1M','1M-5M','5M-10M','10M-100M']
meta_df = pd.read_csv(meta_path)
meta_df = meta_df[['install','score']]
meta_df = meta_df.replace({'error':0})
meta_df = meta_df[~meta_df['score'].isin(['0.0','error'])]
meta_df = meta_df.astype({'install':'int64','score':'float'})
# meta_df['score'] = meta_df['install'].round(0)

meta_df['install_bin'] = pd.cut(meta_df['install'],bins=bins,labels=labels)
meta_df['install_bin'] = meta_df['install_bin'].astype('string')
meta_df = meta_df.sort_values(by=['install'])
# meta_df = meta_df.round({'score':0})
print(meta_df)
g = sns.jointplot(data=meta_df,x='install_bin',y='score',marginal_ticks=True,  height=5, ratio=3 )
g.fig.set_figwidth(8)
g.fig.set_figheight(4)

for tick in g.ax_joint.get_xticklabels():         
    tick.set_rotation(30)

g.ax_joint.set_xlabel('# of Downloads', fontweight='bold',size=14)
g.ax_joint.set_ylabel('Avg. Ratings', fontweight='bold',size=14)
plt.tight_layout()
plt.show()