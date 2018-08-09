names = ['KNN',
        'Logit',
        'Tree',
        "Forst",
        'SVM',
        'LinearSVM',
        'GaussioanNB',
        'XGboost']

clfs = [(KNeighborsClassifier(n_neighbors=4)), 
        (LogisticRegression(C=1000)),
        (DecisionTreeClassifier()),
        (RandomForestClassifier()),
        (SVC()),
        (LinearSVC()),
        (GaussianNB()),
        (XGBClassifier())
         ]
for name, clf in zip(names, clfs):
    CVScores = cross_val_score(clf, X_train_scaled, y_train, cv=5, scoring='recall')
    print(f'{name} CV_recall is:', np.mean(CVScores))
    
# logit > linearSVM > SVM/XGboost 