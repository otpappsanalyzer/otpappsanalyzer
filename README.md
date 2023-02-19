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

**2. Malware_analysis**.
This folder contains scripts to check the hash value of OTP apps to virus total API. The Virus Total scanning result is stored outside this repository due to its size. The summary of the result is provided in this repo. The vt_scan_customized.py script required several functions from the vt_work.py script. Make sure you provide your Virus Total Key in this script to access the VT API. More information about this API can be found in https://support.virustotal.com/hc/en-us/articles/115002100149-API. 

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
