import io

import numpy as np
from tqdm import tqdm

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
    def __init__(self, word_vectors_path):
        self._word_vectors = load_vectors(word_vectors_path)
        self._word_extractor = WordExtractor()
    
    def extract(self, text):
        relevant_word_vectors = []
        for word in self._word_extractor.extract(text):
            if self._word_vectors.get(word) is not None:
                relevant_word_vectors.append(
                    self._word_vectors[word])
    
        if relevant_word_vectors:
            return np.mean(relevant_word_vectors, axis=0)
        else:
            return self._word_vectors['icon']