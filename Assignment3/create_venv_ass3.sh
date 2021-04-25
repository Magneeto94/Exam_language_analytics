#!/usr/bin/env bash

VENVNAME=venv_ass3

python3 -m venv $VENVNAME
source $VENVNAME/bin/activate
pip install --upgrade pip

pip install ipython
# pip install pandas
# pip install numpy
# pip install spacy
# pip install spacytextblob
# pip install tqdm



test -f requirements.txt && pip install -r requirements.txt

pip install -U pip setuptools wheel
#pip install -U spacy
python -m spacy download en_core_web_sm

deactivate