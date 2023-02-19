import pandas as pd
from pandas.io.parsers import read_csv 
import numpy as np
import statsmodels.api as sm # recommended import according to the docs
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


exp_sum_per_app_path = '/home/budi/OTP_project/OTP_code/exported_component/cz_exported_component_sum_per_app_csv_apk_id.csv'
write_path = '/home/budi/OTP_project/OTP_code/exported_component/'

def exp_plot(file,write_path):
    percentiles = np.array([25,50 , 85])
    exp = pd.read_csv(file)
    exp=exp.fillna(0)
    exp = exp[["app_id","exp_activity","exp_provider","exp_service","exp_receiver"]]
    # perm = perm.astype({'dangerous':'int64','normal':'int64','signature':'int64','unknown':'int64','signatureOrSystem':'int64'})
    
    print(exp)

    exp_act = exp['exp_activity']
    act_ecdf = sm.distributions.ECDF(exp_act) 
    act_x = np.linspace(min(exp_act), max(exp_act))
    act_y = act_ecdf(act_x)
    act_val = np.percentile(exp_act, percentiles)

    exp_serv = exp['exp_service']
    serv_ecdf = sm.distributions.ECDF(exp_serv) 
    serv_x = np.linspace(min(exp_serv), max(exp_serv))
    serv_y = serv_ecdf(serv_x)
    serv_val = np.percentile(exp_serv, percentiles)

    exp_rec = exp['exp_receiver']
    rec_ecdf = sm.distributions.ECDF(exp_rec) 
    rec_x = np.linspace(min(exp_rec), max(exp_rec))
    rec_y = rec_ecdf(rec_x)
    rec_val = np.percentile(exp_rec, percentiles)

    exp_prov = exp['exp_provider']
    prov_ecdf = sm.distributions.ECDF(exp_prov) 
    prov_x = np.linspace(min(exp_prov), max(exp_prov))
    prov_y = prov_ecdf(prov_x)
    prov_val = np.percentile(exp_prov, percentiles)

    fig = plt.figure(figsize=(5,4))
    ax = fig.gca()
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.plot(act_x, act_y*100, marker='o', lw = 2, color='red')
    plt.plot(rec_x, rec_y*100, marker='^', lw = 2, color='green')
    plt.plot(prov_x, prov_y*100, marker='s', lw = 2, color='blue')
    plt.plot(serv_x, serv_y*100, marker='X', lw = 2, color='orange')
    # plt.xlim(0,max(cst_x))
    # plt.ylim(0,max(cst_y)*100)
    plt.legend(("Activity", "Receiver","Provider","Service"))
    # plt.rc('axes', labelsize=18)
    # plt.rc('legend', fontsize=18) 
    plt.xlabel('# of Exported Component', size = 14)
    plt.ylabel('CDF', size = 14)
    plt.tight_layout()
    fig.savefig(write_path)
    plt.show()


def main():
    perm_plot = write_path+'ecdf_exported_component.pdf'
    exp_plot(exp_sum_per_app_path,perm_plot)



if __name__=='__main__':
    main()