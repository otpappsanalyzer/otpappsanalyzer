from xml.dom.minidom import parseString


"""Find Permission"""
def permission_ex (manifest_path): 
    perm_list=[]
    # location=[]
    with open(manifest_path,'r') as f:
        data = f.read()
        dom = parseString(data)
        perms = dom.getElementsByTagName('uses-permission')
        for per in perms:
            per_val = per.getAttribute('android:name')
            if per_val not in perm_list and per_val !='':
                perm_list.append(per_val)
                # location.append('uses')
            # print(per.getAttribute('android:name'))

        activity_perm = dom.getElementsByTagName('activity')
        for ap in activity_perm:
            ap_val = ap.getAttribute('android:permission')
            if ap_val not in perm_list and ap_val !='':
                perm_list.append(ap_val)
                # location.append('activity')

        services_perm = dom.getElementsByTagName('service')
        for sp in services_perm:
            sp_val = sp.getAttribute('android:permission')
            if sp_val not in perm_list and sp_val !='':
                perm_list.append(sp_val)

        receiver_perm = dom.getElementsByTagName('receiver')
        for rp in receiver_perm:
            rp_val = rp.getAttribute('android:permission')
            if rp_val not in perm_list and rp_val !='':
                perm_list.append(rp_val)
        provider_perm = dom.getElementsByTagName('provider')
        for pp in provider_perm:
            pp_val = pp.getAttribute('android:permission')
            if pp_val not in perm_list and pp_val !='':
                perm_list.append(pp_val)
    return perm_list

def activity_ex (manifest_path):
    act_list = []
    with open (manifest_path,'r') as f:
        data =f.read()
        dom = parseString(data)
        activities = dom.getElementsByTagName('activity')
        for activity in activities:
            act_list.append(activity.getAttribute('android:name'))
    return act_list

def receiver_ex (manifest_path):
    rec_list = []
    with open (manifest_path,'r') as f:
        data =f.read()
        dom = parseString(data)
        receivers = dom.getElementsByTagName('receiver')
        for receiver in receivers:
            rec_list.append(receiver.getAttribute('android:name'))
    return rec_list

def service_ex (manifest_path):
    ser_list = []
    with open (manifest_path,'r') as f:
        data =f.read()
        dom = parseString(data)
        services = dom.getElementsByTagName('service')
        for service in services:
            ser_list.append(service.getAttribute('android:name'))
    return ser_list

def provider_ex (manifest_path):
    prov_list = []
    with open (manifest_path,'r') as f:
        data =f.read()
        dom = parseString(data)
        providers = dom.getElementsByTagName('provider')
        for provider in providers:
            prov_list.append(provider.getAttribute('android:name'))
    return prov_list

def main_activity_ex(manifest_path):
    act_list = []
    with open (manifest_path,'r') as f:
        data =f.read()
        dom = parseString(data)
        activities = dom.getElementsByTagName('activity')
        for activity in activities:
            intents = activity.getElementsByTagName('intent-filter')
            for intent in intents:
                actions = intent.getElementsByTagName('action')
                for action in actions:
                    if  action.getAttribute('android:name') == 'android.intent.action.MAIN':
                        main_activity = activity.getAttribute('android:name')                       
                        # print (activity.getAttribute('android:name'))
    return main_activity

def exported_activity_ex(manifest_path):
    exported_act_list = []
    with open (manifest_path,'r') as f:
        data =f.read()
        dom = parseString(data)
        activities = dom.getElementsByTagName('activity')
        for activity in activities:
            if activity.getAttribute('android:exported') == 'true':
                exported_act_list.append(activity.getAttribute('android:name'))
    return exported_act_list

def exported_service_ex(manifest_path):
    exported_ser_list = []
    with open (manifest_path,'r') as f:
        data =f.read()
        dom = parseString(data)
        services = dom.getElementsByTagName('service')
        for service in services:
            if service.getAttribute('android:exported') == 'true':
                exported_ser_list.append(service.getAttribute('android:name'))
    return exported_ser_list

def exported_receiver_ex(manifest_path):
    exported_rec_list = []
    with open (manifest_path,'r') as f:
        data =f.read()
        dom = parseString(data)
        receivers = dom.getElementsByTagName('receiver')
        for receiver in receivers:
            if receiver.getAttribute('android:exported') == 'true':
                exported_rec_list.append(receiver.getAttribute('android:name'))
    return exported_rec_list

def exported_provider_ex(manifest_path):
    exported_prov_list = []
    with open (manifest_path,'r') as f:
        data =f.read()
        dom = parseString(data)
        providers = dom.getElementsByTagName('provider')
        for provider in providers:
            if provider.getAttribute('android:exported') == 'true':
                exported_prov_list.append(provider.getAttribute('android:name'))
    return exported_prov_list

def package_name_ex(manifest_path):
    with open (manifest_path,'r') as f:
        data =f.read()
        dom = parseString(data)
        package = dom.getElementsByTagName('manifest')
        for item in package:
            package = item.getAttribute('package')
    return package

def intent_action_ex(manifest_path):
    intent_action_list = []
    with open (manifest_path,'r') as f:
        data =f.read()
        dom = parseString(data)
        activities = dom.getElementsByTagName('activity')
        for activity in activities:
            if activity.getElementsByTagName('intent-filter'):
                act = (activity.getAttribute('android:name'))
                actions = activity.getElementsByTagName('action')
                for action in actions:
                    # print(action.getAttribute('android:name'))
                    intent_act = {'activity':act, 'action':action.getAttribute('android:name')}
                    if intent_act not in intent_action_list:
                        intent_action_list.append(intent_act)
    return intent_action_list

def main():
    print('Permission List')


if __name__ == "__main__":
    main()

