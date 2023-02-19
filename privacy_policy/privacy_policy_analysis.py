'''
This script is for privacy policy analysis
'''
import xml.etree.ElementTree as ET
# from .filepaths import *
import os
import shutil
import os, sys, codecs, fnmatch, time, binascii, requests, json, sqlite3, hashlib
from bs4 import BeautifulSoup
from subprocess import call
# from .filepaths import *
from bs4 import BeautifulSoup
from bs4.element import Comment
import requests
import urllib.request
from urllib.request import Request, urlopen
import pickle
from sklearn.svm import SVC
# from .filepaths import *
from langdetect import detect

#### Check privacy policy
def metaFromWebsite(appID):
    URL = "https://play.google.com/store/apps/details?id="+appID+"&hl=en_AU"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    print("we get here")
    links = getDeveloperLinks(soup)
    print("we get link for metadata")
 
    titleForResult = [e.get_text(separator=" ").strip() for e in soup.find_all("div",{"class":"BgcNfc"})]
    result = [e.get_text(separator=" ").strip() for e in soup.find_all("div",{"class":"hAyfc"})]
    try:
        rating = soup.find("div",{"class":"BHMmbe"}).get_text(separator=" ").strip()
    except:
        rating = "None"
        pass
    try:
        description = soup.find("div",{"class":"DWPxHb"}).get_text(separator=" ").strip()
    except:

        description = "None"
        pass

    Meta = []
    mergedMetaList = mergeLists(titleForResult, result)
    Meta.append(mergedMetaList.get('result'))
    try:
        Meta.append(rating)
    except:
        pass
    try:
        Meta.append(description)
    except:
        pass
    try:
        Meta.append(links)
    except:
        pass
    try:
        Meta.append(mergedMetaList.get('numInstalls'))
        Meta.append(mergedMetaList.get('developer'))
    except:
        pass

    MetaDict = {'Installs':mergedMetaList.get('numInstalls'),'Developer':mergedMetaList.get('developer'),'Description':description, 'Rating':rating,
    'UpdatedDate': mergedMetaList.get('result').get('Updated'), 'CurrentVersion': mergedMetaList.get('result').get('Current Version'),
    'RequiresAndroid':mergedMetaList.get('result').get('Requires Android'),'PrivacyPolicyLink': links.get("Privacy Policy"),
    'DeveloperWebsite': links.get("Developer Website"), 'DeveloperEmail': links.get("Developer Email") }
   
    return MetaDict

def getDeveloperLinks(soup):
    string = ""

    #print(soup)
    for test in soup.find_all("div",{"class":"hAyfc"}):
        stringTest = str(test)

        DeveloperWebsite = ""
        DeveloperEmail = ""
        PrivacyPolicy = ""
        #print("we get here")
        if "<div class=\"BgcNfc\">Developer" in stringTest:
            if stringTest.find("hrTbp\" href=") > 1:
                websitePos = stringTest.find(">Visit website")
                QuoteLast = stringTest.rfind('\"',0,websitePos)

                QuoteSecond = stringTest.rfind('\"',0,QuoteLast)

                DeveloperWebsite = stringTest[QuoteSecond+1:QuoteLast]
                print(DeveloperWebsite)

            if stringTest.find("hrTbp euBY6b\" href=") > 1:
                websitePos = stringTest.find("hrTbp euBY6b\" href=")+27
                endWebPost =stringTest.find('"',websitePos+2)

                DeveloperEmail = stringTest[websitePos:endWebPost]

            if stringTest.find(">Privacy Policy") > 1:
                PrivacyPos = stringTest.find(">Privacy Policy")

                QuoteLast = stringTest.rfind('\"',0,PrivacyPos)

                QuoteSecond = stringTest.rfind('\"',0,QuoteLast)

                PrivacyPolicy = stringTest[QuoteSecond+1:QuoteLast]
                #print(PrivacyPolicy)
                #now i need to find last two substrings before PrivacyPos (" " "), and get the reference there


        links = {"Developer Website":DeveloperWebsite,"Developer Email":DeveloperEmail,"Privacy Policy":PrivacyPolicy}

    return links

def mergeLists(listA, listB):
    numInstalls = 0
    developer = ""
    result = {}
    for a in listA:
        for b in listB:
            editedString = b.replace(a+" ", "")
            if(a == "Installs"):
                # editedString = editedString.replace(",","")
                # editedString = editedString.replace("+","")
                numInstalls = str(editedString)

            if(a == "Offered By"):
                editedString = editedString.replace(",","")
                developer = editedString

            result[a] = editedString

            listB.remove(b)
            break
    dict = {'result':result, 'numInstalls':numInstalls, 'developer':developer}
    return dict

def getPrivacyPolicyText(link):
    PPAccess = True
    # if link == '' or link == None:
    #     print("non existent link")
    #     PPAccess = False
    #     return "No Privacy Policy", PPAccess
    print("link: "+link)

    req = Request(link, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) '
                  'Version/9.1.2 Safari/601.7.5 '})
    try:

        # need to do this because: https://stackoverflow.com/questions/50085366/permissionerror-winerror-31-a-device-attached-to-the-system-is-not-functioning

        html = text_from_html(urllib.request.urlopen(req).read())
        #print("Text from HTML File ----------------")
        #print(html)
        #print("end of HTML Text -------------------")
        print("successfully getting privacy policy text")
        return html.replace("\n", " ").replace("\t", " ").replace("     ", " ").replace(",", " ").replace("\"", ""), PPAccess
    
    except Exception as e:
        print("ERROR TRYING TO GET TEXT FROM HTML--------------")
        html = str(e)
        print("error: "+html)
        PPAccess = False
        return html, PPAccess

