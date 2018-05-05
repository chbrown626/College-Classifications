#Multi-Class Classifier - Multinomial NB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

NBModel = MultinomialNB()

X_train, X_test, y_train, y_test = train_test_split(html_df['HTML'],
                                                    html_df['Categories'],
                                                    test_size = 0.30,
                                                    random_state = 42,
                                                    stratify = html_df['Categories'])

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)
X_test_counts = count_vect.transform(X_test)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_test_tfidf = tfidf_transformer.transform(X_test_counts)

clf = NBModel.fit(X_train_tfidf, y_train)

X_test.head()

#Test 1
print(clf.predict(count_vect.transform(["mimeversion   server cern date sunday nov   gmt contenttype texthtml contentlength   lastmodified saturday feb   gmt cs   home page cs   software engineering technology technique computer science department cornell university fall   course staff samuel weber professorupson   webercscornelledu office hour mf   w   ioi lam ta upson ioicscornelledu office hourst   vineet buch ta upson buchcscornelledu office hour thursday   yaron minsky ta office hour none course material course overview overviewps course handout lecture note recitation note tcltk online resource assignment grade remark stuff c frequently ask question borland samuelcscornelledu last modify oct  "])))
html_df[html_df['HTML'] == "mimeversion   server cern date sunday nov   gmt contenttype texthtml contentlength   lastmodified saturday feb   gmt cs   home page cs   software engineering technology technique computer science department cornell university fall   course staff samuel weber professorupson   webercscornelledu office hour mf   w   ioi lam ta upson ioicscornelledu office hourst   vineet buch ta upson buchcscornelledu office hour thursday   yaron minsky ta office hour none course material course overview overviewps course handout lecture note recitation note tcltk online resource assignment grade remark stuff c frequently ask question borland samuelcscornelledu last modify oct  "]

#Test 2
print(clf.predict(count_vect.transform(["date monday nov   gmt server ncsa mimeversion   contenttype texthtml lastmodifi tuesday nov   gmt contentlength   bill buckle bill buckle professor computer science address department electrical engineering computer science   stanley thomas hall tulane university new orlean la   phone number     fax number     buckleseecstulaneedu recent publication dev prabhu bp buckle fe petry behavior interconnect subpopulation genetic algorithm simd environment submit evolutionary computation postscript kb dev prabhu bp buckle fe petry genetic algorithm scene interpretation prototypical semantic description submit ieee trans system man cybernetic postscript kb congcong x bp buckle number expression modulo commutativity finite semigroup submit siam j discrete mathematic postscript kb research assistant need seminar course evolutionary computation spring   currently teach cpsc   principle computer science cpsc   analysis algorithm"])))
html_df[html_df['HTML'] == "date monday nov   gmt server ncsa mimeversion   contenttype texthtml lastmodifi tuesday nov   gmt contentlength   bill buckle bill buckle professor computer science address department electrical engineering computer science   stanley thomas hall tulane university new orlean la   phone number     fax number     buckleseecstulaneedu recent publication dev prabhu bp buckle fe petry behavior interconnect subpopulation genetic algorithm simd environment submit evolutionary computation postscript kb dev prabhu bp buckle fe petry genetic algorithm scene interpretation prototypical semantic description submit ieee trans system man cybernetic postscript kb congcong x bp buckle number expression modulo commutativity finite semigroup submit siam j discrete mathematic postscript kb research assistant need seminar course evolutionary computation spring   currently teach cpsc   principle computer science cpsc   analysis algorithm"]

#Test 3
print(clf.predict(count_vect.transform(["date thu   nov    gmt server ncsa contenttype texthtml lastmodifi we would   nov    gmt contentlength   karen l karavanic everything ne know learn nyc public school karen l karavanic research assistant paradyn parallel performance tool project university wisconsinmadison computer science department   west dayton street madison wi    css   karavancswiscedu currently pursue phd computer science research interest include parallel computing environment automate performance tuning process operate system database ask uwmadison woman computer science wic frontier science cool program dane county high school student trio student support service free tutoring support uwmadison undergraduate do not miss site web page could save life safe sex page chocolate lover stuyvesant high school alumnus association stuyvesant high school class   thomas legislative information internet us constitution cure anything salt water sweat tear sea isak dinesen ship port safe ship sail sea new thing admiral grace hopper computer pioneer"])))
html_df[html_df['HTML'] == "date thu   nov    gmt server ncsa contenttype texthtml lastmodifi we would   nov    gmt contentlength   karen l karavanic everything ne know learn nyc public school karen l karavanic research assistant paradyn parallel performance tool project university wisconsinmadison computer science department   west dayton street madison wi    css   karavancswiscedu currently pursue phd computer science research interest include parallel computing environment automate performance tuning process operate system database ask uwmadison woman computer science wic frontier science cool program dane county high school student trio student support service free tutoring support uwmadison undergraduate do not miss site web page could save life safe sex page chocolate lover stuyvesant high school alumnus association stuyvesant high school class   thomas legislative information internet us constitution cure anything salt water sweat tear sea isak dinesen ship port safe ship sail sea new thing admiral grace hopper computer pioneer"]

y_pred_NB = NBModel.predict(X_test_tfidf)

#NB Confusion Matrix
from sklearn.metrics import confusion_matrix
import seaborn as sns 

conf_mat = confusion_matrix(y_test, y_pred_NB)
fig, ax = plt.subplots(figsize = (10, 10))
sns.heatmap(conf_mat, annot = True, fmt = 'd', xticklabels = catid_df.Categories.values,
            yticklabels = catid_df.Categories.values)
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()

#Probability predictions
prob_preds = NBModel.predict_proba(X_test_tfidf)
prob_preds

#Print the classification report
from sklearn import metrics

print(metrics.classification_report(y_test, y_pred_NB,
                                    target_names = html_df['Categories'].unique()))
