import re #regex
import string #string
import math
import os
from pathlib import Path
import csv
import argparse


# Destination for the endproduct
output = os.path.join("..", "output", "collocate.csv")


'''
-------------Defining functions that will be used in the main function:-----------------
'''


#Deffining the tokenize funktion
def tokenize(input_string):
    
    pattern = r"[^a-z\s']"
    
    
    #Making the input to lower case.
    input_string = input_string.lower()
    
    #substituting everything that does not match the pattern with nothing
    input_string = re.sub(pattern, '', input_string)
    
    '''
    There is some problems with the regex here. I tried to match both apostrophies words and words with out.
    The problem is that the regex matches everything i want by also a single "t" if there is a word like "can't"
    '''
    #re.findall returns all non-overlapping matches of pattern in a string, as a list of strings.
    token_list = re.findall(r"\b\w+\b", input_string)
    
    return token_list

#Concordance lines
'''
Deffining a function with the following parameters:
- text = a text file
- keyword = The word we are centering the collocation around.
- Window_size = the number of characters that comes before the word. if nothing is put in it will be 50
''' 
def kwic(text, keyword, window_size):
    
    #creating an empty container, to append lines from the texts
    lines = [] 
    
    # re.finditer looks at the keyword, in the text.
    for match in re.finditer(keyword, text):
        #Now match = keyword
        
        # word_start matches all first character index of the pattern that is the keyword.
        #Finding the index of the beginning of the keyword
        word_start = match.start()
        
        # word_end matches all last character index of the pattern that is the keyword.
        #Finding the index of the end of the keyword
        word_end = match.end()
        
        # Left window. the number of characters that comes before the word.
        left_window_start = max(0, word_start-window_size) 
        
        # Slicing from left_window_start to word_start
        left_window = text[left_window_start:word_start] 
        
        # Right window
        right_window_end = word_end + window_size
        right_window = text[word_end : right_window_end]
        
        # print line
        line = f"{left_window} __{keyword}__ {right_window}"
        #tokenizing the line with the tokenize function deffined above.
        line = tokenize(line) 
        #Appending line to lines.
        lines.append(line) 
    
    # the list lines is returned from the function, when it is called.
    #print (lines)
    return lines 


    
#Deffining main function:    
def main():
    
    '''
    -----------------------Defining commandline arguments:------------------------
    '''
    
    ap = argparse.ArgumentParser(description = "[INFO] collocation script")
    #first argument: the path to the csv file that one which to create a network analysis from:
    ap.add_argument("-k", # flag assigned to this command line argument.
                    "--keyword",
                    required=True, # It is required for the one who uses the script to decide on a keyword.
                    type=str, #This argument must be a string.
                    help="the keyword you would like to search for")
    
    ap.add_argument("-w",
                    "--window",
                    required=False, # It is not required to decide on a window size.
                    default=50, # If no window size the default is set to 50
                    type=int, #This argument must be an integer.
                    help="The size of the window you would like to look for.")
    
    
    ap.add_argument("-c",
                    "--corpus",
                    required=False, # It is not required to chose a corpus.
                    default="../data/100_english_novels", # If no corpus is chosen, the default corpus 100_english_novels is chosen
                    type=str, #This argument must be an integer.
                    help="The corpus you would like to calculate collocates for")
    
    
    args = vars(ap.parse_args())
    
    
    keyword = args["keyword"]
    window_size = args["window"]
    corpus = args["corpus"]
    data_path = os.path.join(corpus)
    
    #creating corpus:
    #Creating an empty container, this time as a string.
    corpus = "" 
    
    #Creating a for loop that can run through the novels in the folder corpus.
    for filename in Path(data_path).glob("*.txt"):
        #Opening the file
        with open(filename, "r", encoding="utf-8") as file: 
            #reading the files.
            loaded_text = file.read() 
            # Adding the files as texts to "corpus", which is now a sting containing all the text in the corpus.
            corpus = corpus + loaded_text 
            

    

    '''
    --------------------------Tokenizing corpus:------------------------------------ 
    '''
    #Tokenizing the corpus
    tokenized_corpus = tokenize(corpus)
    
    #Using tokenized on the corpus and saving it.
    tokenized_lines = kwic(corpus, keyword, window_size)
    
    
    
    '''
    --------------------------Counting collocates:--------------------------------
    '''

    #Create a list of collocates
    collocate_list = [] #now creating a list for collocates
    index_number = 0 # creating a variable called index_number, to use in the loops below

    #The first for loop runs through a list of lists. That means each list has it's own index.
    for line in tokenized_lines:
        
        #This for loop only runs through the line of the index it is currently on, and then moves on as the index_number changes
        for token in tokenized_lines[index_number]:
            if token not in collocate_list:
                collocate_list.append(token) #if the token is not already in the collocate_list it is added, to the list.
        index_number += 1 # Making sure the index number grows with 1, everytime the nested for loop is done.
        
        
        
    '''
    ----------Removing the incomplete words, the words that has been cut in half by the kwic function:---------------
    '''
    for collocate in collocate_list: #run through the collocate_list
        if collocate not in tokenized_corpus: 
            #if the incompleet word is not in tokenized_corpus (which contains all words in the corpus, in a list.):
            collocate_list.remove(collocate) #remove it from the collocate list.
            
    # Creating for loops that can count the number of collocates in each line
    collocate_counts = []
    for collocate in collocate_list: #running through every collocate in the collocate_list
        count = 0 #creating a count variable
        for line in tokenized_lines:  # running throught the lines in lines_tokenized
            count = count + line.count(collocate)# for each line we update the count by adding adding to the count everytime a collocae is found.
        collocate_counts.append(count)#and appending it to the collocate_count

        


        
        
    '''
    -------------------Creating the csv, with the values:-------------------
    '''
    
    with open(output, mode = "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["collocate", "raw_frequency", "MI"])
        writer.writeheader()
        
        N = len(tokenized_corpus) #The total number of words in our corpus
        u = tokenized_corpus.count(keyword) #The total number of keyword in our corpus.  
        
        
        index_number = 0 # resetting index_number to 0 as we need to use it agian.
        
        for collocate in collocate_list: 
            # Inside the loop we count how often the keyword appears with the collocate.
            line_keywords = 0
            for line in tokenized_lines:
                if collocate in line:
                    line_keywords = line.count(keyword) + line_keywords
              
            #The rest of the values are calculated:
            v = tokenized_corpus.count(collocate) # v = the collocate
            O11 = collocate_counts[index_number] #O11= collocate and keyword together
            O12 = u - line_keywords #O12 = keyword without collocate?
            O21 = v - O11 #O21 collocate without keyword
            R1 = O11 + O12
            C1 = O11 + O21
            E11 = (R1*C1)/N 

            #E11 has to be positive
            if E11 <= 0:
                continue
            
            else: # calculating the MI
                MI = math.log(O11/E11)
                
                # using writer.writerow to write rows into csv files.
                writer.writerow({"collocate": collocate, "raw_frequency": O11, "MI": MI})
                print(f"Word: {collocate}, frequency: {O11}, MI: {MI}")
            
            #index_number = index_number + 1    
            index_number += 1

            
if __name__=="__main__":
    main()