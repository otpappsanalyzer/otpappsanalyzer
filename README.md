### Hi there 👋
This is complimentary repository for USENIX paper with a title of "More Than Just a Random Number Generator!
On the Security and Privacy of Android One-Time Password Authenticator Apps".

Herewith the explation for each folder content.

**1. Metadata.**
The scripts inside this folder is used to scrap the metadata of OTP apps from the Google Play Store. The python script needs javascript from the folder **apps_screening**. Make sure you have installed the Google-play-scraper NPM library in your environment. 
For more information about installing NPM can be found in :
https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
For more information about installing the google-play-scraper library can be found in:
https://www.npmjs.com/package/google-play-scraper. 

**2. app_extractor**
This folder contains the app_extractor.py script that is used to decompile the *.apk files using APKtool. The *.apk files and the decompiled (Smali) version of the apps is not uploaded to this repository due to the excessive file size. Please contact the author if you like to have the APK files.

**3. app_downloads**
This folder contains the preparing_list_for_raccoon.py script that is used to reformat the string that is needed to feed the Raccoon apps downloader bulk process. More detail about Racoon can be found at https://raccoon.onyxbits.de/. 

**4 certificate_analysis**
This folder contains scripts that are used to extract the certificate signing version as well as other cryptographic signing mechanisms used to package the OTP apps. We have three different tools including Keytool, APKsigner version 2 and APKsigner version 3. As a note, APKSigner version 3 only runs on Ubuntu 20 or the latest. There are three subfolders to save the result of measurement for each app.

**5 dynamic_analysis**
This folder contains scripts that are used for section 5 of the paper. There are three main experiments including the jailbreak detection mechanism, the traffic interception attack mechanism and the communication to the third-party detection.

**6 exported_component**
This folder contains scripts that are used to extract the unprotected component in the OTP apps. This folder also contains the result of measurement and three code snippet that use as examples of the unprotected exported component and unprotected intent-filter.

**7 library_analysis**
This folder contains scripts that are used to extract the third-party library and also the script that use to plot the third-party library distribution in OTP apps. The list of the third-party library is summarised from several previous studies on the third-party library in Android apps.

**8. Malware_analysis**.
This folder contains scripts to check the hash value of OTP apps to virus total API. The Virus Total scanning result is stored outside this repository due to its size. The summary of the result is provided in this repo. The vt_scan_customized.py script required several functions from the vt_work.py script. Make sure you provide your Virus Total Key in this script to access the VT API. More information about this API can be found in https://support.virustotal.com/hc/en-us/articles/115002100149-API. 

**9 package_analysis**
This folder contains scripts that are used to extract the the binary protection mechanism embedded in the OTP apps package. The script leverages APKID to extract the appearance of anti_vm, anti_debug, anti_disassembly, obfuscator and packer in the OTP apps. More detail about APKID can be found at https://github.com/rednaga/APKiD.

**10 permission_analysis**
This folder contains scripts that are used to extract the permission required by each OTP app. The manifest extractor required the manifest file located outside of this repository. Make sure you set the path of the manifest directory after the decompile process of each apk file. The decompiled version of apk files will contain a file named Manifest.xml.

**11 privacy_policy_analysis**
This folder contains scripts that are used to extract the privacy policy-related things from the OTP apps or used as complimentary for section 6 of the paper. The machine learning subfolder contains an SVM model trained using privacy policy data taken from a previous study. The classification aimed to detect whether privacy policy states that the apps share the user information with the third-party server or not.

**12 root_detection**
This folder contains scripts that are used to extract API/system call from each OTP app. We leverage Androguard to extract the API/System call to detect the appearance of three main API calls that are important for OTP apps including the API call that is used to detect jailbreak detection, the usage of secure hardware for cryptographic operation and the usage of biometric authentication. The result of this experiment is used to support subsection 4.7 in the paper. 

**13 user_review**
This folder contains scripts that are used to extract negatives comment from the user. The negative comment can represent the complaint of the user classified by several types of keywords. User complaints and reviews can be used as a reference to choose suitable OTP apps for the user.

**14 XLDH_library_analysis**
This folder contains the XLDH_extractor.py script that is used to compare the third-party library adopted by OTP apps with the Cross Library data harvesting library. This kind of library is legally exfiltrated the user information taken from the legit library to the third-party server. 

<!--
**otpappsanalyzer/otpappsanalyzer** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
