import os
import sys
sys.path.append(os.path.join(".."))
from pathlib import Path #Importing Path that we are going to acces our files with.
import pandas as pd
import matplotlib.pyplot as plt
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
#Initialise spacy
nlp = spacy.load("en_core_web_sm") #nlp = natural language processing.
import numpy as np



def main():
    
    '''
    --------------------------Loading the new file:----------------------------
    '''
    
    filepath = os.path.join("..", "data", "headlines.csv")

    headlines = pd.read_csv(filepath)
    
    # new_data now also consist of a column/series of scores (sentiment scores)
#     print("first 10 values of the dataframe:")
#     print(headlines.head(10))

    #Deleting the series named "Unnamed: 0"
    del headlines["Unnamed: 0"]
    
    '''
    ------------------Calculating avarage score:-----------------------
    '''
    
    #Calculation the avarage score for for each date using groupby() and mean()
    avg_data = headlines.groupby("publish_date").mean()

    

    #The dataframe no longer contains the headlines, and only 1 date for each day.
    #The avarage score for the sentiment is calculated and saved. The df is now considarably smaler.
    len(avg_data)
    avg_data
    
    
    '''
    -------------------------smoothing out sentiment scores:------------------
    '''
    ###
    ### In order to get the right plot the plot has to be made from a normal list.
    ###
    
    #Creating container for our avarage scores
    mean_scores = []
    
    for i in avg_data["scores"]:
        # appending avg_scores to list.
        mean_scores.append(i)
    
    #Smoothing out the mean_scores
    smoothed_sentiment_weeks = pd.Series(mean_scores).rolling(7).mean()
    smoothed_sentiment_months = pd.Series(mean_scores).rolling(30).mean()
    
    
#     smoothed_sentiment_weeks = pd.Series(avg_data["scores"]).rolling(7).mean()
#     smoothed_sentiment_months = pd.Series(avg_data["scores"]).rolling(30).mean()
    
    '''
    -----------------------Creating plot for weeks:------------------------------
    '''
    #plotting the size of the figure.
    fig = plt.figure(figsize = (10,5)) 

    #Creating a title for the plot.
    plt.title("Sentiment for headlines 2003-2021", fontsize = 32)

    #naming x and y labels
    plt.xlabel("Years since 2003", fontsize = 20)
    plt.ylabel("Level of sentiment", fontsize = 20)

    #plotting:
    plt.plot(smoothed_sentiment_weeks)
    #plt.plot(smoothed_sentiment_months)
    #plt.plot(smoothed_sentiment_years)


    #Adding a legend in right corner.
    plt.legend(["Average weekly"],
               loc='upper right',
               fontsize= 10)

    #changing the numbers of the x-asis.
    plt.xticks(np.arange(0, len(mean_scores)+1,365.25), range(2003,2021))
    plt.savefig("../output/sentiment_week.png")
    
    
    '''
    -----------------------Creating plot for months:------------------------------
    '''
    #plotting the size of the figure.
    fig = plt.figure(figsize = (10,5)) 

    #Creating a title for the plot.
    plt.title("Sentiment for headlines 2003-2020", fontsize = 32)

    #naming x and y labels
    plt.xlabel("Years since 2003", fontsize = 20)
    plt.ylabel("Level of sentiment", fontsize = 20)

    #plotting:
    plt.plot(smoothed_sentiment_months)
    #plt.plot(smoothed_sentiment_years)


    #Adding a legend in right corner.
    plt.legend(["Average monthly"],
               loc='upper right',
               fontsize= 10)

    #changing the numbers of the x-asis.
    plt.xticks(np.arange(0, len(mean_scores)+1,365.25), range(2003,2021))
    plt.savefig("../output/sentiment_months.png")
    
    
if __name__ =='__main__':
    main()