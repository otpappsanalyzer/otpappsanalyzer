import os

decompiled_app = '/home/budi/crypto_project/sandbox/com.blocking.sites'

def third_party_library_dict():
    d = {'Library': ('AdlibraryPath', 'Category'), 'Admob': ('com/admob', 'Targeted ads'), 'Facebook': ('com/facebook', 'Social networking service'), 'Flurry'
: ('com/flurry', 'Analytics'), 'Twitter4j': ('com/twitter4j', 'Social networking service'), 'Jsoup': ('com/jsoup', 'Utility'), 'Revmob': ('com/revmob'
, 'Targeted ads'), 'Millennialmedia': ('com/millennialmedia', 'Targeted ads'), 'Nostra13': ('com/nostra13', 'Utility'), 'Inmobi': ('com/inmobi',
'Targeted ads'), 'Acra': ('com/acra', 'Utility'), 'Unity3d': ('com/unity3d', 'Game engine'), 'Oauth': ('com/oauth', 'Utility'), 'Ksoap2': ('com/ksoap2',
'Utility'), 'Chartboost': ('com/chartboost', 'Targeted ads'), 'Paypal': ('com/paypal', 'Payment'), 'Bugsense': ('com/bugsense', 'Utilities'), 'Qbiki': (
'com/qbiki', 'Development aid'), 'Loopj': ('com/loopj', 'Utility'), 'Adobe': ('com/adobe', 'Utility'), 'Phonegap': ('com/phonegap', 'Utility'),
'Biznessapps': ('com/biznessapps', 'Development aid'), 'Smaato': ('com/smaato', 'Targeted ads'), 'Codehaus': ('com/codehaus', 'Utility'), 'Mopub':
('com/mopub', 'Targeted ads'), 'Urbanairship': ('com/urbanairship', 'Payment'), 'Kawa': ('com/kawa', 'Utility'), 'Adwhirl': ('com/adwhirl', 'Targeted ads'),
'Appbrain': ('com/appbrain', 'Utility'), 'Umeng': ('com/umeng', 'Mobile analytics'), 'Adfonic': ('com/adfonic', 'Targeted ads'), 'Titanium':
('com/titanium', 'Development aid'), 'Appcelerator': ('com/appcelerator', 'Utility'), 'Ansca': ('com/ansca', 'Utility'), 'Tapjoy': ('com/tapjoy', 'Targeted ads')
, 'Applovin': ('com/applovin', 'Targeted ads'), 'Amazon': ('com/amazon/analytics', 'Mobile analytics'), 'Badlogic': ('com/badlogic', 'Game engine'),
'Jumptap': ('com/jumptap', 'Targeted ads'), 'Crittercism': ('com/crittercism', 'Utility'), 'Mobclix': ('com/mobclix', 'Targeted ads'), 'Playhaven':
('com/playhaven', 'Targeted ads'), 'Inneractive': ('com/inneractive', 'Targeted ads'), 'Appmk': ('com/appmk', 'Utility'), 'Tencent': ('com/tencent',
'Targeted ads'), 'Andengine': ('com/andengine', 'Social gaming'), 'Baidu': ('com/baidu/location', 'Targeted ads'), 'Appyet': ('com/appyet',
'Development aid'), 'Osmdroid': ('com/osmdroid', 'Utility'), 'Anywheresoftware': ('com/anywheresoftware', 'Utility'), 'Scribe': ('com/scribe', 'Content provider'),
'Heyzap': ('com/heyzap', 'Social gaming'), 'Localytics': ('com/localytics', 'Analytics'), 'Anddev': ('com/anddev', 'Utility'), 'Mixpanel':
('com/mixpanel', 'Mobile analytics'), 'Greystripe': ('com/greystripe', 'Targeted ads'), 'Amazonaws': ('com/amazonaws', 'Utility'),
'Qualcomm': ('com/qualcomm', 'Utility'), 'Cocos2dx': ('com/cocos2dx', 'Game engine'), 'Roboguice': ('com/roboguice', 'Utility'), 'Mozilla': ('com/mozilla', 'Utility'),
'Springframework': ('com/springframework', 'Utility'), 'Nuance': ('com/nuance', 'Utility'), 'Mobfox': ('com/mobfox', 'Targeted ads'), 'Openfeint':
('com/openfeint', 'Game engine'), 'Apsalar': ('com/apsalar', 'Analytics'), 'Actionbarsherlock': ('com/actionbarsherlock', 'Utility'), 'Airpush':
('com/airpush', 'Targeted ads'), 'Admarvel': ('com/admarvel', 'Targeted ads'), 'Mdotm': ('com/mdotm', 'Targeted ads'), 'Github': ('com/github', 'Utility'),
'Tapfortap': ('com/tapfortap', 'Targeted ads'), 'Apperhand': ('com/apperhand', 'Targeted ads'), 'Scoreloop': ('com/scoreloop', 'Social gaming'),
'Comscore': ('com/comscore', 'Analytics'), 'Mediba': ('com/mediba', 'Targeted ads'), 'Weibo': ('com/weibo', 'Social networking service'),
 'Twitter': ('com/twitter', 'Social networking service'), 'Zestadz': ('com/zestadz', 'Targeted ads'), 'Mcsoxford': ('com/mcsoxford', 'Utility'),
 'Nbpcorp': ('com/nbpcorp', 'Targeted ads'), 'Adknowledge': ('com/adknowledge', 'Targeted ads'), 'Mobclick': ('com/mobclick', 'Mobile analytics'), 'Zong': ('com/zong', 'Payment'), 'Htmlcleaner': ('com/htmlcleaner', 'Utility'), 'Mapsforge': ('com/mapsforge', 'Content provider'), 'Socialize': ('com/socialize', 'Social networking service')
, 'Wiyun': ('com/wiyun', 'Social gaming'), 'Dom4j': ('com/dom4j', 'Utility'), 'Cauly': ('com/cauly', 'Targeted ads'), 'Bouncycastle': ('com/bouncycastle', 'Utility'), 'Smartadserver': ('com/smartadserver', 'Targeted ads'), 'Ormma': ('com/ormma', 'Targeted ads'), 'Winterwell': ('com/winterwell', 'Social networking service'), 'Sponsorpay': ('com/sponsorpay', 'Targeted ads'), 'Omniture': ('com/omniture', 'Mobile analytics'), 'Kenai': ('com/kenai', 'Development aid'), 'Dropbox': ('com/dropbox', 'Utility'), 'Leadbolt': ('com/leadbolt', 'Targeted ads'), 'Fedorvlasov': ('com/fedorvlasov', 'Utility'),
 'Mocoplex': ('com/mocoplex', 'Targeted ads'), 'Brightcove': ('com/brightcove', 'Content provider'), 'Alipay': ('com/alipay', 'Payment'), 'Greendroid'
: ('com/greendroid', 'Development aid'), 'Ccil': ('com/ccil', 'Utility'), 'Adwo': ('com/adwo', 'Targeted ads'), 'Commonsware': ('com/commonsware',
'Utility'), 'Aviary': ('com/aviary', 'Utility'), 'Vpon': ('com/vpon', 'Targeted ads'), 'Swarmconnect': ('com/swarmconnect', 'Targeted ads'),
'Spongycastle': ('com/spongycastle', 'Utility'), 'Iflytek': ('com/iflytek', 'Utility'), 'Pontiflex': ('com/pontiflex', 'Targeted ads'), 'Mobisage':
('com/mobisage', 'Targeted ads'), 'Papaya': ('com/papaya', 'Social gaming'), 'Xtify': ('com/xtify', 'Targeted ads'), 'Burstly': ('com/burstly', 'Targeted ads'),
 'Ideaworks3d': ('com/ideaworks3d', 'Utility'), 'Nullwire': ('com/nullwire', 'Utility'), 'Inapp': ('com/inapp', 'Utility'), 'Getjar': ('com/getjar',
 'Secondary market'), 'Webtrends': ('com/webtrends', 'Mobile analytics'), 'Livestream': ('com/livestream', 'Content provider'), 'Vervewireless':
 ('com/vervewireless', 'Targeted ads'), 'Gamesalad': ('com/gamesalad', 'Game engine'), 'Adchina': ('com/adchina', 'Targeted ads'), 'Yume': ('com/yume',
 'Targeted ads'), 'Rosaloves': ('com/rosaloves', 'Utility'), 'Nexage': ('com/nexage', 'Targeted ads'), 'Googlecode': ('com/googlecode', 'Development aid'),
 'Ngigroup': ('com/ngigroup', 'Targeted ads'), 'Cocos2d': ('com/cocos2d', 'Game engine'), 'Jcifs': ('com/jcifs', 'Utility'), 'Madhouse': ('com/madhouse',
 'Targeted ads'), 'Sonicnotify': ('com/sonicnotify', 'Targeted ads'), 'Everbadge': ('com/everbadge', 'Targeted ads'), 'Pjsip': ('com/pjsip', 'Utility'),
'Fmod': ('com/fmod', 'Utility'), 'Bumptech': ('com/bumptech', 'Utility'), 'Qwapi': ('com/qwapi', 'Targeted ads'), 'Medialets': ('com/medialets',
'Targeted ads'), 'Renren': ('com/renren', 'Social networking service'), 'Eclipse': ('com/eclipse', 'Utility'), 'Vdopia': ('com/vdopia', 'Targeted ads'),
'Rhythmnewmedia': ('com/rhythmnewmedia', 'Targeted ads'), 'Suizong': ('com/suizong', 'Targeted ads'), 'Adview': ('com/adview', 'Targeted ads'),
'Devsmart': ('com/devsmart', 'Ui component'), 'Wooboo': ('com/wooboo', 'Targeted ads'), 'Twitterapime': ('com/twitterapime', 'Social networking service'),
'Jboss': ('com/jboss', 'Utility'), 'Noqoush': ('com/noqoush', 'Targeted ads'), 'Opencv': ('com/opencv', 'Utility'), 'Fiksu': ('com/fiksu', 'Targeted ads'
), 'Adserver': ('com/adserver', 'Targeted ads'), 'Microsoft': ('com/microsoft/Targeted ads', 'Targeted ads'), 'Admogo': ('com/admogo', 'Targeted ads')
, 'Groovy': ('com/groovy', 'Development aid'), 'Htmlparser': ('com/htmlparser', 'Utility'), 'Kuguo': ('com/kuguo', 'Targeted ads'),
'Mads': ('com/mads', 'Targeted ads'), 'Jcraft': ('com/jcraft', 'Utility'), 'Restlet': ('com/restlet', 'Utility'), 'Ubikod': ('com/ubikod', 'Mobile analytics'),
'Widespace': ('com/widespace', 'Targeted ads'), 'Jakewharton': ('com/jakewharton', 'Ui component'), 'Yicha': ('com/yicha', 'Targeted ads'), 'Casee':
('com/casee', 'Targeted ads'), 'Energysource': ('com/energysource', 'Targeted ads'), 'Wqmobile': ('com/wqmobile', 'Targeted ads'), 'Fortumo': ('com/fortumo', 'Payment'), 'Kuad': ('com/kuad', 'Targeted ads'), 'Skyhookwireless': ('com/skyhookwireless', 'Utility'), 'Adcenix': ('com/adcenix', 'Targeted ads'),
'Wutka': ('com/wutka', 'Utility'), 'Openintents': ('com/openintents', 'Game engine'), 'Winad': ('com/winad', 'Targeted ads'), 'Utilities':
('com/utilities', 'Utility'), 'Mapabc': ('com/mapabc', 'Content provider'), 'Guohead': ('com/guohead', 'Targeted ads'), 'Db4o': ('com/db4o', 'Utility'),
'Ignitevision': ('com/ignitevision', 'Mobile analytics'), 'Osgi': ('com/osgi', 'Utility'), 'Gfan': ('com/gfan', 'Secondary market'), 'Apprupt': ('com/apprupt',
'Targeted ads'), 'Lmmob': ('com/lmmob', 'Targeted ads'), 'Fractalist': ('com/fractalist', 'Targeted ads'), 'Mortbay': ('com/mortbay', 'Utility'),
'Maps': ('com/maps', 'Utility'), 'Moolah': ('com/moolah', 'Targeted ads'), 'Radiumone': ('com/radiumone', 'Targeted ads'), 'Push': ('com/push', 'Utility')
, 'Donson': ('com/donson', 'Targeted ads'), 'Exchange': ('com/exchange', 'Utility'), 'Transpera': ('com/transpera', 'Targeted ads'), 'Andnav':
('com/andnav', 'Content provider'), 'Oneriot': ('com/oneriot', 'Targeted ads'), 'Proguard': ('com/proguard', 'Utility'), 'Mopay': ('com/mopay', 'Payment'), 'Donple': ('com/donple', 'Targeted ads'), 'Viewpagerindicator': ('com/viewpagerindicator', 'Ui component'), 'Stericson': ('com/stericson', 'Utility'),
'Adzhidian': ('com/adzhidian', 'Targeted ads'), 'Simpleframework': ('com/simpleframework', 'Utility'), 'Joelapenna': ('com/joelapenna', 'Social networking service'), 'Quipper': ('com/quipper', 'Content provider'), 'Sellaring': ('com/sellaring', 'Targeted ads'), 'Hamcrest': ('com/hamcrest', 'Utility'
), 'Yuku': ('com/yuku', 'Utility'), 'Thehttpclient': ('com/thehttpclient', 'Utility'), 'Ximad': ('com/ximad', 'Secondary market'), 'Motorola': ('com/motorola', 'Utility'), 'Adpooh': ('com/adpooh', 'Targeted ads'), 'Zongfuscated': ('com/zongfuscated', 'Payment'), 'Intuit': ('com/intuit', 'Payment'),
'Kankan': ('com/kankan', 'Ui component'), 'Jdom': ('com/jdom', 'Utility'), 'Novell': ('com/novell', 'Development aid'), 'Min3d': ('com/min3d', 'Utility'), 'Relaxng': ('com/relaxng', 'Utility'), 'Afzkl': ('com/afzkl', 'Utility'), 'Slf4j': ('com/slf4j', 'Utility'), 'Ocpsoft': ('com/ocpsoft', 'Utility'
), 'J256': ('com/j256', 'Utility'), 'Helllabs': ('com/helllabs', 'Utility'), 'Apwidgets': ('com/apwidgets', 'Utility'), 'Imagezoom': ('com/imagezoom',
 'Utility'), 'Onbarcode': ('com/onbarcode', 'Utility'), 'Joda': ('com/joda', 'Utility'), 'Mobiledatagroup': ('com/mobiledatagroup', 'Content provider'
), 'Jaxen': ('com/jaxen', 'Utility'), 'Tecnick': ('com/tecnick', 'Utility'), 'Kobjects': ('com/kobjects', 'Utility'), 'Achartengine':
('com/achartengine', 'Utility'), 'Lgpl': ('com/lgpl', 'Utility'), 'Appmakr': ('com/appmakr', 'Utility'), 'Spreada': ('com/spreada', 'Mobile analytics'), 'Aspectj':
('com/aspectj', 'Utility'), 'Objenesis': ('com/objenesis', 'Utility'), 'Metalev': ('com/metalev', 'Utility'), 'Yaml': ('com/yaml', 'Utility'), 'Jbox2d':
 ('com/jbox2d', 'Utility'), 'Scoreninja': ('com/scoreninja', 'Social gaming'), 'Jaudiotagger': ('com/jaudiotagger', 'Utility'), 'Libsvg':
 ('com/libsvg', 'Utility'), 'Taptwo': ('com/taptwo', 'Ui component'), 'Easymock': ('com/easymock', 'Ui component'), 'Aerserv': ('com/aerserv', 'Targeted ads'),
 'Fasterxml': ('com/fasterxml', 'Utility'), 'Perk': ('com/perk', 'Analytics'), 'Google Ads': ('com/google/android/gms/ads', 'Targeted ads'),
 'Millenial media': ('com/millennialmedia', 'Targeted ads'), 'MoPub': ('com/mopub', 'Targeted ads'), 'Google Analytics': ('com/google/android/gms/analytics',
 'Mobile analytics'), 'Amazon Insights': ('com/amazon/insights', 'Analytics'), 'Kontagent': ('com/kontagent', 'Analytics'), 'Crashlytics': ('com/crashlytics'
, 'Utilities'), 'OUTFIT7': ('com/outfit7', 'Targeted ads'), 'DOMOB': ('cn/domob', 'Targeted ads'), 'SMARTMAD': ('cn/smartmad', 'Targeted ads'),
'IQzone': ('com/IQzone', 'Targeted ads'), 'AdIQuity': ('com/adiquity', 'Targeted ads'), 'ADITION': ('com/adition', 'Targeted ads'), 'AdMarvel':
('com/admarvel', 'Targeted ads'), 'AdMob': ('com/admob', 'Targeted ads'), 'Receptiv': ('com/receptive', 'Targeted ads'), 'MobFox': ('com/mobfox', 'Targeted ads'),
 'AdsWizz': ('com/adswizz', 'Targeted ads'), 'Appboy': ('com/appboy', 'Targeted ads'), 'AppFlood': ('com/appflood', 'Targeted ads'), 'Applifier':
 ('com/applifier', 'Targeted ads'), 'AppLovin': ('com/applovin', 'Targeted ads'), 'AppNexus': ('com/appnexus', 'Targeted ads'), 'apprupt': ('com/apprupt',
'Targeted ads'), 'Appsflyer': ('com/appsflyer', 'Targeted ads'), 'Bee7': ('com/bee7', 'Targeted ads'), 'bluekai': ('com/bluekai', 'Targeted ads'),
'BrightRoll': ('com/brightroll', 'Targeted ads'), 'Unknown': ('jp/appAdForce', 'Targeted ads'), 'CrossPromotion': ('com/crossPromotion', 'Targeted ads'),
 'DirectTAP': ('com/directtap', 'Targeted ads'), 'FIKSU': ('com/fiksu', 'Targeted ads'), 'FusePowered': ('com/fusepowered', 'Targeted ads'),
 'GrowMobile': ('com/growmobile', 'Targeted ads'), 'heyZap': ('com/heyzap', 'Targeted ads'), 'hyprMX': ('com/hyprmx', 'Targeted ads'), 'ironSource':
 ('com/ironsource', 'Targeted ads'), 'AdColony (Jirbo)': ('com/jirbo', 'Targeted ads'), 'jumptap': ('com/jumptap', 'Targeted ads'), 'Kahuna': ('com/kahuna',
 'Targeted ads'), 'MDOTM': ('com/mdotm', 'Targeted ads'), 'MediaBrix': ('com/mediabrix', 'Targeted ads'), 'mobclix': ('com/mobclix', 'Targeted ads'),
 'mologiq': ('com/mologiq', 'Targeted ads'), 'nanigans': ('com/nanigans', 'Targeted ads'), 'NativeX': ('com/nativex', 'Targeted ads'), 'Pollfish':
 ('com/pollfish', 'Targeted ads'), 'quantcast': ('com/quantcast', 'Targeted ads'), 'RADIUMONE': ('com/radiumone', 'Targeted ads'), 'Smart Ad Server':
 ('com/smartadserver', 'Targeted ads'), 'Fyber': ('com/sponsorpay', 'Targeted ads'), 'StartApp': ('com/startapp', 'Targeted ads'), 'Supersonic':
 ('com/supersonicads', 'Targeted ads'), 'phunware': ('com/tapit', 'Targeted ads'), 'TapJoy': ('com/tapjoy', 'Targeted ads'), 'TAPSENSE': ('com/tapsense', 'Targeted ads'
), 'TREMOR': ('com/tremorvideo', 'Targeted ads'), 'Trialpay': ('com/trialpay', 'Targeted ads'), 'Unity Ads': ('com/unity3d/ads', 'Targeted ads'),
'Urban Ariship': ('com/urbanairship', 'Targeted ads'), 'Vungle': ('com/vungle', 'Targeted ads'), 'Nativex': ('com/w3i', 'Targeted ads'), 'YOC': ('com/yoc'
, 'Targeted ads'), 'YOZIO': ('com/yozio', 'Targeted ads'), 'YuMe': ('com/yume', 'Targeted ads'), 'ZestADZ': ('com/zestadz', 'Targeted ads'),'kiip':
('me/kiip', 'Targeted ads'), 'metaps': ('net/metaps', 'Targeted ads'), 'YouAppi ': ('com/youappi ', 'Targeted ads'), 'LEADBOLT': ('com/leadbolt',
'Targeted ads'), 'FreeWheel': ('com/freewheel', 'Targeted ads'), 'Adxtracking': ('com/AdX', 'Mobile analytics'), 'Ktplay': ('com/ktplay', 'Mobile analytics'),
'mobile app tracking': ('com/mobileapptracker', 'Mobile analytics'), 'adjust': ('com/adjust', 'Mobile analytics'), 'APP DYNAMICS': ('com/appdynamics',
'Mobile analytics'), 'AppFireworks': ('com/appfireworks', 'Mobile analytics'), 'Apptimize': ('com/apptimize', 'Mobile analytics'), 'At Internet':
('com/atinternet', 'Mobile analytics'), 'Kochava': ('com/kochava', 'Mobile analytics'), 'New Relic': ('com/newrelic', 'Mobile analytics'), 'Omniata':
('com/omniata', 'Mobile analytics'), 'Ooyala': ('com/ooyala', 'Mobile analytics'), 'OtherLevels': ('com/otherlevels', 'Mobile analytics'), 'Session m':
('com/sessionm', 'Mobile analytics'), 'Swrve': ('com/swrve', 'Mobile analytics'), 'UPSIGHT': ('com/upsight', 'Mobile analytics'), 'webtrekk':
('com/webtrekk', 'Mobile analytics'), 'webtrends': ('com/webtrends', 'Mobile analytics'), 'INFOnline': ('de/infonline', 'Mobile analytics'), 'PartyTrack':
('it/partytrack', 'Mobile analytics'), 'HOCKETAPP': ('net/hockeyapp', 'Utility'), 'COREMEDIA': ('com/coremedia', 'Utility'), 'FGL': ('com/fgl', 'Utility'),
 'Helpshift': ('com/helpshift', 'Utility'), 'kamcord': ('com/kamcord', 'Utility'), 'Prime31': ('com/prime31', 'Utility'), 'SmartFoxServer':
 ('com/smartfoxserver', 'Utility'), 'Steema': ('com/steema', 'Utility'), 'ThreatMetrix': ('com/threatmetrix', 'Utility'), 'TIM Group': ('com/timgroup', 'Utility'
), 'Truvie': ('com/truvie', 'Utility'), 'Squareup': ('com/squareup', 'Payment'), 'Batch ': ('com/batch ', 'Mobile analytics'), 'Oneaudience ':
 ('com/oneaudience ', 'Mobile analytics'), 'Crystalapp': ('co/crystalapp ', 'Utility::Contentblocker'), 'Tjeannin': ('com/Tjeannin ', 'Utility')}

    return d
    """New libraries :
    -daasu      -bugsnag
    -amplitude  -cottacush
    -firebase   -fasterxml
    -github     -tapadoo
    -airbnb     -yakivmospan
    -chaos  
    """

