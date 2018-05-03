#Create the DTM (document term matrix) features
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
vectorizer = TfidfVectorizer()
train_vect = vectorizer.fit_transform(html_tr)
test_vect = vectorizer.transform(html_te)

#Dictionary of terms
vectorizer.vocabulary_

#Reviewing terms from the documents
vectorizer.vocabulary_['computer']
vectorizer.vocabulary_['syllabus']
vectorizer.vocabulary_['registrar']
vectorizer.vocabulary_['financial']

syl_idx = vectorizer.vocabulary_['syllabus']

train_vect

#Normalized TFIDF vector
train_vect.todense()
train_vect = train_vect.todense()

#Masking with NumPy Arrays
import numpy as np

np.array(categories_tr) == 'faculty'
mask = np.array(categories_tr) == 'faculty'
mask

categories_tr

train_vect[mask, syl_idx].mean()
