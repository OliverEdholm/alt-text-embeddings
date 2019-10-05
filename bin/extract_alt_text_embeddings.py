import sys
import json
from pathlib import Path

import cv2
import numpy as np
from tqdm import tqdm

from src.sanity_check import is_valid
from src.embeddings import MeanWordEmbeddingExtractor


def main():
    icons_dir_path, word_vectors_path = sys.argv[1:]
    
    icons_dir_path = Path(icons_dir_path)
    
    print('loading alt text embedding extractor')
    alt_text_embedding_extractor = MeanWordEmbeddingExtractor(word_vectors_path)
    
    print('extracting and saving alt text embeddings')
    for json_path in tqdm(list(icons_dir_path.glob('*.json'))):
        try:
            with open(str(json_path), 'r') as f:
                attributes = json.load(f)['attributes']

            if attributes.get('alt'):  # is not None or decorative a.k.a ""
                identifier = json_path.name.split('.')[0]

                image = cv2.imread(str(json_path.parent) + '/' + '{}.jpg'.format(identifier))

                if is_valid(attributes['alt']):
                    embedding = alt_text_embedding_extractor.extract(attributes['alt'])
                    
                    np.save('{}/{}.npy'.format(json_path.parent, identifier), embedding)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
