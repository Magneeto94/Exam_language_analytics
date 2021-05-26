# Assignment 4 network analysis


### Running the script:
 
- After cloning the repository to worker02 or locally on your machine with "git clone https://github.com/Magneeto94/Exam_language_analytics.git" you will be able to use the scripts. 
- Navigate to the folder: “cd Assignment4”
- Install the virtual environment with the following command: “bash create_venv_ass4.sh”
- Activate the venv with the following command: “source venv_ass4/bin/activate”
- run the script (there is 2 arguments):
    - The path to the file you would like to create a network from. The default is set to be: “-f fake_or_real_news.csv". Therefore, no argument is required from the user.
    - The minimum number of edges the nodes should have in the network: “-e number”. The default here is set to 10 edges, so no number is required in this argument either.
