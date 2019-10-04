from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class WordExtractor:
    def __init__(self):
        self._stop_words = set(stopwords.words('english'))
        self._lemmatizer = WordNetLemmatizer()
    
    def extract(self, text, remove_stop_words=True, lemmatize=True):
        words = text.lower().split(' ')
        
        if lemmatize:
            words = [self._lemmatizer.lemmatize(word)
                     for word in words]
        
        if remove_stop_words:
            words = [word
                     for word in words
                     if word not in self._stop_words]
        
        return words
