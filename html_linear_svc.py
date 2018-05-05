#Creating the LinearSVC model
model = LinearSVC()

#Creating the train and test sets
X_train, X_test, y_train, y_test, indices_train, indices_test = train_test_split(html_feat,
                                                                                 labels,
                                                                                 html_df.index,
                                                                                 test_size = 0.33,
                                                                                 random_state = 42)

#Fitting the model
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

#Creating the LinearSVC confusion matrix
conf_mat = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots(figsize = (10, 10))
sns.heatmap(conf_mat, annot = True, fmt = 'd', xticklabels = catid_df.Categories.values,
            yticklabels = catid_df.Categories.values)
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()

#Determine what caused misclassifications
from IPython.display import display

for predicted in catid_df.CatID:
    for actual in catid_df.CatID:
        if predicted != actual and conf_mat[actual, predicted] >= 10:
            print("'{}' predicted as '{}' : {} examples.".format(id_to_cat[actual], id_to_cat[predicted],
                  conf_mat[actual, predicted]))
            display(html_df.loc[indices_test[(y_test == actual) & (y_pred == predicted)
                                            ]][['Categories', 'HTML']])
            print('')

#Creating the LineaarSVC unigrams and bigrams
model.fit(html_feat, labels)

N = 2
for Categories, CatID in sorted(cat_to_id.items()):
    indices = np.argsort(model.coef_[CatID])
    feature_names = np.array(tfidf.get_feature_names())[indices]
    unigrams = [v for v in reversed(feature_names) if len(v.split(' ')) == 1][:N]
    bigrams = [v for v in reversed(feature_names) if len(v.split(' ')) == 2][:N]
    print("# '{}':".format(Categories))
    print("  . Top unigrams:\n       . {}".format('\n       . '.join(unigrams)))
    print("  . Top bigrams:\n       . {}".format('\n       . '.join(bigrams)))

#Accuracy report
print(metrics.classification_report(y_test, y_pred,
                                    target_names = html_df['Categories'].unique()))
