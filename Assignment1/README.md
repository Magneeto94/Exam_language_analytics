# Assignment 1: Word Count
<br>

__Basic scripting with Python__

__Assignment:__
Using the corpus called 100-english-novels found on the cds-language GitHub repo, write a Python programme which does the following:

- Calculate the total word count for each novel
- Calculate the total number of unique words for each novel
- Save result as a single file consisting of three columns: filename, total_words, unique_words


### Running the script

- After cloning the repository to worker02 or locally on your machine with __"git clone https://github.com/Magneeto94/Exam_language_analytics.git"__
- To set up the virtuel inviorement run: “bash create_venv_ass1.sh"
    - The virtual environment "venv_ass1" will be created and the dependencies from the “requirements.txt” file will be installed in it.
- Activate the venv with: "source venv_ass1/bin/activate"
    - The virtual environment is now activated.
- To run the script move to the src folder: "cd src"
- Then run: "python word_counts.py"
- Results for the ten first files will be printed to the terminal, the rest of the results can be found in the output folder in the csv-file “wordcount.csv”