def smali_finder(folder_path):
    smali_list = []
    for roots,dirs,files in os.walk(folder_path):
        for dir in dirs:
            if 'smali' in dir:
                smali_path = roots+'/'+dir
                smali_list.append(smali_path)
    return smali_list

def lib_finder(smali_path):
    taint_lib_list =[]
    lib_dict = third_party_library_dict()
    for roots,dirs,files in os.walk(smali_path):
        for dir in dirs:
            dir_path = roots+'/'+dir
            for lib_name,lib_type in lib_dict.items():
                match_item = {'lib_name':lib_name,'lib_type':lib_type[1]}
                if lib_type[0] in dir_path and match_item not in taint_lib_list:
                    taint_lib_list.append(match_item)
                    break

    return taint_lib_list

def check_lib(folder_path):
    library_list =[]
    smali_list = smali_finder(folder_path)
    for item in smali_list:
        tainted_lib = lib_finder(item)
        for lib in tainted_lib:
            TargetedAds = False
            MobileAnalytics = False
            Analytics = False
            AnyTrackingLibrary = False

            if(lib['lib_type'] == "Targeted ads"):
                TargetedAds = True
                AnyTrackingLibrary = True
            if(lib['lib_type'] == "Mobile analytics"):
                MobileAnalytics = True
                AnyTrackingLibrary = True
            if(lib['lib_type'] == "Analytics"):
                Analytics = True
                AnyTrackingLibrary = True

            item_value = {'lib_name':lib['lib_name'], 'lib_type':lib['lib_type'], 'TargetedAds':TargetedAds ,
                'MobileAnalytics':MobileAnalytics , 'Analytics':Analytics, 'AnyTrackingLibrary':AnyTrackingLibrary}
            
            if item_value not in library_list:
                library_list.append(item_value)

    return library_list

def main():
    lib_list = check_lib(decompiled_app)
    for item in lib_list:
        print(item)
if __name__=='__main__':
    main()