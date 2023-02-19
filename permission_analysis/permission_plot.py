import pandas as pd
from pandas.io.parsers import read_csv 
import numpy as np
import statsmodels.api as sm # recommended import according to the docs
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


permission_sum_per_app_path = '/home/budi/OTP_project/OTP_code/permission_analysis/permission_sum_per_app.csv'
write_path = '/home/budi/OTP_project/OTP_code/permission_analysis/'

def permission_plot(file,write_path):
    percentiles = np.array([25,50 , 85])
    perm = pd.read_csv(file)
    perm=perm.fillna(0)
    perm = perm.astype({'dangerous':'int64','normal':'int64','signature':'int64','unknown':'int64','signatureOrSystem':'int64'})
    print(perm)

    dangerous = perm['dangerous']
    dgr_ecdf = sm.distributions.ECDF(dangerous) 
    dgr_x = np.linspace(min(dangerous), max(dangerous))
    dgr_y = dgr_ecdf(dgr_x)
    dgr_val = np.percentile(dangerous, percentiles)

    normal = perm['normal']
    nrm_ecdf = sm.distributions.ECDF(normal) 
    nrm_x = np.linspace(min(normal), max(normal))
    nrm_y = nrm_ecdf(nrm_x)
    nrm_val = np.percentile(normal, percentiles)

    signature = perm['signature']
    sgt_ecdf = sm.distributions.ECDF(signature) 
    sgt_x = np.linspace(min(signature), max(signature))
    sgt_y = sgt_ecdf(sgt_x)
    sgt_val = np.percentile(signature, percentiles)

    customized = perm['unknown']
    cst_ecdf = sm.distributions.ECDF(customized) 
    cst_x = np.linspace(min(customized), max(customized))
    cst_y = cst_ecdf(cst_x)
    cst_val = np.percentile(customized, percentiles)

    fig = plt.figure(figsize=(6,2.5))
    ax = fig.gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.plot(dgr_x, dgr_y*100, marker='o', lw = 2, color='red')
    plt.plot(nrm_x, nrm_y*100, marker='^', lw = 2, color='green')
    plt.plot(sgt_x, sgt_y*100, marker='s', lw = 2, color='blue')
    plt.plot(cst_x, cst_y*100, marker='X', lw = 2, color='orange')
    plt.xlim(0,max(cst_x))
    plt.ylim(0,max(cst_y)*100)
    plt.legend(("Dangerous", "Normal","Signature","Customized"))
    # plt.rc('axes', labelsize=18)
    # plt.rc('legend', fontsize=18) 
    plt.xlabel('# of Permissions', size = 14)
    plt.ylabel('ECDF', size = 14)
    plt.tight_layout()
    plt.tight_layout()
    fig.savefig(write_path)
    plt.show()


def main():
    perm_plot = write_path+'permission.pdf'
    permission_plot(permission_sum_per_app_path,perm_plot)



if __name__=='__main__':
    main()