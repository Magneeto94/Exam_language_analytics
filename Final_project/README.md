# Final Project, sentiment analysis of the Harry Potter books 1-7




### Set up venv and run scripts
- After cloning the repository to worker02 or locally on your machine with "git clone https://github.com/Magneeto94/Exam_language_analytics.git" you will be able to use the scripts. 

- To set up the virtual environment run: “bash create_venv_FP.sh”
    - The virtual environment venv_FP will be created with the dependencies from the requirements.txt file.
- To activate the virtual environment run: “source venv_FP/bin/activate
    - “venv_FP” is now activated
- Move to the src folder to find the python scripts: “HP_cleaning.py” and “HP_sentiment.py”
    - The “HP_cleaning.py”, returns a csv-file based on the txt-files found in the data folder.
    - The “HP_sentiment.py” creates outputs based on the csv-file created by “HP_cleaning.py”
- To run these scripts run:
    - “python HP_cleaning.py”.
    - “python HP_sentiment.py”
- The graph created by “sentiment.py” can be found in the output folder.
- The txt-file “book_sentiment.txt” can also be found in the output folder.