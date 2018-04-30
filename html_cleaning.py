#Loading nlp/text analysis packages
import spacy
nlp = spacy.load('en_core_web_lg')
from nltk.corpus import stopwords
en_stopwords = stopwords.words('english')  # might have to use 'en' instead of 'english'
stopwords = set(en_stopwords)  # weirdly, you have to make the set after loading the stopwords first

#Data cleaning function
def clean_text(docs,
               lowercase=True,
               remove_punctuation=True,
               remove_stopwords=True,
               remove_numbers=True,
               stem_or_lemmatize='lemmatize'):
    """
    Performs typical text cleaning with spacy's NLP, regex, and built-in Python string methods.
    Note: if using lemmatization, the words will be lowercased

    :param list docs sender: List of strings; should be separate documents
    :param bool lowercase: If True, lowercases all strings
    :param bool remove_punctuation: The body of the message
    :param priority: The priority of the message, can be a number 1-5
    :type priority: integer or None
    :return: the message id
    """
    # lowercase
    if lowercase:
        docs = [d.lower() for d in docs]
    elif not lowercase and stem_or_lemmatize is 'lemmatize':
        print('warning! spacy will lowercase during lemmatization even though lowercase=False')

    # remove punctuation
    if remove_punctuation:
        import string
        table = str.maketrans({key: None for key in string.punctuation})
        docs = [d.translate(table) for d in docs]

    # remove stopwords
    if remove_stopwords:
        # this gets a bit complicated, because if the words aren't already lowercased, we need to lowercase
        # them when checking for stopwords
        no_stop_docs = []
        for d in docs:
            no_stops = []
            for word in d.split():
                if word.lower() not in stopwords:
                    no_stops.append(word)
            no_stop_docs.append(' '.join(no_stops))

        docs = no_stop_docs

    # remove numbers
    if remove_numbers:
        from string import digits
        remove_digits = str.maketrans('', '', digits)
        docs = [d.translate(remove_digits) for d in docs]

    # tokenize and lemmatize  -- spacy also lowercases for us
    if stem_or_lemmatize is 'lemmatize':
        nlp_docs = [nlp(d) for d in docs]

        # keep the word if it's a pronoun, otherwise use the lemma
        # otherwise spacy substitutes '-PRON-' for pronouns
        lemmas = [[w.lemma_ if w.lemma_ != '-PRON-'
                       else w.lower_
                       for w in d]
                  for d in nlp_docs]

        docs = [' '.join(l) for l in lemmas]
    elif stem_or_lemmatize is 'stem':
        from nltk.stem.porter import PorterStemmer
        stemmer = PorterStemmer()
        stemmed_docs = []
        for d in docs:
            stems = []
            for word in d.split():
                stems.append(stemmer.stem(word))
            stemmed_docs.append(' '.join(stems))
        docs = stemmed_docs
    elif stem_or_lemmatize is None:
        print('not stemming or lemmatizing')
    else:
        print("stem_or_lemmatize should be one of ['stem', 'lemmatize', None]")

    return docs

#Cleaning the HTML data
clean_html = clean_text(text)

#Reviewing the cleaned text
len(clean_html)
clean_html[25]
