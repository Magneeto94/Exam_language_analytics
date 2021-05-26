import os, sys
sys.path.append(os.path.join(".."))
import csv
import itertools
import re
import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
#Initialise spacy
nlp = spacy.load("en_core_web_sm") #nlp = natural language processing.
import matplotlib.pyplot as plt
from pathlib import Path
#For calculating mean score of sentiment
import statistics
from tqdm import tqdm

#Adding spaCyTextBlob to spaCy pipline:
spacy_text_blob = SpacyTextBlob()
nlp.add_pipe(spacy_text_blob)


def main():
    
    # Path to where the books are saved.
    filepath = os.path.join("..", "data", "Book_Text")

    #Creating empty dataframe to hold the data created in the loop.
    hp_df = pd.DataFrame()

    #Running through the files opening and reading the text files in the filepath.
    for txt_file in Path(filepath).glob("*.txt"):
        file = open(txt_file, "r")
        file = file.read()

        #Removing everything from the dataframe exept for letters, whitespaces appostrophes and dots.
        pattern = r"[^a-zA-Z\s'.]"
        file = re.sub(pattern, '', file)

        #Splitting the book on new line, as these indicate the start of a headline or chapter.
        book = file.split("\n")


        #Removing the first index, by slicing, as this have some unwanted text I don't want to use.
        book = book[1:len(book)]

        #creating two empty lists for headlines and the sepperated text.
        headlines = []
        sepperated = []

        #making a for-loop that runs through the lenth of the book list.
        for i in range(len(book)):

            # creating a chapter number based on index to ad to the titles of the chapters to be able to sort based on it later.
            chapter_num = str(i+1)

            #Adding zeroes, that way every chapter consists of two digits.
            chapter_num = chapter_num.zfill(2)

            # Isolating the headline of each chapter and pushing it to a list.
            #Splitting the text on double spaces because there is a double space between each headlina and a chapter
            headline = str(chapter_num) + "_" + str(book[i].split("  ")[0])
            headlines.append(headline)

            #Isolating the text of the chapters in a list, but the headlines are still in the text.
            sep = book[i].split("  ", 1)
            sepperated.append(sep)

        #now creating the list that is going to consist of the chapters of the books
        chapters = []

        for text in sepperated:

            #making sure I am working with a string
            chapter = str(text)

            #splitting the string on comma. "chapter" is now a list
            chapter = chapter.split(",")

            #saving only the last index of the list.
            chapter = chapter[-1]

            #Appending to chapters.
            chapters.append(chapter)

        #Slicing away the last element in the list as this is not part of the story.
        chapters = chapters[:len(chapters)-1]


        #Now creating a list to contain the name of the books.
        books = []

        #Using the range of the headlines, as this is the number of rows there are going to be in the data set for each book.
        for i in range(len(headlines)):

            #using the filepath to name them, and making sure it is a string, which we can slice.
            name_of_book = str(txt_file)

            #Slicing in the path to only keep the name of the book.
            name_of_book = name_of_book[18:len(name_of_book)-4]

            #Appending to books.
            books.append(name_of_book)


        #Creating Dataframe from the three columns: headlines, chapters, books.
        df = pd.DataFrame(list(zip(headlines, chapters, books)),
                            columns =['Headline', 'Chapter_text', 'Book'])

        #Saving the dataframe
        hp_df = hp_df.append(df, ignore_index = True)
    
    
    #Sorting values, first based on books, then based on Headline.
    hp_df = hp_df.sort_values(by=['Book','Headline']).reset_index(drop=True)
    
    
    #Creating empty list to store the avg sentiment score for each chapter
    avg_sentiment = []

    #For-loop for runnning through the chapters.
    for chapter in tqdm(hp_df["Chapter_text"]):

        #Creating an empty list to contain the sentiment scores of each sentence.
        polarity = []

        # Turning each chapter into a doc object using spacy.
        doc_chapter = nlp(chapter)

        #Now creating a forloop that runs through each chapters as doc-objects.
        for sentence in doc_chapter.sents:

            #calculating the sentiment score
            score = sentence._.sentiment.polarity

            #Appending the sentiment scores to the polarity list.
            polarity.append(score)

        #Calculating the average sentimen score for each chapter
        chapter_sentiment = statistics.mean(polarity)

        #Appending the chapter sentiment scores to the avg_sentiment list.
        avg_sentiment.append(chapter_sentiment)
    
    
    #Creating a new column (series) from the list avg_sentiment.
    hp_df["avg_sentiment"] = avg_sentiment
    
    
    #writing to csv-file
    hp_df.to_csv(os.path.join("..", "data", "hp_df.csv"))
    
    
    print(hp_df.head(10))
    
if __name__ =='__main__':
    main()