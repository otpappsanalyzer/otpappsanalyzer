import manifest_extractor
import os

base_path = '/media/budi/Seagate Expansion Drive/crypto_project/decompiled_apps/ab.cryptocurrency/AndroidManifest.xml'

def getPermissionsDictionary():
    dictionary = {'ACCEPT_HANDOVER': 'dangerous', 'ACCESS_BACKGROUND_LOCATION': 'dangerous', 'ACCESS_CALL_AUDIO': 'signature|appop', 'ACCESS_CHECKIN_PROPERTIES': 'N/A',
     'ACCESS_COARSE_LOCATION': 'dangerous', 'ACCESS_FINE_LOCATION': 'dangerous', 'ACCESS_LOCATION_EXTRA_COMMANDS': 'normal', 'ACCESS_MEDIA_LOCATION': 'dangerous',
     'ACCESS_NETWORK_STATE': 'normal', 'ACCESS_NOTIFICATION_POLICY': 'normal', 'ACCESS_WIFI_STATE': 'normal', 'ACCOUNT_MANAGER': 'N/A', 'ACTIVITY_RECOGNITION': 'dangerous',
     'ADD_VOICEMAIL': 'dangerous', 'ANSWER_PHONE_CALLS': 'dangerous', 'BATTERY_STATS': 'signature|privileged|development', 'BIND_ACCESSIBILITY_SERVICE': 'signature',
     'BIND_APPWIDGET': 'N/A', 'BIND_AUTOFILL_SERVICE': 'signature', 'BIND_CALL_REDIRECTION_SERVICE': 'signature|privileged',
     'BIND_CARRIER_MESSAGING_CLIENT_SERVICE': 'signature', 'BIND_CARRIER_MESSAGING_SERVICE': 'N/A', 'BIND_CARRIER_SERVICES': 'signature|privileged',
     'BIND_CHOOSER_TARGET_SERVICE': 'signature', 'BIND_CONDITION_PROVIDER_SERVICE': 'signature', 'BIND_CONTROLS': 'N/A', 'BIND_DEVICE_ADMIN': 'signature',
     'BIND_DREAM_SERVICE': 'signature', 'BIND_IN_CALL_SERVICE': 'signature|privileged', 'BIND_INPUT_METHOD': 'signature', 'BIND_MIDI_DEVICE_SERVICE': 'signature',
     'BIND_NFC_SERVICE': 'signature', 'BIND_NOTIFICATION_LISTENER_SERVICE': 'signature', 'BIND_PRINT_SERVICE': 'signature', 'BIND_QUICK_ACCESS_WALLET_SERVICE': 'signature',
     'BIND_QUICK_SETTINGS_TILE': 'N/A', 'BIND_REMOTEVIEWS': 'signature|privileged', 'BIND_SCREENING_SERVICE': 'signature|privileged',
     'BIND_TELECOM_CONNECTION_SERVICE': 'signature|privileged', 'BIND_TEXT_SERVICE': 'signature', 'BIND_TV_INPUT': 'signature|privileged',
     'BIND_VISUAL_VOICEMAIL_SERVICE': 'signature|privileged', 'BIND_VOICE_INTERACTION': 'signature', 'BIND_VPN_SERVICE': 'signature', 'BIND_VR_LISTENER_SERVICE': 'signature',
     'BIND_WALLPAPER': 'signature|privileged', 'BLUETOOTH': 'normal', 'BLUETOOTH_ADMIN': 'normal', 'BLUETOOTH_PRIVILEGED': 'N/A', 'BODY_SENSORS': 'dangerous',
     'BROADCAST_PACKAGE_REMOVED': 'N/A', 'BROADCAST_SMS': 'N/A', 'BROADCAST_STICKY': 'normal', 'BROADCAST_WAP_PUSH': 'N/A', 'CALL_COMPANION_APP': 'normal',
     'CALL_PHONE': 'dangerous', 'CALL_PRIVILEGED': 'N/A', 'CAMERA': 'dangerous', 'CAPTURE_AUDIO_OUTPUT': 'N/A', 'CHANGE_COMPONENT_ENABLED_STATE': 'N/A',
     'CHANGE_CONFIGURATION': 'signature|privileged|development', 'CHANGE_NETWORK_STATE': 'normal', 'CHANGE_WIFI_MULTICAST_STATE': 'normal', 'CHANGE_WIFI_STATE': 'normal',
     'CLEAR_APP_CACHE': 'signature|privileged', 'CONTROL_LOCATION_UPDATES': 'N/A', 'DELETE_CACHE_FILES': 'signature|privileged', 'DELETE_PACKAGES': 'N/A',
     'DIAGNOSTIC': 'N/A', 'DISABLE_KEYGUARD': 'normal', 'DUMP': 'N/A', 'EXPAND_STATUS_BAR': 'normal', 'FACTORY_TEST': 'N/A', 'FOREGROUND_SERVICE': 'normal',
     'GET_ACCOUNTS': 'dangerous', 'GET_ACCOUNTS_PRIVILEGED': 'signature|privileged', 'GET_PACKAGE_SIZE': 'normal', 'GET_TASKS': 'N/A',
     'GLOBAL_SEARCH': 'signature|privileged', 'INSTALL_LOCATION_PROVIDER': 'N/A', 'INSTALL_PACKAGES': 'N/A', 'INSTALL_SHORTCUT': 'normal',
     'INSTANT_APP_FOREGROUND_SERVICE': 'signature|development|instant|appop', 'INTERACT_ACROSS_PROFILES': 'N/A', 'INTERNET': 'normal', 'KILL_BACKGROUND_PROCESSES': 'normal',
     'LOADER_USAGE_STATS': 'signature|privileged|appop', 'LOCATION_HARDWARE': 'N/A', 'MANAGE_DOCUMENTS': 'N/A', 'MANAGE_EXTERNAL_STORAGE': 'signature|appop|preinstalled',
     'MANAGE_OWN_CALLS': 'normal', 'MASTER_CLEAR': 'N/A', 'MEDIA_CONTENT_CONTROL': 'N/A', 'MODIFY_AUDIO_SETTINGS': 'normal', 'MODIFY_PHONE_STATE': 'N/A',
     'MOUNT_FORMAT_FILESYSTEMS': 'N/A', 'MOUNT_UNMOUNT_FILESYSTEMS': 'N/A', 'NFC': 'normal', 'NFC_PREFERRED_PAYMENT_INFO': 'normal', 'NFC_TRANSACTION_EVENT': 'normal',
     'PACKAGE_USAGE_STATS': 'signature|privileged|development|appop|retailDemo', 'PERSISTENT_ACTIVITY': 'N/A', 'PROCESS_OUTGOING_CALLS': 'dangerous',
     'QUERY_ALL_PACKAGES': 'N/A', 'READ_CALENDAR': 'dangerous', 'READ_CALL_LOG': 'dangerous', 'READ_CONTACTS': 'dangerous', 'READ_EXTERNAL_STORAGE': 'dangerous',
     'READ_INPUT_STATE': 'N/A', 'READ_LOGS': 'N/A', 'READ_PHONE_NUMBERS': 'dangerous', 'READ_PHONE_STATE': 'dangerous', 'READ_PRECISE_PHONE_STATE': 'N/A',
     'READ_SMS': 'dangerous', 'READ_SYNC_SETTINGS': 'normal', 'READ_SYNC_STATS': 'normal', 'READ_VOICEMAIL': 'signature|privileged', 'REBOOT': 'N/A',
     'RECEIVE_BOOT_COMPLETED': 'normal', 'RECEIVE_MMS': 'dangerous', 'RECEIVE_SMS': 'dangerous', 'RECEIVE_WAP_PUSH': 'dangerous', 'RECORD_AUDIO': 'dangerous',
     'REORDER_TASKS': 'normal', 'REQUEST_COMPANION_RUN_IN_BACKGROUND': 'normal', 'REQUEST_COMPANION_USE_DATA_IN_BACKGROUND': 'normal', 'REQUEST_DELETE_PACKAGES': 'normal',
     'REQUEST_IGNORE_BATTERY_OPTIMIZATIONS': 'normal', 'REQUEST_INSTALL_PACKAGES': 'signature', 'REQUEST_PASSWORD_COMPLEXITY': 'normal', 'RESTART_PACKAGES': 'N/A',
     'SEND_RESPOND_VIA_MESSAGE': 'N/A', 'SEND_SMS': 'dangerous', 'SET_ALARM': 'normal', 'SET_ALWAYS_FINISH': 'N/A', 'SET_ANIMATION_SCALE': 'N/A', 'SET_DEBUG_APP': 'N/A',
     'SET_PREFERRED_APPLICATIONS': 'N/A', 'SET_PROCESS_LIMIT': 'N/A', 'SET_TIME': 'N/A', 'SET_TIME_ZONE': 'N/A', 'SET_WALLPAPER': 'normal', 'SET_WALLPAPER_HINTS': 'normal',
     'SIGNAL_PERSISTENT_PROCESSES': 'N/A', 'SMS_FINANCIAL_TRANSACTIONS': 'signature|appop', 'START_VIEW_PERMISSION_USAGE': 'signature|installer', 'STATUS_BAR': 'N/A',
     'SYSTEM_ALERT_WINDOW': 'signature|preinstalled|appop|pre23|development', 'TRANSMIT_IR': 'normal', 'UNINSTALL_SHORTCUT': 'N/A', 'UPDATE_DEVICE_STATS': 'N/A',
     'USE_BIOMETRIC': 'normal', 'USE_FINGERPRINT': 'normal', 'USE_FULL_SCREEN_INTENT': 'normal', 'USE_SIP':'dangerous', 'VIBRATE': 'normal', 'WAKE_LOCK': 'normal',
     'WRITE_APN_SETTINGS': 'N/A', 'WRITE_CALENDAR': 'dangerous', 'WRITE_CALL_LOG': 'dangerous', 'WRITE_CONTACTS': 'dangerous',
     'WRITE_EXTERNAL_STORAGE': 'dangerous', 'WRITE_GSERVICES': 'N/A', 'WRITE_SECURE_SETTINGS': 'N/A', 'WRITE_SETTINGS': 'signature|preinstalled|appop|pre23',
     'WRITE_SYNC_SETTINGS': 'normal', 'WRITE_VOICEMAIL': 'signature|privileged','BIND_JOB_SERVICE' : 'signature','INSTALL_PACKAGES':'dangerous','DUMP':'dangerous',
     'GET_TASK':'dangerous','READ_INTERNAL_STORAGE':'signature|privileged'}
    return dictionary

def find_permission_level(permission_list):
    diction = getPermissionsDictionary()
    permissionListLevel = []
    for perm in permission_list:
        finalPerm = perm.rfind(".")
        actualPermission = perm[1+finalPerm:]
        # print(actualPermission)
        if actualPermission in diction:
            new = diction[actualPermission]
            # print(actualPermission,new)
        else:
            new = "customized"#| Third-party"
            # print(actualPermission,new)
        
        if 'signature' in new:
            new = 'signature'
        
        item = {'permission':perm,'level':new}
        permissionListLevel.append(item)
    return permissionListLevel    

def main():
    permissionlist = manifest_extractor.permission_ex(base_path)
    perm_level = find_permission_level(permissionlist)
    for x in perm_level:
        print(x)

if __name__=='__main__':
    main()