def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

## machine learning function
filepaths_NeuralNetworkModel = '/home/budi/OTP_project/OTP_code/privacy_policy/MachineLearning/finalized_model.sav'

def testSVCPickle(text):
    filename = filepaths_NeuralNetworkModel
    loaded_model = pickle.load(open(filename, 'rb'))
    listText = []
    print('before reading policy text')
    listText.append(text)
    print('after reading policy text')

    print("listText: ")
    print(listText)

    predictionText = loaded_model.predict(listText)
    print('predictionText: ', predictionText)

    listText = []
    return predictionText

def PPShares3rdParty(text):
    if testSVCPickle(text)[0] == 1:
        print("Privacy Policy is Positive for sharing information with third party")
        return True

    print("Privacy Policy is Negative for sharing information with third party")
    return False

def DetectLanguage(text):
    try:
        language = detect(text)
    except:
        language = "N/A"
    return language


if __name__ == "__main__":
    file_name = '/home/budi/OTP_project/OTP_code/privacy_policy/csv_apk_id.csv'
    reader = open(file_name, "r")
    list_app_id = []
    list_app_id = reader.read().split("\n")
    reader.close()

    file_name_privacy_policy = '/home/budi/OTP_project/OTP_code/privacy_policy/report/privacy_policy_test_again_redirect_link.csv'
    temp_list =[]
    # with open (file_name_privacy_policy,'r') as temp_file:
    #     for line in temp_file:
    #         temp_list.append(line.strip('\n'))
    f_pp = open(file_name_privacy_policy, "a")
    # f_pp.write("App id; Valid Privacy Policy available; Privacy Policy Claimed sharing data with third party\n")
    

    count = 0
    for app_id in list_app_id[count:]:
        appID = app_id.split(';')[0]
        print('--------------------------------------------------->>>>>>>')
        print('Starting analysis for appID = ', appID)
        
        print("----- Meta Info -----")

        '''
        The below is needed when there is only app id information avaible, we need to get metadata
        '''
        try:
            appMeta = metaFromWebsite(appID)
            print("we get appMeta")
            # print(appMeta)
            meta_info_installs = appMeta.get('Installs')
            # print("Rating ....")
            meta_info_rating = appMeta.get('Rating')
            meta_info_description = appMeta.get('Description')
            meta_info_developer = appMeta.get('Developer')
            meta_info_last_update = appMeta.get('UpdatedDate')
            meta_info_current_version = appMeta.get('CurrentVersion')
            meta_info_android_version = appMeta.get('RequiresAndroid')
            meta_info_developer_email = appMeta.get('DeveloperEmail')
            meta_info_developer_website = appMeta.get('DeveloperWebsite')
            privacy_policy_link = appMeta.get('PrivacyPolicyLink')

            print("----Checking Privacy Policy .....")

            PrivacyPolicyResults = getPrivacyPolicyText(appMeta.get('PrivacyPolicyLink'))

            PrivacyPolicyText = PrivacyPolicyResults[0]
            PrivacyPolicyAccess = PrivacyPolicyResults[1]

            print('this is privacy polycy link :'+privacy_policy_link)
            if privacy_policy_link=='' or privacy_policy_link== None:
                print('this is accessed')
                f_pp.write("{}; {}; {}; {}; {}\n".format(appID, "No Privacy Policy Link", "None", "None", "None"))

            elif PrivacyPolicyAccess == True:
                try:
                    privacy_policy_text = PrivacyPolicyText
                    privacy_policy_access = PrivacyPolicyAccess

                    # print('privacy_policy_text:', privacy_policy_text)
                    print('privacy_policy_access: ', privacy_policy_access)

                    privacy_policy_classification = PPShares3rdParty(PrivacyPolicyText)
                    print('privacy_policy_classification: ', privacy_policy_classification)
                    
                    privacy_policy_language = DetectLanguage(PrivacyPolicyText)
                    print('privacy_policy_language: ', privacy_policy_language)

                    f_pp.write("{}; {}; {}; {}; {}\n".format(appID, privacy_policy_link, privacy_policy_classification, privacy_policy_language,'text fine'))
                except:    
                    # f_pp.write("{}; {}; {}\n".format(appID, "Invalid Privacy Policy text format/No Privacy Policy Link","None"))
                    f_pp.write("{}; {}; {}; {}; {}\n".format(appID, privacy_policy_link,"None",privacy_policy_language,privacy_policy_text))
                    pass
            else:
                f_pp.write("{}; {}; {}; {}; {}\n".format(appID, privacy_policy_link, "None", "None", PrivacyPolicyText))
        
        except:
            print("We failed to get metadata")
            f_pp.write("{}; {}; {}; {}; {}\n".format(appID, "No Meta Data", "None", "None", "None"))        
            pass
        
            
    f_pp.close()
    
