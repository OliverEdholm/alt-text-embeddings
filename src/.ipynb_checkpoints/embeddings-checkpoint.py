import io

import numpy as np

from src.sanity_check import is_valid
from src.text_processing import WordExtractor


def load_vectors(fname):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    n, d = map(int, fin.readline().split())
    data = {}
    for line in tqdm(fin):
        tokens = line.rstrip().split(' ')
        data[tokens[0]] = np.array([float(n)
                                    for n in tokens[1:]])
    return data


class MeanWordEmbeddingExtractor:
    def __init__(self):
        self._word_vectors = load_vectors('data/crawl-300d-2M.vec')
        self._word_extractor = WordExtractor()
    
    def extract(self, text):
        return np.mean([word_vectors.get(word, np.zeros(300)) 
                        for word in word_extractor.extract(alt_text)], axis=0)