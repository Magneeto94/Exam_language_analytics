import os, sys
sys.path.append(os.path.join(".."))
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from pathlib import Path
import pandas as pd



def main():

    
    hp_df = pd.read_csv(os.path.join("..", "data", "hp_df.csv"))

    '''
    ------------------------------PLOTTING:---------------
    '''
    #Saving each book in seperate data frames.
    HP1 = hp_df[hp_df["Book"]=="01harry_potter_and_the_philosophers_stone"]
    HP2 = hp_df[hp_df["Book"]=="02harry_potter_and_the_chamber_of_secrets"]
    HP3 = hp_df[hp_df["Book"]=="03harry_potter_and_the_prisoner_of_azkaban"]
    HP4 = hp_df[hp_df["Book"]=="04harry_potter_and_the_goblet_of_fire"]
    HP5 = hp_df[hp_df["Book"]=="05harry_potter_and_the_order_of_the_phoenix"]
    HP6 = hp_df[hp_df["Book"]=="06harry_potter_and_the_half_blood_prince"]
    HP7 = hp_df[hp_df["Book"]=="07harry_potter_and_the_deadly_hallows"]
    
    
    #Defining the figure size of the plot.
    figure(figsize=(15, 7), dpi=80)
    
    #Adding title to the plot
    plt.title("Average sentiment score per chapter for HP Books", fontsize = 30)

    
    #Adding titles to the x and y labels
    plt.xlabel("chapter number", fontsize = 25)
    plt.ylabel("Level of sentiment", fontsize = 25)
    
    

    
    #Plotting the sentiment score for each chapter
    plt.plot(HP1["avg_sentiment"])
    plt.plot(HP2["avg_sentiment"])
    plt.plot(HP3["avg_sentiment"])
    plt.plot(HP4["avg_sentiment"])
    plt.plot(HP5["avg_sentiment"])
    plt.plot(HP6["avg_sentiment"])
    plt.plot(HP7["avg_sentiment"])

    
    #Adding legend to the plot.
    plt.legend(["HP1", "HP2", "HP3", "HP4", "HP5", "HP6", "HP7"],
                   loc='lower right',
                   fontsize= 8)
    
    #Saving plot in output folder.
    plt.savefig(os.path.join("..", "output", "HP_allbooks_sentiment.png"))
    
    
    book_sentiment = open(os.path.join("..", "output", "book_sentiment.txt"), "w")
    book_sentiment.write("Average sentiment score of the books: \n\n")
    book_sentiment.write("(HP1) Harry Potter and the Philosophers Stone   : " + str(round(HP1["avg_sentiment"].mean(), 4)) + "\n" +
                         "(HP2) Harry Potter and the Chamber of Secrets   : " + str(round(HP2["avg_sentiment"].mean(), 4)) + "\n" +
                         "(HP3) Harry Potter and the Prisoner of Azkaban  : " + str(round(HP3["avg_sentiment"].mean(), 4)) + "\n" +
                         "(HP4) Harry Potter and the Goblet of Fire:      : " + str(round(HP4["avg_sentiment"].mean(), 4)) + "\n" +
                         "(HP5) Harry Potter and the Order of the Phoenix : " + str(round(HP5["avg_sentiment"].mean(), 4)) + "\n" +
                         "(HP6) Harry Potter and the Half Blood Prince    : " + str(round(HP6["avg_sentiment"].mean(), 4)) + "\n" +
                         "(HP7) Harry Potter and the Deadly Hallows       : " + str(round(HP7["avg_sentiment"].mean(), 4)) + "\n" )
    book_sentiment.close()


if __name__ =='__main__':
    main()