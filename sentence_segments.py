#!/usr/bin/env python

from pathlib import Path

from pybo import Text

data_dir = Path('texts')
data_dir.mkdir(exist_ok=True)

# find all files to process, leaving aside those already processed
texts = [d for d in data_dir.glob('*.txt') if 'pybo' not in d.stem]
if not texts:
    exit('There are no .txt files to process.\nExiting')

# processing all the files
for t in texts:
    text = Text(t)
    print(f'processing "{t.name}".', flush=True)
    text.tokenize_sentences_plaintext
