#!/usr/bin/env python

from pathlib import Path

from pybo import Text

data_dir = Path('texts')
data_dir.mkdir(exist_ok=True)

for f in data_dir.glob('*.txt'):
    if 'pybo' not in f.stem:
        print(f'processing {f.name}', flush=True)
        t = Text(f)
        t.tokenize_sentences_plaintext
