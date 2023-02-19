from xml.dom.minidom import parseString

# base_path = '/home/budi/crypto_project/sandbox/trx.org.freewallet.app/AndroidManifest.xml'
# base_path = '/home/budi/crypto_project/sandbox/adblocker.lite.browser/AndroidManifest.xml'
base_path='/home/budi/adblocker_project/extracted_apk/2021/com.brave.browser/AndroidManifest.xml'
def permission_ex (manifest_path): 
    perm_list=[]
    with open(manifest_path,'r') as f:
        data = f.read()
        dom = parseString(data)
        perms = dom.getElementsByTagName('uses-permission')
        for per in perms:
            perm_list.append(per.getAttribute('android:name'))
            # print(per.getAttribute('android:name'))
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

def find_allias(manifest_path):
    with open (manifest_path,'r') as f:
        data =f.read()
        dom = parseString(data)
        manifest = dom.getElementsByTagName('manifest')
        # print(package[0])

        for item in manifest:
            tag_list=[]
            element = item.attributes
            for i in range(element.length):
                manifest_item = element.item(i).name
                tag_list.append(manifest_item)
    
    for item in tag_list:
        if 'xmlns' in item:
            xmlns,alias_name = map(str.strip,item.split(':'))
    return alias_name

def intent_action_ex(manifest_path):
    intent_action_list = []
    alias_name = find_allias(manifest_path)
    with open (manifest_path,'r') as f:
        data =f.read()
        dom = parseString(data)
        activities = dom.getElementsByTagName('activity')
        aliases = dom.getElementsByTagName('activity-alias')
        for activity in activities:
            if activity.getElementsByTagName('intent-filter'):
                act = (activity.getAttribute('android:name'))
                actions = activity.getElementsByTagName('action')
                for action in actions:
                    # print(action.getAttribute('android:name'))
                    int_act = {'activity':act, 'action':action.getAttribute('android:name')}
                    if int_act not in intent_action_list:    
                        intent_action_list.append(int_act)
        for activity in aliases:
            if activity.getElementsByTagName('intent-filter'):
                act = (activity.getAttribute(alias_name+':name'))
                actions = activity.getElementsByTagName('action')
                for action in actions:
                    # print(action.getAttribute('android:name'))
                    int_act = {'activity':act, 'action':action.getAttribute(alias_name+':name')}
                    if int_act not in intent_action_list:    
                        intent_action_list.append(int_act)
    return intent_action_list

def main():
    # perms = permission_ex(base_path)
    # print('Permission List')
    # for x in perms:
    #     print(x)

    # activities = activity_ex(base_path)
    # print('Activity List')
    # for activity in activities:
    #     print(activity)

    # receivers = receiver_ex(base_path)
    # print('Receiver List')
    # for receiver in receivers:
    #     print(receiver)

    # services = service_ex(base_path)
    # print('Service List')
    # for service in services:
    #     print(service)

    # providers = provider_ex(base_path)
    # print('Provider List')
    # for provider in providers:
    #     print(provider)

    # main_activity = main_activity_ex(base_path)
    # print('Main Activity')
    # print(main_activity)

    # exported_activities = exported_activity_ex(base_path)
    # print('Exported Activity List')
    # for activity in exported_activities:
    #     print(activity)

    # exported_services = exported_service_ex(base_path)
    # print('Exported Service List')
    # for service in exported_services:
    #     print(service)

    # exported_receivers = exported_receiver_ex(base_path)
    # print('Exported Receiver List')
    # for receiver in exported_receivers:
    #     print(receiver)

    # exported_providers = exported_provider_ex(base_path)
    # print('Exported Provider List')
    # for provider in exported_providers:
    #     print(provider)

    # package_name = package_name_ex(base_path)
    # print('Package Name :')
    # print(package_name)

    # alias_name = find_allias(base_path)
    # print(alias_name)
    intent_action = intent_action_ex(base_path)
    print('Intent Filter with Action :')
    for item in intent_action:
        print (item['activity'], item['action'])

if __name__ == "__main__":
    main()

