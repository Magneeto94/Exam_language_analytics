from tqdm import tqdm
import os
import sys
sys.path.append(os.path.join(".."))
from pathlib import Path #Importing Path that we are going to acces our files with.
import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
#Initialise spacy

#Disabeling tagger (assigns part of speech tags), parser (genrates dependency parses) and ner (named entity recognition) to be able to run through the data faster.
nlp = spacy.load("en_core_web_sm", disable=['tagger', 'parser', 'ner']) #nlp = natural language processing.
nlp.add_pipe(nlp.create_pipe('sentencizer'))
import numpy as np



def main():
    
    #Adding spaCyTextBlob to spaCy pipline:
    spacy_text_blob = SpacyTextBlob()
    nlp.add_pipe(spacy_text_blob)
    
    
    '''
    Reading file from path and saving data in data.
    The lines are commented out beacause i made a dataframe containing scores further down in the code, so i don't have to calculate
    the scores sentiment scores again.
    The dataframe is saved in a csv-file called Headlines.csv
    '''
    
    filepath = os.path.join("..", "data", "abcnews-date-text.csv")
    data = pd.read_csv(filepath)
    
    # Creating a container for the sentiment scores:
    output = []

    #The loop runs through the headlines in the csv-file.
    #Disabeling to make the code run faster, since there is a lot of data and the processing time is long.
    for doc in tqdm(nlp.pipe(data["headline_text"],
                        batch_size=50)):
        output.append(doc._.sentiment.polarity) #appending the scores to our output container.

    # Creating a new dataframe
    data_df = pd.DataFrame(data)

    # Appending a new series/column to the new df, with the scores
    data_df["scores"] = output
    
    
    
    '''
    Writing new dataframe to csv-file.
    '''
    
    #Writing the newly created dataframe to a csv, so it does not have to be created again later.
    data_df.to_csv('../data/headlines.csv')
    
    
    
if __name__ =='__main__':
    main()