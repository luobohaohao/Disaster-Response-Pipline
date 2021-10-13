# Disaster-Response-Pipline
# Project overview
In Udacity Data Scientist course, I've learned and built on my data engineering skills. In this project, I'll apply these skills to analyze disaster data from Figure Eight to build a model to classify disaster messages.These data all downloaded from workspace in Udacity data scientist course.All the steps I followed course guideline

# Dependencies
1.Python 3

2.Machine Learning Libraries: NumPy, SciPy, Pandas, Sciki-Learn

3.Natural Language Process Libraries: NLTK

4.SQLlite Database Libraqries: SQLalchemy

5.Model Loading and Saving Library: os,Pickle

6.Web App and Data Visualization: Flask, Plotly

7.Others:sys

# Folder Structure
- app
| - template
| |- master.html  # main page of the web application
| |- go.html  # classification result page of the web application
|- run.py  # script for running the web application using Flask

- data
|- disaster_categories.csv  # messages categories dataset usesd for training the model
|- disaster_messages.csv  # messages dataset used for training the model
|- process_data.py # Script data processing
|- DisasterResponse.db   # database to save clean data to

- models
|- train_classifier.py # Model training script
|- classifier.pkl  # Model file

# Instructions
1. Run the following commands in the project's root directory to set up your database and model.
   - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
   - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python app/run.py`

3. Go to your local host to check your result

# Execution Results
1.When I opened my local host website,firstly I saw the visulization result
![image](https://user-images.githubusercontent.com/30916036/137123772-14d56925-2fea-4674-a5a5-9fb5cfec05f9.png)

2.When I typed a text message in the bar,it showed the classified result.
![image](https://user-images.githubusercontent.com/30916036/137123945-c685fecd-0da6-4678-a32b-0ebde491cdae.png)

3.Here is the model model evaluation score for test datasets.
![image](https://user-images.githubusercontent.com/30916036/137124192-2a55673f-1f5d-426f-a747-93d7ed8e2af8.png)

