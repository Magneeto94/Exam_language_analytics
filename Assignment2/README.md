# Assignment 2: String processing with Python

DESCRIPTION:

__String processing with Python__

Using a text corpus found on the cds-language GitHub repo or a corpus of your own found on a site such as Kaggle, write a Python script which calculates collocates for a specific keyword.



- The script should take a directory of text files, a keyword, and a window size (number of words) as input parameters, and an output file called out/{filename}.csv
- These parameters can be defined in the script itself
- Find out how often each word collocates with the target across the corpus
- Use this to calculate mutual information between the target word and all collocates across the corpus
- Save result as a single file consisting of four columns: collocate, raw_frequency, MI


- BONUS CHALLENGE: Use argparse to take inputs from the command line as parameters


__General instructions__

- For this assignment, you should upload a standalone .py script which can be executed from the command line.
- Save your script as collocation.py
- Make sure to include a requirements.txt file and your data
- You can either upload the scripts here or push to GitHub and include a link - or both!
- Your code should be clearly documented in a way that allows others - to easily follow the structure of your script and to use them from the command line


## Run the script

This script only use basic python, so no there is no need for a new virtual enviorement. <br>

__Argparse__
<br>
- This script uses three command line arguments
    - The first is the keyword which is the only argument required to run the function. Its flag is -k
    
    - The next argument is optional and defines the window of the collocates. If no windov is chosen 50 is the default. Its flaf is -w
    
    - The last argument is the path of the corpus that the collocates should be counted on. If no corpus is chosen the 100_english_novels corpus is chosen. Its flag is -c
    

To run the script move to the src folder and run: __python collocates.py -k "***The word you would like to search for*** __





