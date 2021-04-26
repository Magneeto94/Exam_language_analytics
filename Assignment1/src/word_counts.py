'''
------------------------------Importing packages:-------------------------------------
'''
#Importing operating system
import os
#Importing pandas as pd.
import pandas as pd
#Importing Path that we are going to acces our files with
from pathlib import Path 
import re


#Defining main function
def main():
    
    '''
    -----------------Creating data to save in csv:----------------------------
    '''
    
    #Saving the path to where the data is located
    data_path = os.path.join("..", "data", "100_english_novels", "corpus")

    #Creating containers for Auther_name, total_words and unique_words.
    Auther_name = []
    total_words = []
    unique_words = []

    # Creating a loop that runs through the txt files saved in the data_path
    for filename in Path(data_path).glob("*.txt"): #Looking trough all the files that ends on .txt
        
        #Opening each file.
        with open(filename, "r", encoding="utf-8") as file:
            
            #Creating a regex that only returns all letters, including capital letters, and spaces.
            regex = re.compile('[^a-zA-Z\s]')
            
            #Reading the files and..
            #Making everything into lower case so the same words spelled with different cases are not counted twice in unique_words.
            loaded_text = file.read().lower()
            
            #Now using the regex to remove all charactors that are not spaces or letters
            loaded_text = regex.sub('', loaded_text)
            
            #Splitting the loaded text on whitespace. Each word is now a an item in a list in each text.
            #This enable me to count the number of words in the text.
            split_text = loaded_text.split()
                          
            #Using the "set" function to get the unique wordcount for each text. Set only counts words once.
            unique_set = set(split_text)
            
            #Slicing the filename, so the name only contains the name of the file and not the entire path. (ex. Anon_Clara_1864.txt)
            Auther = str(filename)
            Auther = Auther[34:len(Auther)]
        
            #wordcount.append(f"{Auther}, {len(split_text)}, {len(unique_set)}.")
            Auther_name.append(Auther)
            total_words.append(len(split_text))
            unique_words.append(len(unique_set))
    
    '''
    ------------------------------Transforming data into csv and saving:-------------------------
    '''
    
    #Merging the lists Auther_name, total_words and unique_words. which now contains the values gethered from the .txt-files
    merged_list = {'Auther_name': Auther_name, 'total_words': total_words, 'unique_words': unique_words}
    
    #Transforming merged list to a dataframe
    df = pd.DataFrame(merged_list)
    
    #Sorting the dataframe alphabetically and giving the values new indexes, so Anon_Clara gets index 0 and so on.
    df = df.sort_values('Auther_name', ignore_index=True)
    
    #Writing data to the path and saving it as a csv-file
    df.to_csv('../output/wordcount.csv')
    
    
if __name__ =='__main__':
    main()