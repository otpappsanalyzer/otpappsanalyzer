"""Build a sentiment analysis / polarity model

Sentiment analysis can be casted as a binary text classification problem,
that is fitting a linear classifier on features extracted from the text
of the user messages so as to guess whether the opinion of the author is
positive or negative.

In this examples we will use a movie review dataset.

"""
# Author: Olivier Grisel <olivier.grisel@ensta.org>
# License: Simplified BSD

import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn import metrics


'''
This script was created by Jake. This is a very simple classifier based on SVM

input: a corpus of privacy policy
note: there are two corpus: (1) ./Scikit_Model/CorpusFolder/Train: is the original corpus with 350 policy text and (2) ./Scikit_Model/ReducedCorpus/Train: it is used in our paper for checking for apps that claim sharing user information with third party.
output: a trained classifer saved as xx.sav file for later use in our privacy policy analysis

'''


if __name__ == "__main__":
    # NOTE: we put the following in a 'if __name__ == "__main__"' protected
    # block to be able to use a multi-core grid search that also works under
    # Windows, see: http://docs.python.org/library/multiprocessing.html#windows
    # The multiprocessing module is used as the backend of joblib.Parallel
    # that is used when n_jobs != 1 in GridSearchCV

    # the training data folder must be passed as first argument
    # path = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\corpus\SciKit 7 October\CorpusFolder\Train"
    
    path = r"/home/tham/app-gadadyi-new/App-Garadyi/MachineLearning/privacy_policy_classifier_corpus/Scikit_Model/CorpusFolder/Train"
    # path = r"/home/tham/app-gadadyi-new/App-Garadyi/MachineLearning/privacy_policy_classifier_corpus/Scikit_Model/ReducedCorpus/Train"

    privacy_policy_corpus_dataset = path
    dataset = load_files(privacy_policy_corpus_dataset, shuffle=False)
    print("n_samples: %d" % len(dataset.data))

    # split the dataset in training and test set:
    docs_train, docs_test, y_train, y_test = train_test_split(
        dataset.data, dataset.target, test_size=0.20, random_state=None)

    # TASK: Build a vectorizer / classifier pipeline that filters out tokens
    # that are too rare or too frequent
    pipeline = Pipeline([
        ('vect', TfidfVectorizer(min_df=3, max_df=0.95)),
        ('clf', LinearSVC(C=1000)),
    ])

    # TASK: Build a grid search to find out whether unigrams or bigrams are
    # more useful.
    # Fit the pipeline on the training set using grid search for the parameters
    parameters = {
        'vect__ngram_range': [(1, 1), (1, 2)],
    }
    grid_search = GridSearchCV(pipeline, parameters, n_jobs=-1)
    grid_search.fit(docs_train, y_train)

    # TASK: print the mean and std for each candidate along with the parameter
    # settings for all the candidates explored by grid search.
    n_candidates = len(grid_search.cv_results_['params'])
    for i in range(n_candidates):
        print(i, 'params - %s; mean - %0.2f; std - %0.2f'
                 % (grid_search.cv_results_['params'][i],
                    grid_search.cv_results_['mean_test_score'][i],
                    grid_search.cv_results_['std_test_score'][i]))

    # TASK: Predict the outcome on the testing set and store it in a variable
    # named y_predicted
    y_predicted = grid_search.predict(docs_test)

    # Print the classification report
    print(metrics.classification_report(y_test, y_predicted,
                                        target_names=dataset.target_names))

    # Print and plot the confusion matrix
    cm = metrics.confusion_matrix(y_test, y_predicted)
    print(cm)

    import matplotlib.pyplot as plt
    plt.matshow(cm)
    plt.show()

    #
    # Save the trained model for later use
    #     
    import pickle
    # filename = '/home/tham/app-gadadyi-new/App-Garadyi/MachineLearning/privacy_policy_classifier_corpus/Scikit_Model/finalized_model_350_corpus_th.sav'
    filename = '/home/tham/app-gadadyi-new/App-Garadyi/MachineLearning/privacy_policy_classifier_corpus/Scikit_Model/finalized_model_103_corpus_th.sav'
    
    # filename = r'C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\corpus\Scikit_Model\finalized_model.sav'
    pickle.dump(grid_search, open(filename, 'wb'))
    

    ###
    #Test the model with a given privacy policy

    
    listText = []
    # listText.append("   Privacy Policy  This privacy policy has been compiled to better serve those who are concerned with how their Personally Identifiable Information (PII) is being used online.  If you choose to use our service  then you agree to the collection and use of information in relation to this policy. The Personal Information that we collect is used for providing and improving the service. We will not use or share your information with anyone except as described in this Privacy Policy.  Please read our privacy policy carefully to get a clear understanding of how we collect  use  protect or otherwise handle your Personally Identifiable Information in accordance with our website.  Information collection and use  For a better experience  while using our service  we may require you to provide us with certain personally identifiable information  including but not limited to none . The information that we request will be retained by us and used as described in this privacy policy.  The app does use third party services that may collect information used to identify you.  Link to privacy policy of third party service providers:    Google Play Services  AdMob  Firebase Analytics    Log data  We want to inform you that whenever you use our service  in a case of an error in the app we collect data and information (through third party products) on your phone called Log Data. This Log Data may include information such as your device Internet Protocol (IP) address  device name  operating system version  the configuration of the app when utilizing our service  the time and date of your use of the service  and other statistics.  Cookies  Cookies are files with a small amount of data that are commonly used as anonymous unique identifiers. These are sent to your browser from the websites that you visit and are stored on your device's internal memory.  We do not use cookies. However  the app may use third party code and libraries that use cookies to collect information and improve their services. You have the option to either accept or refuse these cookies and know when a cookie is being sent to your device. If you choose to refuse our cookies  you may not be able to use some portions of our service.  Service providers  We do not sell  trade  or otherwise transfer to outside parties your Personally Identifiable Information unless we provide users with advance notice. This does not include website hosting partners and other parties who assist us in operating our website  conducting our business  or serving our users  so long as those parties agree to keep this information confidential. We may employ third-party companies and individuals due to the following reasons:    To facilitate our service;  To provide the service on our behalf;  To perform service-related services;  To assist us in analyzing how our service is used.    We want to inform users of this service that these third parties have access to your Personal Information. The reason is to perform the tasks assigned to them on our behalf. However  they are obligated not to disclose or use the information for any other purpose.  Security  We never ask for personal or private information like names  email addresses  or credit card numbers.  We value your trust in providing us your Personal Information  thus we are striving to use commercially acceptable means of protecting it. But remember that no method of transmission over the internet  or method of electronic storage is 100% secure and reliable  and we cannot guarantee its absolute security.  Links to other sites  This service may contain links to other sites. If you click on a third-party link  you will be directed to that site. Note that these external sites are not operated by us. Therefore  we strongly advise you to review the Privacy Policy of these websites. We have no control over and assume no responsibility for the content  privacy policies  or practices of any third-party sites or services.  Children's privacy  We do not collect information from children under 13. We don't let third-parties  including ad networks or plug-ins  collect PII from children under 13.  Changes to this privacy policy  We may update our Privacy Policy from time to time. Thus  you are advised to review this page periodically for any changes. We will notify you of any changes by posting the new Privacy Policy on this page. These changes are effective immediately after they are posted on this page.  Contacting us  If there are any questions regarding this privacy policy  you may contact us using the information below.  level38.co  ")
    # listText.append('This Privacy Policy describes the policies and procedures of DApps Platform, Inc., SIX DAYS LLC (“we,” “our,” or “us”) pertaining to the collection, use, and disclosure of your information on www.trustwallet.com and related mobile applications and products we offer (the “Services” or “Trust Wallet”). OVERVIEW Your privacy is important to us. At Trust Wallet, we follow a few fundamental principles: We don’t ask you for personally identifiable information (defined below). That being said, your contact information, such as your phone number, social media handle, or email address (depending on how you contact us), may be collected when you communicate with us or if you report a bug or other error related to Trust Wallet. We don’t share your information with third parties except to deliver you our Services and products, comply with the law, make Trust Wallet better, protect our rights, or effectuate a business transfer. We’re not a huge, faceless corporation. We’re just developers trying to deliver an incredible product. If you have any questions or concerns about this policy, please reach out to us at support@trustwallet.com. HOW YOU ACCEPT THIS POLICY By using Trust Wallet, including downloading one of our mobile applications, visiting our website, you agree to the use, disclosure, and procedures outlined in this Privacy Policy. WHAT PERSONAL INFORMATION DO WE COLLECT FROM OUR USERS? The information we collect from you falls into two categories: (i) personally identifiable information (i.e., data that could potentially identify you as an individual) (“Personal Information”), and (ii) non-personally identifiable information (i.e., information that cannot be used to identify who you are) (“Non-Personal Information”). This Privacy Policy covers both categories and will tell you how we might collect and use each type. We do our best not to collect any Personal Information from Trust Wallet users. That being said, when using our Services, we do collect PUBlIC wallet addresses that you generate through Trust Wallet. Further, we may collect some Personal Information from you when you communicate with us, including your contact information, such as your phone number, social media handle, or email address (depending on how you reach out). Like other online services, we also collect a variety of Non-Personal Information, including: Information you create through the Trust Wallet’s website or mobile applications, including public wallet addresses. Various analytics data, such as: (i) the IP address of the computer you use to access Trust Wallet; (ii) the type of browser software you are using; (iii) the operating system you are using; (iv) the date and time you access or use Trust Wallet; (v) the website address, if any, that linked you to Trust Wallet; (vi) the website address, if any, you leave our website and travel to; and (vii) other non-personally identifiable traffic data. HOW WE COLLECT INFORMATION When You Contact Us. We may collect certain information if you choose to contact us, if you use our Services or if you report a bug or other error with Trust Wallet. This may include contact information such as your name, email address, phone number, and public wallet address. We, or companies that provide services on our behalf, may also collect certain Non-Personal Information from you, such as your locally hosted public wallet (a “Wallet”) addresses. Information We Automatically Collect Users who visit our website or use our application may have their device’s IP address logged for the purpose of generating anonymous statistics or troubleshooting the performance of our web servers. Your IP address will not be used to track or identify you, but may be used to determine your geographic location in order to determine which of our services you are presented with. Users of our website or mobile applications will receive an anonymous unique device id (“UDID”) for the purpose of identifying the device to Trust Wallet servers. This UDID will not be tied to users’ identities, but will be used for debugging purposes and to differentiate devices when users access our Services using multiple devices. Third Party Services Certain features on Trust Wallet rely on various third-party products and services (collectively “Third Party Services”), such as the Ethereum network, Google Analytics, Apple’s application platform, Coinbase, Changelly, Fabric, and Shapeshift. These services may collect certain Personal Information, such as your public Wallet addresses. Trust Wallet uses Google Analytics, a web analytics service provided by Google, Inc. (“Google”). Google uses cookies to help the website analyze how users use our website. The information generated by the cookie about your use of our website (including your IP address) will be transmitted to and stored by Google on servers in the United States. Google will use this information for the purpose of evaluating your use of the website, compiling reports on website activity for website operators and providing other services relating to website activity and internet usage. Google may also transfer this information to third parties where required to do so by law, or where such third parties process the information on Google’s behalf. Google will not associate your IP address with any other data held by Google. You may choose to accept the cookies by selecting the appropriate settings on your browser if you do this you may not be able to use the full functionality of our website. By using our website, you consent to the processing of data about you by Google in the manner and for the purposes set out above. Please note that your use of these Third Party Services is governed by their respective Terms of Service and Privacy Policies. We use and disclose any collected information in accordance with our own Privacy Policy. HOW WE USE THE INFORMATION WE GATHER We primarily use the limited information we collect to enhance Trust Wallet. Except if we sell all or a portion of our business, or as otherwise described below, we do not rent, trade, or sell your Personal Information. Use of Information to Provide Trust Wallet to You Some ways we may use your Personal Information are to: Contact you when necessary; Respond to your comments, questions, or issues related to bugs or errors with Trust Wallet; Provide you with additional information; Send you information and marketing materials about services and products available through Trust Wallet, using push notifications or other means; Train our team members; or Other internal business purposes. Aggregated Personal Data and Non-Personal Information We may share or disclose aggregated Personal Data or Non-Personal Information with service providers or with other persons we conduct business with, including but not limited potential third-parties for the purpose of showcasing the performance of the company. These service providers and other persons may also share with us aggregated Non-Personal Information that they have independently developed or acquired. Additionally, we may combine aggregate information from the pixel tags, web beacons, and cookies with similar data we collect from other visitors to help us improve our Services. When doing so, we do our best to ensure that the any aggregated information cannot be linked back to you. Agents or Third Party Partners We may provide your Personal Information to our employees, contractors, agents, service providers, and designees (“Agents”) to enable them to perform certain services for us exclusively, including: Improvement of website-related services and features; and Perform maintenance services. Business Transfers We may choose to buy or sell assets. In these types of transactions, customer information is typically one of the business assets that would be transferred. Also, if we (or our assets) are acquired, or if we go out of business, enter bankruptcy, or go through some other change of control, your Personal Information could be one of the assets transferred to or acquired by a third party. By accepting this Privacy Policy, as outlined above, you consent to any such transfer. Protection of Us and Others We reserve the right to access, read, preserve, and disclose any information that we reasonably believe is necessary to: comply with the law or a court order; cooperate with law enforcement; enforce or apply our Terms of Use and other agreements; or protect the rights, property, or safety of Trust Wallet, our employees, our users, or others. WHAT PERSONAL INFORMATION CAN I ACCESS OR CHANGE? You can request access to the information we have collected from you. You can do this by contacting us at support@trustwallet.com. We will make sure to provide you with a copy of the data we process about you. To comply with your request, we may ask you to verify your identity. We will fulfill your request by sending your copy electronically. For any subsequent access request, we may charge you with an administrative fee. If you believe that the information we have collected is incorrect, you are welcome to contact us so we can update it and keep your data accurate. Any data that is no longer needed for purposes specified in the “How We Use the Information We Gather” section will be deleted after ninety (90) days. Wallet addresses created through the Trust Wallet application cannot be deleted from the Ethereum blockchain, therefore we are unable to delete this personal information. If at any point you wish for Trust Wallet to delete information about you, you may contact us at support@trustwallet.com. DATA RETENTION If you delete your Wallet or addresses from the Trust Wallet Android mobile application, uninstall Trust Wallet mobile applications from your device, or request that your information be deleted, we still may retain some information that you have provided to us to maintain Trust Wallet or to comply with relevant laws. DATA SECURITY We are committed to making sure your ')# and therefore cannot guarantee complete security. We employ several physical and electronic safeguards to keep your information safe, including encrypted user passwords, two factor verification and authentication on passwords where possible, and securing all connections with industry standard transport layer security. Even with all these precautions, we cannot fully guarantee against the access, disclosure, alteration, or deletion of data through events, including but not limited to hardware or software failure or unauthorized use. Any information that you provide to us is done so entirely
    listText.append('This app only asks for permission to use the Camera for scanning QR codes for payments and setting up nodes. It does not ask for any personal information.')
    # listText.append(' ')
    print("listText: ")
    print(listText)
    print(type(docs_test))
    predictionText = grid_search.predict(listText)
    print(type(predictionText))
    print(predictionText)