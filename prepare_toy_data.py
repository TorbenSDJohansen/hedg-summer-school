"""
@author: tsdj

"""


import os

from histocc import DATASETS
from sklearn.model_selection import train_test_split
from transformers import CanineTokenizer

import pandas as pd

from dirs import DATA_DIR


def tokenize(dataset: pd.DataFrame) -> list[int]:
    tokenizer = CanineTokenizer.from_pretrained('google/canine-s')
    
    for hisco in dataset['occ1']:
        tokenized = tokenizer.encode_plus(
            hisco,
            add_special_tokens=True,
            padding = 'max_length',
            max_length = 128,
            return_token_type_ids=False,
            return_attention_mask=True,
            return_tensors='pt',
            truncation = True
        )


def main():
    keys = DATASETS['keys']()
    mapping = dict(keys[['hisco', 'code']].values)

    toydata = DATASETS['toydata']()
    toydata['label'] = toydata['hisco_1'].transform(lambda x: mapping[x])

    train, test = train_test_split(
        toydata[['occ1', 'label']],
        test_size=0.1,
        random_state=42,
        )

    train.to_csv(os.path.join(DATA_DIR, 'toy_data_train.csv'), index=False)
    test.to_csv(os.path.join(DATA_DIR, 'toy_data_test.csv'), index=False)


if __name__ == '__main__':
    main()
