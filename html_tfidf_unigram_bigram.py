#Alternate DTM TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, encoding='latin-1', ngram_range=(1, 2), stop_words='english')

html_feat = tfidf.fit_transform(html_df.HTML).toarray()
labels = html_df.CatID
html_feat.shape

#Finding correlated terms from each category
from sklearn.feature_selection import chi2
import numpy as np

N = 2
for Categories, CatID in sorted(cat_to_id.items()):
      features_chi2 = chi2(html_feat, labels == CatID)
      indices = np.argsort(features_chi2[0])
      feature_names = np.array(tfidf.get_feature_names())[indices]
      unigrams = [v for v in feature_names if len(v.split(' ')) == 1]
      bigrams = [v for v in feature_names if len(v.split(' ')) == 2]
      print("# '{}':".format(Categories))
      print("  . Most correlated unigrams:\n. {}".format('\n. '.join(unigrams[-N:])))
      print("  . Most correlated bigrams:\n. {}".format('\n. '.join(bigrams[-N:])))
