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
            
            
            #Making everything into lower case so the same words spelled with different cases are not counted twice in unique_words.
            loaded_text = file.read().lower()
            
            '''
            Creating a pattern, using "^" as a negation modifier to match everything,
            that is not in the pattern: all lower case letters, whitespaces and apostrophes.
            '''
            #Leaving the apostrophes to be able to differentiate between for example "trolls" and "troll's"
            pattern = r"[^a-z\s']"
            
            #substituting everything that is not in pattern with nothing.
            loaded_text = re.sub(pattern, '', loaded_text)
            
            
            #Splitting text text and thereby creating a list.
            split_text = loaded_text.split() #If no argument is given, the function splits on whitespace.
            #This enable me to count the number of words in the text.
                          
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
    merged_dict = {'Auther_name': Auther_name, 'total_words': total_words, 'unique_words': unique_words}
    
    #Transforming merged dictionary to a dataframe
    df = pd.DataFrame(merged_dict)
    
    #Sorting the dataframe alphabetically and giving the values new indexes, so Anon_Clara gets index 0 and so on.
    df = df.sort_values('Auther_name', ignore_index=True)
    
    #Printing the 10 first rows of the dataframe, before it is written to a csv file
    print(df.head(10))
    
    #Writing data to the path and saving it as a csv-file
    df.to_csv('../output/wordcount.csv')
    
    
if __name__ =='__main__':
    main()