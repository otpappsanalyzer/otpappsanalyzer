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


if __name__ == "__main__":
    # NOTE: we put the following in a 'if __name__ == "__main__"' protected
    # block to be able to use a multi-core grid search that also works under
    # Windows, see: http://docs.python.org/library/multiprocessing.html#windows
    # The multiprocessing module is used as the backend of joblib.Parallel
    # that is used when n_jobs != 1 in GridSearchCV

    # the training data folder must be passed as first argument
    # path = r"C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\corpus\SciKit 7 October\CorpusFolder\Train"
    path = r"/home/tham/app-gadadyi-new/App-Garadyi/MachineLearning/privacy_policy_classifier_corpus/Scikit_Model/ReducedCorpus/Train"
    
    movie_reviews_data_folder = path
    dataset = load_files(movie_reviews_data_folder, shuffle=False)
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
    listText = []
    listText.append("   Privacy Policy  This privacy policy has been compiled to better serve those who are concerned with how their Personally Identifiable Information (PII) is being used online.  If you choose to use our service  then you agree to the collection and use of information in relation to this policy. The Personal Information that we collect is used for providing and improving the service. We will not use or share your information with anyone except as described in this Privacy Policy.  Please read our privacy policy carefully to get a clear understanding of how we collect  use  protect or otherwise handle your Personally Identifiable Information in accordance with our website.  Information collection and use  For a better experience  while using our service  we may require you to provide us with certain personally identifiable information  including but not limited to none . The information that we request will be retained by us and used as described in this privacy policy.  The app does use third party services that may collect information used to identify you.  Link to privacy policy of third party service providers:    Google Play Services  AdMob  Firebase Analytics    Log data  We want to inform you that whenever you use our service  in a case of an error in the app we collect data and information (through third party products) on your phone called Log Data. This Log Data may include information such as your device Internet Protocol (IP) address  device name  operating system version  the configuration of the app when utilizing our service  the time and date of your use of the service  and other statistics.  Cookies  Cookies are files with a small amount of data that are commonly used as anonymous unique identifiers. These are sent to your browser from the websites that you visit and are stored on your device's internal memory.  We do not use cookies. However  the app may use third party code and libraries that use cookies to collect information and improve their services. You have the option to either accept or refuse these cookies and know when a cookie is being sent to your device. If you choose to refuse our cookies  you may not be able to use some portions of our service.  Service providers  We do not sell  trade  or otherwise transfer to outside parties your Personally Identifiable Information unless we provide users with advance notice. This does not include website hosting partners and other parties who assist us in operating our website  conducting our business  or serving our users  so long as those parties agree to keep this information confidential. We may employ third-party companies and individuals due to the following reasons:    To facilitate our service;  To provide the service on our behalf;  To perform service-related services;  To assist us in analyzing how our service is used.    We want to inform users of this service that these third parties have access to your Personal Information. The reason is to perform the tasks assigned to them on our behalf. However  they are obligated not to disclose or use the information for any other purpose.  Security  We never ask for personal or private information like names  email addresses  or credit card numbers.  We value your trust in providing us your Personal Information  thus we are striving to use commercially acceptable means of protecting it. But remember that no method of transmission over the internet  or method of electronic storage is 100% secure and reliable  and we cannot guarantee its absolute security.  Links to other sites  This service may contain links to other sites. If you click on a third-party link  you will be directed to that site. Note that these external sites are not operated by us. Therefore  we strongly advise you to review the Privacy Policy of these websites. We have no control over and assume no responsibility for the content  privacy policies  or practices of any third-party sites or services.  Children's privacy  We do not collect information from children under 13. We don't let third-parties  including ad networks or plug-ins  collect PII from children under 13.  Changes to this privacy policy  We may update our Privacy Policy from time to time. Thus  you are advised to review this page periodically for any changes. We will notify you of any changes by posting the new Privacy Policy on this page. These changes are effective immediately after they are posted on this page.  Contacting us  If there are any questions regarding this privacy policy  you may contact us using the information below.  level38.co  ")
    print("listText: ")
    print(listText)
    print(type(docs_test))
    predictionText = grid_search.predict(listText)
    print(predictionText)
    import pickle
    filename = '/home/tham/app-gadadyi-new/App-Garadyi/MachineLearning/privacy_policy_classifier_corpus/Scikit_Model\finalized_model_th.sav"'
    # filename = r'C:\Users\jake_\OneDrive\Desktop\Macquarie University\Personal Projects\Cybersecurity\Django\three\mysite\corpus\Scikit_Model\finalized_model.sav'
    pickle.dump(grid_search, open(filename, 'wb'))
    