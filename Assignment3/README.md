# Dictionary-based sentiment analysis with Python
<br>



Download the following CSV file from Kaggle:
<br>
https://www.kaggle.com/therohk/million-headlines
<br>

This is a dataset of over a million headlines taken from the Australian news source ABC (Start Date: 2003-02-19 ; End Date: 2020-12-31).

## Assignment
- Calculate the sentiment score for every headline in the data. You can do this using the spaCyTextBlob approach that we covered in class or any other dictionary-based approach in Python.
- Create and save a plot of sentiment over time with a 1-week rolling average
- Create and save a plot of sentiment over time with a 1-month rolling average
- Make sure that you have clear values on the x-axis and that you include the following: a plot title; labels for the x and y axes; and a legend for the plot
- Write a short summary (no more than a paragraph) describing what the two plots show. You should mention the following points: 1) What (if any) are the general trends? 2) What (if any) inferences might you draw from them?


## Setting up the virtual environment

- After cloning the repository to worker02 or locally on your machine with __"git clone https://github.com/Magneeto94/Exam_language_analytics.git"__
- To set up the virtuel inviorement __"run bash create_venv_ass3"__
    - The virtual environment "venv_ass3" will be activated.
- Now move to the folder src via the terminal
- This folder contains 2 scrits:
    - __creating_csv.py:__ to create a new data frame with a column containing the sentiment scores for the headlines
    - __sentiment.py:__ that creates the graphs of the sentiment scores and saves it in out put.
    - creating_csv.py takes about half an hour to run. The csv file that contains the new dataframe is placed in the data folder, so it is not nessasary to run the script to get the data frame.
    
- The 2 python scripts can be run from the src folder with "python sentiment.py" or "python creating_csv.py"



__Write a short summary (no more than a paragraph) describing what the two plots show. <br>
You should mention the following points:__
1) What (if any) are the general trends? <br>
2) What (if any) inferences might you draw from them?
<br>
<br>
The two plots show, the sentiment score of the headlines calculated by spacy's text blob, as an avarage of each rolling week and each rolling month. From the plots it looks like the genneral trend is a decrease in the sentiment score from 2003 to 2011 where it the sentiment score starts going up and peaks around 2015, where it starts to fall again. this is easiest to read from the monthly plot, but the weekly plot has the same tendency.


