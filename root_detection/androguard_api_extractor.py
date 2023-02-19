import os
import pandas as pd
# selected_app_id='/home/budi/OTP_project/OTP_code/root_detection/test.csv'
selected_app_id = '/home/budi/OTP_project/OTP_code/metadata/csv_apk_id.csv'
andro_res_path = '/home/budi/OTP_project/Androguard_API/'
report_path = '/home/budi/OTP_project/OTP_code/root_detection/'
def extract_api(app_id,res_path):
    api_found = []
    api_flag = ['Runtime;->exec','PackageManager;->getPackageInfo', 'Os;->stat','Os;->access','RootBeer;->isRooted','RootTools']
    app_in_andro = res_path+app_id+'.txt'
    print('extracting API flag from : ' + app_id)
    with open (app_in_andro,'r') as fl:
        for line in fl:
            for item in api_flag:
                if item in line:
                    flag = item.replace(';->','.')
                    found_item = {'app_id':app_id,'api_flag':flag}
                    if found_item not in api_found:
                        api_found.append(found_item)
    return api_found

def safetynet_attest(app_id,res_path):
    api_found = []
    api_flag = ['SafetyNet;->getClient','SafetyNetApi']
    app_in_andro = res_path+app_id+'.txt'
    print('extracting Safetynet API flag from : ' + app_id)
    with open (app_in_andro,'r') as fl:
        for line in fl:
            for item in api_flag:
                if item in line:
                    flag = item.replace(';->','.')
                    found_item = {'app_id':app_id,'api_flag':flag}
                    if found_item not in api_found:
                        api_found.append(found_item)
    return api_found


def biometric_api(app_id,res_path):
    api_found = []
    api_flag = ['BiometricManager','BiometricPrompt','FingerprintManager','BiometricService','FingerprintService']
    app_in_andro = res_path+app_id+'.txt'
    print('extracting Biometric API flag from : ' + app_id)
    with open (app_in_andro,'r') as fl:
        for line in fl:
            for item in api_flag:
                if item in line:
                    flag = item.replace(';->','.')
                    found_item = {'app_id':app_id,'api_flag':flag}
                    if found_item not in api_found:
                        api_found.append(found_item)
    return api_found

def security_on_chip(app_id,res_path):
    api_found = []
    api_flag = ['KeyStore;->getInstance','KeyGenParameterSpec;->Builder;->isStrongBoxBacked','isStrongBoxBacked','isInsideSecureHardware','StrongBoxUnavailableException']
    app_in_andro = res_path+app_id+'.txt'
    print('extracting Security on Chip API flag from : ' + app_id)
    with open (app_in_andro,'r') as fl:
        for line in fl:
            for item in api_flag:
                if item in line:
                    flag = item.replace(';->','.')
                    found_item = {'app_id':app_id,'api_flag':flag}
                    if found_item not in api_found:
                        api_found.append(found_item)
    return api_found

def main():
    root_api=[]
    with open(selected_app_id,'r') as fl:
        for line in fl:
            app_id = line.strip()
            api_res = extract_api(app_id,andro_res_path)
            for item in api_res:
                root_api.append(item)

            net_res = safetynet_attest(app_id,andro_res_path)
            for net in net_res:
                root_api.append(net)

            bio_res = biometric_api(app_id,andro_res_path)
            for bio in bio_res:
                root_api.append(bio)
            chip_res = security_on_chip(app_id,andro_res_path)
            for chip in chip_res:
                root_api.append(chip)
    print(root_api)
    root_df = pd.DataFrame.from_records(root_api)
    detail_path = report_path+'androguard_api_classes.csv'
    root_df.to_csv(detail_path,index=False)
    print(root_df)

if __name__=='__main__':
    main()